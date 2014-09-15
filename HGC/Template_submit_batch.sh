#!/bin/sh
export SCRAM_ARCH=slc6_amd64_gcc472
currentpath=$PWD
cd /afs/cern.ch/work/k/khurana/HGCAL/Digi/CMSSW_6_2_0_SLHC16/src/EventGeneration/HGC/
eval `scram runtime -sh`
cmsRun CFGFile
