import numpy as np
import h5py
from tqdm import tqdm

resolutions = [32, 64, 128, 256, 512, 1024, 2048]

results = []
for N in tqdm(resolutions):
  Nx = 4 #N//4
  dy = 2.0 / N
  
  path_isentropic = f'hse/isentropic_{N}/run.h5'
  f_isentropic = h5py.File(path_isentropic, 'r')
  Nite = len(f_isentropic.keys())-2
  init_pressure = np.array(f_isentropic['ite_0000/prs'])[:, Nx//2]
  final_pressure = np.array(f_isentropic[f'ite_{Nite-1:04}/prs'])[:, Nx//2]

  diff = init_pressure - final_pressure
  isentropic_L1 = np.sum(np.abs(diff)) * dy
  isentropic_max_v = np.max(np.abs(f_isentropic[f'ite_{Nite-1:04}/v']))

  path_isothermal = f'hse/isothermal_{N}/run.h5'
  f_isothermal = h5py.File(path_isothermal, 'r')
  Nite = len(f_isothermal.keys())-2
  init_pressure = np.array(f_isothermal['ite_0000/prs'])[:, Nx//2]
  final_pressure = np.array(f_isothermal[f'ite_{Nite-1:04}/prs'])[:, Nx//2]

  diff = init_pressure - final_pressure
  isothermal_L1 = np.sum(np.abs(diff)) * dy
  isothermal_max_v = np.max(np.abs(f_isothermal[f'ite_{Nite-1:04}/v']))

  results.append((N, isentropic_L1, isothermal_L1, isentropic_max_v, isothermal_max_v))

np.savetxt('hse.dat', np.array(results))
