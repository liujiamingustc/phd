/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONPATTERN.CPP - Implementation of OOTEN ONPattern class

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

#include "ONPattern.h"

//---------------------------------------------------------------------------

#pragma package(smart_init)


ONPattern::ONPattern(void) {}

ONPattern::ONPattern(int enIndex, ONSystem* parent):ONElement(enIndex, parent) {}

ONPattern::ONPattern(const ONPattern &o):ONElement(o.epanetIndex(), o.parent()) {}

ONPattern* ONPattern::clone(void)
{
    return new ONPattern(*this);
}

ONPattern::~ONPattern(void) {}

ONElement::elementTpe ONPattern::type(void) const
{
    return etPattern;
}

string ONPattern::id(void) const
{
    char* idc = new char[15];
    int errcode;
    errcode = ENgetpatternid(epanetIndex(), idc);
    if(errcode) checkError(errcode, "ONPattern::id()");
    string id(idc);
    return id;
}

vector<double> ONPattern::values(void) const
{
    vector<double> v;
    int i;
    for (i = 0; i < size(); i++)
        v.push_back(value(i));
    return v;
}

void ONPattern::setValues(vector<double> values)
{
    int errcode;
    float* factors = new float[values.size()];
    for (unsigned int i = 0; i<values.size(); i++)
        factors[i] = values[i];
    errcode = ENsetpattern(epanetIndex(), factors, values.size());
    delete[] factors;
    if(errcode) checkError(errcode, "ONPattern::setValues()");
}

int ONPattern::size(void) const
{
    int len;
    int errcode;
    errcode = ENgetpatternlen(epanetIndex(), &len);
    if(errcode) checkError(errcode, "ONPattern::length()");
    return len;
}

double ONPattern::value(int index) const
{
    float value;
    int errcode;
    errcode = ENgetpatternvalue(epanetIndex(), index+1, &value); //Epanet counts pattern indexes from 1 and OOTEN from 0
    if(errcode) checkError(errcode, "ONPattern::value()");
    return value;
}

