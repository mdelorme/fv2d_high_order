import numpy as np
import h5py
from tqdm import tqdm
import matplotlib.pyplot as plt

L = 2
Nx = 4

"large perturbation"

N_ref = 8192
y_ref = np.linspace(0,L,N_ref)
path_ref = f'perturb/amplitude1/ref_perturb1.h5'
file_ref = h5py.File(path_ref, 'r')
Nite = len(file_ref.keys())-2
v_ref = np.array(file_ref[f'ite_{Nite-1:04}/v'])[:, Nx//2]

N = 512
y = np.linspace(0,L,N)
path_wb = f'perturb/amplitude1/pcm_wb/hse/isentropic_{N}/run.h5'
file_wb = h5py.File(path_wb, 'r')
Nite = len(file_wb.keys())-2
v_wb = np.array(file_wb[f'ite_{Nite-1:04}/v'])[:, Nx//2]

path_weno = f'perturb/amplitude1/pcm_wb/hse/isentropic_{N}/run.h5'
file_weno = h5py.File(path_weno, 'r')
Nite = len(file_weno.keys())-2
v_weno = np.array(file_weno[f'ite_{Nite-1:04}/v'])[:, Nx//2]

plt.figure(figsize=(30,15))
plt.plot(y_ref, v_ref, label='Reference (N=8192)', color='b')
plt.plot(y, v_wb, label='pcm_wb (N=512)', color='r')
plt.plot(y, v_weno, label='weno5 (N=512)', color='g')

plt.xlabel('y')
plt.ylabel('velocity')
plt.title('velocity, amplitude=1e-1')
plt.legend()
plt.tight_layout()
plt.show()



"small perturbation"

path_ref = f'perturb/amplitude8/ref_perturb8.h5'
file_ref = h5py.File(path_ref, 'r')
Nite = len(file_ref.keys())-2
v_ref = np.array(file_ref[f'ite_{Nite-1:04}/v'])[:, Nx//2]

path_wb = f'perturb/amplitude8/pcm_wb/hse/isentropic_{N}/run.h5'
file_wb = h5py.File(path_wb, 'r')
Nite = len(file_wb.keys())-2
v_wb = np.array(file_wb[f'ite_{Nite-1:04}/v'])[:, Nx//2]

path_weno = f'perturb/amplitude8/pcm_wb/hse/isentropic_{N}/run.h5'
file_weno = h5py.File(path_weno, 'r')
Nite = len(file_weno.keys())-2
v_weno = np.array(file_weno[f'ite_{Nite-1:04}/v'])[:, Nx//2]

plt.figure(figsize=(30,15))
plt.plot(y_ref, v_ref, label='Reference (N=8192)', color='b')
plt.plot(y, v_wb, label='pcm_wb (N=512)', color='r')
plt.plot(y, v_weno, label='weno5 (N=512)', color='g')

plt.xlabel('y')
plt.ylabel('velocity')
plt.title('velocity, amplitude=1e-8')
plt.legend()
plt.tight_layout()
plt.show()


