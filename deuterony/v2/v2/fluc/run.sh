#!/bin/bash
#PBS -l walltime=24:00:00
#PBS -l select=1:mem=1gb

module add gsl-2.1-gcc
module add root-6.14.04
module add python36-modules-gcc
module add boost-1.60-gcc-serial
module add cmake/3.15.3

cd /storage/brno12-cerit/home/poledto1/hydro/hybrid/root_scripts/v2/fluc
root -q -b 'vn_EP_pT.c("../../../sampler.out/lhc5020-10-20-norm135/",400,400,2,"LHC5020_1020-test-dnes")'
