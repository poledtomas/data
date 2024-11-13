import os
import math as mt
import sys

def two_diff_cumulant(pnx,pny,Qx,Qy,mq,mp,M):

    diff_cumulant= float((pnx*Qx+pny*Qy-mq)/(mp*M-mq))
    
    return diff_cumulant

def four_diff_cumulant(pxn, pyn, qx2n, qy2n, Qxn, Qyn, Qx2n, Qy2n, M, mp, mq):
    qxn = pxn
    qyn = pyn

    Qn_sq = Qxn * Qxn + Qyn * Qyn

    one = pxn * Qxn**3 + pxn * Qxn * Qyn**2 + pyn * Qxn**2 * Qyn + pyn * Qyn**3
    two = qx2n * Qxn**2 - qx2n * Qyn**2 + 2 * qy2n * Qxn * Qyn
    three = pxn * Qxn * Qx2n - pyn * Qyn * Qx2n + pxn * Qyn * Qy2n + pyn * Qxn * Qy2n
    four = 2 * M * (pxn * Qxn + pyn * Qyn)
    five = 2 * mq * Qn_sq
    six = 7 * (qxn * Qxn + qyn * Qyn)
    seven = Qxn * qxn + Qyn * qyn
    eight = qx2n * Qx2n + qy2n * Qy2n
    nine = 2 * (pxn * Qxn + pyn * Qyn)
    ten = 2 * mq * M
    eleven = 6 * mq

    numerator = one - two - three - four - five + six - seven + eight + nine + ten - eleven
    denominator = (mp * M - 3 * mq) * (M - 1) * (M - 2)

    return numerator / denominator


def two_cumulant(Qx,Qy,M):
    Qsq=Qx*Qx+Qy*Qy
    numerator=Qx*Qx+Qy*Qy-M
    denominator=M*(M-1)
    #cumulant = (Qx*Qx+Qy*Qy-RFP)/(RFP*(RFP-1))
    return numerator/denominator

def four_cumulant(Qx, Qy, Qx2, Qy2, M):
    Q_sq = Qx * Qx + Qy * Qy
    Q2_sq = Qx2 * Qx2 + Qy2 * Qy2
    Q_isq = Qx * Qx - Qy * Qy

    first = Q_sq * Q_sq + Q2_sq - 2 * (Qx2 * Q_isq + 2 * Qy2 * Qx * Qy)
    second = 2 * (2 * (M - 2) * Q_sq - M * (M - 3))

    numerator = first - second
    denominator = M * (M - 1) * (M - 2) * (M - 3)

    return numerator / denominator

def vn_C_pT(directory, NoF, NoE, order):
    print(f"\n\nCalculating v_{int(order)}{{2}} (pT)...")
    print(f"Processing events from directory: {directory}")

    # Cuts
    eventStep = 1  # number of events in one super-event (to increase statistics)
    etaCut = 0.8
    ptMinCut = 0.2
    ptMaxCut = 3.0
    ptBins = 14
    NS = 10
    dpt = (ptMaxCut-ptMinCut)/ptBins
    POI=[0]*ptBins 
    dn2=[0]*ptBins
    dn4=[0]*ptBins
    vn2=[0]*ptBins
    vn4=[0]*ptBins

    dn2_nom=[0]*ptBins
    dn2_denom=[0]*ptBins
    dn4_nom=[0]*ptBins
    dn4_denom=[0]*ptBins
    
    # Loop over files
    for ifls in range(1, NoF + 1):
        filename = os.path.join(directory, f"{ifls}_fin.oscar")
        
        if not os.path.exists(filename):
            print(f"Warning: Missing file #{ifls}")
            continue

        with open(filename, "r") as infile:
            for _ in range(3):  # Skip the first three lines
                next(infile)

            nevents = 0

            # Loop over events in file
            for iev in range(0, NoE, eventStep):
                Qx=Qy=Qx2=Qy2=0
                RFP = 0
                POI=[0]*ptBins 
                qx=[0]*ptBins
                qy=[0]*ptBins
                qx2=[0]*ptBins
                qy2=[0]*ptBins
                cn2_nom=0
                cn2_denom=0
                cn4_nom=0
                cn4_denom=0
                commulant=[0]*ptBins
                cumulantfour=[0]*ptBins
                for _ in range(eventStep):
                    line = infile.readline()
                    pars = line.strip().split(" ")
                    npart =int(pars[4])
                   
                    if npart > 0:
                        nevents += 1

                        # Loop over particles
                        for _ in range(npart):
                            line = infile.readline()
                            pars = line.strip().split(" ")
                            m  = float(pars[4])
                            E  = float(pars[5])
                            px = float(pars[6])
                            py = float(pars[7])
                            pz = float(pars[8])
                            id = float(pars[9])
			    			                                
                            pt = float(mt.sqrt(px*px+py*py))
                            pabs = float(mt.sqrt((px*px+py*py+pz*pz)))
                            eta = float(0.5*(mt.log((pabs+pz)/(pabs-pz))))
                            phi = float(mt.atan2(py, px))
                            
                            if (abs(eta) < etaCut and pt > ptMinCut and pt < ptMaxCut):
                                RFP += 1
                                ptBin = int((pt - ptMinCut) / dpt)
                                POI[ptBin] += 1
                                Qx += mt.cos(order * phi)
                                Qy += mt.sin(order * phi)
                                Qx2 += mt.cos(2*order * phi)
                                Qy2 += mt.sin(2*order * phi)
                                qx[ptBin] += mt.cos(order*phi)
                                qy[ptBin] += mt.sin(order*phi)
                                qx2[ptBin] += mt.cos(2*order*phi)
                                qy2[ptBin] += mt.sin(2*order*phi)
                                
                    infile.readline()

                if RFP>0:
                    
                    cumulant2 = two_cumulant(Qx,Qy,RFP)
                    cn2_nom += RFP*(RFP-1)*cumulant2
                    cn2_denom += RFP*(RFP-1)

                    cumulant4 = four_cumulant(Qx,Qy,Qx2,Qy2,RFP)
                    cn4_nom += RFP*(RFP-1)*(RFP-2)*(RFP-3)*cumulant4
                    cn4_denom += RFP*(RFP-1)*(RFP-2)*(RFP-3)
                    
                   
                    for ipt in range (ptBins):
                        
                        if (POI[ipt] > 0):
                            commulant[ipt]=two_diff_cumulant(qx[ipt],qy[ipt],Qx,Qy,POI[ipt],POI[ipt],RFP)
                            cumulantfour[ipt]=four_diff_cumulant(qx[ipt],qy[ipt],qx2[ipt],qy2[ipt], Qx, Qy, Qx2,Qy2, RFP,POI[ipt],POI[ipt])
                            
                            dn2_nom[ipt] += (POI[ipt]*RFP - POI[ipt])*commulant[ipt]
                            dn2_denom[ipt] += POI[ipt]*RFP - POI[ipt]


                            dn4_nom[ipt] += (POI[ipt]*RFP - 3*POI[ipt])*(RFP-1)*(RFP-2)*cumulantfour[ipt]
                            dn4_denom[ipt] += (POI[ipt]*RFP - 3*POI[ipt])*(RFP-1)*(RFP-2)
                            
    cn2 = cn2_nom / cn2_denom
    cn4 = cn4_nom / cn4_denom -2 * cn2 * cn2
    
    with open("necotest.dat", "w") as file:
        for ipt in range(ptBins):
            dn2[ipt] = dn2_nom[ipt]/dn2_denom[ipt]
            vn2[ipt] = dn2[ipt]/mt.sqrt(cn2)

            dn4[ipt] = dn4_nom[ipt] / dn4_denom[ipt] - 2 * dn2[ipt] * cn2
            vn4[ipt] = -dn4[ipt] / pow(-cn4, 0.75)

            ptBin = (ipt+0.5)*dpt + ptMinCut
            file.write("%s\t"%round(ptBin,2))
            file.write("%s\t"%vn2[ipt])
            file.write("%s\n"%vn4[ipt])
        
   

vn_C_pT(str(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]))
#vn_C_pT("../../sampler.out/lhc5020-00-05-norm135/", NoF=10, NoE=10, order=2)
