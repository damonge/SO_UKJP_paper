import numpy as np
import healpy as hp
import pymaster as nmt
import sacc
import noisecalc as nc


class Global(object):
    def __init__(self):
        self.nbands = 6
        self.nside = 256
        self.npix = hp.nside2npix(self.nside)
        self.freqs = np.array([27., 39., 93., 145., 225., 280.])
        self.fwhms = np.array([91., 63., 30., 17., 11., 9.])
        self.fsky = 0.1
        self.root = "/mnt/extraspace/damonge/SO_UK/BBSims/"
        self.nlb = 10


gl = Global()


def get_ells():
    return np.arange(3*gl.nside)


def get_beam(band):
    fwhm = gl.fwhms[band]
    sigma = np.radians(fwhm/60)/2.355
    ls = get_ells()
    return np.exp(-0.5*ls*(ls+1)*sigma**2)


def get_binary_mask():
    return hp.read_map(f"{gl.root}mask_binary.fits.gz")


def get_mask():
    return hp.ud_grade(
        hp.read_map(f"{gl.root}mask_apodized.fits"),
        nside_out=gl.nside)


def get_nls(sens, oof, N_tube_years):
    lmax = 3*gl.nside-1
    one_over_f_mode = {'optimistic': 1, 'pessimistic': 0}[oof]
    ncal = nc.SOSatV3point1(sensitivity_mode=sens,
                            N_tubes=N_tube_years,
                            survey_years=1.0,
                            one_over_f_mode=one_over_f_mode)
    l, _, nl_from_2 = ncal.get_noise_curves(f_sky=gl.fsky,
                                            ell_max=lmax+1,
                                            delta_ell=1,
                                            deconv_beam=False)
    nl = np.zeros([gl.nbands, lmax+1])
    nl[:, 2:] = nl_from_2
    return get_ells(), nl


def get_component_map_paths(component,
                            simtype,
                            seed):
    if component == 'sync':  # Fix this typical typo
        component = 'synch'

    if component not in  ['cmb', 'dust', 'synch']:
        raise NotImplementedError(f"Unknown component {component}")
    
    if component == 'cmb':
        sseed = '%04d' % seed
        fnames = [f"{gl.root}cmb/{sseed}/SO_SAT_{int(freq)}_cmb_{sseed}_CMB_r0_20201207.fits.gz"
                  for freq in gl.freqs]
        return fnames

    if simtype in ['Gaussian', 'gaussian']:
        sseed = '%04d' % seed
        fnames = [f"{gl.root}gaussian/{sseed}/"+
                  f"SO_SAT_{int(freq)}_{component}_{sseed}_gaussian_20201207.fits.gz"
                  for freq in gl.freqs]
        return fnames

    raise NotImplementedError("Only CMB and Gaussian foregrounds available")


def get_maps_sim(seed, fg_type, A_lens=1.0,
                 with_cmb=True, with_fg=True, with_noise=True,
                 sens='baseline', oof='optimistic', N_tube_years=[1, 9, 5]):
    if with_cmb:
        names = get_component_map_paths('cmb', None, seed)
        maps = np.array([hp.ud_grade(hp.read_map(nm, field=None),
                                     nside_out=gl.nside)
                         for nm in names])
        if A_lens < 1.0:
            maps *= np.sqrt(A_lens)
    else:
        maps = np.zeros([gl.nbands, 2, gl.npix])

    if with_fg:
        for comp in ['dust', 'synch']:
            names = get_component_map_paths(comp, fg_type, seed)
            maps += np.array([hp.ud_grade(hp.read_map(nm, field=None),
                                          nside_out=gl.nside)
                              for nm in names])

    if with_noise:
        np.random.seed(seed)
        # Account for noise inhomogeneity
        mskb = get_binary_mask()
        msk = get_mask()
        nhits = msk/np.amax(msk)
        nhits[nhits < 1E-3] = 1
        inhom = mskb/np.sqrt(nhits)
        _, nls = get_nls(sens, oof, N_tube_years)
        nmaps = np.zeros([gl.nbands, 2, gl.npix])
        for i in range(gl.nbands):
            nl = nls[i]
            nmaps[i, 0, :] = hp.synfast(nl, nside=gl.nside)*inhom
            nmaps[i, 1, :] = hp.synfast(nl, nside=gl.nside)*inhom
        maps += nmaps

    return maps


def get_bins():
    return nmt.NmtBin.from_nside_linear(gl.nside, nlb=gl.nlb)


def get_workspace_fname(b1, b2):
    if b2 < b1:
        fname = f"{gl.root}wsps/wsp_{b2}_{b1}.fits"
    fname = f"{gl.root}wsps/wsp_{b1}_{b2}.fits"
    return fname


def get_Bbl_fname(b1, b2):
    if b2 < b1:
        fname = f"{gl.root}wsps/Bbl_{b2}_{b1}.npz"
    fname = f"{gl.root}wsps/Bbl_{b1}_{b2}.npz"
    return fname


def pair_ordering():
    ncls = 0
    for b1 in range(gl.nbands):
        for b2 in range(b1, gl.nbands):
            yield b1, b2, ncls
            ncls += 1
