import FWCore.ParameterSet.Config as cms

import subprocess

process = cms.Process("TagProbe")

process.load('Configuration.StandardSequences.Services_cff')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.MessageLogger.cerr.FwkReport.reportEvery = 10

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource", 
    fileNames = cms.untracked.vstring(),
)
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(500) )

process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.load("Configuration.StandardSequences.Reconstruction_cff")

import os
if "CMSSW_7_4_" in os.environ['CMSSW_VERSION']:

    #run 251168
    process.GlobalTag.globaltag = cms.string('74X_dataRun2_Prompt_v1')
    sourcefilesfolder = "/store/data/Run2015B/SingleMuon/AOD/PromptReco-v1/000/251/168/00000"
    files = subprocess.check_output([ "/afs/cern.ch/project/eos/installation/0.3.15/bin/eos.select", "ls", sourcefilesfolder ])
    process.source.fileNames = [ sourcefilesfolder+"/"+f for f in files.split() ]

    #run 251244
    sourcefilesfolder = "/store/data/Run2015B/SingleMuon/AOD/PromptReco-v1/000/251/244/00000"
    files = subprocess.check_output([ "/afs/cern.ch/project/eos/installation/0.3.15/bin/eos.select", "ls", sourcefilesfolder ])
    process.source.fileNames.extend( [ sourcefilesfolder+"/"+f for f in files.split() ] )

    #run 251251
    sourcefilesfolder = "/store/data/Run2015B/SingleMuon/AOD/PromptReco-v1/000/251/251/00000"
    files = subprocess.check_output([ "/afs/cern.ch/project/eos/installation/0.3.15/bin/eos.select", "ls", sourcefilesfolder ])
    process.source.fileNames.extend( [ sourcefilesfolder+"/"+f for f in files.split() ] )

    #run 251252
    sourcefilesfolder = "/store/data/Run2015B/SingleMuon/AOD/PromptReco-v1/000/251/252/00000"
    files = subprocess.check_output([ "/afs/cern.ch/project/eos/installation/0.3.15/bin/eos.select", "ls", sourcefilesfolder ])
    process.source.fileNames.extend( [ sourcefilesfolder+"/"+f for f in files.split() ] )

    # to add following runs: 251491, 251493, 251496, ..., 251500 
    print process.source.fileNames
    #print process.source.fileNames, dataSummary
elif "CMSSW_7_6_" in os.environ['CMSSW_VERSION']:
    process.GlobalTag.globaltag = cms.string('76X_dataRun2_v15')
    process.source.fileNames = [
            '/store/data/Run2015D/SingleMuon/AOD/16Dec2015-v1/10000/00A3E567-75A8-E511-AD0D-0CC47A4D769E.root',
            '/store/data/Run2015D/SingleMuon/AOD/16Dec2015-v1/10000/06CC1B3A-FDA7-E511-B02B-00259073E388.root',
            '/store/data/Run2015D/SingleMuon/AOD/16Dec2015-v1/10000/0A9FEDA2-6DA8-E511-A451-002590596490.root',
            '/store/data/Run2015D/SingleMuon/AOD/16Dec2015-v1/10000/0AEF074D-EBA7-E511-B229-0002C94CDAF4.root',
            '/store/data/Run2015D/SingleMuon/AOD/16Dec2015-v1/10000/12998942-7BA8-E511-B1AA-003048FFCB84.root',
            '/store/data/Run2015D/SingleMuon/AOD/16Dec2015-v1/10000/145E4DB2-EFA7-E511-8E21-00266CF3DFE0.root',
            '/store/data/Run2015D/SingleMuon/AOD/16Dec2015-v1/10000/148E0F6C-EEA7-E511-A70E-0090FAA588B4.root',
            '/store/data/Run2015D/SingleMuon/AOD/16Dec2015-v1/10000/149A16F7-6DA8-E511-8A40-003048FFCC0A.root',
            '/store/data/Run2015D/SingleMuon/AOD/16Dec2015-v1/10000/18D542EB-FAA7-E511-A011-00259073E4E8.root',
            '/store/data/Run2015D/SingleMuon/AOD/16Dec2015-v1/10000/24537A2D-0BA8-E511-8D7C-20CF300E9ECF.root',
    ]
elif "CMSSW_8_0_"in os.environ['CMSSW_VERSION']:
    process.GlobalTag.globaltag = cms.string('80X_dataRun2_Prompt_v9')

    process.source.fileNames = [
        '/store/data/Run2016C/SingleMuon/AOD/PromptReco-v2/000/276/283/00000/0001E5C0-AE44-E611-9F88-02163E014235.root',
        '/store/data/Run2016C/SingleMuon/AOD/PromptReco-v2/000/276/283/00000/007E4250-AE44-E611-867E-02163E011AB6.root',
        '/store/data/Run2016C/SingleMuon/AOD/PromptReco-v2/000/276/283/00000/00997A4B-B044-E611-9FBB-02163E011EDE.root',
        '/store/data/Run2016C/SingleMuon/AOD/PromptReco-v2/000/276/283/00000/02BB51AA-B044-E611-8DB0-02163E014168.root',
        '/store/data/Run2016C/SingleMuon/AOD/PromptReco-v2/000/276/283/00000/0466BA91-AE44-E611-825B-02163E0136EF.root',
        '/store/data/Run2016C/SingleMuon/AOD/PromptReco-v2/000/276/283/00000/0485506E-AE44-E611-A24B-02163E0140ED.root',
        '/store/data/Run2016C/SingleMuon/AOD/PromptReco-v2/000/276/283/00000/0494A580-B044-E611-993A-02163E012944.root',
        '/store/data/Run2016C/SingleMuon/AOD/PromptReco-v2/000/276/283/00000/04C4B374-B044-E611-97D0-02163E011ECD.root',
        '/store/data/Run2016C/SingleMuon/AOD/PromptReco-v2/000/276/283/00000/06056373-B044-E611-B41D-02163E0137AA.root',
        '/store/data/Run2016C/SingleMuon/AOD/PromptReco-v2/000/276/283/00000/064D926A-B044-E611-9CAA-02163E011FCC.root',
        ]
elif "CMSSW_9_2_"in os.environ['CMSSW_VERSION']:
    process.GlobalTag.globaltag = cms.string('92X_dataRun2_Express_v2')

    process.source.fileNames = [
        '/store/express/Run2017B/ExpressPhysics/FEVT/Express-v1/000/297/101/00000/0C01D9CD-D253-E711-9D2F-02163E013511.root'
    ]  
elif "CMSSW_9_4_" in os.environ['CMSSW_VERSION']:
    process.GlobalTag.globaltag = cms.string('91X_mcRun2_asymptotic_v3')

    process.source.fileNames = [
            '/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/40000/0001B172-B9D8-E711-9771-34E6D7E05F1B.root',
            '/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/40000/000D8EBA-DDD8-E711-9CC1-90E2BACBAA90.root',
            '/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/40000/00187E27-4AD7-E711-B889-0CC47AD98D08.root',
            '/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/40000/0063F440-69D8-E711-B1AB-0CC47A1E0DBC.root',
            '/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/40000/0069F8CB-60D8-E711-BC59-002590E7D7D0.root',
            '/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/40000/00B5B771-28D8-E711-8BFF-FA163ED9E97A.root',
            '/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/40000/00E5B76F-DBD8-E711-B65D-02163E013935.root',
            '/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/40000/00FFF78E-03D8-E711-8B50-FA163EB4E1E2.root',
            '/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/40000/02306463-3FD8-E711-A33F-0025904C7DF8.root',
            '/store/data/Run2017B/SingleMuon/AOD/17Nov2017-v1/40000/02A63A34-09D8-E711-B377-1866DA879ED8.root'
            
            
    ] 

elif "CMSSW_10_1_" in os.environ['CMSSW_VERSION']:
    process.GlobalTag.globaltag = cms.string('101X_dataRun2_Prompt_v9')
    
    process.source.fileNames = [
        '/store/data/Run2018A/SingleMuon/AOD/PromptReco-v2/000/316/615/00000/08BE45E7-F15D-E811-BC09-FA163E137E19.root',
        ]            
            


else: raise RuntimeError, "Unknown CMSSW version %s" % os.environ['CMSSW_VERSION']

## SELECT WHAT DATASET YOU'RE RUNNING ON
TRIGGER="SingleMu"
#TRIGGER="DoubleMu"

## ==== Fast Filters ====
process.goodVertexFilter = cms.EDFilter("VertexSelector",
    src = cms.InputTag("offlinePrimaryVertices"),
    cut = cms.string("!isFake && ndof > 4 && abs(z) <= 25 && position.Rho <= 2"),
    filter = cms.bool(True),
)
# process.noScraping = cms.EDFilter("FilterOutScraping",
#     applyfilter = cms.untracked.bool(True),
#     debugOn = cms.untracked.bool(False), ## Or 'True' to get some per-event info
#     numtrack = cms.untracked.uint32(10),
#     thresh = cms.untracked.double(0.25),
#     src = cms.untracked.InputTag('isolatedTracks')
# )

process.load("HLTrigger.HLTfilters.triggerResultsFilter_cfi")


if TRIGGER == "SingleMu":
    process.triggerResultsFilter.triggerConditions = cms.vstring( 'HLT_Mu50_v*','HLT_IsoMu27_v*', 'HLT_IsoMu24_v*','HLT_IsoMu20_v*')
elif TRIGGER == "DoubleMu":
    process.triggerResultsFilter.triggerConditions = cms.vstring( 'HLT_Mu8_v*', 'HLT_Mu17_v*',
                                                                  'HLT_Mu8_TrkIsoVVL_v*', 'HLT_Mu17_TrkIsoVVL_v*',
                                                                  'HLT_Mu17_TkMu8_v*', 'HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v*' )
else:
    raise RuntimeError, "TRIGGER must be 'SingleMu' or 'DoubleMu'"

process.triggerResultsFilter.l1tResults = ""
process.triggerResultsFilter.throw = False
process.triggerResultsFilter.hltResults = cms.InputTag("TriggerResults","","HLT")

#decomment when you have it
#process.triggerResultsFilterFake = process.triggerResultsFilter.clone(
#    triggerConditions = cms.vstring( 'HLT_Mu40_v*', 'HLT_Mu5_v*', 'HLT_Mu12_v*', 'HLT_Mu24_v*')
#)

process.fastFilter     = cms.Sequence(process.goodVertexFilter + process.triggerResultsFilter)

##    __  __                       
##   |  \/  |_   _  ___  _ __  ___ 
##   | |\/| | | | |/ _ \| '_ \/ __|
##   | |  | | |_| | (_) | | | \__ \
##   |_|  |_|\__,_|\___/|_| |_|___/
##                                 
## ==== Merge CaloMuons and Tracks into the collection of reco::Muons  ====
#from RecoMuon.MuonIdentification.calomuons_cfi import calomuons;
# process.mergedMuons = cms.EDProducer("CaloMuonMerger",
#     mergeTracks = cms.bool(True),
#     mergeCaloMuons = cms.bool(False), # AOD
#     muons     = cms.InputTag("slimmedMuons"), 
#     caloMuons = cms.InputTag("calomuons"),
#     tracks    = cms.InputTag("isolatedTracks"),
#     minCaloCompatibility = calomuons.minCaloCompatibility,
#     ## Apply some minimal pt cut
#     muonsCut     = cms.string("pt > 3 && track.isNonnull"),
#     caloMuonsCut = cms.string("pt > 3"),
#     tracksCut    = cms.string("pt > 3"),
# )

## ==== Trigger matching
process.load("MuonAnalysis.MuonAssociators.patMuonsWithTrigger_cff")
## with some customization
process.muonMatchHLTL2.maxDeltaR = 10000
process.muonMatchHLTL3.maxDeltaR = 10000 # huge deltaR so they always get matched

from MuonAnalysis.MuonAssociators.patMuonsWithTrigger_cff import *
changeRecoMuonInput(process, "muons")
useL1Stage2Candidates(process)
appendL1MatchingAlgo(process)
addHLTL1Passthrough(process)

from MuonAnalysis.TagAndProbe.common_variables_cff import *
process.load("MuonAnalysis.TagAndProbe.common_modules_cff")

process.tagMuons = cms.EDFilter("PATMuonSelector",
    src = cms.InputTag("patMuonsWithTrigger"),
    cut = cms.string('(pt > 25) &&  (abs(eta)<2.4) && (isPFMuon>0) && (isGlobalMuon = 1) && (globalTrack().normalizedChi2() < 10) && (globalTrack().hitPattern().numberOfValidMuonHits()>0)&& (numberOfMatchedStations() > 1)&& (innerTrack().hitPattern().numberOfValidPixelHits() > 0)&& (innerTrack().hitPattern().trackerLayersWithMeasurement() > 5) &&  (((pfIsolationR04.sumChargedHadronPt + max(0., pfIsolationR04.sumNeutralHadronEt + pfIsolationR04.sumPhotonEt - 0.5 * pfIsolationR04.sumPUPt) ) / pt)<0.2)'),
)

process.oneTag  = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("tagMuons"), minNumber = cms.uint32(1))

process.probeMuons = cms.EDFilter("PATMuonSelector",
                                  src = cms.InputTag("patMuonsWithTrigger"),
                                  cut = cms.string("track.isNonnull && pt > 10 &&  abs(eta)<2.4 &&  (charge!=0)"),
                                  )

process.tpPairs = cms.EDProducer("CandViewShallowCloneCombiner",
    #cut = cms.string('60 < mass < 140 && abs(daughter(0).vz - daughter(1).vz) < 4'),
    cut = cms.string('40 < mass'),
    decay = cms.string('tagMuons@+ probeMuons@-')
)
process.onePair = cms.EDFilter("CandViewCountFilter", src = cms.InputTag("tpPairs"), minNumber = cms.uint32(1))

#from MuonAnalysis.TagAndProbe.muon.tag_probe_muon_extraIso_cff import ExtraIsolationVariables

# from MuonAnalysis.TagAndProbe.puppiIso_cfi import load_fullPFpuppiIsolation
# process.fullPuppIsolationSequence = load_fullPFpuppiIsolation(process)
# from MuonAnalysis.TagAndProbe.puppiIso_cff import PuppiIsolationVariables

process.tpTree = cms.EDAnalyzer("TagProbeFitTreeProducer",
    # choice of tag and probe pairs, and arbitration
    tagProbePairs = cms.InputTag("tpPairs"),
    arbitration   = cms.string("None"),
    # probe variables: all useful ones
    variables = cms.PSet(
        AllVariables,
    #     ExtraIsolationVariables,
    #     PuppiIsolationVariables,
    #     isoTrk03Abs = cms.InputTag("probeMuonsIsoValueMaps","probeMuonsIsoFromDepsTk"),
    #     isoTrk03Rel = cms.InputTag("probeMuonsIsoValueMaps","probeMuonsRelIsoFromDepsTk"),
    #     dxyBS = cms.InputTag("muonDxyPVdzmin","dxyBS"),
    #     dxyPVdzmin = cms.InputTag("muonDxyPVdzmin","dxyPVdzmin"),
    #     dzPV = cms.InputTag("muonDxyPVdzmin","dzPV"),
    #     JetPtRatio= cms.InputTag("AddLeptonJetRelatedVariables","JetPtRatio"),
    #     JetPtRel= cms.InputTag("AddLeptonJetRelatedVariables","JetPtRel"),
    #     JetNDauCharged= cms.InputTag("AddLeptonJetRelatedVariables","JetNDauCharged"),
    #     JetBTagCSV= cms.InputTag("AddLeptonJetRelatedVariables","JetBTagCSV"),
    #     miniIsoCharged = cms.InputTag("muonMiniIsoCharged","miniIso"),
    #     activity_miniIsoCharged = cms.InputTag("muonMiniIsoCharged","activity"),
    #     miniIsoPUCharged = cms.InputTag("muonMiniIsoPUCharged","miniIso"),
    #     activity_miniIsoPUCharged = cms.InputTag("muonMiniIsoPUCharged","activity"),
    #     miniIsoNeutrals = cms.InputTag("muonMiniIsoNeutrals","miniIso"),
    #     activity_miniIsoNeutrals = cms.InputTag("muonMiniIsoNeutrals","activity"),
    #     miniIsoPhotons = cms.InputTag("muonMiniIsoPhotons","miniIso"),
    #     activity_miniIsoPhotons = cms.InputTag("muonMiniIsoPhotons","activity"),
    #     nSplitTk  = cms.InputTag("splitTrackTagger"),
    #     mt  = cms.InputTag("probeMetMt","mt"),
        ),
        flags = cms.PSet(
            TrackQualityFlags,
            MuonIDFlags,
            HighPtTriggerFlags,
            HighPtTriggerFlagsDebug,
            ),
        tagVariables = cms.PSet(
    #  #   TriggerVariables, 
    #  #   MVAIsoVariablesPlainTag, 
    #  #   pt = cms.string("pt"),
    #  #   eta = cms.string("eta"),
    #  #   phi = cms.string("phi"),
    #  #   combRelIso = cms.string("(isolationR03.emEt + isolationR03.hadEt + isolationR03.sumPt)/pt"),
    #  #   chargedHadIso04 = cms.string("pfIsolationR04().sumChargedHadronPt"),
    #  #   neutralHadIso04 = cms.string("pfIsolationR04().sumNeutralHadronEt"),
    #  #   photonIso04 = cms.string("pfIsolationR04().sumPhotonEt"),
    #  #   combRelIsoPF04dBeta = IsolationVariables.combRelIsoPF04dBeta,
    #  #   combRelIsoPF03dBeta = IsolationVariables.combRelIsoPF03dBeta,
    #  #   dzPV = cms.InputTag("muonDxyPVdzminTags","dzPV"),
            AllVariables,
    #     ExtraIsolationVariables,
    #     nVertices   = cms.InputTag("nverticesModule"),
    #     isoTrk03Abs = cms.InputTag("probeMuonsIsoValueMaps","probeMuonsIsoFromDepsTk"),
    #     isoTrk03Rel = cms.InputTag("probeMuonsIsoValueMaps","probeMuonsRelIsoFromDepsTk"),
    #     dxyBS = cms.InputTag("muonDxyPVdzminTags","dxyBS"),
    #     dxyPVdzmin = cms.InputTag("muonDxyPVdzminTags","dxyPVdzmin"),
    #     dzPV = cms.InputTag("muonDxyPVdzminTags","dzPV"),
    #     nSplitTk  = cms.InputTag("splitTrackTagger"),
    #     l1rate = cms.InputTag("l1rate"),
    #     bx     = cms.InputTag("l1rate","bx"),
    #     #mu17ps = cms.InputTag("l1hltprescale","HLTMu17TotalPrescale"), 
    #     #mu8ps  = cms.InputTag("l1hltprescale","HLTMu8TotalPrescale"), 
    #     instLumi = cms.InputTag("addEventInfo", "instLumi"),
    #     met = cms.InputTag("tagMetMt","met"),
    #     mt  = cms.InputTag("tagMetMt","mt"),
            ),
        tagFlags = cms.PSet(HighPtTriggerFlags,HighPtTriggerFlagsDebug),
         pairVariables = cms.PSet(
            #nJets30 = cms.InputTag("njets30Module"),
            dz      = cms.string("daughter(0).vz - daughter(1).vz"),
    #     pt      = cms.string("pt"), 
    #     rapidity = cms.string("rapidity"),
    #     deltaR   = cms.string("deltaR(daughter(0).eta, daughter(0).phi, daughter(1).eta, daughter(1).phi)"), 
    #     probeMultiplicity = cms.InputTag("probeMultiplicity"),
    #     probeMultiplicity_TMGM = cms.InputTag("probeMultiplicityTMGM"),
    #     probeMultiplicity_Pt10_M60140 = cms.InputTag("probeMultiplicityPt10M60140"),
    #     ## New TuneP variables
    #     newTuneP_probe_pt            = cms.InputTag("newTunePVals", "pt"),
    #     newTuneP_probe_sigmaPtOverPt = cms.InputTag("newTunePVals", "ptRelError"),
    #     newTuneP_probe_trackType     = cms.InputTag("newTunePVals", "trackType"),
    #     newTuneP_mass                = cms.InputTag("newTunePVals", "mass"),
    ),
    pairFlags = cms.PSet(
        BestZ = cms.InputTag("bestPairByZMass"),
    ),
    isMC           = cms.bool(False),
    addRunLumiInfo = cms.bool(True),
)
if TRIGGER == "DoubleMu":
    for K,F in MuonIDFlags.parameters_().iteritems():
        setattr(process.tpTree.tagFlags, K, F)


process.load("MuonAnalysis.TagAndProbe.muon.tag_probe_muon_extraIso_cfi")
process.load("PhysicsTools.PatAlgos.recoLayer0.pfParticleSelectionForIso_cff")

# process.miniIsoSeq = cms.Sequence(
#     process.pfParticleSelectionForIsoSequence +
#     process.muonMiniIsoCharged + 
#     process.muonMiniIsoPUCharged + 
#     process.muonMiniIsoNeutrals + 
#     process.muonMiniIsoPhotons 
# )

# process.load("JetMETCorrections.Configuration.JetCorrectionProducersAllAlgos_cff")
# process.ak4PFCHSJetsL1L2L3 = process.ak4PFCHSJetsL1.clone( correctors = ['ak4PFCHSL1FastL2L3'] )

# process.extraProbeVariablesSeq = cms.Sequence(
#     process.probeMuonsIsoSequence +
#     process.computeCorrectedIso + 
#     process.splitTrackTagger +
#     process.muonDxyPVdzmin + 
#     process.probeMetMt + process.tagMetMt +
#     process.miniIsoSeq +
#     process.ak4PFCHSL1FastL2L3CorrectorChain * process.AddLeptonJetRelatedVariables +
#     process.fullPuppIsolationSequence 
# )

process.tnpSimpleSequence = cms.Sequence(
    process.tagMuons +
    process.oneTag     +
    process.probeMuons +
    process.tpPairs    +
    process.onePair    +
    process.nverticesModule +
    process.njets30Module +
#    process.extraProbeVariablesSeq +
#    process.probeMultiplicities + 
    #process.addEventInfo +
    #process.l1rate +
    #process.l1hltprescale + 
    process.bestPairByZMass + 
    process.newTunePVals +
    process.muonDxyPVdzminTags +
    process.tpTree
)

process.tagAndProbe = cms.Path( 
    process.fastFilter *
    #process.mergedMuons                 *
    process.patMuonsWithTriggerSequence *
    process.tnpSimpleSequence
)


process.TFileService = cms.Service("TFileService", fileName = cms.string("tnpZ_Data.root"))
