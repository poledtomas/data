#!/bin/bash
#PBS -l walltime=90:00:00
#PBS -l select=1:mem=10gb:cluster=nympha

module add gsl-2.1-gcc
module add root-6.14.04
module add python36-modules-gcc
module add boost-1.60-gcc-serial
module add cmake/3.15.3

cd /storage/brno12-cerit/home/poledto1/hydro/hybrid/root_scripts/v2

root -q -b 'vn_C_pT_pair.c("../../sampler.out/lhc2760-10-20-norm114-3000/",3000,500,2,2212,"LHC276_1020_3000")'