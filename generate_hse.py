import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy.optimize import newton
from scipy.integrate import romb
from tqdm import tqdm

## This setup comes from Kapelli, Mishra "A well-balanced finite volume scheme for the Euler equations with gravitation. The exact preservation of hydrostatic equilibrium with arbitrary entropy stratification", 2016, A&A
## The script builds a polytropic profile in hydrostatic equilibrium that can be either isothermal, or isentropic
## this profile is then generated for a certain number of points given in parameter and saved to profile_N.dat with
## N the number of points

def usage():
    print(f'Usage : python3 {sys.argv[0]} Npoints Mode')
    print(' Mode can be isentropic or isothermal')   
    exit(1)

## Reading number of points on the command line
try:
    N = int(sys.argv[1])
    mode = sys.argv[2]
except:
    usage()

if mode not in ('isothermal', 'isentropic'):
    usage()

## Base parameters
L = 2       ## Size of the box
dy = L/N    ## Spatial step 
g  = -1.0     ## Gravity
Ng = 2      ## Number fo ghosts on each side of the domain
Nt = N+2*Ng ## Total number of points in the domain

# We add ghosts on each side for prolongation
y = np.linspace((0.5-Ng)*dy, L+(Ng-0.5)*dy, N+Ng*2)

# Thermodynamics configuration
R = 1.0
cv = R*3.0/2.0
gamma0 = 5.0/3.0

# Top boundary configuration
rho0 = 1.0
p0 = 1.0

# Isentropic/isothermal configurations
S = R / (gamma0-1.0) * np.log(p0 / rho0**gamma0)
T = 1.0

rho = np.ones_like(y)
p   = np.ones_like(y)

# Recovering the pressure
if mode == 'isentropic':
    rho = np.pow(rho0**(gamma0-1.0) + g / (np.exp(S/cv)) * (gamma0-1.0)/gamma0 * y, 1.0 / (gamma0-1.0))
    p = np.exp(S/cv)*rho**gamma0
else:
    H0 = R*T/g
    rho = rho0 * np.exp(y/H0)
    p   = p0   * np.exp(y/H0)

fig, ax = plt.subplots(2, 1, figsize=(8, 10))
ax_left = ax[0]
ax_left.plot(y, rho, color='blue')
ax_left.tick_params(axis='y', labelcolor='blue')
ax_left.set_ylabel('Density', color='blue')
ax_left.set_xlim(0.0, L)
ax_right = ax_left.twinx()
ax_right.plot(y, p, color='red')
ax_right.tick_params(axis='y', labelcolor = 'red')
ax_right.set_yscale('log')
ax_right.set_ylabel('Pressure', color='red')
if mode == 'isothermal':
    ax_right.set_ylim(0.09, 1.1) 
    ax_left.set_ylim(0.1, 1.05) 
else:
    ax_right.set_ylim(0.01, 1.05)  
    ax_left.set_ylim(0.0, 1.05)

hse = (p[:-1]-p[1:]) / dy + 0.5 * (rho[1:]+rho[:-1])*g
ax[1].axhline(0.0, linestyle='--', color='black')
yhse = 0.5 * (y[:-1]+y[1:])
ax[1].plot(yhse, np.abs(hse), color='red')
ax[1].set_yscale('log')

prefix = f'profile_{mode}_{N}'

ax[0].set_xlabel('y')
ax[1].set_xlabel('y')
ax[1].set_ylabel('Hydrostatic Equilibrium error')

plt.suptitle(mode.capitalize() + " atmosphere")
plt.savefig(prefix+'.png')
plt.close('all')

## Generating output file
dat = np.empty((N, 5))
dat[:,0] = y[Ng:Ng+N]
dat[:,1] = rho[Ng:Ng+N]
dat[:,2] = 0.0 # u
dat[:,3] = 0.0 # v
dat[:,4] = p[Ng:Ng+N]
profile_filename = prefix + '.dat'
np.savetxt(profile_filename, dat)

## Calculating sound crossing time (eq 38)
one_over_cs = 1.0 / np.sqrt(gamma0 * p / rho)
tau = 2.0 * romb(one_over_cs[Ng:N+Ng+1], dx=dy)
print(f"{mode} sound crossing time tau_sound = {tau}") ## Should be ~3.1 for isothermal setups and ~4.3 for isentropic setups

## Generating ini file
f_in = open('template.ini', 'r')
template = ''.join(f_in.readlines())
f_in.close()

template = template.format(128, N, L, 2.0*tau, profile_filename, g)

f_out = open(prefix+'.ini', 'w')
f_out.write(template)
f_out.close()
