#!/bin/bash
#PBS -l walltime=60:00:00
#PBS -l select=1:mem=30gb:cluster=nympha

module add gsl-2.1-gcc
module add root-6.14.04
module add python36-modules-gcc
module add boost-1.60-gcc-serial
module add cmake/3.15.3

cd /storage/brno12-cerit/home/poledto1/hydro/hybrid/root_scripts/spectrum

root -q -b 'antispectrum.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-20-30-norm150-3000-deuteron/",100,200,"lhc2760-20-30-norm150-3000")'
root -q -b 'antispectrum.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-30-40-norm150-3000-deuteron/",100,200,"lhc2760-30-40-norm150-3000")'
root -q -b 'antispectrum.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-40-50-norm150-3000-deuteron/",100,200,"lhc2760-40-50-norm150-3000")'
root -q -b 'antispectrum.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-50-60-norm150-3000-deuteron/",100,200,"lhc2760-50-60-norm150-3000")'
root -q -b 'antispectrum.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-60-70-norm150-3000-deuteron/",100,200,"lhc2760-60-70-norm150-3000")'
root -q -b 'antispectrum.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-70-80-norm150-3000-deuteron/",100,200,"lhc2760-70-80-norm150-3000")'
root -q -b 'antispectrum.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-80-90-norm150-3000-deuteron/",100,200,"lhc2760-80-90-norm150-3000")'