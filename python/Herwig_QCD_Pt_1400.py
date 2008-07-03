import FWCore.ParameterSet.Config as cms

configurationMetadata = cms.untracked.PSet(
	version = cms.untracked.string('$Revision: 1.2 $'),
	name = cms.untracked.string('$Source: /cvs_server/repositories/CMSSW/CMSSW/Configuration/GenProduction/python/Herwigpp_base_cff.py,v $'),
	annotation = cms.untracked.string('Summer08 CSA: Herwig++ generation of QCD events, CTEQ6L used, MinKT=1400 GeV')
)

source = cms.Source("ThePEGSource",
	dataLocation = cms.string('${HERWIGPATH}'),
	repository = cms.string('HerwigDefaults.rpo'),
	eventHandlers = cms.string('/Herwig/EventHandlers'),
	generatorModule = cms.string('/Herwig/Generators/LHCGenerator'),
	configFiles = cms.vstring(),
	run = cms.string('LHC'),

	crossSection = cms.untracked.double(1.845050e-07),
	filterEfficiency = cms.untracked.double(1.0),

		cm10TeV = cms.vstring(
			'set /Herwig/Generators/LHCGenerator:EventHandler:LuminosityFunction:Energy 10000.0',
			'set /Herwig/Shower/Evolver:IntrinsicPtGaussian 2.1*GeV',
		),

		QCDCSAParameters = cms.vstring(
			'cd /Herwig/MatrixElements/',
			'insert SimpleQCD:MatrixElements[0] MEQCD2to2',
			'cd /',
			'set /Herwig/Cuts/JetKtCut:MinKT 1400*GeV',
			'set /Herwig/UnderlyingEvent/MPIHandler:Algorithm 1',
		),

		basicSetup = cms.vstring(
			'cd /Herwig/Generators',
			'set LHCGenerator:NumberOfEvents 10000000',
			'set LHCGenerator:DebugLevel 1',
			'set LHCGenerator:PrintEvent 0',
			'set LHCGenerator:MaxErrors 10000',
			'cd /',
		),

		disableCtau10mmDecays = cms.vstring(
			'cd /Herwig/Particles',
			'set K-/K-->nu_ebar,e-;:OnOff Off',
			'set K+/K+->nu_e,e+;:OnOff Off',
			'set K-/K-->nu_mubar,mu-;:OnOff Off',
			'set K+/K+->nu_mu,mu+;:OnOff Off',
			'set K-/K-->pi0,nu_ebar,e-;:OnOff Off',
			'set K+/K+->pi0,nu_e,e+;:OnOff Off',
			'set K-/K-->pi0,nu_mubar,mu-;:OnOff Off',
			'set K+/K+->pi0,nu_mu,mu+;:OnOff Off',
			'set K-/K-->pi0,pi0,nu_ebar,e-;:OnOff Off',
			'set K+/K+->pi0,pi0,nu_e,e+;:OnOff Off',
			'set K-/K-->pi-,gamma,gamma;:OnOff Off',
			'set K+/K+->pi+,gamma,gamma;:OnOff Off',
			'set K-/K-->pi-,pi0;:OnOff Off',
			'set K+/K+->pi+,pi0;:OnOff Off',
			'set K-/K-->pi-,pi0,pi0;:OnOff Off',
			'set K+/K+->pi+,pi0,pi0;:OnOff Off',
			'set K-/K-->pi+,pi-,nu_ebar,e-;:OnOff Off',
			'set K+/K+->pi+,pi-,nu_e,e+;:OnOff Off',
			'set K-/K-->pi+,pi-,nu_mubar,mu-;:OnOff Off',
			'set K+/K+->pi+,pi-,nu_mu,mu+;:OnOff Off',
			'set K-/K-->pi+,pi-,pi-;:OnOff Off',
			'set K+/K+->pi+,pi+,pi-;:OnOff Off',
			'set K_L0/K_L0->gamma,e-,e+;:OnOff Off',
			'set K_L0/K_L0->gamma,gamma;:OnOff Off',
			'set K_L0/K_L0->pi0,gamma,gamma;:OnOff Off',
			'set K_L0/K_L0->pi0,pi0;:OnOff Off',
			'set K_L0/K_L0->pi0,pi0,pi0;:OnOff Off',
			'set K_L0/K_L0->pi+,nu_ebar,e-;:OnOff Off',
			'set K_L0/K_L0->pi-,nu_e,e+;:OnOff Off',
			'set K_L0/K_L0->pi+,nu_mubar,mu-;:OnOff Off',
			'set K_L0/K_L0->pi-,nu_mu,mu+;:OnOff Off',
			'set K_L0/K_L0->pi+,pi0,nu_ebar,e-;:OnOff Off',
			'set K_L0/K_L0->pi-,pi0,nu_e,e+;:OnOff Off',
			'set K_L0/K_L0->pi+,pi-;:OnOff Off',
			'set K_L0/K_L0->pi+,pi-,pi0;:OnOff Off',
			'set K_S0/K_S0->gamma,gamma;:OnOff Off',
			'set K_S0/K_S0->pi0,pi0;:OnOff Off',
			'set K_S0/K_S0->pi+,nu_ebar,e-;:OnOff Off',
			'set K_S0/K_S0->pi-,nu_e,e+;:OnOff Off',
			'set K_S0/K_S0->pi+,pi-,e-,e+;:OnOff Off',
			'set K_S0/K_S0->pi+,pi-;:OnOff Off',
			'set Lambda0/Lambda0->n0,gamma;:OnOff Off',
			'set Lambda0/Lambda0->n0,pi0;:OnOff Off',
			'set Lambda0/Lambda0->p+,nu_ebar,e-;:OnOff Off',
			'set Lambda0/Lambda0->p+,pi-,gamma;:OnOff Off',
			'set Lambda0/Lambda0->p+,pi-;:OnOff Off',
			'set Lambdabar0/Lambdabar0->nbar0,gamma;:OnOff Off',
			'set Lambdabar0/Lambdabar0->nbar0,pi0;:OnOff Off',
			'set Lambdabar0/Lambdabar0->pbar-,nu_e,e+;:OnOff Off',
			'set Lambdabar0/Lambdabar0->pbar-,pi+,gamma;:OnOff Off',
			'set Lambdabar0/Lambdabar0->pbar-,pi+;:OnOff Off',
			'set mu+/mu+->nu_mubar,nu_e,e+;:OnOff Off',
			'set mu-/mu-->nu_mu,nu_ebar,e-;:OnOff Off',
			'set Omegabar+/Omegabar+->Lambdabar0,K+;:OnOff Off',
			'set Omegabar+/Omegabar+->Xibar0,nu_e,e+;:OnOff Off',
			'set Omegabar+/Omegabar+->Xibar0,pi+;:OnOff Off',
			'set Omegabar+/Omegabar+->Xibar+,pi0;:OnOff Off',
			'set Omega-/Omega-->Lambda0,K-;:OnOff Off',
			'set Omega-/Omega-->Xi0,nu_ebar,e-;:OnOff Off',
			'set Omega-/Omega-->Xi0,pi-;:OnOff Off',
			'set Omega-/Omega-->Xi-,pi0;:OnOff Off',
			'set pi-/pi-->nu_ebar,e-;:OnOff Off',
			'set pi+/pi+->nu_e,e+;:OnOff Off',
			'set pi-/pi-->nu_mubar,mu-;:OnOff Off'
			'set pi-/pi-->nu_mubar,mu-;:OnOff Off',
			'set pi+/pi+->nu_mu,mu+;:OnOff Off',
			'set Sigmabar+/Sigmabar+->nbar0,nu_e,e+;:OnOff Off',
			'set Sigmabar+/Sigmabar+->nbar0,pi+,gamma;:OnOff Off',
			'set Sigmabar-/Sigmabar-->nbar0,pi-;:OnOff Off',
			'set Sigmabar+/Sigmabar+->nbar0,pi+;:OnOff Off',
			'set Sigmabar-/Sigmabar-->pbar-,gamma;:OnOff Off',
			'set Sigmabar-/Sigmabar-->pbar-,pi0;:OnOff Off',
			'set Sigma-/Sigma-->n0,nu_ebar,e-;:OnOff Off',
			'set Sigma-/Sigma-->n0,pi-,gamma;:OnOff Off',
			'set Sigma-/Sigma-->n0,pi-;:OnOff Off',
			'set Sigma+/Sigma+->n0,pi+;:OnOff Off',
			'set Sigma+/Sigma+->p+,gamma;:OnOff Off',
			'set Sigma+/Sigma+->p+,pi0;:OnOff Off',
			'set Xi0/Xi0->Lambda0,gamma;:OnOff Off',
			'set Xi0/Xi0->Lambda0,pi0;:OnOff Off',
			'set Xi0/Xi0->Sigma0,gamma;:OnOff Off',
			'set Xibar0/Xibar0->Lambdabar0,gamma;:OnOff Off',
			'set Xibar0/Xibar0->Lambdabar0,pi0;:OnOff Off',
			'set Xibar0/Xibar0->Sigmabar0,gamma;:OnOff Off',
			'set Xibar+/Xibar+->Lambdabar0,nu_e,e+;:OnOff Off',
			'set Xibar+/Xibar+->Lambdabar0,pi+;:OnOff Off',
			'set Xi-/Xi-->Lambda0,nu_ebar,e-;:OnOff Off',
			'set Xi-/Xi-->Lambda0,pi-;:OnOff Off',
			'cd /',
		),

		parameterSets = cms.vstring(
			'cm10TeV',
			'QCDCSAParameters',
			'basicSetup',
			'disableCtau10mmDecays',
		),
)
