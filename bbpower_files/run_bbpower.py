import numpy as np
import os
import argparse


def get_bbpower_command(info):
    prefix_out = info['prefix_out']+'/'
    fname_sacc = info['sacc']
    pyexec = info.get('pyexec', 'python')
    cmd = f'{pyexec} -m bbpower BBCompSep '
    cmd += f'--cells_coadded={fname_sacc} '
    cmd += f'--cells_coadded_cov={fname_sacc} '
    cmd += f'--cells_noise=None '
    cmd += f'--cells_fiducial=None '
    cmd += f'--output_dir={prefix_out} '
    cmd += f'--config_copy={prefix_out}bbpower_copy '
    cmd += f'--config={prefix_out}config.yml'
    return cmd


def get_bbpower_config(info):
    A_sync_BB = info['fg'].get('A_sync_BB', 1.6)
    alpha_sync_BB = info['fg'].get('alpha_sync_BB', -0.93)
    A_dust_BB = info['fg'].get('A_dust_BB', 28.0)
    alpha_dust_BB = info['fg'].get('alpha_dust_BB', -0.16)
    Alens = info['fg'].get('Alens', 1.)
    r = info['fg'].get('r', 0.)
    beta_sync = info['fg'].get('beta_sync', -3.0)
    nu0_sync = 23.
    beta_dust = info['fg'].get('beta_dust', 1.54)
    temp_dust = info['fg'].get('temp_dust', 20.0)
    nu0_dust = 353.
    use_moments = info['fg'].get("use_moments", False)
    use_decorr = info['fg'].get("use_decorr", False)
    sampler = info.get('sampler', 'single_point')
    nwalkers = info.get('nwalkers', 32)
    nsamples = info.get('nsamples', 10000)

    stout=""
    stout+="# These parameters are accessible to all stages\n"
    stout+="global:\n"
    stout+="    # HEALPix resolution parameter\n"
    stout+="    nside: 256\n"
    stout+="    # Use D_l = l*(l+1)*C_l/(2*pi) instead of C_l?\n"
    stout+="    compute_dell: True\n"
    stout+="\n"
    stout+="BBCompSep:\n"
    stout+="    # Sampler type. Options are:\n"
    stout+="    #  - 'emcee': a full MCMC will be run using emcee.\n"
    stout+="    #  - 'fisher': only the Fisher matrix (i.e. the likelihood\n"
    stout+="    #        Hessian matrix) will be calculated around the fiducial\n"
    stout+="    #        parameters chosen as prior centers.\n"
    stout+="    #  - 'maximum_likelihood': only the best-fit parameters will\n"
    stout+="    #        be searched for.\n"
    stout+="    #  - 'single_point': only the chi^2 at the value used as the\n"
    stout+="    #        center for all parameter priors will be calculated.\n"
    stout+="    #  - 'timing': will compute the average time taken by one\n"
    stout+="    #        likelihood computation.\n"
    stout+=f"    sampler: {sampler}\n"
    stout+="    # If you chose emcee:\n"
    stout+="    # Number of walkers\n"
    stout+=f"    nwalkers: {nwalkers}\n"
    stout+="    # Number of iterations per walker\n"
    stout+=f"    n_iters: {nsamples}\n"
    stout+="    # Likelihood type. Options are:\n"
    stout+="    #  - 'chi2': a standard chi-squared Gaussian likelihood.\n"
    stout+="    #  - 'h&l': Hamimeche & Lewis likelihood.\n"
    stout+="    likelihood_type: 'chi2'\n"
    stout+="    # Which polarization channels do you want to include?\n"
    stout+="    # Can be ['E'], ['B'] or ['E','B'].\n"
    stout+="    pol_channels: ['B']\n"
    stout+="    # Scale cuts (will apply to all frequencies)\n"
    stout+="    l_min: 30\n"
    stout+="    l_max: 300\n"
    stout+="\n"
    stout+="    # CMB model\n"
    stout+="    cmb_model:\n"
    stout+="        # Template power spectrum. Should contained the lensed power spectra\n"
    stout+="        # with r=0 and r=1 respectively.\n"
    stout+="        cmb_templates: [\"./examples/data/camb_lens_nobb.dat\", \n"
    stout+="                        \"./examples/data/camb_lens_r1.dat\"]\n"
    stout+="        # Free parameters\n"
    stout+="        params:\n"
    stout+="            # tensor-to-scalar ratio\n"
    stout+="            # See below for the meaning of the different elements in the list.\n"
    stout+=f"            r_tensor: ['r_tensor', 'tophat', [-0.1, {r}, 0.1]]\n"
    stout+="            # Lensing amplitude\n"
    stout+=f"            A_lens: ['A_lens', 'tophat', [0.00,{Alens},2.00]]\n"
    stout+="\n"
    stout+="    # Foreground model\n"
    stout+="    fg_model:\n"
    stout+="        # Include moment parameters?\n"
    stout+=f"        use_moments: {use_moments}\n"
    stout+="        moments_lmax: 384\n"
    stout+="\n"
    stout+="        # Add one section per component. They should be called `component_X`,\n"
    stout+="        # starting with X=1\n"
    stout+="        component_1:\n"
    stout+="            # Name for this component\n"
    stout+="            name: Dust\n"
    stout+="            # Type of SED. Should be one of the classes stored in fgbuster.components\n"
    stout+="            # https://github.com/fgbuster/fgbuster/blob/master/fgbuster/component_model.py\n"
    stout+="            sed: Dust\n"
    stout+="            # Type of power spectra for all possible polarization channel combinations.\n"
    stout+="            # Any combinations not added here will be assumed to be zero.\n"
    stout+="            # The names should be one of the classes in bbpower/fgcls.py. This is quite\n"
    stout+="            # limiter for now, so consider adding to it if you want something fancier.\n"
    stout+="            cl:\n"
    stout+="                EE: ClPowerLaw\n"
    stout+="                BB: ClPowerLaw\n"
    stout+="            # Parameters of the SED\n"
    stout+="            sed_parameters:\n"
    stout+="                # The key can be anything you want, but each parameter in the model\n"
    stout+="                # must have a different name.\n"
    stout+="                # The first item in the list is the name of the parameter used by fgbuster\n"
    stout+="                # The second item is the type of prior. The last item are the numbers\n"
    stout+="                # necessary to define the prior. They should be:\n"
    stout+="                #  - Gaussian: [mean,sigma]\n"
    stout+="                #  - tophat: [lower edge, start value, upper edge]\n"
    stout+="                #  - fixed: [parameter value]\n"
    stout+="                # nu0-type parameters can only be fixed.\n"
    stout+=f"                beta_d: ['beta_d', 'Gaussian', [{beta_dust}, 0.11]]\n"
    stout+=f"                temp_d: ['temp', 'fixed', [{temp_dust}]]\n"
    stout+=f"                nu0_d: ['nu0', 'fixed', [{nu0_dust}]]\n"
    if use_decorr:
        stout+="            decorr:\n"
        stout+="                decorr_amp_d: ['decorr_amp', 'tophat', [0.9, 1.0, 1.1]]\n"
        stout+=f"                decorr_nu0_d: ['decorr_nu0', 'fixed', [{nu0_dust}]]\n"
    stout+="            cl_parameters:\n"
    stout+="                # Same for power spectrum parameters\n"
    stout+="                # (broken down by polarization channel combinations)\n"
    stout+="                EE:\n"
    stout+=f"                   amp_d_ee: ['amp', 'tophat', [0., {A_dust_BB}, \"inf\"]]\n"
    stout+=f"                   alpha_d_ee: ['alpha', 'tophat', [-1., {alpha_dust_BB}, 0.]]\n"
    stout+="                   l0_d_ee: ['ell0', 'fixed', [80.]]\n"
    stout+="                BB:\n"
    stout+=f"                   amp_d_bb: ['amp', 'tophat', [0., {A_dust_BB}, \"inf\"]]\n"
    stout+=f"                   alpha_d_bb: ['alpha', 'tophat', [-1., {alpha_dust_BB}, 0.]]\n"
    stout+="                   l0_d_bb: ['ell0', 'fixed', [80.]]\n"
    stout+="            # If this component should be correlated with any other, list them here\n"
    stout+="            cross:\n"
    stout+="                # In this case the list should contain:\n"
    stout+="                # [component name, prior type, prior parameters]\n"
    stout+="                # Each of this will create a new parameter, corresponding to a constant\n"
    stout+="                # scale- and frequency-independend correlation coefficient between\n"
    stout+="                # the two components.\n"
    stout+="                epsilon_ds: ['component_2', 'tophat', [-1., 0., 1.]]\n"
    stout+="            moments:\n"
    stout+="                # Define gammas for varying spectral indices of components\n"
    stout+="                gamma_d_beta : ['gamma_beta', 'tophat', [-6., -3.5, -2.]]\n"
    stout+="                amp_d_beta : ['amp_beta', 'tophat', [0., 0., 1]]\n"
    stout+="\n"
    stout+="        component_2:\n"
    stout+="            name: Synchrotron\n"
    stout+="            sed: Synchrotron\n"
    stout+="            cl:\n"
    stout+="                EE: ClPowerLaw\n"
    stout+="                BB: ClPowerLaw\n"
    stout+="            sed_parameters:\n"
    stout+=f"                beta_s: ['beta_pl', 'Gaussian', [{beta_sync}, 0.3]]\n"
    stout+=f"                nu0_s: ['nu0', 'fixed', [{nu0_sync}]]\n"
    stout+="            cl_parameters:\n"
    stout+="                EE:\n"
    stout+=f"                    amp_s_ee: ['amp', 'tophat', [0., {A_sync_BB}, \"inf\"]]\n"
    stout+=f"                    alpha_s_ee: ['alpha', 'tophat', [-1., {alpha_sync_BB}, 0.]]\n"
    stout+="                    l0_s_ee: ['ell0', 'fixed', [80.]]\n"
    stout+="                BB:\n"
    stout+=f"                    amp_s_bb: ['amp', 'tophat', [0., {A_sync_BB}, \"inf\"]]\n"
    stout+=f"                    alpha_s_bb: ['alpha', 'tophat', [-1., {alpha_sync_BB}, 0.]]\n"
    stout+="                    l0_s_bb: ['ell0', 'fixed', [80.]]\n" 
    if use_decorr:
        stout+="            decorr:\n"
        stout+="                decorr_amp_s: ['decorr_amp', 'tophat', [0.9, 1.0, 1.1]]\n"
        stout+=f"                decorr_nu0_s: ['decorr_nu0', 'fixed', [{nu0_sync}]]\n"
    stout+="            moments:\n"
    stout+="                # Define gammas for varying spectral indices of components\n"
    stout+="                gamma_s_beta : ['gamma_beta', 'tophat', [-6., -3.5, -2.]]\n"
    stout+="                amp_s_beta : ['amp_beta', 'tophat', [0., 0., 1]]\n"
    stout+="\n"
    f = open(info['prefix_out'] + '/config.yml', 'w')
    f.write(stout)


    

parser = argparse.ArgumentParser(description="Run bbpower")
parser.add_argument('--Alens_suffix', type=str, help="Alens")
parser.add_argument('--fg_suffix', type=str, help="FG type")
parser.add_argument('--noise_suffix', type=str, help="Noise type")
parser.add_argument('--sampler', type=str, default='fisher', help="Sampler type")
parser.add_argument('--seed_ini', type=int, default=0,
                    help="Seed to start from")
parser.add_argument('--nsims', type=int, default=500,
                    help="Number of sims to process")
parser.add_argument('--use_moments', action='store_true', default=False,
                    help="Use moment expansion")
args = parser.parse_args()

prefix_glob = '/mnt/extraspace/damonge/SO_UK/BBSims/outputs/'
noise_suffix = args.noise_suffix
fg_suffix = args.fg_suffix
alens_suffix = args.Alens_suffix

dirname = f'{prefix_glob}{fg_suffix}_{alens_suffix}_{noise_suffix}/'
mom = '_wmom' if args.use_moments else ''

for seed in range(args.seed_ini, args.seed_ini+args.nsims):
    print(seed)
    sseed = "%04d" % seed
    params = {'prefix_out': f'{dirname}results_{fg_suffix}_{alens_suffix}_{sseed}{mom}',
              'sacc': f'{dirname}cls_{fg_suffix}_{alens_suffix}_{sseed}.fits',
              'sampler': args.sampler, 'fg': {'use_moments': args.use_moments},
              'pyexec': '/users/damonge/miniconda3/envs/rosatx/bin/python'}
              

    os.system(f"mkdir -p {params['prefix_out']}")
    get_bbpower_config(params)
    cmd = get_bbpower_command(params)
    os.system(cmd)
