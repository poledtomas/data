import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math as mt

v2=[]
v2pi=[]
v2k=[]
v2p=[]
cen=["0005","0510","1020","2030","3040","4050","5060"]

# Table1 = v2[0] = pi+- 0005, Taable7 = v6[6]= pi+- 5060
 #Table8 = v2[7] = K+- 0005, Taable14 = v6[13]= pi+- 5060

data_dir="/Users/tomaspolednicek/Desktop/OneDrive - České vysoké učení technické v Praze/diplomka/LHC276/v2/data"
data_exp = "/Users/tomaspolednicek/Desktop/OneDrive - České vysoké učení technické v Praze/diplomka/LHC276/v2/data_exp"
for i in range(1,66):
    
    v2.append(pd.read_csv(data_exp+"/Table%s.csv"%i,skiprows=15,header=None, names=["pt", "v2","stat +","stat -","sys +","sys -"]))


for i in cen:
    v2pi.append(pd.read_csv(data_dir+"/vn_cumulants_pT_pair_211_LHC276_%s.dat"%i,sep="\t",skiprows=1, header=None, names=["pt", "v2","chyba","v2_4","chyba2"]))
    v2k.append(pd.read_csv(data_dir+"/vn_cumulants_pT_pair_321_LHC276_%s.dat"%i,sep="\t",skiprows=1, header=None, names=["pt", "v2","chyba","v2_4","chyba2"]))
    v2p.append(pd.read_csv(data_dir+"/vn_cumulants_pT_pair_2212_LHC276_%s.dat"%i,sep="\t",skiprows=1, header=None, names=["pt", "v2","chyba","v2_4","chyba2"]))

fig, ax = plt.subplots(1, 1, figsize=(9, 7),sharex='col', sharey='row')
   
#ax.errorbar(v2[0]["pt"],v2[0]["v2"], yerr =(v2[0]["stat +"]), fmt='o',ecolor='black',color='blue',elinewidth=2,capsize=4)  
#ax.plot(v2p[0]["pt"],v2p[0]["v2"],color='darkcyan',linewidth=2)

#ax.errorbar(v2[1]["pt"],v2[1]["v2"], yerr =(v2[1]["stat +"]), fmt='o',ecolor='black',color='red',elinewidth=2,capsize=4)  x
#ax.plot(v2p[1]["pt"],v2p[1]["v2"],color='darkcyan',linewidth=2)

#ax.errorbar(v2[2]["pt"],v2[2]["v2"], yerr =(v2[2]["stat +"]), fmt='o',ecolor='black',color='green',elinewidth=2,capsize=4)  
ax.plot(v2p[0]["pt"],v2p[0]["v2"],color='darkcyan',linewidth=2, label="Trento3d + vHLLE + SMASH")
ax.errorbar(v2[28]["pt"],v2[28]["v2"], yerr =(v2[28]["stat +"]), fmt='o',ecolor='black',color='blue',elinewidth=2,capsize=4, label ="ALICE data 0-5%") 


ax.legend(loc=0,fontsize=15)
ax.autoscale(tight=True)
ax.grid(True)
ax.annotate('$\mathrm{Pb+Pb\ \sqrt{s_{NN}}=2.76\ TeV}$', (0.1,0.23),fontsize=22)
ax.set_xlabel('$p_t$[GeV]',fontsize=18)
ax.set_ylabel('$v_2\{2\}$',fontsize=18)
ax.annotate('$p$+'r'$\bar{p}$', (0.5, 0.13),fontsize=22)
ax.set_xlim([0, 4])
ax.set_ylim([0, 0.3])
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=15)

plt.show()
