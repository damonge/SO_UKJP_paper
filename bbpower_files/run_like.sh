#!/bin/bash

pyexec=/users/damonge/miniconda3/envs/rosatx/bin/python
ncores=12

for oof in opt pess
do
    #for ntube in Y29 Y30 Y31 Y32 Y33 Y34
    for ntube in Y25 Y26 Y27 Y28
    do
	noi=base_${oof}_${ntube}
	for Al in Alens0p3
	do
	    #addqueue -q cmb -c ${noi}_${Al} -s -n 1x${ncores} ${pyexec} run_bbpower.py --Alens_suffix ${Al} --fg_suffix gaussian --noise_suffix ${noi} --seed_ini 0 --nsims 100
	    #addqueue -q cmb -c ${noi}_${Al} -s -n 1x${ncores} ${pyexec} run_bbpower.py --Alens_suffix ${Al} --fg_suffix gaussian --noise_suffix ${noi} --seed_ini 0 --nsims 10 --sampler emcee
	    #addqueue -q cmb -c ${noi}_${Al} -s -n 1x${ncores} ${pyexec} run_bbpower.py --Alens_suffix ${Al} --fg_suffix gaussian --noise_suffix ${noi} --seed_ini 0 --nsims 10 --sampler emcee --use_moments
	    addqueue -q cmb -c ${noi}_${Al} -s -n 1x${ncores} ${pyexec} run_bbpower.py --Alens_suffix ${Al} --fg_suffix gaussian --noise_suffix ${noi} --seed_ini 0 --nsims 30 --use_moments
	done
    done
done
