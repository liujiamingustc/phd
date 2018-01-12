/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONPSV.CPP - Implementation of OOTEN ONPSV (pressures sustaining valve) class

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

#include "ONPSV.h"

//---------------------------------------------------------------------------

#pragma package(smart_init)

ONPSV::ONPSV(void) {}

ONPSV::ONPSV(int enIndex, ONSystem* parent, ONNode* startNode, ONNode* endNode)
        :ONValve(enIndex, parent, startNode, endNode) {}

ONPSV::ONPSV(ONPSV &o):ONValve(o.epanetIndex(), o.parent(), o.startNode(), o.endNode()) {}

ONLink* ONPSV::clone(void)
{
    return (ONLink*)(new ONPSV(*this));
}

ONPSV::~ONPSV(void) {}

ONElement::elementTpe ONPSV::type(void) const
{
    return etPSV;
}


