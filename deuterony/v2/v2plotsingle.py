import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math as mt

data_dir_exp="/Users/tomaspolednicek/Desktop/deuterony/v2/expdata/zasilka-PEVE82TJ59426LM9"
data_dir= "/Users/tomaspolednicek/Desktop/deuterony/v2/deuteron/2212"
v2exp=pd.read_csv(data_dir_exp+"/Table32.csv",skiprows=15,header=None, names=["pt", "v2","stat +","stat -","sys +","sys -"])

v2EP=pd.read_csv(data_dir+"/vn_ EP_pT_pair_2212_lhc2760-20-30-deuteron.dat",sep="\t",skiprows=1, header=None, names=["pt", "v2","chyba","v2_4","chyba2"])
v2cm=pd.read_csv(data_dir+"/vn_cumulants_pT_pair_2212_lhc2760-20-30-deuteron.dat",sep="\t",skiprows=1, header=None, names=["pt", "v2","chyba","v2_4","chyba2"])

v2EP_proton=pd.read_csv(data_dir+"/vn_ EP_pT_pair_2212_lhc2760-20-30-deuteron-EP.dat",sep="\t",skiprows=1, header=None, names=["pt", "v2","chyba","v2_4","chyba2"])
v2EP_anti=pd.read_csv(data_dir+"/vn_ EP_pT_pair_-2212_lhc2760-20-30-deuteron-EP.dat",sep="\t",skiprows=1, header=None, names=["pt", "v2","chyba","v2_4","chyba2"])

fig, ax = plt.subplots(1, 1, figsize=(9, 7),sharex='col', sharey='row')

ax.plot(v2EP["pt"],v2EP["v2"],color='red',linewidth=2,label="$v_2$ EP method")
ax.plot(v2cm["pt"],v2cm["v2"],color='blue',linewidth=2,label="$v_2$ cumulant method")
ax.plot(v2EP_proton["pt"],v2EP_proton["v2"],color='green',linewidth=2,label="$v_2$ proton EP method")
ax.plot(v2EP_anti["pt"],v2EP_anti["v2"],color='gold',linewidth=2,label="$v_2$ antiproton EP method")
ax.plot(v2EP_anti["pt"],(v2EP_anti["v2"]+v2EP_proton["v2"])/2,color='black',linewidth=2,label="$v_2$ antiproton EP method")


ax.errorbar(v2exp["pt"],v2exp["v2"], yerr =(v2exp["stat +"]), fmt='o',ecolor='black',color='blue',elinewidth=2,capsize=4,label="Alice data")
    

ax.legend(loc=0)
ax.autoscale(tight=True)
ax.grid(True)
ax.set_xlabel('$p_t$[GeV]')
ax.set_ylabel('$v_2$')
ax.set_xlim([-0.2, 3])
ax.set_ylim([-0.01, 0.3])
ax.tick_params( axis='x')
ax.tick_params(axis='y')
ax.annotate('$\mathrm{Pb+Pb\ \sqrt{s_{NN}}=2.76\ TeV\ 20-30\%}$ ',(1.2,0.02),fontsize=15)

#ax.annotate(''r'$ p+\bar{p}$',(0.2,0.1),fontsize=22)
ax.annotate('$K^{\pm}$ ',(0.2,0.05),fontsize=22)
#ax.annotate('$\pi^{\pm}$ ',(0.2,0.05),fontsize=22)

plt.show()
