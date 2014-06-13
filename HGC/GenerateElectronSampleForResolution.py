import os
from ROOT import *
ptVector=[5, 10, 15, 20, 30, 40, 50, 70, 100, 150, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
EtaVector=[2.00]
command = 'sleep 1; ' 

def SubmitJobfunc(pt, eta):
    pt_ = int(pt)
    eta_ = int(eta*100)
    postname='Pt'+str(pt_)+'_eta'+str(eta_)+'_Muon'
    shellfilename = 'temporary_Res_submit_'+postname+'.sh'
    #print "pt = ",pt
    #print "eta = ",eta
    #print shellfilename
    os.system('rm '+shellfilename)

    cfgfilename='temporary_Res_cfg_'+postname+'cfg.py'
    print cfgfilename
    os.system('rm '+cfgfilename)

    filecfg = open(cfgfilename,'a')
    for linecfg in open('Template-GEN-SIM-HGC-SingleElectron_cfg.py','r'):
        linecfg = linecfg.replace('ETAVAL',str(eta))
        linecfg = linecfg.replace('ETAINTVAL',str(eta_))
        linecfg = linecfg.replace('PTVAL',str(pt))
        filecfg.write(linecfg)
    filecfg.close()
    #os.system('chmod 777 '+cfgfilename)
        

    fileshell = open(shellfilename,'a')
    for linesh in open('Template_submit_batch.sh','r'):
        linesh = linesh.replace('CFGFile',cfgfilename)
        fileshell.write(linesh)
    fileshell.close()
    os.system('chmod 777 '+shellfilename)
    tmpcmnd = 'bsub  -q 1nw '+' '+shellfilename+';'
    command =  tmpcmnd
    
    print command
    #os.system(command)
    return 0





for ipt in range(len(ptVector)):
    for ieta in range(len(EtaVector)):
        SubmitJobfunc( ptVector[ipt], EtaVector[ieta] )


