import FWCore.ParameterSet.Config as cms

#                                                    
# Full-scale Digitization of the simulated hits      
# in all CMS subdets : Tracker, ECAL, HCAl, Muon's;  
# MixingModule (at least in zero-pileup mode) needs  
# to be included to make Digi's operational, since   
# it's required for ECAL/HCAL & Muon's                
# Defined in a separate fragment
#                                                    
# Tracker Digis (Pixel + SiStrips)
# returns sequence "trDigi"
#
from SimTracker.Configuration.SimTracker_cff import *

# Calorimetry Digis (Ecal + Hcal) - * unsuppressed *
# returns sequence "calDigi"
from SimCalorimetry.Configuration.SimCalorimetry_cff import *
# Muon Digis (CSC + DT + RPC)
# returns sequence "muonDigi"
#
from SimMuon.Configuration.SimMuon_cff import *
#
# include TrackingParticle Producer
# NOTA BENE: it MUST be run here at the moment, since it depends 
# of the availability of the CrossingFrame in the Event
#
from SimGeneral.Configuration.SimGeneral_cff import *

#Special parameterization for cosmics
simSiPixelDigis.TofLowerCut = cms.double(18.5)
simSiPixelDigis.TofUpperCut = cms.double(43.5)
simSiStripDigis.CosmicDelayShift = cms.untracked.double(31)

simEcalUnsuppressedDigis.cosmicsPhase = cms.bool(True)
simEcalUnsuppressedDigis.cosmicsShift = cms.double(1.)
EcalTrigPrimESProducer.DatabaseFile = cms.untracked.string("TPG_cosmics_ZS.txt.gz")
simEcalDigis.ebDccAdcToGeV = cms.double(0.00875)
simEcalDigis.srpBarrelLowInterestChannelZS = cms.double(0.0153125)

simHcalDigis.hbhe.level = cms.int32(-10000)
simHcalDigis.ho.level   = cms.int32(-10000)
simHcalDigis.hf.level   = cms.int32(-10000)

doAllDigi = cms.Sequence(trDigi+calDigi+muonDigi)
pdigi = cms.Sequence(cms.SequencePlaceholder("randomEngineStateProducer")*cms.SequencePlaceholder("mix")*doAllDigi*trackingParticles)


