#!/bin/bash
#PBS -l walltime=28:00:00
#PBS -l select=1:mem=30gb:cluster=nympha

module add gsl-2.1-gcc
module add root-6.14.04
module add python36-modules-gcc
module add boost-1.60-gcc-serial
module add cmake/3.15.3

cd /storage/brno12-cerit/home/poledto1/hydro/hybrid/root_scripts/v2

root -q -b 'vn_cumulants_centrality.c("../../sampler.out/lhc5020-00-05-norm135/",100,100,2)'
root -q -b 'vn_cumulants_centrality.c("../../sampler.out/lhc5020-05-10-norm135/",100,100,2)'
root -q -b 'vn_cumulants_centrality.c("../../sampler.out/lhc5020-10-20-norm135/",100,100,2)'
root -q -b 'vn_cumulants_centrality.c("../../sampler.out/lhc5020-20-30-norm135/",100,100,2)'
root -q -b 'vn_cumulants_centrality.c("../../sampler.out/lhc5020-30-40-norm135/",100,100,2)'
root -q -b 'vn_cumulants_centrality.c("../../sampler.out/lhc5020-40-50-norm135/",100,100,2)'
root -q -b 'vn_cumulants_centrality.c("../../sampler.out/lhc5020-50-60-norm135/",100,100,2)'
root -q -b 'vn_cumulants_centrality.c("../../sampler.out/lhc5020-60-70-norm135/",100,100,2)'
root -q -b 'vn_cumulants_centrality.c("../../sampler.out/lhc5020-70-80-norm135/",100,100,2)'
root -q -b 'vn_cumulants_centrality.c("../../sampler.out/lhc5020-80-90-norm135/",100,100,2)'

root -q -b 'vn_cumulants_centrality.c("../../sampler.out/lhc2760-00-05-norm114/",100,100,2)'
root -q -b 'vn_cumulants_centrality.c("../../sampler.out/lhc2760-05-10-norm114/",100,100,2)'
root -q -b 'vn_cumulants_centrality.c("../../sampler.out/lhc2760-10-20-norm114/",100,100,2)'
root -q -b 'vn_cumulants_centrality.c("../../sampler.out/lhc2760-20-30-norm114/",100,100,2)'
root -q -b 'vn_cumulants_centrality.c("../../sampler.out/lhc2760-30-40-norm114/",100,100,2)'
root -q -b 'vn_cumulants_centrality.c("../../sampler.out/lhc2760-40-50-norm114/",100,100,2)'
root -q -b 'vn_cumulants_centrality.c("../../sampler.out/lhc2760-50-60-norm114/",100,100,2)'
root -q -b 'vn_cumulants_centrality.c("../../sampler.out/lhc2760-60-70-norm114/",100,100,2)'
root -q -b 'vn_cumulants_centrality.c("../../sampler.out/lhc2760-70-80-norm114/",100,100,2)'
root -q -b 'vn_cumulants_centrality.c("../../sampler.out/lhc2760-80-90-norm114/",100,100,2)'

