import numpy as np
import argparse


parser = argparse.ArgumentParser(description="Compute covariance from sims")
parser.add_argument('output_dir', type=str, help='Output directory')
args = parser.parse_args()

cls = []
for seed in range(500):
    sseed = "%04d" % seed
    fname = f"{args.output_dir}/cls_{sseed}.npz"
    print(fname)
    try:
        cl = np.load(fname)['cls']
        cls.append(cl)
    except:
        print(f"Missed {seed}")
cls = np.array(cls)

nsims, ncls, npols, nbpw = cls.shape
clmean = np.mean(cls, axis=0).flatten()
clmean_bb = np.mean(cls[:, :, 3, :], axis=0).flatten()
cov = np.cov(cls.reshape([nsims, ncls*npols*nbpw]).T)
cov_bb = np.cov(cls[:, :, 3, :].reshape([nsims, ncls*nbpw]).T)
np.savez(f"{args.output_dir}/summary.npz",
         clmean=clmean, clmean_bb=clmean_bb,
         cov=cov, cov_bb=cov_bb)
