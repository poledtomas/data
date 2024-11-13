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
# Table8 = v2[7] = K+- 0005, Taable14 = v6[13]= pi+- 5060
cen1=str(input("Select centrality? For exampale: 1020 \n"))
data_dir="C:\\Users\\tposo\\OneDrive - České vysoké učení technické v Praze\\Plocha\\diplomka\\LHC276\\v2\\data"

for i in range(1,15):
    
    v2.append(pd.read_csv("C:\\Users\\tposo\\v2_2760\\Table%s.csv"%i,skiprows=15,header=None, names=["pt", "v2","stat +","stat -","sys +","sys -"]))


for i in cen:
    v2pi.append(pd.read_csv(data_dir+"\\vn_cumulants_pT_pair_211_LHC276_%s.dat"%i,sep="\t",skiprows=1, header=None, names=["pt", "v2","chyba","v2_4","chyba2"]))
    v2k.append(pd.read_csv(data_dir+"\\vn_cumulants_pT_pair_321_LHC276_%s.dat"%i,sep="\t",skiprows=1, header=None, names=["pt", "v2","chyba","v2_4","chyba2"]))
    v2p.append(pd.read_csv(data_dir+"\\vn_cumulants_pT_pair_2212_LHC276_%s.dat"%i,sep="\t",skiprows=1, header=None, names=["pt", "v2","chyba","v2_4","chyba2"]))

#fig, ax = plt.subplots(sharex=True, figsize=(9,6))   
fig, ax = plt.subplots(2, 1, figsize=(9, 7),sharex='col', sharey='row')
plt.subplots_adjust(hspace=0,wspace=0)

v2pi_trento3d=pd.read_csv(data_dir+"\\vn_cumulants_pT_pair_211_LHC276trento2d_1020.dat",sep="\t",skiprows=1, header=None, names=["pt", "v2","chyba","v2_4","chyba2"])
v2k_trento3d=pd.read_csv(data_dir+"\\vn_cumulants_pT_pair_321_LHC276trento2d_1020.dat",sep="\t",skiprows=1, header=None, names=["pt", "v2","chyba","v2_4","chyba2"])

if cen1 == "1020":
    ax[0].plot(v2pi[2]["pt"],v2pi[2]["v2"],color='darkcyan',linewidth=2,label="Trento3d + vHLLE + SMASH")
    ax[0].plot(v2pi_trento3d["pt"],v2pi_trento3d["v2"],color='red',linewidth=2,label="Trento2d + vHLLE + SMASH")
    ax[0].errorbar(v2[2]["pt"],v2[2]["v2"], yerr =(v2[2]["stat +"]), fmt='o',ecolor='black',color='blue',elinewidth=2,capsize=4,label="Alice data, $\pi^{\pm}$, $K^{\pm}$")
    
    ax[1].plot(v2k[2]["pt"],v2k[2]["v2"],color='darkcyan',linewidth=2)
    ax[1].plot(v2k_trento3d["pt"],v2k_trento3d["v2"],color='red',linewidth=2)
    ax[1].errorbar(v2[9]["pt"],v2[9]["v2"], yerr =(v2[9]["stat +"]), fmt='o',ecolor='black',color='blue',elinewidth=2,capsize=4)

for i in range(2):
    
     ax[0].legend(loc=0,fontsize=15)
     ax[i].autoscale(tight=True)
     ax[i].grid(True)
     ax[i].set_xlabel('$p_t$[GeV]',fontsize=18)
     ax[i].set_ylabel('$v_2\{2\}$',fontsize=18)
     ax[i].set_xlim([0, 3])
     ax[i].set_ylim([0, 0.3])
     ax[i].tick_params( axis='x', labelsize=15)
     ax[i].tick_params(axis='y', labelsize=15)
ax[1].annotate('$\mathrm{Pb+Pb\ \sqrt{s_{NN}}=2.76\ TeV}$ '+ '%s'%int(cen1[:2])+' - '+'%s'%int(cen1[2:4])+"%",(0.1,0.18),fontsize=22)
ax[0].annotate('$\pi^{\pm}$ ',(0.2,0.1),fontsize=22)
ax[1].annotate('$K^{\pm}$ ',(0.2,0.05),fontsize=22)

plt.show()
