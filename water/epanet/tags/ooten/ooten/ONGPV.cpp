/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONGPV.CPP - Implementation of OOTEN ONGPV (general purpose valve) class

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

#include "ONGPV.h"

//---------------------------------------------------------------------------

#pragma package(smart_init)

ONGPV::ONGPV(void) {}

ONGPV::ONGPV(int enIndex, ONSystem *parent, ONNode* startNode, ONNode* endNode)
        :ONValve(enIndex, parent, startNode, endNode) {}

ONGPV::ONGPV(ONGPV &o):ONValve(o.epanetIndex(), o.parent(), o.startNode(), o.endNode()) {}

ONLink* ONGPV::clone(void)
{
    return (ONLink*)(new ONGPV(*this));
}

ONGPV::~ONGPV(void) {}

ONElement::elementTpe ONGPV::type(void) const
{
    return etGPV;
}

