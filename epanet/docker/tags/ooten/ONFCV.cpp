/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONFCV.CPP - Implementation of OOTEN ONFCV (flow control valve) class

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

#include "ONFCV.h"


//---------------------------------------------------------------------------

#pragma package(smart_init)

ONFCV::ONFCV(void) {}

ONFCV::ONFCV(int enIndex, ONSystem* parent, ONNode* startNode, ONNode* endNode)
        :ONValve(enIndex, parent, startNode, endNode) {}

ONFCV::ONFCV(ONFCV &o):ONValve(o.epanetIndex(), o.parent(), o.startNode(), o.endNode()) {}

ONLink* ONFCV::clone(void)
{
    return (ONLink*)(new ONFCV(*this));
}

ONFCV::~ONFCV(void) {}

ONElement::elementTpe ONFCV::type(void) const
{
    return etFCV;
}

