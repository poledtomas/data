#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <iomanip>
#include <string.h>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <cmath>
#include <chrono>

using namespace std;

double bessi0(double x)
{
    double ax,ans;
    double y;
    if((ax=fabs(x)) < 3.75)
    {
        y=x/3.75;
        y*=y;
        ans=1.0+y*(3.5156229+y*(3.0899424+y*(1.2067492+y*(0.2659732+y*(0.360768e-1+y*0.45813e-2)))));
    }
    else
    {
        y=3.75/ax;
        ans=(exp(ax)/sqrt(ax))*(0.39894228+y*(0.1328592e-1
            +y*(0.225319e-2+y*(-0.157565e-2+y*(0.916281e-2
            +y*(-0.2057706e-1+y*(0.2635537e-1+y*(-0.1647633e-1
            +y*0.392377e-2))))))));
    }
    return ans;
}

double bessi1(double x)
{
    double ax, ans, y;
    if((ax=fabs(x))<3.75)
    {
        y=x/3.75;
        y*=y;
        ans=ax*(0.5+y*(0.87890594+y*(0.51498869+y*(0.15084934
            +y*(0.2658733e-1+y*(0.301532e-2+y*0.32411e-3))))));
    }
    else
    {
        y=3.75/ax;
        ans=0.2282967e-1+y*(-0.2895312e-1+y*(0.1787654e-1
            -y*0.420059e-2));
        ans=0.39894228+y*(-0.3988024e-1+y*(-0.362018e-2
            +y*(0.163801e-2+y*(-0.1031555e-1+y*ans))));
        ans *= (exp(ax)/sqrt(ax));
    }
    return x < 0.0 ? -ans : ans;
}



// NoF - number of files
// NoE - number of events

void vn_EP_pT_error(const char* direct, int NoF, int NoE, double order){

    cout << endl << endl << "Calculating v2..." << endl;
    //cout << "Processing events from directory: " << direct << endl;

    // Cuts
    const double etaCut = 1 ;
    const double yCut = 0.5;
    const double ptMinCut = 0.7;
    const double ptMaxCut = 2.8;
    const int nBins = 10;
    const double dpt = (ptMaxCut-ptMinCut)/nBins ;

    double vn_obs[nBins]={0.0};
    double sd1[nBins]={0.0}, vnerr[nBins]={0.0};

    int nevents[nBins] = {0};

    int npar, maxpar;
    int  npart, Nparticipants ;
    int centrality_events = 0;

    double Rn = 0.0;

    double E, px, py, pz;
    int ele, id;


    // Loop over files
    for (int ifls = 1; ifls < NoF + 1; ifls++) {

        FILE *infile;
    char line[500];
    char delims[] = " ,\n\t";
    char *strtokresult = NULL;
    char *pars[12];

    string filename;
    string buffer;
    filename.append(direct);
    filename.append(to_string(ifls));
    filename.append("_fin.oscar");

    infile = fopen(filename.c_str(), "r");

        if (infile == NULL){

            cout << "Warning: Missing file #" << ifls << endl;
        }
        else{

            fgets(line,500,infile);
            fgets(line,500,infile);
            fgets(line,500,infile);

            // Loop over events in file
            for (int iev = 0; iev < NoE; iev++) 
            {
                while (fgets(line, 500, infile) != NULL) {
            
                fgets(line,500,infile);
                strtokresult = strtok(line, delims);
                npar = 0;
                maxpar = 5;

                while( (strtokresult != NULL) && (npar < maxpar) )
                {

                    pars[npar]= strtokresult;
                    strtokresult = strtok( NULL, delims );
                    npar += 1;
                }

                int npart = atoi(pars[4]);

                if (npart > 0)
                {
                    double Qx = 0.0, Qy = 0.0;
                    vector<double> E_ev, px_ev, py_ev, pz_ev;
                    vector<int> ele_ev, id_ev;

                    // First loop over particles - calculate flow vector
                    for (int i = 0; i < npart; i++)
                    {
                        fgets(line,500,infile);
                        strtokresult = strtok(line, delims);
                        npar = 0;
                        maxpar = 6;

                        while( (strtokresult != NULL) && (npar < maxpar) )
                        {

                            pars[npar]= strtokresult;
                            strtokresult = strtok( NULL, delims );
                            npar += 1;
                        }

                        //m  = atof(pars[3]);
                        E  = atof(pars[4]);
                        px = atof(pars[0]);
                        py = atof(pars[1]);
                        pz = atof(pars[2]);
                        id = atof(pars[5]);

                        double pabs = sqrt(px*px+py*py+pz*pz);
                        double pt = sqrt(px*px+py*py);
                        double eta = 0.5*log((pabs+pz)/(pabs-pz));
                        double phi = atan2(py,px);
                        double rap = 0.5 * log((E + pz) / (E - pz));

                        if (abs(rap)<yCut && pt>ptMinCut && pt<ptMaxCut && abs(id)==1000010020)
                        {
                            Qx += pt*cos(order*phi);
                            Qy += pt*sin(order*phi);
                        }

                        id_ev.push_back(id);
                        E_ev.push_back(E);
                        px_ev.push_back(px);
                        py_ev.push_back(py);
                        pz_ev.push_back(pz);
                        //ele_ev.push_back(ele);
                    }

                    double _vn_obs[nBins] = {0.0};
                    double QxA = 0.0, QxB = 0.0, QyA = 0.0, QyB = 0.0;
                    int _nvn[nBins] = {0};

                    // Second loop over particles
                    for (int i = 0; i < npart; i++)
                    {
                        double pabs = sqrt(px_ev[i]*px_ev[i]+py_ev[i]*py_ev[i]+pz_ev[i]*pz_ev[i]);
                        double pt = sqrt(px_ev[i]*px_ev[i]+py_ev[i]*py_ev[i]);
                        double eta = 0.5*log((pabs+pz_ev[i])/(pabs-pz_ev[i]));
                        double phi = atan2(py_ev[i],px_ev[i]);
			double rap = 0.5 * log((E + pz_ev[i]) / (E - pz_ev[i]));
                        if (pt>ptMinCut && pt<ptMaxCut && abs(rap)<yCut &&  abs(id_ev[i]) == 1000010020)
                        {
                            double _Qx = Qx - pt*cos(order*phi);  // corrected flow vector
                            double _Qy = Qy - pt*sin(order*phi);  // corrected flow vector
                            double cosn = cos(order*phi);
                            double sinn = sin(order*phi);
                            double psin = atan2(_Qy,_Qx)/order;
                            int ptBin = floor((pt-ptMinCut)/dpt);
                            _vn_obs[ptBin] += (cosn*cos(order*psin) + sinn*sin(order*psin));
                            _nvn[ptBin]++;
                        }

                        if (abs(rap)<yCut && pt>ptMinCut && pt<ptMaxCut)
                        {
                            if (i%2 == 0)
                            {
                                QxA += pt*cos(order*phi);
                                QyA += pt*sin(order*phi);
                            }
                            else
                            {
                                QxB += pt*cos(order*phi);
                                QyB += pt*sin(order*phi);
                            }
                        }
                    }

                    double psi2A = atan2(QyA,QxA)/order;
                    double psi2B = atan2(QyB,QxB)/order;
                    Rn += cos(order*(psi2A-psi2B));

                    for (int i = 0; i < nBins; i++)
                    {
                        if (_nvn[i]>0)
                        {
                             nevents[i]++;
                             _vn_obs[i] /= _nvn[i];
                        }
                        vn_obs[i] += _vn_obs[i];
                        sd1[i] += _vn_obs[i] * _vn_obs[i];
                    }
                }
                fgets(line,500,infile);
                }
            }
        }
    }

    cout << "Number of events: " << nevents[0] << endl;

    for (int i=0; i<nBins; i++)
    {
        vn_obs[i] /= nevents[i];
        vnerr[i] = sqrt(sd1[i]/nevents[i] - vn_obs[i]*vn_obs[i]);
    }

    Rn = sqrt(Rn/nevents[0]) ;
    cout << "Rn^sub = " << Rn << endl;

    const double pf = sqrt(M_PI)/(2.0*sqrt(2.0)) ;
    double ksiMin=0., ksiMax = 20. ;

    while(ksiMax-ksiMin>0.01)
    {
        double ksi = 0.5*(ksiMin+ksiMax) ;
        double R = pf*ksi*exp(-0.25*ksi*ksi)*(bessi0(0.25*ksi*ksi)+bessi1(0.25*ksi*ksi)) ;
        if(R>Rn) ksiMax = ksi ;
        else ksiMin = ksi ;
    }

    const double ksi = sqrt(2)*0.5*(ksiMin+ksiMax) ;

    cout << "ksi = " << ksi << endl;

    Rn = pf*ksi*exp(-0.25*ksi*ksi)*(bessi0(0.25*ksi*ksi)+bessi1(0.25*ksi*ksi));

    // Write results into the text file (append)
    ofstream fout;
    //fout.open("vn_EP_pT_error.dat", ofstream::app);
    //fout << direct << "\t" << (int)order << endl;

    fout.open("v2_30_40_coal11all.dat", ofstream::trunc);
    fout << "/storage/brno12-cerit/home/poledto1/hydro/scripts/OSCAR/" << endl;

    double vn[nBins] = {0.0};
    double ptBin[nBins] = {0.0};

    for (int ipt=0; ipt<nBins; ipt++)
    {
        vn[ipt] = vn_obs[ipt] / Rn;
        vnerr[ipt] = vnerr[ipt] / Rn / sqrt(nevents[ipt]);
        ptBin[ipt] = ptMinCut + (ipt + 0.5) * dpt;
        cout << ptBin[ipt] << "\t" << vn[ipt] << "\t" << vnerr[ipt] << endl;
        fout << ptBin[ipt] << "\t" << vn[ipt] << "\t" << vnerr[ipt] << endl;
    }

    fout << endl;
    fout.close();

    cout << "Results have been written to 'vn_EP_pT_error.dat'" << endl;
}
