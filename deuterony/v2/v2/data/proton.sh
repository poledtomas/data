#!/bin/bash
#PBS -l walltime=70:00:00
#PBS -l select=1:mem=30gb

module add gsl-2.1-gcc
module add root-6.14.04
module add python36-modules-gcc
module add boost-1.60-gcc-serial
module add cmake/3.15.3

cd /storage/brno12-cerit/home/poledto1/hydro/hybrid/root_scripts/v2/data


root -q -b 'vn_C_pT_pair.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-20-30-part1-300/",100,200,2,2212,"lhc2760-20-30-part1-300")'
root -q -b 'vn_C_pT_pair.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-20-30-part2-300/",100,200,2,2212,"lhc2760-20-30-part2-300")'

root -q -b 'vn_C_pT_pair.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-30-40-part1-300/",100,200,2,2212,"lhc2760-30-40-part1-300")'
root -q -b 'vn_C_pT_pair.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-30-40-part2-300/",100,200,2,2212,"lhc2760-30-40-part2-300")'

root -q -b 'vn_C_pT_pair.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-40-50-part1-300/",100,200,2,2212,"lhc2760-30-40-part1-300")'
root -q -b 'vn_C_pT_pair.c("/storage/brno12-cerit/home/poledto1/hydro/hybrid/sampler.out/lhc2760-40-50-part2-300/",100,200,2,2212,"lhc2760-30-40-part2-300")'
