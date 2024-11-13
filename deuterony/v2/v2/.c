#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

void vn_comulants_centrality(const char* direct, int NoF, int NoE, int order)
{
  cout << endl << endl << "Calculating dN/deta..." << endl;
  cout << "Processing events from directory: " << direct << endl;

  // Borders of eta
  const double etaMin = -5.0;
  const double etaMax =  5.0;
  const int nBins = 50;
  const double deta = (etaMax-etaMin)/nBins;
  double dN[nBins] = {0.0};

  // Maximum number of particles - length of arrays
  //const int NP = 60000;

  double px, py, pz;
  double ele;
  int npart, nevents = 0;

  int npar, maxpar;
  double cn2_nom, cn2_denom, cn4_denom, cn4_nom;

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
    if (infile == NULL) 
    {
      cout << "Warning: Missing file #" << ifls << endl;
    }
    else
    {
      fgets(line,500,infile);
      fgets(line,500,infile);
      fgets(line,500,infile);
      // Loop over events in file
      for (int iev = 0; iev < NoE; iev++)
      {
        int RFP = 0;
        double cumulant2 = 0.0;
        double cumulant4 = 0.0;
        double Qx = 0.0, Qy = 0.0;
        double Qx2 = 0.0, Qy2 = 0.0;
        complex<double> Q, Q2;

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
          nevents++;
          // Loop over particles
          for (int i = 0; i < npart; i++)
          {
            fgets(line,500,infile);
            strtokresult = strtok(line, delims);
            npar = 0;
            maxpar = 12;
            while( (strtokresult != NULL) && (npar < maxpar) )
            {
              pars[npar]= strtokresult;
              strtokresult = strtok( NULL, delims );
              npar += 1;
            }
            px = atof(pars[6]);
            py = atof(pars[7]);
            pz = atof(pars[8]);
            ele = atoi(pars[11]);
            float phi = atan2(py, px);
            float eta = 0.5*log((sqrt(px*px+py*py+pz*pz)+pz)/(sqrt(px*px+py*py+pz*pz)-pz));
            if (ele != 0 && eta < etaMax && eta > etaMin)
            {
                RFP++; 
                Qx += TMath::Cos(order*phi);
                Qy += TMath::Sin(order*phi);
                Qx2 += TMath::Cos(2*order*phi);
                Qy2 += TMath::Cos(2*order*phi);
                
            }
          }

          fgets(line,500,infile);
        }
        if (RFP > 0)
        {
          Q = complex<double>(Qx, Qy);
          Q2 = complex<double>(Qx2, Qy2);
          // calculation of cumulants
          cumulant2 = (double)(abs(Q)*abs(Q)-RFP)/(RFP*(RFP-1));
          cumulant4 = (pow(abs(Q),4) + pow(abs(Q2),2) - 2*real(Q2*conj(Q)*conj(Q)) - 4*(RFP-2)*abs(Q)*abs(Q) 
            + 2*RFP*(RFP-3)) / (RFP*(RFP-1)*(RFP-2)*(RFP-3));

          cn2_nom += RFP*(RFP-1)*cumulant2;
          cn2_denom += RFP*(RFP-1);
          cn4_nom += (RFP*(RFP-1)*(RFP-2)*(RFP-3))*cumulant4;
          cn4_denom += RFP*(RFP-1)*(RFP-2)*(RFP-3);
        }
      }
    }
    if ((ifls)%((int)NoF/20) == 0) cout << (int)100*ifls/NoF << "%" << endl;
  }
  double cn2=cn2_nom/cn2_denom;
  double cn4 =cn4_nom/cn4_denom -2*cn2*cn2;

    cout<< sqrt(cn2)<< "\t" << pow(-cn4, 0.25)<<endl;


  cout << "Number of events in chosen centrality interval: " << nevents << endl;


}