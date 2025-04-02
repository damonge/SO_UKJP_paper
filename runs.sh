#!/bin/bash

pyexec=/users/damonge/miniconda3/envs/rosatx/bin/python
ncores=8


## Y25
# Gaussian, Alens=0.3, 0.1 2 1, base-opt
#addqueue -q cmb -c baseline_Y25 -s -n 1x${ncores} ${pyexec} runsim.py gaussian_Alens0p3_base_opt_Y25 --seed_ini 0 --nsims 500 --Alens=0.3 --ntube_LF 0.1 --ntube_MF 2 --ntube_UHF 1 --sensitivity baseline --one_over_f optimistic
python summarise.py /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_opt_Y25
python tosacc.py gaussian_Alens0p3 --dir_data /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_wonoise/ --dir_cov /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_opt_Y25/ --seed_ini 0 --nsims 100

## Y26
# Gaussian, Alens=0.3, 0.1 4.5 2, base-opt
#addqueue -q cmb -c baseline_Y26 -s -n 1x${ncores} ${pyexec} runsim.py gaussian_Alens0p3_base_opt_Y26 --seed_ini 0 --nsims 500 --Alens=0.3 --ntube_LF 0.1 --ntube_MF 4.5 --ntube_UHF 2 --sensitivity baseline --one_over_f optimistic
python summarise.py /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_opt_Y26
python tosacc.py gaussian_Alens0p3 --dir_data /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_wonoise/ --dir_cov /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_opt_Y26/ --seed_ini 0 --nsims 100

## Y27
# Gaussian, Alens=0.3, 1 8.5 3, base-opt
#addqueue -q cmb -c baseline_Y27 -s -n 1x${ncores} ${pyexec} runsim.py gaussian_Alens0p3_base_opt_Y27 --seed_ini 0 --nsims 500 --Alens=0.3 --ntube_LF 1 --ntube_MF 8.5 --ntube_UHF 3 --sensitivity baseline --one_over_f optimistic
python summarise.py /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_opt_Y27
python tosacc.py gaussian_Alens0p3 --dir_data /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_wonoise/ --dir_cov /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_opt_Y27/ --seed_ini 0 --nsims 100

## Y28
# Gaussian, Alens=0.3, 2 12.5 4, base-opt
#addqueue -q cmb -c baseline_Y28 -s -n 1x${ncores} ${pyexec} runsim.py gaussian_Alens0p3_base_opt_Y28 --seed_ini 0 --nsims 500 --Alens=0.3 --ntube_LF 2 --ntube_MF 12.5 --ntube_UHF 4 --sensitivity baseline --one_over_f optimistic
python summarise.py /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_opt_Y28
python tosacc.py gaussian_Alens0p3 --dir_data /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_wonoise/ --dir_cov /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_opt_Y28/ --seed_ini 0 --nsims 100

## Y29
# Gaussian, Alens=0.3, 3 16.5 5, base-opt
#addqueue -q cmb -c baseline_Y29 -s -n 1x${ncores} ${pyexec} runsim.py gaussian_Alens0p3_base_opt_Y29 --seed_ini 0 --nsims 500 --Alens=0.3 --ntube_LF 3 --ntube_MF 16.5 --ntube_UHF 5 --sensitivity baseline --one_over_f optimistic
#python summarise.py /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_opt_Y29
#python tosacc.py gaussian_Alens0p3 --dir_data /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_wonoise/ --dir_cov /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_opt_Y29/ --seed_ini 0 --nsims 100

## Y30
# Gaussian, Alens=0.3, 4 20.5 6, base-opt
#addqueue -q cmb -c baseline_Y30 -s -n 1x${ncores} ${pyexec} runsim.py gaussian_Alens0p3_base_opt_Y30 --seed_ini 0 --nsims 500 --Alens=0.3 --ntube_LF 4 --ntube_MF 20.5 --ntube_UHF 6 --sensitivity baseline --one_over_f optimistic
#python summarise.py /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_opt_Y30
#python tosacc.py gaussian_Alens0p3 --dir_data /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_wonoise/ --dir_cov /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_opt_Y30/ --seed_ini 0 --nsims 100

## Y31
# Gaussian, Alens=0.3, 5 24.5 7, base-opt
#addqueue -q cmb -c baseline_Y31 -s -n 1x${ncores} ${pyexec} runsim.py gaussian_Alens0p3_base_opt_Y31 --seed_ini 0 --nsims 500 --Alens=0.3 --ntube_LF 5 --ntube_MF 24.5 --ntube_UHF 7 --sensitivity baseline --one_over_f optimistic
#python summarise.py /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_opt_Y31
#python tosacc.py gaussian_Alens0p3 --dir_data /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_wonoise/ --dir_cov /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_opt_Y31/ --seed_ini 0 --nsims 100

## Y32
# Gaussian, Alens=0.3, 6 28.5 8, base-opt
#addqueue -q cmb -c baseline_Y32 -s -n 1x${ncores} ${pyexec} runsim.py gaussian_Alens0p3_base_opt_Y32 --seed_ini 0 --nsims 500 --Alens=0.3 --ntube_LF 6 --ntube_MF 28.5 --ntube_UHF 8 --sensitivity baseline --one_over_f optimistic
#python summarise.py /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_opt_Y32
#python tosacc.py gaussian_Alens0p3 --dir_data /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_wonoise/ --dir_cov /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_opt_Y32/ --seed_ini 0 --nsims 100

## Y33
# Gaussian, Alens=0.3, 7 32.5 9, base-opt
#addqueue -q cmb -c baseline_Y33 -s -n 1x${ncores} ${pyexec} runsim.py gaussian_Alens0p3_base_opt_Y33 --seed_ini 0 --nsims 500 --Alens=0.3 --ntube_LF 7 --ntube_MF 32.5 --ntube_UHF 9 --sensitivity baseline --one_over_f optimistic
#python summarise.py /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_opt_Y33
#python tosacc.py gaussian_Alens0p3 --dir_data /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_wonoise/ --dir_cov /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_opt_Y33/ --seed_ini 0 --nsims 100

## Y34
# Gaussian, Alens=0.3, 8 36.5 10, base-opt
#addqueue -q cmb -c baseline_Y34 -s -n 1x${ncores} ${pyexec} runsim.py gaussian_Alens0p3_base_opt_Y34 --seed_ini 0 --nsims 500 --Alens=0.3 --ntube_LF 8 --ntube_MF 36.5 --ntube_UHF 10 --sensitivity baseline --one_over_f optimistic
#python summarise.py /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_opt_Y34
#python tosacc.py gaussian_Alens0p3 --dir_data /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_wonoise/ --dir_cov /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_opt_Y34/ --seed_ini 0 --nsims 100


## Y25
# Gaussian, Alens=0.3, 0.1 2 1, base-pess
#addqueue -q cmb -c baseline_Y25 -s -n 1x${ncores} ${pyexec} runsim.py gaussian_Alens0p3_base_pess_Y25 --seed_ini 0 --nsims 500 --Alens=0.3 --ntube_LF 0.1 --ntube_MF 2 --ntube_UHF 1 --sensitivity baseline --one_over_f pessimistic
python summarise.py /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_pess_Y25
python tosacc.py gaussian_Alens0p3 --dir_data /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_wonoise/ --dir_cov /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_pess_Y25/ --seed_ini 0 --nsims 100

## Y26
# Gaussian, Alens=0.3, 0.1 4.5 2, base-pess
#addqueue -q cmb -c baseline_Y26 -s -n 1x${ncores} ${pyexec} runsim.py gaussian_Alens0p3_base_pess_Y26 --seed_ini 0 --nsims 500 --Alens=0.3 --ntube_LF 0.1 --ntube_MF 4.5 --ntube_UHF 2 --sensitivity baseline --one_over_f pessimistic
python summarise.py /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_pess_Y26
python tosacc.py gaussian_Alens0p3 --dir_data /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_wonoise/ --dir_cov /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_pess_Y26/ --seed_ini 0 --nsims 100

## Y27
# Gaussian, Alens=0.3, 1 8.5 3, base-pess
#addqueue -q cmb -c baseline_Y27 -s -n 1x${ncores} ${pyexec} runsim.py gaussian_Alens0p3_base_pess_Y27 --seed_ini 0 --nsims 500 --Alens=0.3 --ntube_LF 1 --ntube_MF 8.5 --ntube_UHF 3 --sensitivity baseline --one_over_f pessimistic
python summarise.py /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_pess_Y27
python tosacc.py gaussian_Alens0p3 --dir_data /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_wonoise/ --dir_cov /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_pess_Y27/ --seed_ini 0 --nsims 100

## Y28
# Gaussian, Alens=0.3, 2 12.5 4, base-pess
#addqueue -q cmb -c baseline_Y28 -s -n 1x${ncores} ${pyexec} runsim.py gaussian_Alens0p3_base_pess_Y28 --seed_ini 0 --nsims 500 --Alens=0.3 --ntube_LF 2 --ntube_MF 12.5 --ntube_UHF 4 --sensitivity baseline --one_over_f pessimistic
python summarise.py /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_pess_Y28
python tosacc.py gaussian_Alens0p3 --dir_data /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_wonoise/ --dir_cov /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_pess_Y28/ --seed_ini 0 --nsims 100

## Y29
# Gaussian, Alens=0.3, 3 16.5 5, base-pess
#addqueue -q cmb -c baseline_Y29 -s -n 1x${ncores} ${pyexec} runsim.py gaussian_Alens0p3_base_pess_Y29 --seed_ini 0 --nsims 500 --Alens=0.3 --ntube_LF 3 --ntube_MF 16.5 --ntube_UHF 5 --sensitivity baseline --one_over_f pessimistic
#python summarise.py /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_pess_Y29
#python tosacc.py gaussian_Alens0p3 --dir_data /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_wonoise/ --dir_cov /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_pess_Y29/ --seed_ini 0 --nsims 100

## Y30
# Gaussian, Alens=0.3, 4 20.5 6, base-pess
#addqueue -q cmb -c baseline_Y30 -s -n 1x${ncores} ${pyexec} runsim.py gaussian_Alens0p3_base_pess_Y30 --seed_ini 0 --nsims 500 --Alens=0.3 --ntube_LF 4 --ntube_MF 20.5 --ntube_UHF 6 --sensitivity baseline --one_over_f pessimistic
#python summarise.py /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_pess_Y30
#python tosacc.py gaussian_Alens0p3 --dir_data /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_wonoise/ --dir_cov /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_pess_Y30/ --seed_ini 0 --nsims 100

## Y31
# Gaussian, Alens=0.3, 5 24.5 7, base-pess
#addqueue -q cmb -c baseline_Y31 -s -n 1x${ncores} ${pyexec} runsim.py gaussian_Alens0p3_base_pess_Y31 --seed_ini 0 --nsims 500 --Alens=0.3 --ntube_LF 5 --ntube_MF 24.5 --ntube_UHF 7 --sensitivity baseline --one_over_f pessimistic
#python summarise.py /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_pess_Y31
#python tosacc.py gaussian_Alens0p3 --dir_data /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_wonoise/ --dir_cov /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_pess_Y31/ --seed_ini 0 --nsims 100

## Y32
# Gaussian, Alens=0.3, 6 28.5 8, base-pess
#addqueue -q cmb -c baseline_Y32 -s -n 1x${ncores} ${pyexec} runsim.py gaussian_Alens0p3_base_pess_Y32 --seed_ini 0 --nsims 500 --Alens=0.3 --ntube_LF 6 --ntube_MF 28.5 --ntube_UHF 8 --sensitivity baseline --one_over_f pessimistic
#python summarise.py /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_pess_Y32
#python tosacc.py gaussian_Alens0p3 --dir_data /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_wonoise/ --dir_cov /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_pess_Y32/ --seed_ini 0 --nsims 100

## Y33
# Gaussian, Alens=0.3, 7 32.5 9, base-pess
#addqueue -q cmb -c baseline_Y33 -s -n 1x${ncores} ${pyexec} runsim.py gaussian_Alens0p3_base_pess_Y33 --seed_ini 0 --nsims 500 --Alens=0.3 --ntube_LF 7 --ntube_MF 32.5 --ntube_UHF 9 --sensitivity baseline --one_over_f pessimistic
#python summarise.py /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_pess_Y33
#python tosacc.py gaussian_Alens0p3 --dir_data /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_wonoise/ --dir_cov /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_pess_Y33/ --seed_ini 0 --nsims 100

## Y34
# Gaussian, Alens=0.3, 8 36.5 10, base-pess
#addqueue -q cmb -c baseline_Y34 -s -n 1x${ncores} ${pyexec} runsim.py gaussian_Alens0p3_base_pess_Y34 --seed_ini 0 --nsims 500 --Alens=0.3 --ntube_LF 8 --ntube_MF 36.5 --ntube_UHF 10 --sensitivity baseline --one_over_f pessimistic
#python summarise.py /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_pess_Y34
#python tosacc.py gaussian_Alens0p3 --dir_data /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_wonoise/ --dir_cov /mnt/extraspace/damonge/SO_UK/BBSims/outputs/gaussian_Alens0p3_base_pess_Y34/ --seed_ini 0 --nsims 100
