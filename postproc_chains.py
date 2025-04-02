import numpy as np
import matplotlib.pyplot as plt
import config as cf


for wmom in ['', '_wmom']:
    print(f"Moments: {wmom}")
    for oof in ['opt', 'pess']:
        print(f"oof {oof}")
        #for Alens in ['1p0', '0p3', '0p0']:
        for Alens in ['0p3']:
            print(f" Alens = {Alens}")
            #for noise in ['1p0_9p0_5p0', '1p0_15p0_5p0', '1p0_19p0_10p0', '1p0_35p0_10p0']:
            run_summary = {'years': [], 'p_names': None, 'p_bf': [], 'p_bf_std': [],
                           'p_mean': [], 'p_sigma': [], 'p_sigma_std': [], 'p_sigma_f': []}
            for noise in ['Y25', 'Y26', 'Y27', 'Y28', 'Y29', 'Y30', 'Y31', 'Y32', 'Y33', 'Y34']:
                params = []
                sigmas_fisher = []
                means = []
                sigmas = []

                nsims = 3
                for seed in range(nsims):
                    sseed = "%04d" % seed
                    d = np.load(f"/mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens{Alens}_base_{oof}_{noise}/results_gaussian_Alens{Alens}_{sseed}{wmom}/fisher.npz")
                    params.append(d['params'])
                    try:
                        sigF = np.sqrt(np.diag(np.linalg.inv(d['fisher'])))
                    except:
                        sigF = None
                    if run_summary['p_names'] is None:
                        run_summary['p_names'] = d['names']
                    d = np.load(f"/mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens{Alens}_base_{oof}_{noise}/results_gaussian_Alens{Alens}_{sseed}{wmom}/emcee.npz")
                    # Remove burn-in
                    ch = d['chain'][:, 5000:, :]
                    # Flatten and compute stats
                    nwalkers, nsteps, nparams = ch.shape
                    ch = ch.reshape([nwalkers*nsteps, nparams])
                    means.append(np.mean(ch, axis=0))
                    sigmas.append(np.std(ch, axis=0))
                    if sigF is None:
                        sigF = np.std(ch, axis=0)
                    sigmas_fisher.append(sigF)
                params = np.array(params)
                sigmas_fisher = np.array(sigmas_fisher)
                means = np.array(means)
                sigmas = np.array(sigmas)
                run_summary['years'].append(noise)
                run_summary['p_bf'].append(np.mean(params, axis=0))
                run_summary['p_bf_std'].append(np.std(params, axis=0)/np.sqrt(nsims))
                run_summary['p_mean'].append(np.mean(means, axis=0))
                run_summary['p_sigma'].append(np.mean(sigmas, axis=0))
                run_summary['p_sigma_std'].append(np.std(sigmas, axis=0)/np.sqrt(nsims))
                run_summary['p_sigma_f'].append(np.mean(sigmas_fisher, axis=0))

                print(noise)
                print("  ", np.mean(params, axis=0)[1]*1000, np.std(params, axis=0)[1]*1000)
                print("  ", np.mean(means, axis=0)[1]*1000, np.std(means, axis=0)[1]*1000)
                print("  ", np.mean(sigmas, axis=0)[1]*1000, np.std(sigmas, axis=0)[1]*1000, np.amin(sigmas, axis=0)[1]*1000)
                print("  ", np.mean(sigmas_fisher, axis=0)[1]*1000, np.std(sigmas_fisher, axis=0)[1]*1000)
            print("\n")
            for k in ['p_bf', 'p_bf_std', 'p_mean', 'p_sigma', 'p_sigma_std', 'p_sigma_f']:
                run_summary[k] = np.array(run_summary[k])
            np.savez(f"/mnt/extraspace/damonge/SO_UK/BBSims/outputs/summary_gaussian_Alens{Alens}_base_{oof}{wmom}_years.npz", **run_summary)
        print("\n")
