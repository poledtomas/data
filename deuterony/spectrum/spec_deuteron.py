import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_exp_dir = "/Users/tomaspolednicek/Desktop/deuterony/spectrum/exp_data"
data_hydro_dir = "/Users/tomaspolednicek/Desktop/deuterony/spectrum/hadrony/spectrum"
cen ="1020"
spec_deuteron_exp=pd.read_csv(data_exp_dir+"/spec_deuteron_1020.dat", sep=" ", header=None, names=["pt", "pt_max", "pt_min","spec","sys","sysminus","neco1","neco"])
spec_deuteron=pd.read_csv(data_hydro_dir+"/spectrum_deuteron_lhc2760-10-20-3000-deuteron.dat", sep="\t", header=None, names=["pt", "deuteron","antideuteron","kaon","errord","errorantid","errorp"])

fig, axes = plt.subplots(sharex=True, figsize=(9,7))
axes.autoscale(tight=True)
axes.set_yscale("log")

axes.errorbar(spec_deuteron_exp["pt"],spec_deuteron_exp["spec"], yerr =(spec_deuteron_exp["sys"]), fmt='o',ecolor='black',color='red',elinewidth=2,capsize=4, label="ALICE data")

axes.plot(spec_deuteron["pt"],spec_deuteron["deuteron"]*1000, color='darkcyan',linewidth=2,label="Trento3d IS + vHLLE + SMASH")

axes.annotate('$\pi^+$', (0.6, 70),fontsize=17)
axes.annotate('$K^+/10$', (0.1, 0.6),fontsize=17)
axes.annotate('$p/50$', (0.25, 0.01),fontsize=17)   


axes.autoscale(tight=True)
axes.grid(True)
axes.annotate('$\mathrm{Pb+Pb\ \sqrt{s_{NN}}=2.76\ TeV}$ '+ '%s'%int(cen[:2])+' - '+'%s'%int(cen[2:4])+"%", (1.5,8),fontsize=17)
axes.set_xlabel('$p_t$[GeV]',fontsize=18)
axes.set_ylabel('$d^2N/(2 \pi ptdp_tdy)$[$GeV^{-2}$]',fontsize=18)
axes.legend(loc=0,fontsize=15)
axes.tick_params(axis='x', labelsize=15)
axes.tick_params(axis='y', labelsize=15)
axes.set_xlim([0.7, 3.2])
axes.set_ylim([10e-2, 30])
axes.annotate('$d$', (1.22, 4),fontsize=19)

fig.savefig('spectrum_deuteron_276_%s.png'%cen)
    

plt.show()