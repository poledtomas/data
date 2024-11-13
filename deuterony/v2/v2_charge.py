import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math as mt

data_dir_exp="/Users/tomaspolednicek/Desktop/deuterony/v2/expdata/"
data= "/Users/tomaspolednicek/Desktop/deuterony/v2/v2/data"
    
v2=pd.read_csv(data_dir_exp+"/chargetable4050.csv",skiprows=13,header=None, names=["pt", "v2","stat +","stat -","sys +","sys -"])


fig, ax = plt.subplots(1, 1, figsize=(9, 7),sharex='col', sharey='row')
v2viz1=pd.read_csv(data+"/vn_cumulants_pT_charge__lhc2760-40-50-norm114-3000-deuteron-zetaS3-0.2.dat",sep="\t",skiprows=1, header=None, names=["pt", "v2","chyba","v2_4","chyba2"])
v2viz2 = pd.read_csv(data+"/vn_cumulants_pT_charge__lhc2760-40-50-norm114-3000-deuteron-zetaS3-0.4.dat",sep="\t",skiprows=1, header=None, names=["pt", "v2","chyba","v2_4","chyba2"])
v2viz3=pd.read_csv(data+"/vn_cumulants_pT_charge__lhc2760-40-50-norm114-3000-deuteron-zetaS3-0.8.dat",sep="\t",skiprows=1, header=None, names=["pt", "v2","chyba","v2_4","chyba2"])

ax.plot(v2viz1["pt"],v2viz1["v2"],color='red',linewidth=2,label="norm = 114,$\eta/s = 0.12$, $\zeta/s = 0.2$")
ax.plot(v2viz2["pt"],v2viz2["v2"],color='gold',linewidth=2,label="norm = 114,$\eta/s = 0.12$, $\zeta/s = 0.4$")
ax.plot(v2viz3["pt"],v2viz3["v2"],color='black',linewidth=2,label="norm = 114, $\eta/s = 0.12$, $\zeta/s = 0.8$")

ax.errorbar(v2["pt"],v2["v2"], yerr =(v2["stat +"]), fmt='o',ecolor='black',color='blue',elinewidth=2,capsize=4,label="Alice data, all charge particles")
    

ax.legend(loc=0)
ax.autoscale(tight=True)
ax.grid(True)
ax.set_xlabel('$p_t$[GeV]')
ax.set_ylabel('$v_2\{2\}$')
ax.set_xlim([-0.2, 3])
ax.set_ylim([-0.01, 0.3])
ax.tick_params( axis='x')
ax.tick_params(axis='y')
ax.annotate('$\mathrm{Pb+Pb\ \sqrt{s_{NN}}=2.76\ TeV\ 40-50\%}$ ',(1.2,0.02),fontsize=15)

plt.show()
