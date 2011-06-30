#ifndef Fireworks_Core_FWGeoTopNode_h
#define Fireworks_Core_FWGeoTopNode_h
// -*- C++ -*-
//
// Package:     Core
// Class  :     FWGeoTopNode
// 
/**\class FWGeoTopNode FWGeoTopNode.h Fireworks/Core/interface/FWGeoTopNode.h

 Description: [one line class summary]

 Usage:
    <usage>

*/
//
// Original Author:  Matevz Tadel, Alja Mrak Tadel
//         Created:  Thu Jun 23 01:25:00 CEST 2011
// $Id: FWGeoTopNode.h,v 1.2 2011/06/25 04:29:23 amraktad Exp $
//

#include "Fireworks/Core/interface/FWGeometryTableManager.h"
#include "TEveElement.h"
#include "TAtt3D.h"
#include "TAttBBox.h"

class TGeoHMatrix;

class FWGeometryTableManager;
class FWGeometryBrowser;
class TBuffer3D;
class TGeoNode;


class FWGeoTopNode : public TEveElementList,
                     public TAtt3D,
                     public TAttBBox
{
public:
   FWGeoTopNode(FWGeometryBrowser*);
   virtual ~FWGeoTopNode();

   virtual void Paint(Option_t* option="");

   virtual void ComputeBBox();
private:
   FWGeoTopNode(const FWGeoTopNode&); // stop default
   const FWGeoTopNode& operator=(const FWGeoTopNode&); // stop default


   void setupBuffMtx(TBuffer3D& buff,TGeoHMatrix& mat);

   void paintChildNodesRecurse(int idx, TGeoHMatrix& mtx);
   void  paintShape(FWGeometryTableManager::NodeInfo& nodeInfo, TGeoHMatrix& nm);
   FWGeometryBrowser       *m_geoBrowser;
};


#endif