/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONTCV.CPP - Implementation of OOTEN ONTCV (throttle control valve) class

VERSION:    1.00beta
DATE:       13 June 2003
AUTHOR:     JE van Zyl
            Rand Afrikaans University
            Johannesburg
            South Africa
            jevz@ing.rau.ac.za

*******************************************************************
*/

//---------------------------------------------------------------------------


#pragma hdrstop

#include "ONTCV.h"

//---------------------------------------------------------------------------

#pragma package(smart_init)

ONTCV::ONTCV(void) {}

ONTCV::ONTCV(int enIndex, ONSystem* parent, ONNode* startNode, ONNode* endNode)
        :ONValve(enIndex, parent, startNode, endNode) {}

ONTCV::ONTCV(ONTCV &o):ONValve(o.epanetIndex(), o.parent(), o.startNode(), o.endNode()) {}

ONLink* ONTCV::clone(void)
{
    return (ONLink*)(new ONTCV(*this));
}

ONTCV::~ONTCV(void) {}

ONElement::elementTpe ONTCV::type(void) const
{
    return etTCV;
}


