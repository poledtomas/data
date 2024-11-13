#!/bin/bash
#PBS -l walltime=60:00:00
#PBS -l select=1:mem=30gb:cluster=nympha

module add gsl-2.1-gcc
module add root-6.14.04
module add python36-modules-gcc
module add boost-1.60-gcc-serial
module add cmake/3.15.3

cd /storage/brno12-cerit/home/poledto1/hydro/hybrid/root_scripts/spectrum


root -q -b 'spectrum_deuteron.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-20-30-3000-deuteron/",3000,500,"lhc2760-20-30-3000-deuteron")'