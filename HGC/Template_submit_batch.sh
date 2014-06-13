#!/bin/sh
export SCRAM_ARCH=slc6_amd64_gcc472
cd /afs/cern.ch/work/k/khurana/private/HGCAL/try/CMSSW_6_2_0_SLHC13/src/HGCAnalyzer/HGCSimHitsAnalyzer/EventGenerator
eval `scram runtime -sh`
cmsRun CFGFile
