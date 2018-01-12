/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONJUNCTION.CPP - Implementation of OOTEN ONJunction class

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

#include "ONJunction.h"

//---------------------------------------------------------------------------

#pragma package(smart_init)

ONJunction::ONJunction(void)
{
    demandPattern_ = 0;
}

ONJunction::ONJunction(int enIndex, ONSystem* parent, ONPattern* demandPattern)
    :ONNode(enIndex, parent)
{
    demandPattern_ = demandPattern;
}

ONJunction::ONJunction(const ONJunction &o) : ONNode(o.epanetIndex(), o.parent())
{
    demandPattern_ = o.demandPattern();
}

ONNode* ONJunction::clone(void)
{
    return (ONNode*)(new ONJunction(*this));
}

ONJunction::~ONJunction(void) {}

ONElement::elementTpe ONJunction::type(void) const
{
    return etJunction;
}

double ONJunction::baseDemand(void) const
{
    int errcode;
    float value;
    errcode = ENgetnodevalue(epanetIndex(), EN_BASEDEMAND, &value);
    if(errcode) checkError(errcode, "ONJunction::baseDemand()");
    return value;
}

void ONJunction::setBaseDemand(double demand)
{
    int errcode;
    errcode = ENsetnodevalue(epanetIndex(), EN_BASEDEMAND, demand);
    if(errcode) checkError(errcode, "ONJunction::setBaseDemand()");
}

ONPattern* ONJunction::demandPattern(void) const
{
    return demandPattern_;
}

void ONJunction::setDemandPattern(ONPattern* pattern)
{
    int errcode;
    if (pattern == 0)
        errcode = ENsetnodevalue(epanetIndex(), EN_PATTERN, 0); //set deamand pattern to 0 if junction does not have a demand pattern
    else
        errcode = ENsetnodevalue(epanetIndex(), EN_PATTERN, pattern->epanetIndex());
    if(errcode) checkError(errcode, "ONJunction::setDemandPattern()");
    demandPattern_ = pattern;
}

double ONJunction::emitterCoeff(void) const
{
    int errcode;
    float value;
    errcode = ENgetnodevalue(epanetIndex(), EN_EMITTER, &value);
    if(errcode) checkError(errcode, "ONJunction::emitterCoeff()");
    return value;
}

void ONJunction::setEmitterCoeff(double coeff)
{
    int errcode;
    errcode = ENsetnodevalue(epanetIndex(), EN_EMITTER, coeff);
    if(errcode) checkError(errcode, "ONJunction::setEmitterCoeff()");
}

double ONJunction::demand(void) const
{
    int errcode;
    float value;
    errcode = ENgetnodevalue(epanetIndex(), EN_DEMAND, &value);
    if(errcode) checkError(errcode, "ONJunction::demand()");
    return value;
}

