import pptk
import numpy as np
import plyfile

data = plyfile.PlyData.read('output.ply')['vertex']
xyz = np.c_[data['x'], data['y'], data['z']]
rgb = np.c_[data['red'], data['green'], data['blue']]
# n = np.c_[data['nx'], data['ny'], data['nz']]

v = pptk.viewer(xyz)
# v.attributes(rgb / 255., 0.5 * (1 + n))