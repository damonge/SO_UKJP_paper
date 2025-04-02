import numpy as np
import config as cf
import sacc
import argparse
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser(description="Transform sim to SACC format")
parser.add_argument('run_name', type=str, help='Name for this run')
parser.add_argument('--dir_data', type=str, help='Directory where the data is')
parser.add_argument('--dir_cov', type=str, help='Directory where the covariance is')
parser.add_argument('--seed_ini', type=int, default=0,
                    help="Seed to start from")
parser.add_argument('--nsims', type=int, default=100,
                    help="Number of sims to process")
args = parser.parse_args()


# Read token C_ells to figure out shape
fname = f"{args.dir_data}/cls_0000.npz"
cls = np.load(fname)['cls'][:, 3, :]
ncls, nbpws = cls.shape

# Read covariance
fname = f"{args.dir_cov}/summary.npz"
cv = np.load(fname)['cov_bb']
# Reform to avoid off-diagonal noise
cv = cv.reshape([ncls, nbpws, ncls, nbpws])
cov = np.zeros([ncls, ncls, nbpws, nbpws])
for _, _, icl1 in cf.pair_ordering():
    for _, _, icl2 in cf.pair_ordering():
        m = cv[icl1][ :, icl2, :]
        d = np.diag(m)
        cov[icl1, icl2] = np.diag(d)
cov = np.transpose(cov, axes=[0, 2, 1, 3])
cov = cov.reshape([ncls*nbpws, ncls*nbpws])
print(len(cls.flatten()))

# Read bandpowers
Bbl = []
ls = cf.get_ells()
for b1, b2, _ in cf.pair_ordering():
    windows = np.load(cf.get_Bbl_fname(b1, b2))['Bbl'][3, :, 3, :]
    Bbl.append(sacc.BandpowerWindow(ls, windows.T))

# Generate binning
bn = cf.get_bins()
ell_eff = bn.get_effective_ells()

def gen_sacc_init():
    s = sacc.Sacc()
    ls = cf.get_ells()

    # Add tracers
    for b, f in enumerate(cf.gl.freqs):
        nus = np.array([f-1, f, f+1])
        bnu = np.array([0.0, 1.0, 0.0])
        bl = cf.get_beam(b)
        s.add_tracer('NuMap', f'band{b+1}',
                     quantity='cmb_polarization',
                     spin=2, nu=nus, bandpass=bnu,
                     ell=ls, beam=bl,
                     nu_unit='GHz',
                     map_unit='uK_CMB')
    return s



for seed in range(args.seed_ini, args.seed_ini+args.nsims):
    print(seed)
    sseed = "%04d" % seed
    fname = f"{args.dir_data}/cls_{sseed}.npz"
    cls = np.load(fname)['cls'][:, 3, :]
    s = gen_sacc_init()
    for b1, b2, icl in cf.pair_ordering():
        n1 = f'band{b1+1}'
        n2 = f'band{b2+1}'
        s.add_ell_cl('cl_bb', n1, n2, ell_eff, cls[icl], window=Bbl[icl])
    s.add_covariance(cov)
    s.save_fits(f"{args.dir_cov}/cls_{args.run_name}_{sseed}.fits", overwrite=True)
