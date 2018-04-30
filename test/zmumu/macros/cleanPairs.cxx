#include "TTree.h"
#include "TFile.h"
#include "TStopwatch.h"
#include "TSystem.h"
#include "TRandom.h" 
#include "TString.h"
#include <cstdlib>
#include <cmath>


void cleanPairs(TString _output){
    using namespace std;
    TTree *tIn  = (TTree *) gFile->Get("tpTree/fitter_tree");
    Float_t pt, abseta, tag_pt, tag_eta;
    UInt_t event;
    
    tIn->SetBranchAddress("pt", &pt);
    tIn->SetBranchAddress("abseta", &abseta);
    tIn->SetBranchAddress("tag_pt", &tag_pt);
    tIn->SetBranchAddress("tag_eta", &tag_eta);
    tIn->SetBranchAddress("event", &event);

    //for data
    //TFile *fOut = new TFile((TString)"root://eoscms//eos/cms/store/group/phys_muon/perrin/Ntuple_for_doubletrigg2017/DoubleMuonNtuples/"+_output+".root", "RECREATE");
    //for mc
    TFile *fOut = new TFile((TString)"root://eoscms//eos/cms/store/group/phys_muon/perrin/Ntuple_for_doubletrigg2017/DoubleMuonNtuples/MC/"+_output+".root", "RECREATE");
    fOut->mkdir("tpTree")->cd();
    TTree *tOut = tIn->CloneTree(0);

    
    int step = tIn->GetEntries()/100;
    //int step = 1;
    double evDenom = 100.0/double(tIn->GetEntries());
    TStopwatch timer; timer.Start();
	float ptNow, tagPtNow;
    float ptNext, tagPtNext;
    TRandom *rando = new TRandom();
    for (int i = 0, n = tIn->GetEntries(); i < n; ++i) {
    //for (int i = 0, n = 100; i < n; ++i) {
        tIn->GetEntry(i);
        
        if ((i+1) % step == 0) {
            double totalTime = timer.RealTime()/60.; timer.Continue();
            double fraction = double(i+1)/double(n+1), remaining = totalTime*(1-fraction)/fraction;
            printf("Done %9d/%9d   %5.1f%%   (elapsed %5.1f min, remaining %5.1f min)\n", i, n, i*evDenom, totalTime, remaining);
            fflush(stdout);
        }
        
        ptNow = pt;
        tagPtNow = tag_pt;
        
        tIn->GetEntry(i+1);
        ptNext = pt;
        tagPtNext = tag_pt;
        
        if ((ptNext==tagPtNow)&&(tagPtNext==ptNow)){
         //   printf("found a double pair ! \n");
            float theRand = rando->Uniform(0,2);
            if (theRand>=1) tIn->GetEntry(i); else tIn->GetEntry(i+1);
            i++;
        }
        else tIn->GetEntry(i);
        tOut->Fill();

        
       // printf("event=%i, pt=%f, abseta=%f, tag_pt=%f, tag_eta=%f \n", event, pt, abseta, tag_pt, tag_eta);
        
    }
    
    tOut->AutoSave(); // according to root tutorial this is the right thing to do
    fOut->Close();
}
