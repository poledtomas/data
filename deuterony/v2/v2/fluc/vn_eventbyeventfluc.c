#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;
void vn_eventbyeventfluc(const char* direct, int NoF, int NoE, int order, string centrality)
{
  cout << endl << endl << "Calculating v_" << (int)order << "{2} (pT)..." << endl;
  cout << "Processing events from directory: " << direct << endl;

  // Cuts
  const double etaCut = 0.8;
  const double ptMinCut = 0.2;
  const double ptMaxCut = 3.0;
  const int ptBins = 14;
  const int eventStep = 1; // number of events in one super-event (to increase statistics)
  const int NS = 10; // number of subsamples to estimate the error
  const double dpt = (ptMaxCut-ptMinCut)/ptBins;

  // Maximum number of particles - length of arrays
  //const int NP = 60000;

  double px, py, pz, m, E;
  double ele;
  int id;
  int npart, nevents = 0;
  int npar, maxpar;

  // Write results into the text file (append)
  ofstream fout;
  string file="vn_evetbyeventfluc_";
  string dat= ".dat";
  string mezera = "_";
  string hadron = to_string(order);
  string filename = file+hadron+mezera+centrality+dat;
  fout.open(filename, ofstream::app);
  fout << direct << "\t" << (int)order << endl;
  
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
      for (int iev = 0; iev < NoE; iev += eventStep)
      {
        int RFP = 0, POI[ptBins] = {0}; // RFP = M (all particles), POI = m (particles in given ptBin)
        double cumulant2 = 0.0, cn2_nom=0,cn2_denom=0, cn4_nom=0,cn4_denom=0,  vn4=0,vn2=0,cn2=0,cn4=0;
        double cumulant4 = 0.0;
        double Qx = 0.0, Qy = 0.0;
        double Qx2 = 0.0, Qy2 = 0.0;
        complex<double> Q, Q2;

        for (int k = 0; k < eventStep; k++) {
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
              m  = atof(pars[4]);
              E  = atof(pars[5]);
              px = atof(pars[6]);
              py = atof(pars[7]);
              pz = atof(pars[8]);
              id = atoi(pars[9]);

              float pt = sqrt(px*px+py*py);
              float pabs = sqrt(px*px+py*py+pz*pz);
              float eta = 0.5*log((pabs+pz)/(pabs-pz));
              float phi = atan2(py, px);
              float rap = 0.5*log((E+pz)/(E-pz));
             
              if(fabs(eta)<etaCut && pt>ptMinCut && pt<ptMaxCut)
              {
                RFP++; 
                Qx += cos(order*phi);
                Qy += sin(order*phi);
                Qx2 += cos(2*order*phi);
                Qy2 += sin(2*order*phi);

                
              
              }
            }
          }
          fgets(line,500,infile);
        }

        if (RFP > 0)
        {
          Q = complex<double>(Qx, Qy);
          Q2 = complex<double>(Qx2, Qy2);
          //cout << Q << "\t"<<Q2<< endl;
          
           cumulant2 = (double)(abs(Q)*abs(Q)-RFP)/(RFP*(RFP-1));
           
           
           cumulant4 = (pow(abs(Q),4) + pow(abs(Q2),2) - 2*real(Q2*conj(Q)*conj(Q)) - 4*(RFP-2)*abs(Q)*abs(Q)+ 2*RFP*(RFP-3)) / (RFP*(RFP-1)*(RFP-2)*(RFP-3));
           
            cn2_nom = RFP*(RFP-1)*cumulant2;
            cn2_denom = RFP*(RFP-1);
          
            cn4_nom = (RFP*(RFP-1)*(RFP-2)*(RFP-3))*cumulant4;
            cn4_denom = RFP*(RFP-1)*(RFP-2)*(RFP-3);
          
            cn2 = cn2_nom/cn2_denom;
            cn4 = cn4_nom / cn4_denom - 2 * cn2 * cn2;
          
            vn2 = sqrt(cn2);
            vn4 = pow(-cn4, 0.25);

            cout <<cn2<<"\t" << cn4 <<endl;
            fout << iev << "\t" << vn2 <<"\t"<<vn4<< endl;


          

         
        }
      }
    }
    if ((ifls)%((int)NoF/20) == 0) cout << (int)100*ifls/NoF << "%" << endl;
  }

  cout << "Total number of events: " << nevents << endl;
  fout.close();

  
}