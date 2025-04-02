import numpy as np
import healpy as hp
import matplotlib.pyplot as plt
import config as cf
import pymaster as nmt
import argparse
import os
import yaml


parser = argparse.ArgumentParser(description="Compute all cls for a bunch of sims")
parser.add_argument('run_name', type=str, help='Output directory')
parser.add_argument('--with_cmb', action='store_true', default=True,
                    help="Include CMB")
parser.add_argument('--no_cmb', dest='with_cmb', action='store_false',
                    help="Exclude CMB")
parser.add_argument('--with_fg', action='store_true', default=True,
                    help="Include foregrounds")
parser.add_argument('--no_fg', dest='with_fg', action='store_false',
                    help="Exclude foregrounds")
parser.add_argument('--with_noise', action='store_true', default=True,
                    help="Include noise")
parser.add_argument('--no_noise', dest='with_noise', action='store_false',
                    help="Exclude noise")
parser.add_argument('--ntube_LF', type=float, default=1.0,
                    help="Number of tube-years in LF")
parser.add_argument('--ntube_MF', type=float, default=9.0,
                    help="Number of tube-years in MF")
parser.add_argument('--ntube_UHF', type=float, default=5.0,
                    help="Number of tube-years in UHF")
parser.add_argument('--sensitivity', type=str, default='baseline',
                    help="White noise type")
parser.add_argument('--one_over_f', type=str, default='optimistic',
                    help="One-over-eff noise type")
parser.add_argument('--Alens', type=float, default=1.0,
                    help="Alens")
parser.add_argument('--seed_ini', type=int, default=0,
                    help="Seed to start from")
parser.add_argument('--nsims', type=int, default=500,
                    help="Number of sims to process")
args = parser.parse_args()

output_dir = f"{cf.gl.root}outputs/{args.run_name}"
os.system(f"mkdir -p {output_dir}")

print("Saving run params")
dsave = vars(args)
with open(f"{output_dir}/run_params.yml", 'w') as f:
    yaml.dump(dsave, f)

print("Bins")
b = cf.get_bins()

print("Beams")
beams = np.array([cf.get_beam(i) for i in range(cf.gl.nbands)])
print(beams.shape)

print("Mask")
mask = cf.get_mask()

print("Workspaces")
wsps = [nmt.NmtWorkspace.from_file(cf.get_workspace_fname(b1, b2))
        for b1, b2, _ in cf.pair_ordering()]

for seed in range(args.seed_ini, args.seed_ini+args.nsims):
    try:
        print(f"Simulation {seed}")
        maps = cf.get_maps_sim(seed, 'gaussian',
                               A_lens=args.Alens,
                               with_cmb=args.with_cmb,
                               with_fg=args.with_fg,
                               with_noise=args.with_noise,
                               sens=args.sensitivity,
                               oof=args.one_over_f,
                               N_tube_years=[args.ntube_LF, args.ntube_MF, args.ntube_UHF])

        print("Fields")
        fields = [nmt.NmtField(mask, mp, spin=2, purify_b=True, beam=bl)
                  for mp, bl in zip(maps, beams)]

        print("Cls")
        cls = []
        for b1, b2, icl in cf.pair_ordering():
            f1 = fields[b1]
            f2 = fields[b2]
            wsp = wsps[icl]
            cl = wsp.decouple_cell(nmt.compute_coupled_cell(f1, f2))
            cls.append(cl)
        cls = np.array(cls)

        print("Saving")
        sseed = "%04d" % seed
        np.savez(f"{output_dir}/cls_{sseed}.npz", cls=cls)
    except:
        print(f"Error with {seed}")
