"""courbes d'erreurs sur la velocite en fonction de la resolution en presence d'une perturbation (isentropic)"""

import os
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.ticker as ticker


dir_ampl = ['amplitude1', 'amplitude6', 'amplitude8']
dir_method = ['pcm_wb', 'plm', 'weno5']
colors = ['r', 'g', 'b']
linestyles = ['-', '--', ':']
labels = [[r'PCM-WB, $A=10^{-1}$', r'PLM, $A=10^{-1}$', r'WENO5, $A=10^{-1}$'], [r'PCM_WB, $A=10^{-6}$', r'PLM, $A=10^{-6}$', r'WENO5, $A=10^{-6}$'], [r'PCM_WB, $A=10^{-8}$', r'PLM, $A=10^{-8}$', r'WENO5, $A=10^{-8}$']]

Npts = (32, 64, 128, 256, 512, 1024, 2048)
fig, ax = plt.subplots(figsize=(30,16))

for i, ampl in enumerate(dir_ampl):
    ampl_data = []
    for meth in dir_method:
        data_path = os.path.join('./perturb/', ampl, meth, 'perturb_velocity.dat')
        data = np.loadtxt(data_path)
        N = data[:,0]
        L1_velocity = data[:, 1]
    
        ampl_data.append((N, L1_velocity))
    
    for (logN, logL1), linestyle, label in zip(ampl_data, linestyles, labels[i]):
        ax.plot(logN, logL1, 'x-', color=colors[i], linestyle=linestyle, label=label)


ax.set_title(r'$L1(v - v_{ref})$ en fonction de $N$')
ax.set_xlabel('N')
ax.set_ylabel(r'$L1$')
ax.set_yscale('log')
ax.set_xscale('log')
ax.grid(True)
ax.xaxis.set_major_locator(ticker.FixedLocator(Npts))
ax.xaxis.set_major_formatter(ticker.StrMethodFormatter("{x:d}"))
ax.legend()

plt.tight_layout()
plt.show()

