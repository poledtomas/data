import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math as mt

data_dir= "/Users/tomaspolednicek/Desktop/data/data"

data_dir_exp="/Users/tomaspolednicek/Desktop/data/deuterony/v2/expdata/zasilka-PEVE82TJ59426LM9"
data = "/Users/tomaspolednicek/Desktop/data/deuterony/v2/deuteron/211"

v2exp=pd.read_csv(data_dir_exp+"/Table4.csv",skiprows=15,header=None, names=["pt", "v2","stat +","stat -","sys +","sys -"])
v2deuteron =pd.read_csv(data_dir+"/vn_SP_pT_pair_1000010020_lhc2760-50-60.dat",skiprows=2,sep="\t",header=None, names=["pt", "v2"])

v22030_pion=pd.read_csv(data_dir+"/vn_SP_pT_pair_211_lhc2760-20-30.dat", skiprows=2,sep="\t",header=None, names=["pt", "v2"])
vn_cm= pd.read_csv(data+"/vn_cumulants_pT_pair_211_lhc2760-20-30-deuteron.dat",sep ="\t",skiprows=1,header=None, names=["pt", "v2","stat +","stat -","sys +"])

fig, ax = plt.subplots(1, 1, figsize=(9, 7),sharex='col', sharey='row')

ax.plot(v2deuteron["pt"],v2deuteron["v2"],color='red',linewidth=2,label="$v_2$ SP method")
    
ax.plot(vn_cm["pt"],vn_cm["v2"],color='gold',linewidth=2,label="$v_2$ cummulat method")

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
#ax.annotate('$K^{\pm}$ ',(0.2,0.05),fontsize=22)
ax.annotate('$\pi^{\pm}$ ',(0.2,0.05),fontsize=22)

plt.show()
