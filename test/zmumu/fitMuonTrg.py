import FWCore.ParameterSet.Config as cms
import sys, os, shutil
from optparse import OptionParser
### USAGE: cmsRun fitMuonID.py TEST tight loose mc mc_all
###_id: tight, loose, medium, soft

#_*_*_*_*_*_
#Read Inputs
#_*_*_*_*_*_

def FillNumDen(num, den):
    '''Declares the needed selections for a givent numerator, denominator'''
    #Define the mass distribution
    if den == "highptid" :
        process.TnP_MuonID.Variables.pair_newTuneP_mass = cms.vstring("Tag-muon Mass", _mrange, "130", "GeV/c^{2}")
    else:
        process.TnP_MuonID.Variables.mass = cms.vstring("Tag-muon Mass", _mrange, "130", "GeV/c^{2}")
    #NUMS
    if num == "hlt_Mu17Mu8_leg17":
        process.TnP_MuonID.Categories.DoubleIsoMu17Mu8_IsoMu17leg  = cms.vstring("hlt_Mu17Mu8_leg17", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Expressions.hlt_Mu17Mu8_leg17Var= cms.vstring("hlt_Mu17Mu8_leg17Var", "DoubleIsoMu17Mu8_IsoMu17leg==1", "DoubleIsoMu17Mu8_IsoMu17leg")
        process.TnP_MuonID.Cuts.hlt_Mu17Mu8_leg17= cms.vstring("hlt_Mu17Mu8_leg17", "hlt_Mu17Mu8_leg17Var", "0.5")
    elif num == "hlt_Mu17_Mu8_OR_TkMu8_leg8":
        process.TnP_MuonID.Categories.DoubleIsoMu17Mu8_IsoMu8leg = cms.vstring("hlt_Mu17Mu8_leg8", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Categories.DoubleIsoMu17TkMu8_IsoMu8leg = cms.vstring("hlt_Mu17TkMu8_leg8", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Expressions.hlt_Mu17_Mu8_OR_TkMu8_leg8Var = cms.vstring("hlt_Mu17TkMu8_leg8Var", "(DoubleIsoMu17TkMu8_IsoMu8leg==1) || (DoubleIsoMu17Mu8_IsoMu8leg==1)", "DoubleIsoMu17TkMu8_IsoMu8leg","DoubleIsoMu17Mu8_IsoMu8leg")
        process.TnP_MuonID.Cuts.hlt_Mu17_Mu8_OR_TkMu8_leg8= cms.vstring("hlt_Mu17_Mu8_OR_TkMu8_leg8", "hlt_Mu17_Mu8_OR_TkMu8_leg8Var", "0.5")
    elif num == "hlt_TkMu8_leg8":
        process.TnP_MuonID.Categories.DoubleIsoMu17TkMu8_IsoMu8leg = cms.vstring("hlt_Mu17TkMu8_leg8", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Expressions.hlt_TkMu8_leg8Var = cms.vstring("hlt_TkMu8_leg8Var", "DoubleIsoMu17TkMu8_IsoMu8leg==1", "DoubleIsoMu17TkMu8_IsoMu8leg")
        process.TnP_MuonID.Cuts.hlt_TkMu8_leg8 = cms.vstring("hlt_TkMu8_leg8", "hlt_TkMu8_leg8Var", "0.5")
    #Not used: should be the same as hlt_Mu17Mu8_leg17 
    #elif num == "hlt_Mu17TkMu8_leg17":
    #    process.TnP_MuonID.Categories.DoubleIsoMu17TkMu8_IsoMu17leg = cms.vstring("hlt_Mu17TkMu8_leg17", "dummy[pass=1,fail=0]")
    #    process.TnP_MuonID.Expressions.hlt_Mu17TkMu8_leg17Var= cms.vstring("hlt_Mu17TkMu8_leg17Var", "DoubleIsoMu17TkMu8_IsoMu17leg==1", "DoubleIsoMu17TkMu8_IsoMu17leg")
    #    process.TnP_MuonID.Cuts.hlt_Mu17TkMu8_leg17= cms.vstring("hlt_Mu17TkMu8_leg17", "hlt_Mu17TkMu8_leg17Var", "0.5")
    #Not used: use OR of both leg instead
    #elif num == "hlt_Mu17TkMu8_leg8":
    #    process.TnP_MuonID.Categories.DoubleIsoMu17TkMu8_IsoMu8leg = cms.vstring("hlt_Mu17TkMu8_leg8", "dummy[pass=1,fail=0]")
    #    process.TnP_MuonID.Expressions.hlt_Mu17TkMu8_leg8Var= cms.vstring("hlt_Mu17TkMu8_leg8Var", "DoubleIsoMu17TkMu8_IsoMu8leg==1", "DoubleIsoMu17TkMu8_IsoMu8leg")
    #    process.TnP_MuonID.Cuts.hlt_Mu17TkMu8_leg8= cms.vstring("hlt_Mu17TkMu8_leg8", "hlt_Mu17TkMu8_leg8Var", "0.5")
    #elif num == "hlt_Mu17Mu8_leg8":
    #    process.TnP_MuonID.Categories.DoubleIsoMu17Mu8_IsoMu8leg = cms.vstring("hlt_Mu17Mu8_leg8", "dummy[pass=1,fail=0]")
    #    process.TnP_MuonID.Expressions.hlt_Mu17Mu8_leg8Var= cms.vstring("hlt_Mu17Mu8_leg8Var", "DoubleIsoMu17Mu8_IsoMu8leg==1", "DoubleIsoMu17Mu8_IsoMu8leg")
    #    process.TnP_MuonID.Cuts.hlt_Mu17Mu8_leg8= cms.vstring("hlt_Mu17Mu8_leg8", "hlt_Mu17Mu8_leg8Var", "0.5")
    #Not used (should compute efficiency per event, not per probe)
    #elif num == "hlt_Mu17Mu8_DZ_leg17":
    #    process.TnP_MuonID.Categories.DoubleIsoMu17Mu8dZ_Mu17leg = cms.vstring("hlt_Mu17Mu8_DZ_leg17", "dummy[pass=1,fail=0]")
    #    process.TnP_MuonID.Expressions.hlt_Mu17Mu8_DZ_leg17Var = cms.vstring("hlt_Mu17Mu8_DZ_leg17Var", "DoubleIsoMu17Mu8dZ_Mu17leg==1", "DoubleIsoMu17Mu8dZ_Mu17leg")
    #    process.TnP_MuonID.Cuts.hlt_Mu17Mu8_DZ_leg17 = cms.vstring("hlt_Mu17Mu8_DZ_leg17", "hlt_Mu17Mu8_DZ_leg17Var", "0.5")
    #elif num == "hlt_Mu17TkMu8_DZ_leg17":
    #    process.TnP_MuonID.Categories.DoubleIsoMu17TkMu8dZ_Mu17 = cms.vstring("hlt_Mu17TkMu8_DZ_leg17", "dummy[pass=1,fail=0]")
    #    process.TnP_MuonID.Expressions.hlt_Mu17TkMu8_DZ_leg17Var= cms.vstring("hlt_Mu17TkMu8_DZ_leg17Var", "DoubleIsoMu17TkMu8dZ_Mu17==1", "DoubleIsoMu17TkMu8dZ_Mu17")
    #    process.TnP_MuonID.Cuts.hlt_Mu17TkMu8_DZ_leg17= cms.vstring("hlt_Mu17TkMu8_DZ_leg17", "hlt_Mu17TkMu8_DZ_leg17Var", "0.5")
    #DEN
    if den == "looseidniso":
        #process.TnP_MuonID.Categories.LooseIDandLooseIso= cms.vstring("Loose ID and ISO Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Categories.PF  = cms.vstring("PF Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Variables.combRelIsoPF04dBeta = cms.vstring("dBeta rel iso dR 0.4", "-2", "9999999", "")
    elif den == "tightidniso":
        process.TnP_MuonID.Variables.dzPV  = cms.vstring("dzPV", "-1000", "1000", "")
        process.TnP_MuonID.Categories.Tight2012 = cms.vstring("Tight Id. Muon", "dummy[pass=1,fail=0]")
        process.TnP_MuonID.Variables.combRelIsoPF04dBeta = cms.vstring("dBeta rel iso dR 0.4", "-2", "9999999", "")
        #process.TnP_MuonID.Categories.Tight2012andTightIso = cms.vstring("Tight ID and ISO Muon", "dummy[pass=1,fail=0]")
    #Request tag to satifie "other leg" trigger
    #not: if are inverted wrt NUMS
    if num == "hlt_Mu17Mu8_leg17":
        pass
        #process.TnP_MuonID.Categories.tag_DoubleIsoMu17Mu8_IsoMu8leg = cms.vstring("tag_DoubleIsoMu17Mu8_IsoMu8leg", "dummy[pass=1,fail=0]")
        #process.TnP_MuonID.Categories.tag_DoubleIsoMu17TkMu8_IsoMu8leg = cms.vstring("tag_DoubleIsoMu17TkMu8_IsoMu8leg", "dummy[pass=1,fail=0]")
    elif num == "hlt_Mu17_Mu8_OR_TkMu8_leg8":
        pass
        #process.TnP_MuonID.Categories.tag_DoubleIsoMu17Mu8_IsoMu17leg  = cms.vstring("tag_DoubleIsoMu17Mu8_IsoMu17leg", "dummy[pass=1,fail=0]")
        #process.TnP_MuonID.Categories.tag_DoubleIsoMu17TkMu8_IsoMu17leg  = cms.vstring("tag_DoubleIsoMu17Mu8_IsoMu17leg", "dummy[pass=1,fail=0]")
    elif num == "hlt_TkMu8_leg8":
        #TkMu17
        #process.TnP_MuonID.Categories.tag_DoubleIsoMu17TkMu8_IsoMu17leg  = cms.vstring("tag_DoubleIsoMu17Mu8_IsoMu17leg", "dummy[pass=1,fail=0]")
        #Mu17
        process.TnP_MuonID.Categories.tag_DoubleIsoMu17TkMu8_IsoMu17leg  = cms.vstring("tag_DoubleIsoMu17TkMu8_IsoMu17leg", "dummy[pass=1,fail=0]")
                                    
def FillVariables(par):
    '''Declares only the parameters which are necessary, no more'''
    if par == 'newpt' or 'newpt_eta':
        process.TnP_MuonID.Variables.pair_newTuneP_probe_pt = cms.vstring("muon p_{T} (tune-P)", "0", "1000", "GeV/c")
    if par == 'eta':
        process.TnP_MuonID.Variables.eta  = cms.vstring("muon #eta", "-2.5", "2.5", "")
    if par == 'pt' or 'pt_eta':
        process.TnP_MuonID.Variables.pt  = cms.vstring("muon p_{T}", "0", "1000", "GeV/c")
    if par == 'pt_eta' or 'newpt_eta':
        process.TnP_MuonID.Variables.abseta  = cms.vstring("muon |#eta|", "0", "2.5", "")
    if par == 'vtx':
        print 'I filled it'
        process.TnP_MuonID.Variables.tag_nVertices   = cms.vstring("Number of vertices", "0", "999", "")

def FillBin(par):
    '''Sets the values of the bin paramters and the bool selections on the denominators'''
    #Parameter 
    if par == 'newpt_eta':
        DEN.pair_newTuneP_probe_pt = cms.vdouble(20, 25, 30, 40, 50, 55, 60, 120) 
        DEN.abseta = cms.vdouble( 0., 0.9, 1.2, 2.1, 2.4)
    #elif par == 'newpt':
    #    DEN.pair_newTuneP_probe_pt = cms.vdouble(21, 25, 30, 40, 50, 55, 60, 120, 200)
    #elif par == 'newpt':
    #    DEN.pair_newTuneP_probe_pt = cms.vdouble(21, 25, 30, 40, 50, 55, 60, 100, 200)
    elif par == 'newpt':
        DEN.pair_newTuneP_probe_pt = cms.vdouble(21, 25, 30, 40, 50, 55, 60, 90, 200)
    #elif par == 'newpt':
    #    DEN.pair_newTuneP_probe_pt = cms.vdouble(21, 25, 30, 40, 50, 55, 60, 80, 200)
    #elif par == 'newpt':
    #    DEN.pair_newTuneP_probe_pt = cms.vdouble(21, 25, 30, 40, 50, 55, 60, 75, 90, 200)
    #elif par == 'newpt':
    #    DEN.pair_newTuneP_probe_pt = cms.vdouble(21, 25, 30, 40, 50, 55, 60, 70, 90, 200)
    elif par == 'eta':
        DEN.eta = cms.vdouble(-2.4, -2.1, -1.6, -1.2, -0.9, -0.3, -0.2, 0.2, 0.3, 0.9, 1.2, 1.6, 2.1, 2.4)
    #elif par == 'pt':
    #    DEN.pt = cms.vdouble(20, 25, 30, 40, 50, 60, 120, 200)
    #elif par == 'pt':
    #    DEN.pt = cms.vdouble(20, 25, 30, 40, 50, 60, 100, 200)
    elif par == 'pt':
        DEN.pt = cms.vdouble(20, 25, 30, 40, 50, 60, 90, 200)
    #elif par == 'pt':
    #    DEN.pt = cms.vdouble(20, 25, 30, 40, 50, 60, 80, 200)
    #elif par == 'pt':
    #    DEN.pt = cms.vdouble(20, 25, 30, 40, 50, 60, 75, 90, 200)
    #elif par == 'pt':
    #    DEN.pt = cms.vdouble(20, 25, 30, 40, 50, 60, 70, 90, 200)
    elif par == 'pt_eta':
        DEN.pt = cms.vdouble(20, 25, 30, 40, 50, 60, 120)
        #DEN.pt = cms.vdouble(20, 25, 30, 40, 50, 60, 80, 100, 120)
        DEN.abseta = cms.vdouble( 0., 0.9, 1.2, 2.1, 2.4)
    elif par == 'vtx':
        DEN.tag_nVertices = cms.vdouble(0.5,2.5,4.5,6.5,8.5,10.5,12.5,14.5,16.5,18.5,20.5,22.5,24.5,26.5,28.5,30.5,32.5,34.5,36.5,38.5,40.5,42.5,44.5,46.5,48.5,50.5)
    #Selections
    #Request prescale on tag
    if num == "hlt_Mu17Mu8_leg17":
        pass
    #    DEN.tag_DoubleIsoMu17Mu8_IsoMu8leg = cms.vstring("pass")
    #    DEN.tag_DoubleIsoMu17TkMu8_IsoMu8leg = cms.vstring("pass")
    elif num == "hlt_Mu17_Mu8_OR_TkMu8_leg8":
        pass
        #DEN.tag_DoubleIsoMu17Mu8_IsoMu17leg= cms.vstring("pass")
        #DEN.tag_DoubleIsoMu17TkMu8_IsoMu17leg= cms.vstring("pass")
    elif num == "hlt_TkMu8_leg8":
        #pass
        DEN.tag_DoubleIsoMu17TkMu8_IsoMu17leg= cms.vstring("pass")
    if den == "gentrack": pass
    elif den == "looseidniso": 
        #DEN.LooseIDandLooseIso= cms.vstring("pass")
        DEN.PF = cms.vstring("pass")
        DEN.combRelIsoPF04dBeta= cms.vdouble(0, 0.25)
    elif den == "tightidniso": 
        #DEN.Tight2012andTightIso= cms.vstring("pass")
        DEN.Tight2012 = cms.vstring("pass")
        DEN.dzPV = cms.vdouble(-0.5, 0.5)
        DEN.combRelIsoPF04dBeta= cms.vdouble(0, 0.15)


args = sys.argv[1:]
iteration = ''
if len(args) > 1: iteration = args[1]
print "The iteration is", iteration
num = 'tight'
if len(args) > 2: num = args[2]
print 'The den is', num 
den = 'tight'
if len(args) > 3: den = args[3]
print 'The den is', den 
scenario = "data_all"
if len(args) > 4: scenario = args[4]
print "Will run scenario ", scenario
sample = 'data'
if len(args) > 5: sample = args[5]
print 'The sample is', sample
if len(args) > 6: par = args[6]
print 'The binning is', par 
bgFitFunction = 'default'
if len(args) > 7: bgFitFunction = args[7]
if bgFitFunction == 'CMSshape':
    print 'Will use the CMS shape to fit the background'
elif bgFitFunction == 'custom':
    print 'Will experiment with custom fit functions'
else:
    print 'Will use the standard fit functions for the backgroud'


process = cms.Process("TagProbe")
process.load('FWCore.MessageService.MessageLogger_cfi')
process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1) )

if not num  in ['hlt_Mu17Mu8_leg17', 'hlt_Mu17Mu8_leg8', 'hlt_Mu17TkMu8_leg17', 'hlt_Mu17TkMu8_leg8', 'hlt_Mu17Mu8_DZ_leg17', 'hlt_Mu17TkMu8_DZ_leg17','hlt_Mu17_Mu8_OR_TkMu8_leg8','hlt_TkMu8_leg8']:
    print '@ERROR: num should be in ', ['hlt_Mu17Mu8_leg17', 'hlt_Mu17Mu8_leg8', 'hlt_Mu17TkMu8_leg17', 'hlt_Mu17TkMu8_leg8', 'hlt_Mu17Mu8_DZ_leg17', 'hlt_Mu17TkMu8_DZ_leg17','hlt_Mu17_Mu8_OR_TkMu8_leg8','hlt_TkMu8_leg8'], 'You used', num, '.Abort'
    sys.exit()
#if not den in ['looseid', 'mediumid2016', 'mediumid', 'tightid', 'highptid', 'gentrack']:
if not den in ['looseidniso','tightidniso']:
    print '@ERROR: den should be', ['looseidniso','tightidniso'], 'You used', den, '.Abort'
    sys.exit()
if not par in  ['pt', 'eta', 'vtx', 'pt_eta', 'newpt', 'newpt_eta']:
    print '@ERROR: par should be', ['pt', 'eta', 'vtx', 'pt_eta', 'newpt', 'newpt_eta'], 'You used', par, '.Abort'

#_*_*_*_*_*_*_*_*_*_*_*_*
#Prepare variables, den, num and fit funct
#_*_*_*_*_*_*_*_*_*_*_*_*

#Set-up the mass range
_mrange = "70"
if 'iso' in num:
    _mrange = "77"
print '_mrange is', _mrange
mass_ =" mass"
if den == "highptid" : mass_ = "pair_newTuneP_mass"



Template = cms.EDAnalyzer("TagProbeFitTreeAnalyzer",
        NumCPU = cms.uint32(1),
    SaveWorkspace = cms.bool(False),


    Variables = cms.PSet(
        #essential for all den/num
        #mass = cms.vstring("Tag-muon Mass", _mrange, "130", "GeV/c^{2}"),
        #Jeta    = cms.vstring("muon #eta", "-2.5", "2.5", ""),
        ),

    Categories = cms.PSet(),
    Expressions = cms.PSet(),
    Cuts = cms.PSet(),


    PDFs = cms.PSet(
        voigtPlusExpo = cms.vstring(
            "Voigtian::signal(mass, mean[90,80,100], width[2.495], sigma[3,1,20])".replace("mass",mass_),
            "Exponential::backgroundPass(mass, lp[0,-5,5])".replace("mass",mass_),
            "Exponential::backgroundFail(mass, lf[0,-5,5])".replace("mass",mass_),
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
        vpvPlusExpo = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])".replace("mass",mass_),
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,2,10])".replace("mass",mass_),
            "SUM::signal(vFrac[0.8,0,1]*signal1, signal2)",
            "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])".replace("mass",mass_),
            "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])".replace("mass",mass_),
            "efficiency[0.9,0,1]",
            "signalFractionInPassing[0.9]"
        ),
        vpvPlusExpoMin70 = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])".replace("mass",mass_),
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,3,10])".replace("mass",mass_),
            "SUM::signal(vFrac[0.8,0.5,1]*signal1, signal2)",
            "Exponential::backgroundPass(mass, lp[-0.1,-1,0.1])".replace("mass",mass_),
            "Exponential::backgroundFail(mass, lf[-0.1,-1,0.1])".replace("mass",mass_),
            "efficiency[0.9,0.7,1]",
            "signalFractionInPassing[0.9]"
        ),
        vpvPlusCheb = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])".replace("mass",mass_),
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,3,10])".replace("mass",mass_),
            "SUM::signal(vFrac[0.8,0.5,1]*signal1, signal2)",
            #par3
            "RooChebychev::backgroundPass(mass, {a0[0.25,-0.2,0.5], a1[-0.35,-1,0.1],a2[0.,-0.25,0.25],a3[0.,-2,2]})".replace("mass",mass_),
            "RooChebychev::backgroundFail(mass, {a0[0.25,-0.2,0.5], a1[-0.35,-1,0.1],a2[0.,-0.25,0.25],a3[0.,-2,2]})".replace("mass",mass_),
            "efficiency[0.9,0.7,1]",
            "signalFractionInPassing[0.9]"
        ),
        vpvPlusCMS = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])".replace("mass",mass_),
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,3,10])".replace("mass",mass_),
            "SUM::signal(vFrac[0.8,0.5,1]*signal1, signal2)",
            "RooCMSShape::backgroundPass(mass, alphaPass[70.,60.,90.], betaPass[0.02, 0.01,0.1], gammaPass[0.001, 0.,0.1], peakPass[90.0])".replace("mass",mass_),
            #"RooCMSShape::backgroundFail(mass, alphaFail[70.,60.,90.], betaFail[0.02, 0.01,0.1], gammaFail[0.001, 0.,0.1], peakPass)".replace("mass",mass_),
            "RooCMSShape::backgroundFail(mass, alphaFail[70.,60.,90.], betaFail[0.02, 0.01,0.1], gammaFail[0.02, 0.005,0.1], peakPass)".replace("mass",mass_),
            "efficiency[0.9,0.7,1]",
            "signalFractionInPassing[0.9]"
        ),
        vpvPlusCMSbeta0p2 = cms.vstring(
            "Voigtian::signal1(mass, mean1[90,80,100], width[2.495], sigma1[2,1,3])".replace("mass",mass_),
            "Voigtian::signal2(mass, mean2[90,80,100], width,        sigma2[4,3,10])".replace("mass",mass_),
            "RooCMSShape::backgroundPass(mass, alphaPass[70.,60.,90.], betaPass[0.001, 0.,0.1], gammaPass[0.001, 0.,0.1], peakPass[90.0])".replace("mass",mass_),
            "RooCMSShape::backgroundFail(mass, alphaFail[70.,60.,90.], betaFail[0.03, 0.02,0.1], gammaFail[0.001, 0.,0.1], peakPass)".replace("mass",mass_), #Original
            #"RooCMSShape::backgroundFail(mass, alphaFail[70.,60.,90.], betaFail[0.03, 0.02,0.1], gammaFail[0.02, 0.005,0.1], peakPass)".replace("mass",mass_),
            #"RooCMSShape::backgroundFail(mass, alphaFail[70.,60.,90.], betaFail[0.03, 0.01,0.2], gammaFail[0.02, 0.005,0.1], peakPass)".replace("mass",mass_),
            "SUM::signal(vFrac[0.8,0.5,1]*signal1, signal2)",
            "efficiency[0.9,0.7,1]",
            "signalFractionInPassing[0.9]"
        )
    ),

    binnedFit = cms.bool(True),
    binsForFit = cms.uint32(40),
    saveDistributionsPlot = cms.bool(False),

    Efficiencies = cms.PSet(), # will be filled later
)

if sample == "data_MoriondBCDEFG":
    process.TnP_MuonID = Template.clone(
        InputFileNames = cms.vstring(
            'root://eoscms//eos/cms/store/group/phys_muon/perrin/Ntuple_for_doubletrigg2017/Central_Ntuples_skimmed/Data/TnPTree_80XRereco_Run2016B_GoldenJSON_Run276098to276384.root',
            'root://eoscms//eos/cms/store/group/phys_muon/perrin/Ntuple_for_doubletrigg2017/Central_Ntuples_skimmed/Data/TnPTree_80XRereco_Run2016C_GoldenJSON_Run276098to276384.root', 
            'root://eoscms//eos/cms/store/group/phys_muon/perrin/Ntuple_for_doubletrigg2017/Central_Ntuples_skimmed/Data/TnPTree_80XRereco_Run2016D_GoldenJSON_Run276098to276384.root', 
            'root://eoscms//eos/cms/store/group/phys_muon/perrin/Ntuple_for_doubletrigg2017/Central_Ntuples_skimmed/Data/TnPTree_80XRereco_Run2016E_GoldenJSON_Run276098to276384.root',
            'root://eoscms//eos/cms/store/group/phys_muon/perrin/Ntuple_for_doubletrigg2017/Central_Ntuples_skimmed/Data/TnPTree_80XRereco_Run2016F_GoldenJSON_Run276098to276384.root',
            'root://eoscms//eos/cms/store/group/phys_muon/perrin/Ntuple_for_doubletrigg2017/Central_Ntuples_skimmed/Data/TnPTree_80XRereco_Run2016G_GoldenJSON_Run278819to280384.root' 
            ),
        InputTreeName = cms.string("fitter_tree"),
        InputDirectoryName = cms.string("tpTree"),
        OutputFileName = cms.string("TnP_MuonID_%s.root" % scenario),
        Efficiencies = cms.PSet(),
        )

if sample == "data_MoriondH":
    process.TnP_MuonID = Template.clone(
        InputFileNames = cms.vstring(
            'root://eoscms//eos/cms/store/group/phys_muon/perrin/Ntuple_for_doubletrigg2017/Central_Ntuples_skimmed/Data/TnPTree_80XRereco_Run2016H_v2_GoldenJSON_Run281613to284035.root',
            'root://eoscms//eos/cms/store/group/phys_muon/perrin/Ntuple_for_doubletrigg2017/Central_Ntuples_skimmed/Data/TnPTree_80XRereco_Run2016H_GoldenJSON_Run284036to284044.root'
            ),
        InputTreeName = cms.string("fitter_tree"),
        InputDirectoryName = cms.string("tpTree"),
        OutputFileName = cms.string("TnP_MuonID_%s.root" % scenario),
        Efficiencies = cms.PSet(),
        )

#if sample == "data_MoriondH":
#    process.TnP_MuonID = Template.clone(
#        InputFileNames = cms.vstring(
#            'root://eoscms//eos/cms/store/group/phys_muon/perrin/Moriond2017/Data/TnPTree_80XRereco_Run2016G_GoldenJSON_Run278819to280384_skim2.root',
#            ),
#        InputTreeName = cms.string("fitter_tree"),
#        InputDirectoryName = cms.string("tpTree"),
#        OutputFileName = cms.string("TnP_MuonID_%s.root" % scenario),
#        Efficiencies = cms.PSet(),
#        )
#
if sample == "mc_MoriondBCDEFG" or sample == "mc_MoriondH":
    process.TnP_MuonID = Template.clone(
        InputFileNames = cms.vstring(
            'root://eoscms//eos/cms/store/group/phys_muon/perrin/Ntuple_for_doubletrigg2017/Central_Ntuples_skimmed/MC/MC_Moriond17_DY_tranch4Premix_part1to11_wBCDEFG_wH.root'
            ),
        InputTreeName = cms.string("fitter_tree"),
        InputDirectoryName = cms.string("tpTree"),
        OutputFileName = cms.string("TnP_MuonID_%s.root" % scenario),
        Efficiencies = cms.PSet(),
        )

weightvar = ''
if sample == "mc_MoriondBCDEFG": weightvar = "weightBCDEFG"
elif sample == "mc_MoriondH": weightvar = "weightH"
else: weightvar = "weight"

print 'weightvar is', weightvar

if scenario == "mc_all":
    print "Including the weight for MC"
    process.TnP_MuonID.WeightVariable = cms.string(weightvar)
    #process.TnP_MuonID.Variables.weight = cms.vstring(weightvar,"0","20","")
    exec('process.TnP_MuonID.Variables.%s = cms.vstring(weightvar,\"0\",\"20\",\"\")'%weightvar)
    #eval('process.TnP_MuonID.Variables.weight = cms.vstring(weightvar,\"0\",\"20\",\"\")')


BIN = cms.PSet(
        )

#Num_dic = {'looseid':'LooseID','mediumid2016':'MediumID2016','mediumid':'MediumID','tightid':'TightID','highptid':'HighPtID','looseiso':'LooseRelIso','tightiso':'TightRelIso','tklooseiso':'LooseRelTkIso'}
#Den_dic = {'gentrack':'genTracks','looseid':'LooseID','mediumid2016':'MediumID2016','mediumid':'MediumID','tightid':'TightIDandIPCut','highptid':'HighPtIDandIPCut'}
Den_dic = {'looseidniso':'LooseIDnISO','tightidniso':'TightIDnISO'}
#Sel_dic = {'looseidniso':'LooseIDnISO','tightidniso':'TightIDnISO'}

#Par_dic = {'eta':'eta', 'pt':}

print 'num is', num
print 'den is', den
FillVariables(par)
FillNumDen(num,den)

#print 'den is', den,'dic',Den_dic[den]
#print 'num is', num,'dic',Num_dic[num]
print 'par is', par

ID_BINS = [(num,("NUM_%s_DEN_%s_PAR_%s"%(num,Den_dic[den],par),BIN))]
print 'debug5'

print num
print (num,"NUM_%s_DEN_%s_PAR_%s"%(num,Den_dic[den],par),BIN)

#_*_*_*_*_*_*_*_*_*_*_*
#Launch fit production
#_*_*_*_*_*_*_*_*_*_*_*

for ID, ALLBINS in ID_BINS:
    print 'debug1'
    X = ALLBINS[0]
    B = ALLBINS[1]
    _output = os.getcwd() + '/Efficiency' + iteration
    if not os.path.exists(_output):
        print 'Creating', '/Efficiency' + iteration,', the directory where the fits are stored.'
        os.makedirs(_output)
    if scenario == 'data_all':
        _output += '/DATA' + '_' + sample
    elif scenario == 'mc_all':
        _output += '/MC' + '_' + sample
    if not os.path.exists(_output):
        os.makedirs(_output)
    module = process.TnP_MuonID.clone(OutputFileName = cms.string(_output + "/TnP_MC_%s.root" % (X)))
    #save the fitconfig in the plot directory
    shutil.copyfile(os.getcwd()+'/fitMuonTrg.py',_output+'/fitMuonTrg.py')
    shape = cms.vstring("vpvPlusExpo")
    print 'debug2'



    DEN = B.clone(); num_ = ID;
    FillBin(par)
    print 'num_ is', num_

    if bgFitFunction == 'default':
        if ('pt' in X):
            print 'den is', den 
            print 'num_ is ', num
            if (len(DEN.pt)==9):
                shape = cms.vstring("vpvPlusCMS","*pt_bin4*","vpvPlusCMSbeta0p2","*pt_bin4*","vpvPlusCMSbeta0p2","*pt_bin5*","vpvPlusCMSbeta0p2","*pt_bin6*","vpvPlusCheb","*pt_bin7*","vpvPlusCheb")#new bin
            #if (len(DEN.pt)==9):
            #    shape = cms.vstring("vpvPlusCMS","*pt_bin3*","vpvPlusCheb","*pt_bin4*","vpvPlusCheb","*pt_bin5*","vpvPlusCheb","*pt_bin6*","vpvPlusCheb","*pt_bin7*","vpvPlusCheb","*pt_bin8*","vpvPlusCheb")
            #if (len(DEN.pt)==8):
            #    shape = cms.vstring("vpvPlusCMS","*pt_bin4*","vpvPlusCMSbeta0p2","*pt_bin4*","vpvPlusCMSbeta0p2","*pt_bin5*","vpvPlusCheb","*pt_bin6*","vpvPlusCheb")
            if (len(DEN.pt)==8):
                shape = cms.vstring("vpvPlusCMS","*pt_bin4*","vpvPlusCMSbeta0p2","*pt_bin4*","vpvPlusCMSbeta0p2","*pt_bin5*","vpvPlusCMSbeta0p2","*pt_bin6*","vpvPlusCheb")#Test CMSshape in before-last bin
            if scenario == "data_all":
                if (len(DEN.pt)==7):#for pt_eta
                    #shape = cms.vstring("vpvPlusCMS","*pt_bin3*","vpvPlusCMSbeta0p2","*pt_bin4*","vpvPlusCMSbeta0p2","*eta_bin0*pt_bin5*","vpvPlusCheb","*eta_bin1*pt_bin5*","vpvPlusCMSbeta0p2","*eta_bin2*pt_bin5*","vpvPlusCMSbeta0p2","*eta_bin3*pt_bin5*","vpvPlusCMSbeta0p2")
                    #shape = cms.vstring("vpvPlusCMS","*pt_bin3*","vpvPlusCMSbeta0p2","*pt_bin4*","vpvPlusCMSbeta0p2","*eta_bin0*pt_bin5*","vpvPlusCheb","*eta_bin1*pt_bin5*","vpvPlusCheb","*eta_bin2*pt_bin5*","vpvPlusCMSbeta0p2","*eta_bin3*pt_bin5*","vpvPlusCMSbeta0p2")
                    shape = cms.vstring("vpvPlusExpo","*pt_bin3*","vpvPlusCMSbeta0p2","*pt_bin4*","vpvPlusCMSbeta0p2","*pt_bin5*","vpvPlusCMSbeta0p2")
            elif scenario == "mc_all":
                if (len(DEN.pt)==7):#for pt_eta
                    #shape = cms.vstring("vpvPlusCMS","*pt_bin3*","vpvPlusCMSbeta0p2","*pt_bin4*","vpvPlusCMSbeta0p2","*eta_bin0*pt_bin5*","vpvPlusCheb","*eta_bin1*pt_bin5*","vpvPlusCheb","*eta_bin2*pt_bin5*","vpvPlusCMSbeta0p2","*eta_bin3*pt_bin5*","vpvPlusCMSbeta0p2")
                    #shape = cms.vstring("vpvPlusCMSbeta0p2","*pt_bin0*","vpvPlusExpo","*pt_bin1*","vpvPlusExpo","*pt_bin2*","vpvPlusExpo")
                    shape = cms.vstring("vpvPlusCMSbeta0p2","*pt_bin0*","vpvPlusExpo","*pt_bin1*","vpvPlusExpo","*pt_bin2*","vpvPlusExpo","*pt_bin3*","vpvPlusExpo")
            #if (len(DEN.pt)==9):
            #    shape = cms.vstring("vpvPlusCMS","*pt_bin3*","vpvPlusCMSbeta0p2","*pt_bin4*","vpvPlusCMSbeta0p2","*pt_bin5*","vpvPlusCMSbeta0p2","*pt_bin6*","vpvPlusCMSbeta0p2","*pt_bin7*","vpvPlusCMSbeta0p2","*pt_bin8*","vpvPlusCMS")
            #if (len(DEN.pt)==8):
            #    shape = cms.vstring("vpvPlusCMS","*pt_bin3*","vpvPlusCMSbeta0p2","*pt_bin4*","vpvPlusCMSbeta0p2","*pt_bin5*","vpvPlusCMSbeta0p2","*pt_bin6*","vpvPlusCMS")
            #if (len(DEN.pt)==7):
            #    shape = cms.vstring("vpvPlusCMS","*pt_bin3*","vpvPlusCMSbeta0p2","*pt_bin4*","vpvPlusCMSbeta0p2","*pt_bin5*","vpvPlusCMSbeta0p2")

    mass_variable ="mass"
    print 'den is', den
    if den == "highptid" :
        mass_variable = "pair_newTuneP_mass"
    #compute isolation efficiency
    if scenario == 'data_all':
        if num_.find("Iso4") != -1 or num_.find("Iso3") != -1:
            setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
                EfficiencyCategoryAndState = cms.vstring(num_,"below"),
                UnbinnedVariables = cms.vstring(mass_variable),
                BinnedVariables = DEN,
                BinToPDFmap = shape
                ))
        else:
            setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
                EfficiencyCategoryAndState = cms.vstring(num_,"above"),
                UnbinnedVariables = cms.vstring(mass_variable),
                BinnedVariables = DEN,
                BinToPDFmap = shape
                ))
            print 'yeah'
        setattr(process, "TnP_MuonID_"+ID+"_"+X, module)
        setattr(process, "run_"+ID+"_"+X, cms.Path(module))
        print 'yeah baby'
    elif scenario == 'mc_all' and not par == 'vtx':
        if num_.find("Iso4") != -1 or num_.find("Iso3") != -1:
            setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
                EfficiencyCategoryAndState = cms.vstring(num_,"below"),
                #UnbinnedVariables = cms.vstring(mass_variable,"weight"),
                UnbinnedVariables = cms.vstring(mass_variable,weightvar),
                BinnedVariables = DEN,
                BinToPDFmap = shape
                ))
        else:
            setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
                EfficiencyCategoryAndState = cms.vstring(num_,"above"),
                #UnbinnedVariables = cms.vstring(mass_variable,"weight"),
                UnbinnedVariables = cms.vstring(mass_variable,weightvar),
                BinnedVariables = DEN,
                BinToPDFmap = shape
                ))
        setattr(process, "TnP_MuonID_"+ID+"_"+X, module)
        setattr(process, "run_"+ID+"_"+X, cms.Path(module))
    elif scenario == 'mc_all' and par == 'vtx':
        if num_.find("Iso4") != -1 or num_.find("Iso3") != -1:
            setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
                EfficiencyCategoryAndState = cms.vstring(num_,"below"),
                UnbinnedVariables = cms.vstring(mass_variable),
                BinnedVariables = DEN,
                BinToPDFmap = shape
                ))
        else:
            setattr(module.Efficiencies, ID+"_"+X, cms.PSet(
                EfficiencyCategoryAndState = cms.vstring(num_,"above"),
                UnbinnedVariables = cms.vstring(mass_variable),
                BinnedVariables = DEN,
                BinToPDFmap = shape
                ))
        setattr(process, "TnP_MuonID_"+ID+"_"+X, module)
        setattr(process, "run_"+ID+"_"+X, cms.Path(module))
