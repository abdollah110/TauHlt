import FWCore.ParameterSet.Config as cms

# MonitorTrackGlobal
SiStripMonitorTrack = cms.EDAnalyzer(
    "SiStripMonitorTrack",
    
    TrackProducer = cms.string('generalTracks'),
    TrackLabel    = cms.string(''),
    TrajectoryInEvent = cms.bool(True),
    AlgoName      = cms.string('GenTk'),
    
    RawDigis_On     = cms.bool(False),
    RawDigiProducer = cms.string('simSiStripDigis'),
    RawDigiLabel    = cms.string('VirginRaw'),
    
    OutputMEsInRootFile = cms.bool(False),
    OutputFileName = cms.string('test_monitortrackparameters_rs.root'),    
    
    Cluster_src = cms.InputTag('siStripClusters'),
    
    ModulesToBeExcluded = cms.vuint32(),
    
    Mod_On        = cms.bool(False),
    OffHisto_On   = cms.bool(True),
    Trend_On      = cms.bool(False),
    HistoFlag_On  = cms.bool(False),
    RingFlag_On   = cms.bool(False),
    TkHistoMap_On = cms.bool(True),   
    
    ClusterConditions = cms.PSet( On       = cms.bool(False),
                                  minStoN  = cms.double(0.0),
                                  maxStoN  = cms.double(2000.0),
                                  minWidth = cms.double(0.0),
                                  maxWidth = cms.double(200.0)
                                  ),
    
    TH1nClustersOn = cms.PSet( Nbinx = cms.int32(100),
                             xmin  = cms.double(-0.5),
                             xmax  = cms.double(1999.5),
                             layerswitchon  = cms.bool(True)
                             ),   

    TH1nClustersOff = cms.PSet( Nbinx = cms.int32(200),
                             xmin  = cms.double(-0.5),
                             xmax  = cms.double(8999.5),
                             layerswitchon  = cms.bool(True)
                             ),
    
    TH1ClusterCharge = cms.PSet( Nbinx = cms.int32(100),
                                 xmin  = cms.double(-0.5),
                                 xmax  = cms.double(999.5),
                                 layerswitchon  = cms.bool(True)
                                 ),
    
    TH1ClusterStoN = cms.PSet( Nbinx = cms.int32(100),
                               xmin  = cms.double(-0.5),
                               xmax  = cms.double(299.5),
                               layerswitchon  = cms.bool(True)
                               ),
    
    TH1ClusterChargeCorr = cms.PSet( Nbinx = cms.int32(100),
                                     xmin  = cms.double(-0.5),
                                     xmax  = cms.double(399.5),
                                     layerswitchon  = cms.bool(True)
                                     ),
    
    TH1ClusterStoNCorr = cms.PSet( Nbinx = cms.int32(200),
                                   xmin  = cms.double(-0.5),
                                   xmax  = cms.double(199.5),
                                   layerswitchon  = cms.bool(True),
                                   globalswitchon = cms.bool(True)
                                   ),
    TH1ClusterStoNCorrMod = cms.PSet( Nbinx = cms.int32(50),
                                   xmin  = cms.double(-0.5),
                                   xmax  = cms.double(199.5)
                                   ),
    
    TH1ClusterNoise = cms.PSet( Nbinx = cms.int32(20),
                                xmin  = cms.double(-0.5),
                                xmax  = cms.double(9.5),
                                layerswitchon  = cms.bool(True)
                                ),
    
    TH1ClusterWidth = cms.PSet( Nbinx = cms.int32(20),
                                xmin  = cms.double(-0.5),
                                xmax  = cms.double(19.5),
                                layerswitchon  = cms.bool(True)
                                ),
    
    TH1ClusterSymmEtaCC = cms.PSet( Nbinx = cms.int32(120),
                                    xmin  = cms.double(-0.1),
                                    xmax  = cms.double(1.1)
                                    ),
    
    TH1ClusterWidthCC = cms.PSet( Nbinx = cms.int32(10),
                                  xmin  = cms.double(-0.5),
                                  xmax  = cms.double(9.5)
                                  ),
    
    TH1ClusterEstimatorCC = cms.PSet( Nbinx = cms.int32(120),
                                      xmin  = cms.double(-0.1),
                                      xmax  = cms.double(1.1)
                                      ),
    
    TProfileClusterPGV = cms.PSet( Nbinx = cms.int32(20),
                                   xmin = cms.double(-10.0),
                                   xmax = cms.double(10.0),
                                   Nbiny = cms.int32(20),
                                   ymin = cms.double(-0.1),
                                   ymax = cms.double(1.2)
                                   ),
    
    Trending = cms.PSet( Nbins      = cms.int32(10),
                         Steps      = cms.int32(5),
                         UpdateMode = cms.int32(1)
                         ),

    UseDCSFiltering = cms.bool(True)
    
    )
