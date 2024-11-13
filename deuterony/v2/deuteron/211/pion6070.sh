#!/bin/bash
#PBS -l walltime=100:00:00
#PBS -l select=1:mem=5gb:cpu_flag=avx512vl


module add gsl-2.1-gcc
module add root-6.24.00
module add python36-modules-gcc
module add boost-1.60-gcc-serial

cd /storage/brno12-cerit/home/poledto1/hydro/hybrid/root_scripts/v2/deuteron/211
ln -s /usr/bin/x86_64-linux-gnu-g++ x86_64-linux-gnu-g++-9


root -q -b 'vn_EP_pT_pid.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-60-70-deuteron/",3000,500,2,211,"lhc2760-60-70-deuteron")'

