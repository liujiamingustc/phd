/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONPRV.CPP - Implementation of OOTEN ONPRV (pressure reducing valve) class

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

#include "ONPRV.h"

//---------------------------------------------------------------------------

#pragma package(smart_init)

ONPRV::ONPRV(void) {}

ONPRV::ONPRV(int enIndex, ONSystem* parent, ONNode* startNode, ONNode* endNode)
        :ONValve(enIndex, parent, startNode, endNode) {}

ONPRV::ONPRV(ONPRV &o):ONValve(o.epanetIndex(), o.parent(), o.startNode(), o.endNode()) {}

ONLink* ONPRV::clone(void)
{
    return (ONLink*)(new ONPRV(*this));
}

ONPRV::~ONPRV(void) {}

ONElement::elementTpe ONPRV::type(void) const
{
    return etPRV;
}


