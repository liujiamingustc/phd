/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONPIPE.CPP - Implementation of OOTEN ONPipe class

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

#include "ONPipe.h"

//---------------------------------------------------------------------------

#pragma package(smart_init)

ONPipe::ONPipe(void) {}

ONPipe::ONPipe(int enIndex, ONSystem* parent, ONNode* startNode, ONNode* endNode)
        :ONLink(enIndex, parent, startNode, endNode) {}

ONPipe::ONPipe(const ONPipe &o):ONLink(o.epanetIndex(), o.parent(), o.startNode(), o.endNode()) {}

ONLink* ONPipe::clone(void)
{
    return (ONLink*)(new ONPipe(*this));
}

ONPipe::~ONPipe(void) {}

ONElement::elementTpe ONPipe::type(void) const
{
    return etPipe;
}

double ONPipe::initialRoughness(void) const
{
    int errcode;
    float value;
    errcode = ENgetlinkvalue(epanetIndex(), EN_INITSETTING, &value);
    if(errcode) checkError(errcode, "ONPipe::initialRoughness()");
    return value;
}

void ONPipe::setInitialRoughness(double setting)
{
    int errcode;
    errcode = ENsetlinkvalue(epanetIndex(), EN_INITSETTING, setting);
    if(errcode) checkError(errcode, "ONPipe::setInitialRoughness()");
}

double ONPipe::diameter(void) const
{
    int errcode;
    float value;
    errcode = ENgetlinkvalue(epanetIndex(), EN_DIAMETER, &value);
    if(errcode) checkError(errcode, "ONPipe::diameter()");
    return value;
}

void ONPipe::setDiameter(double diameter)
{
    int errcode;
    errcode = ENsetlinkvalue(epanetIndex(), EN_DIAMETER, diameter);
    if(errcode) checkError(errcode, "ONPipesetDiameter()");
}

double ONPipe::length(void) const
{
    int errcode;
    float value;
    errcode = ENgetlinkvalue(epanetIndex(), EN_LENGTH, &value);
    if(errcode) checkError( errcode, "ONPipe::length()");
    return value;
}

void ONPipe::setLength(double length)
{
    int errcode;
    errcode = ENsetlinkvalue(epanetIndex(), EN_LENGTH, length);
    if(errcode) checkError(errcode, "ONPipe::setLength()");
}

double ONPipe::roughness(void) const
{
    int errcode;
    float value;
    errcode = ENgetlinkvalue(epanetIndex(), EN_ROUGHNESS, &value);
    if(errcode) checkError(errcode, "ONPipe::roughnessCoeff()");
    return value;
}

void ONPipe::setRoughness(double coeff)
{
    int errcode;
    errcode = ENsetlinkvalue(epanetIndex(), EN_ROUGHNESS, coeff);
    if(errcode) checkError(errcode, "ONPipe::setRoughnessCoeff()");
}

double ONPipe::minorLossCoeff(void) const
{
    int errcode;
    float value;
    errcode = ENgetlinkvalue(epanetIndex(), EN_MINORLOSS, &value);
    if(errcode) checkError(errcode, "ONPipe::minorLossCoeff()");
    return value;
}

void ONPipe::setMinorLossCoeff(double coeff)
{
    int errcode;
    errcode = ENsetlinkvalue(epanetIndex(), EN_MINORLOSS, coeff);
    if(errcode) checkError(errcode, "ONPipe::setMinorLossCoeff()");
}

double ONPipe::bulkCoeff(void) const
{
    int errcode;
    float value;
    errcode = ENgetlinkvalue(epanetIndex(), EN_KBULK, &value);
    if(errcode) checkError(errcode, "ONPipe::bulkCoeff()");
    return value;
}

void ONPipe::setBulkCoeff(double coeff)
{
    int errcode;
    errcode = ENsetlinkvalue(epanetIndex(), EN_KBULK, coeff);
    if(errcode) checkError(errcode, "ONPipe::setBulkCoeff()");
}

double ONPipe::wallCoeff(void) const
{
    int errcode;
    float value;
    errcode = ENgetlinkvalue(epanetIndex(), EN_KWALL, &value);
    if(errcode) checkError(errcode, "ONPipe::wallCoeff()");
    return value;
}

void ONPipe::setWallCoeff(double coeff)
{
    int errcode;
    errcode = ENsetlinkvalue(epanetIndex(), EN_KWALL, coeff);
    if(errcode) checkError(errcode, "ONPipe::setWallCoeff()");
}

double ONPipe::velocity(void) const
{
    int errcode;
    float value;
    errcode = ENgetlinkvalue(epanetIndex(), EN_VELOCITY, &value);
    if(errcode) checkError(errcode, "ONPipe::velocity()");
    return value;
}


