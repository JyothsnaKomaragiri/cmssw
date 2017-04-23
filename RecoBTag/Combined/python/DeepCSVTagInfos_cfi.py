import FWCore.ParameterSet.Config as cms
from RecoBTag.SecondaryVertex.combinedSecondaryVertexCommon_cff import combinedSecondaryVertexCommon

pfDeepCSVTagInfos = cms.EDProducer(
	'DeepNNTagInfoProducer',
        trackIPTagInfos = cms.InputTag('ImpactParameterTagInfos'),
	svTagInfos = cms.InputTag('InclusiveSecondaryVertexFinderTagInfos'),
	computer = combinedSecondaryVertexCommon
	)
