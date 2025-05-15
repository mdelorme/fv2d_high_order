# High order experiments for FV2D

This repo is made to store and track the experiments made for the implementation and validation of high-order solvers in FV2D. In particular all the tests regarding the conservation of hydrostatic equilibrium.

## Getting started

First clone the repo

```bash
git clone git@github.com:mdelorme/fv2d_high_order.git
cd fv2d_high_order
```

Then, create a symbolic link to `fv2d` in the `fv2d_high_order` folder. For instance if the `fv2d` binary is, relative to the current folder, placed at `../../fv2d/build/fv2d` the symbolic link command should be

```bash
ln -s ../../fv2d/build/fv2d fv2d
```

Now, everything is in place for running the experiment. Generate all the profiles and run fv2d on them :
```bash
./run_all.sh
```

This will take some time. At the end, the subfolder `hse` will be filled with all the runs, and profiles. In the current directory, you should also find a `hse.dat` file containing three columns : 1. the number of cell in an experiment; 2. The L1 error of the run with the isentropic profile; 3. The L1 error of the run with the isothermal profile. Finally you will also find the logs for each run in the files `log_isentropic_N.log` and `log_isothermal_N.log`.

## Modifying the runs

To run the experiment on a different configuration, simply edit the `template.ini` file and re-run `run_all.sh`. Be aware though that the contents of `hse` will be removed, so remember to back-up what has already been calculated before re-running the script.


