import numpy as np
import h5py
from tqdm import tqdm

resolutions = [32, 64, 128, 256, 512, 1024, 2048]

results = []

Nx = 4
path_ref = f'perturb/amplitude8/ref_perturb8.h5'
file_ref = h5py.File(path_ref, 'r')
Nite = len(file_ref.keys())-2
entire_v_ref = np.array(file_ref[f'ite_{Nite-1:04}/v'])[:, Nx//2]

for N in tqdm(resolutions):
  #N//4
  dy = 2.0 / N
  dV = dy * dy

  path = f'hse/isentropic_{N}/run.h5'
  file = h5py.File(path, 'r')
  Nite = len(file.keys())-2
  final_v = np.array(file[f'ite_{Nite-1:04}/v'])[:, Nx//2]

  r = len(entire_v_ref) // N
  v_ref = entire_v_ref.reshape((N,r))
  v_ref_avg = v_ref.mean(axis=1)

  diff = final_v - v_ref_avg
  velocity_L1 = np.sum(np.abs(diff)) * dV

  results.append((N, velocity_L1))

np.savetxt('perturb_velocity.dat', np.array(results))
