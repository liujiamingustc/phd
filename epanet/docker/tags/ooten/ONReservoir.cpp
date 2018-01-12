/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONRESERVOIR.CPP - Implementation of OOTEN ONReservoir class

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

#include "ONReservoir.h"

//---------------------------------------------------------------------------

#pragma package(smart_init)

ONReservoir::ONReservoir(void) {}

ONReservoir::ONReservoir(int enIndex, ONSystem* parent):ONTank(enIndex, parent) {}

ONReservoir::ONReservoir(const ONReservoir &o) : ONTank(o.epanetIndex(), o.parent()){}

ONNode* ONReservoir::clone(void)
{
    return (ONNode*)(new ONReservoir(*this));
}

ONReservoir::~ONReservoir(void){}

ONElement::elementTpe ONReservoir::type(void) const
{
    return etReservoir;
}

ONCurve* ONReservoir::volumeCurve(void) const
{
    throw ONException("Reservoirs don't use volume curves.", "ONReservoir::volumeCurve()");
}

void ONReservoir::setVolumeCurve(ONCurve* volCurve)
{
    throw ONException("Reservoirs don't use volume curves.", "ONReservoir::setVolumeCurve()");
}

double ONReservoir::totalHead(void) const
{
    return elevation();
}

void ONReservoir::setTotalHead(double hgl)
{
    setElevation(hgl);
}

double ONReservoir::initialLevel(void) const
{
    throw ONException("Function has no effect for reservoirs. Query resevoir total head by using ONReservoir::totalHead()", "ONReservoir::initialLevel()");
}

void ONReservoir::setInitialLevel(double level)
{
    throw ONException("Function has no effect for reservoirs. Change resevoir total head using ONReservoir::setTotalHead()", "ONReservoir::setInitialLevel()");
}

double ONReservoir::level(void) const
{
    throw ONException("Function has no effect for reservoirs. Query resevoir total head by using ONReservoir::totalHead()", "ONReservoir::level()");
}

