/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONLINK.CPP - Implementation of OOTEN ONLink class

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

#include "ONLink.h"

//---------------------------------------------------------------------------

#pragma package(smart_init)

ONLink::ONLink(void)
{
    startNode_ = 0;
    endNode_ = 0;
}

ONLink::ONLink(int enIndex, ONSystem* parent, ONNode* startNode, ONNode* endNode):ONElement(enIndex, parent)
{
    startNode_ = startNode;
    endNode_ = endNode;
}

ONLink::ONLink(const ONLink &o):ONElement(o.epanetIndex(), o.parent())
{
    startNode_ = o.startNode();
    endNode_ = o.endNode();
}

ONLink* ONLink::clone(void)
{
    return new ONLink(*this);
}

ONLink::~ONLink(void) {}

ONElement::elementTpe ONLink::type(void) const
{
    return etLink;
}

string ONLink::id(void) const
{
    char* idc = new char[15];
    int errcode;
    errcode = ENgetlinkid(epanetIndex(), idc);
    if(errcode) checkError(errcode, "ONLink::id()");
    string id(idc);
    return id;
}

ONNode* ONLink::startNode(void) const
{
    return startNode_;
}

ONNode* ONLink::endNode(void) const
{
    return endNode_;
}

bool ONLink::initialStatus(void) const
{
    int errcode;
    float value;
    errcode = ENgetlinkvalue(epanetIndex(), EN_INITSTATUS, &value);
    if(errcode) checkError(errcode, "ONLink::initialStatus()");
    return value; //true = open false = closed
}

void ONLink::setInitialStatus(bool status)
{
    int errcode;
    float value;
    if (status) value = 1;
    else value = 0;
    errcode = ENsetlinkvalue(epanetIndex(), EN_INITSTATUS, value);
    if(errcode) checkError(errcode, "ONLink::setInitialStatus()");
}

double ONLink::flowrate(void) const
{
    int errcode;
    float value;
    errcode = ENgetlinkvalue(epanetIndex(), EN_FLOW, &value);
    if(errcode) checkError(errcode, "ONLink::flowrate()");
    return value;
}

double ONLink::headloss(void) const
{
    int errcode;
    float value;
    errcode = ENgetlinkvalue(epanetIndex(), EN_HEADLOSS, &value);
    if(errcode) checkError(errcode, "ONLink::headloss()");
    return value;
}

bool ONLink::status(void) const
{
    int errcode;
    float value;
    errcode = ENgetlinkvalue(epanetIndex(), EN_STATUS, &value);
    if(errcode) checkError(errcode, "ONLink::status()");
    return value; //true=open false = closed
}

void ONLink::setStatus(bool status)
{
    int errcode;
    float value;
    if (status) value = 1;
    else value = 0;
    errcode = ENsetlinkvalue(epanetIndex(), EN_STATUS, value);
    if(errcode) checkError(errcode, "ONLink::setStatus()");
}

