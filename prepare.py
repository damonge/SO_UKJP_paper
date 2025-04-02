import numpy as np
import healpy as hp
import matplotlib.pyplot as plt
import config as cf
import pymaster as nmt


# Construct beams
print("Beams")
beams = np.array([cf.get_beam(i) for i in range(cf.gl.nbands)])
print(beams.shape)


# Read mask
print("Mask")
mask = cf.get_mask()


# Construct fields
print("Fields")
fields = [nmt.NmtField(mask, None, spin=2, purify_b=True, beam=bl)
          for bl in beams]

# Bins
print("Bins")
b = cf.get_bins()

# Construct all workspaces
print("Workspaces")
for i, j, ncl in cf.pair_ordering():
    print(i, j, ncl)
    f1 = fields[i]
    f2 = fields[j]
    w = nmt.NmtWorkspace.from_fields(f1, f2, b)
    w.write_to(cf.get_workspace_fname(i, j))
    bbl = w.get_bandpower_windows()
    np.savez(cf.get_Bbl_fname(i, j), Bbl=bbl)
