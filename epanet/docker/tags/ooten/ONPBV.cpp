/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONPBV.CPP - Implementation of OOTEN ONPBV (pressure breaker valve) class

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

#include "ONPBV.h"

//---------------------------------------------------------------------------

#pragma package(smart_init)

ONPBV::ONPBV(void) {}

ONPBV::ONPBV(int enIndex, ONSystem* parent, ONNode* startNode, ONNode* endNode)
        :ONValve(enIndex, parent, startNode, endNode) {}

ONPBV::ONPBV(ONPBV &o):ONValve(o.epanetIndex(), o.parent(), o.startNode(), o.endNode()) {}

ONLink* ONPBV::clone(void)
{
    return (ONLink*)(new ONPBV(*this));
}

ONPBV::~ONPBV(void) {}

ONElement::elementTpe ONPBV::type(void) const
{
    return etPBV;
}


