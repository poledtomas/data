#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l select=1:mem=5gb:cpu_flag=avx512vl
module add gsl-2.1-gcc
module add root-6.24.00
module add python36-modules-gcc
module add boost-1.60-gcc-serial

cd /storage/brno12-cerit/home/poledto1/hydro/hybrid/root_scripts/v2/deuteron/deuteron


root -q -b 'vn_EP_pT_error.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-00-05-deuteron/",3000,500,2)'

