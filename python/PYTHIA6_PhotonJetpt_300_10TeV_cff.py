

import FWCore.ParameterSet.Config as cms

source = cms.Source("EmptySource")

from Configuration.GenProduction.PythiaUESettings_cfi import *
generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0),
    comEnergy = cms.double(10000.0),
    crossSection = cms.untracked.double(4.193),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
processParameters = cms.vstring(
            'MSEL=10',
            'CKIN(3)=300  ! minimum pt hat for hard interactions'),
   # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')

       
   


    )
)
configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.1 $'),
    name = cms.untracked.string
('$Source: /local/projects/CMSSW/rep/CMSSW/Configuration/GenProduction/python/PYTHIA6_PhotonJetpt_300_10TeV_cff.py,v $'),
    annotation = cms.untracked.string('PhotonJetpt-300 at 10TeV')
)

ProductionFilterSequence = cms.Sequence(generator)
