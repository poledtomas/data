import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math as mt


data_dir="C:\\Users\\tposo\\OneDrive - České vysoké učení technické v Praze\\Plocha\\diplomka\\LHC276\\v2\\data"
cen_exp=pd.read_csv(data_dir+"\\cen_exp.dat",header=None,sep="\t", names=["cen", "cen1","cen2","v2","stat+","stat -","sys+","sys -"])
cen=pd.read_csv(data_dir+"\\cen.dat",sep="\t",header=None, names=["cen", "v2","v4"])


fig, ax = plt.subplots(1, 1, figsize=(9, 7),sharex='col', sharey='row')

ax.plot(cen["cen"][:7],cen["v2"][:7],marker='h',color='darkcyan',linewidth=2, label="Trento3d + vHLLE + SMASH \n " +r" $\mathrm{\tau _0 =0.6\ fm, \eta/s = 0.15}$")
ax.errorbar(cen_exp["cen"][:7],cen_exp["v2"][:7], yerr =(cen_exp["stat+"][:7]), fmt='o',ecolor='black',color='blue',elinewidth=2,capsize=4, label="ALice data $|\Delta \eta|>1$")  

ax.set_ylabel('$v_2\{2\}$',fontsize=18)
ax.set_xlabel('$cenrality[\%]$',fontsize=18)
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=15)
ax.set_xlim([-1, 60])
ax.set_ylim([0.02, 0.13])
ax.legend(loc=0,fontsize=15)
ax.grid(True)
ax.annotate('$\mathrm{Pb+Pb\ \sqrt{s_{NN}}=2.76\ TeV}$', (25,0.05),fontsize=22)
plt.show()