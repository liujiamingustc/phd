/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONNODE.CPP - Implementation of OOTEN ONNode class

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

#include "ONNode.h"

//---------------------------------------------------------------------------

#pragma package(smart_init)

ONNode::ONNode(void)
{
    sourcePattern_ = 0;
}

ONNode::ONNode(int enIndex, ONSystem* parent):ONElement(enIndex,parent)
{
    sourcePattern_ = 0;
}

ONNode::ONNode(const ONNode &o) : ONElement(o.epanetIndex(), o.parent())
{
    sourcePattern_ = o.sourcePattern();
}

ONNode* ONNode::clone(void)
{
    return new ONNode(*this);
}

ONNode::~ONNode(void) {}

ONElement::elementTpe ONNode::type(void) const
{
    return etNode;
}

string ONNode::id(void) const
{
    char* idc = new char[15];
    int errcode;
    errcode = ENgetnodeid(epanetIndex(), idc);
    if(errcode) checkError(errcode, "ONNode::id()");
    string id(idc);
    return id;
}

double ONNode::elevation(void) const
{
    int errcode;
    float value;
    errcode = ENgetnodevalue(epanetIndex(), EN_ELEVATION, &value);
    if(errcode) checkError(errcode, "ONNode::elevation()");
    return value;
}

void ONNode::setElevation(double elevation)
{
    int errcode;
    errcode = ENsetnodevalue(epanetIndex(), EN_ELEVATION, elevation);
    if(errcode) checkError(errcode, "ONNode::setElevation()");
}

double ONNode::initialQuality(void) const
{
    int errcode;
    float value;
    errcode = ENgetnodevalue(epanetIndex(), EN_INITQUAL, &value);
    if(errcode) checkError(errcode, "ONNode::initialQuality()");
    return value;
}

void ONNode::setInitialQuality(double quality)
{
    int errcode;
    errcode = ENsetnodevalue(epanetIndex(), EN_INITQUAL, quality);
    if(errcode) checkError(errcode, "ONNode::setInitialQuality()");
}

double ONNode::sourceQuality(void) const
{
    int errcode;
    float value;
    errcode = ENgetnodevalue(epanetIndex(), EN_SOURCEQUAL, &value);
    if(errcode) checkError(errcode, "ONNode::sourceQuality()");
    return value;
}

void ONNode::setSourceQuality(double quality)
{
    int errcode;
    errcode = ENsetnodevalue(epanetIndex(), EN_SOURCEQUAL, quality);
    if(errcode) checkError(errcode, "ONNode::setSourceQuality()");
}

ONPattern* ONNode::sourcePattern(void) const
{
    return sourcePattern_;
}

void ONNode::setSourcePattern(ONPattern* p)
{
    int errcode;
    if (p == 0)
        errcode = ENsetnodevalue(epanetIndex(), EN_SOURCEPAT, 0); //set source pattern to 0 if node does not have a source pattern
    else
        errcode = ENsetnodevalue(epanetIndex(), EN_SOURCEPAT, p->epanetIndex());
    if(errcode) checkError(errcode, "ONNode::setSourcePattern()");
    sourcePattern_ = p;
}

ONNode::sourceTpe ONNode::sourceType(void) const
{
    int errcode;
    float value;
    errcode = ENgetnodevalue(epanetIndex(), EN_SOURCETYPE, &value);
    if(errcode) checkError(errcode, "ONNode::sourceType()");
    return static_cast<ONNode::sourceTpe>(value);
}

void ONNode::setSourceType(sourceTpe type)
{
    int errcode;
    errcode = ENsetnodevalue(epanetIndex(), EN_SOURCETYPE, type);
    if(errcode) checkError(errcode, "ONNode::setSourceType()");
}

double ONNode::head(void) const
{
    int errcode;
    float value;
    errcode = ENgetnodevalue(epanetIndex(), EN_HEAD, &value);
    if(errcode) checkError(errcode, "ONNode::head()");
    return value;
}

double ONNode::pressure(void) const
{
    int errcode;
    float value;
    errcode = ENgetnodevalue(epanetIndex(), EN_PRESSURE, &value);
    if(errcode) checkError(errcode, "ONNode::pressure()");
    return value;
}

double ONNode::quality(void) const
{
    int errcode;
    float value;
    errcode = ENgetnodevalue(epanetIndex(), EN_QUALITY, &value);
    if(errcode) checkError(errcode, "ONNode::quality()");
    return value;
}

double ONNode::sourceMass(void) const
{
    int errcode;
    float value;
    errcode = ENgetnodevalue(epanetIndex(), EN_SOURCEMASS, &value);
    if(errcode) checkError(errcode, "ONNode::sourceMass()");
    return value;
}


