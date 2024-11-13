import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math as mt


data_dir="C:\\Users\\tposo\\OneDrive - České vysoké učení technické v Praze\\Plocha\\diplomka\\LHC276\\v2\\data"
#cen_exp=pd.read_csv(data_dir+"\\cen_exp.dat",header=None,sep="\t", names=["cen", "cen1","cen2","v2","stat+","stat -","sys+","sys -"])
cen0005=pd.read_csv(data_dir+"\\vn_cumulants_pT_C__LHC276_0005.dat",skiprows=2,sep="\t",header=None, names=["pt", "v2","error","v4","error2"])
cen3040=pd.read_csv(data_dir+"\\vn_cumulants_pT_C__LHC276_3040.dat",skiprows=2,sep="\t",header=None, names=["pt", "v2","error","v4","error2"])
cen3040exp=pd.read_csv(data_dir+"\\v2_2_3040.dat",sep="\t",header=None, names=["pt", "v2","error","error2"])

fig, ax = plt.subplots(2, 1, figsize=(9, 7),sharex='col', sharey='row')

ax[0].plot(cen0005[0:14]["pt"],cen0005[0:14]["v2"],color='darkcyan',linewidth=2, label="Trento3d + vHLLE + SMASH \n " +r" $\mathrm{\tau _0 =0.6\ fm, \eta/s = 0.15}$")
ax[0].plot(cen0005[16:30]["pt"],cen0005[16:30]["v2"],color='darkcyan',linewidth=2, label="Trento3d + vHLLE + SMASH \n " +r" $\mathrm{\tau _0 =0.6\ fm, \eta/s = 0.15}$")


ax[1].plot(cen3040[0:14]["pt"],cen3040[0:14]["v2"],color='darkcyan',linewidth=2, label="Trento3d + vHLLE + SMASH \n " +r" $\mathrm{\tau _0 =0.6\ fm, \eta/s = 0.15}$")
ax[1].plot(cen3040exp["pt"],cen3040exp["v2"],color='blue',linewidth=2, label="Trento3d + vHLLE + SMASH \n " +r" $\mathrm{\tau _0 =0.6\ fm, \eta/s = 0.15}$")
plt.subplots_adjust(hspace=0,wspace=0.05)

for i in range(2):
    ax[i].grid(True)
    ax[i].set_xlabel('$p_t$[GeV]',fontsize=18)
    ax[i].tick_params(axis='x', labelsize=15)
    ax[i].tick_params(axis='y', labelsize=15)
    ax[i].autoscale(tight=True)
    ax[i].set_ylabel('$v_2\{2,|\Delta \eta|>1\}$',fontsize=18)


plt.show()