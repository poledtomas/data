#!/bin/bash
#PBS -l walltime=70:00:00
#PBS -l select=1:mem=30gb

module add gsl-2.1-gcc
module add root-6.14.04
module add python36-modules-gcc
module add boost-1.60-gcc-serial
module add cmake/3.15.3

cd /storage/brno12-cerit/home/poledto1/hydro/hybrid/root_scripts/v2/data


root -q -b 'vn_C_pT_pair.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-10-20-norm114-3000-deuteron-zetaS3-0.2/",100,200,2,211,"lhc2760-10-20-norm114-3000-deuteron-zetaS3-0.2")'
root -q -b 'vn_C_pT_pair.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-10-20-norm114-3000-deuteron-zetaS3-0.4/",100,200,2,211,"lhc2760-10-20-norm114-3000-deuteron-zetaS3-0.4")'
root -q -b 'vn_C_pT_pair.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-10-20-norm114-3000-deuteron-zetaS3-0.8/",100,200,2,211,"lhc2760-10-20-norm114-3000-deuteron-zetaS3-0.8")'

root -q -b 'vn_C_pT_pair.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-20-30-norm114-3000-deuteron-zetaS3-0.2/",100,200,2,211,"lhc2760-20-30-norm114-3000-deuteron-zetaS3-0.2")'
root -q -b 'vn_C_pT_pair.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-20-30-norm114-3000-deuteron-zetaS3-0.4/",100,200,2,211,"lhc2760-20-30-norm114-3000-deuteron-zetaS3-0.4")'
root -q -b 'vn_C_pT_pair.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-20-30-norm114-3000-deuteron-zetaS3-0.8/",100,200,2,211,"lhc2760-20-30-norm114-3000-deuteron-zetaS3-0.8")'
