#!/bin/bash
#PBS -l walltime=60:00:00
#PBS -l select=1:mem=30gb

module add gsl-2.1-gcc
module add root-6.24.00
module add python36-modules-gcc
module add boost-1.60-gcc-serial


cd /storage/brno12-cerit/home/poledto1/hydro/hybrid/root_scripts/spectrum/deuteron

root -q -b 'spectrum.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-00-05-deuteron/",3000,500,"lhc2760-00-05-deuteron")'
root -q -b 'spectrum.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-05-10-deuteron/",3000,500,"lhc2760-05-10-deuteron")'
root -q -b 'spectrum.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-10-20-deuteron/",3000,500,"llhc2760-10-20-deuteron")'


