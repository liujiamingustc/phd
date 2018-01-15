/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONTANK.CPP - Implementation of OOTEN ONTank class

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

#include "ONTank.h"

//---------------------------------------------------------------------------

#pragma package(smart_init)


ONTank::ONTank(void)
{
    volumeCurve_ = 0;
}

ONTank::ONTank(int enIndex, ONSystem* parent):ONNode(enIndex, parent)
{
    volumeCurve_ = 0;
}

ONTank::ONTank(const ONTank &o) : ONNode(o.epanetIndex(), o.parent())
{
    volumeCurve_ = o.volumeCurve()->clone();
}

ONNode* ONTank::clone(void)
{
    return (ONNode*)(new ONTank(*this));
}

ONTank::~ONTank(void) {}

ONElement::elementTpe ONTank::type(void) const
{
    return etTank;
}

ONCurve* ONTank::volumeCurve(void) const
{
    return volumeCurve_;
}

void ONTank::setVolumeCurve(ONCurve* volCurve)
{
    volumeCurve_ = volCurve;
}

double ONTank::initialLevel(void) const
{
    int errcode;
    float value;
    errcode = ENgetnodevalue(epanetIndex(), EN_TANKLEVEL, &value);
    if(errcode) checkError(errcode, "ONTank::initialLevel()");
    return value;
}

void ONTank::setInitialLevel(double level)
{
    int errcode;
    errcode = ENsetnodevalue(epanetIndex(), EN_TANKLEVEL, level);
    if(errcode) checkError(errcode, "ONTank::setInitialLevel()");
}

double ONTank::level(void) const
{
    int errcode;
    float head, elevation;
    errcode = ENgetnodevalue(epanetIndex(), EN_HEAD, &head);
    if(errcode) checkError(errcode, "ONTank::level()");
    errcode = ENgetnodevalue(epanetIndex(), EN_ELEVATION, &elevation);
    if(errcode) checkError(errcode, "ONTank::level()");
    return head - elevation;
}


