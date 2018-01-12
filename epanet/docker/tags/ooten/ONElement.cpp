/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONELEMENT.CPP - Implementation of OOTEN ONElement class

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

#include "ONElement.h"

//---------------------------------------------------------------------------

#pragma package(smart_init)

ONElement::ONElement(void)
{
    parent_ = 0;
    enIndex_ = 0;
}

ONElement::ONElement(int enIndex, ONSystem* parent)
{
    parent_ = parent;
    enIndex_ = enIndex;
}

ONElement::ONElement(const ONElement &o)
{
    parent_ = o.parent();
    enIndex_ = o.epanetIndex();
}

ONElement::~ONElement(void) {}

ONElement::elementTpe ONElement::type(void) const
{
    return etElement;
}

string ONElement::id(void) const
{
    string str = "" + enIndex_;
    return str;
}

ONSystem* ONElement::parent(void) const
{
    return parent_;
}

int ONElement::epanetIndex(void) const
{
    return enIndex_;
}


