/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONVALVE.CPP - Implementation of OOTEN ONValve class

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

#include "ONValve.h"

//---------------------------------------------------------------------------

#pragma package(smart_init)

ONValve::ONValve(void){}

ONValve::ONValve(int enIndex, ONSystem* parent, ONNode* startNode, ONNode* endNode)
        :ONLink(enIndex, parent, startNode, endNode) {}

ONValve::ONValve(const ONValve &o):ONLink(o.epanetIndex(), o.parent(), o.startNode(), o.endNode()) {}

ONLink* ONValve::clone(void)
{
    return (ONLink*)(new ONValve(*this));
}

ONValve::~ONValve(void) {}

ONElement::elementTpe ONValve::type(void) const
{
    return etValve;
}

bool ONValve::initialSetting(void) const
{
    int errcode;
    float value;
    errcode = ENgetlinkvalue(epanetIndex(), EN_INITSETTING, &value);
    if(errcode) checkError(errcode, "ONValve::initialSetting()");
    return value == 1;
}

void ONValve::setInitialSetting(bool setting)
{
    int errcode;
    float value = (setting);
    errcode = ENsetlinkvalue(epanetIndex(), EN_INITSTATUS, value);
    if(errcode) checkError(errcode, "ONValve::setInitialSetting()");
}

bool ONValve::setting(void) const
{
    int errcode;
    float value;
    errcode = ENgetlinkvalue(epanetIndex(), EN_SETTING, &value);
    if(errcode) checkError(errcode, "ONValve::setting()");
    return value;
}

void ONValve::setSetting(bool setting)
{
    int errcode;
    float value = setting;
    errcode = ENsetlinkvalue(epanetIndex(), EN_SETTING, value);
    if(errcode) checkError(errcode, "ONValve::setSetting()");
}


