#include <iostream>

void data2csv(UInt_t N=0, TString output_file="out.csv",
              TString input_file="8_gev_electrons.root", TString branch="scaled_electron_adc_counts[32]") {

  
  TFile* infile  = new TFile(input_file);
  TTree* T       = (TTree*) infile->Get("T");

  int nentries = T->GetEntries();

  Double_t energy[32] = {0};
  T->SetBranchAddress(branch, energy);

  int   good_count      = 0;

  if (N==0) N=nentries;

  ofstream ofile;
  ofile.open(output_file);

  for (int q = 0; q < N ; q++) {
    T->GetEntry(q);
  
    bool empty = true;

    for (int k = 0; k < 31;k++) {
      if(energy[k]>-500) {
        empty = false;
        break;
      }
	  }
	
    if(empty) continue;

    good_count++;
  
    for (int n = 0; n < 31; n++) {
      TString output = Form("%.6f", energy[n]); //   cout<<output; cout<<energy[n];
      ofile<<output;
      if(n==30)
        ofile<<endl;
      else
        ofile<<",";
    }
  }

  ofile.close();
  return 0;
  
  //  cout << "Good count: " << good_count << " Percentage: " << (float(good_count)/float(N)) << endl;
}
