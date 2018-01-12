/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONPUMP.CPP - Implementation of OOTEN ONPump class

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

#include "ONPump.h"

//---------------------------------------------------------------------------

#pragma package(smart_init)

ONPump::ONPump(void)
{
    headCurve_ = 0;
    efficiencyCurve_ = 0;
}

ONPump::ONPump(int enIndex, ONSystem* parent, ONNode* startNode, ONNode* endNode)
        :ONLink(enIndex, parent, startNode, endNode)
{
    headCurve_ = 0;
    efficiencyCurve_ = 0;
}

ONPump::ONPump(const ONPump &o):ONLink(o.epanetIndex(), o.parent(), o.startNode(), o.endNode())
{
    headCurve_ = o.headCurve()->clone();
    efficiencyCurve_ = o.efficiencyCurve()->clone();
}

ONLink* ONPump::clone(void)
{
    return (ONLink*)(new ONPump(*this));
}

ONPump::~ONPump(void) {}

ONElement::elementTpe ONPump::type(void) const
{
    return etPump;
}

ONCurve* ONPump::headCurve(void) const
{
    return headCurve_;
}

void ONPump::setHeadCurve(ONCurve* headCurve)
{
    headCurve_ = headCurve;
}

ONCurve* ONPump::efficiencyCurve(void) const
{
    return efficiencyCurve_;
}

void ONPump::setEfficiencyCurve(ONCurve* effCurve)
{
    efficiencyCurve_ = effCurve;
}

double ONPump::initialSpeed(void) const
{
    int errcode;
    float value;
    errcode = ENgetlinkvalue(epanetIndex(), EN_INITSETTING, &value);
    if(errcode) checkError(errcode, "ONPump::initialSpeed()");
    return value;
}

void ONPump::setInitialSpeed(double setting)
{
    int errcode;
    errcode = ENsetlinkvalue(epanetIndex(), EN_INITSETTING, setting);
    if(errcode) checkError(errcode, "ONPump::setInitialSpeed()");
}

double ONPump::speed(void) const
{
    int errcode;
    float value;
    errcode = ENgetlinkvalue(epanetIndex(), EN_SETTING, &value);
    if(errcode) checkError(errcode, "ONPump::speed()");
    return value;
}

void ONPump::setSpeed(double setting)
{
    int errcode;
    errcode = ENsetlinkvalue(epanetIndex(), EN_SETTING, setting);
    if(errcode) checkError(errcode, "ONPump::setSpeed()");
}

double ONPump::energy(void) const
{
    int errcode;
    float value;
    errcode = ENgetlinkvalue(epanetIndex(), EN_ENERGY, &value);
    if(errcode) checkError(errcode, "ONPump::getEnergy()" );
    return value;
}


