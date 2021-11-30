#include <iostream>

void ultratest_csv(UInt_t N=0, TString input_file="8_gev_electrons.root", TString branch="scaled_electron_adc_counts[32]") {

  TFile* infile  = new TFile(input_file);
  TTree* T       = (TTree*) infile->Get("T");

  int nentries = T->GetEntries();

  Double_t energy[32] = {0};
  T->SetBranchAddress(branch, energy);

  int   good_count      = 0;

  if (N==0)
    N=nentries;

  for (int q = 0; q < N ; q++) {
    T->GetEntry(q);
  
    int maxbin = 0;
    double maxval = 0;

    bool empty = true;

    for (int k = 0; k < 31;k++) {
      if(energy[k]> -0.9) {
        cout <<"k: " << k << " e: " << energy[k] << endl;
      }
      if(energy[k]>-500) {
        empty = false;
  //      break;
      }
	  }
	
    if(empty)
      continue;

    good_count++;
    for (int n = 0; n < 31; n++) {
      continue;	 
      TString output = Form("%.6f", energy[n]);
      cout<<output;
      // cout<<energy[n];
      if(n==30)
        cout<<endl;
      else
        cout<<",";
    }
  }

//  cout << "Good count: " << good_count << " Percentage: " << (float(good_count)/float(N)) << endl;
}
