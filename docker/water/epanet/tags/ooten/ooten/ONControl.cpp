/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONCONTROL.CPP - Implementation of OOTEN ONControl class

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

#include "ONControl.h"

//---------------------------------------------------------------------------

#pragma package(smart_init)
                                              
ONControl::ONControl(void)
{
    link_ = 0;
    node_ = 0;
}

ONControl::ONControl(int enIndex, ONSystem* parent, ONLink* link, ONNode* node):ONElement(enIndex, parent)
{
    link_ = link;
    node_ = node;
}

ONControl::ONControl(const ONControl &o) : ONElement(o.epanetIndex(), o.parent())
{
    link_ = o.link();
    node_ = o.node();
}

ONControl* ONControl::clone(void)
{
    return new ONControl(*this);
}

ONControl::~ONControl(void) {}

ONElement::elementTpe ONControl::type() const
{
    return etControl;
}

ONControl::controlTpe ONControl::controlType(void)
{
    int errcode;
    int cType;
    int lIndex;
    float setting;
    int nIndex;
    float level;
    errcode =  ENgetcontrol(epanetIndex(), &cType, &lIndex, &setting, &nIndex, &level );
    if(errcode) checkError(errcode, "ONControl::controlType()");
    return static_cast<ONControl::controlTpe> (cType);
}

void ONControl::setControlType(controlTpe tpe)
{
    int errcode;
    int cIndex = epanetIndex();
    int cType;
    int lIndex;
    float setting;
    int nIndex;
    float level;
    errcode =  ENgetcontrol(cIndex, &cType, &lIndex, &setting, &nIndex, &level );
    if(errcode) checkError(errcode, "ONControl::setControlType()");
    errcode = ENsetcontrol(cIndex, tpe, lIndex, setting, nIndex, level);
    if(errcode) checkError(errcode, "ONControl::setControlType()");
}

ONLink* ONControl::link(void) const
{
    return link_;
}

void ONControl::setLink(ONLink* link)
{
    int errcode;
    int cIndex = epanetIndex();
    int cType;
    int lIndex;
    float setting;
    int nIndex;
    float level;
    errcode =  ENgetcontrol(cIndex, &cType, &lIndex, &setting, &nIndex, &level );
    if(errcode) checkError(errcode, "ONControl::setLink()");
    if (link != 0)
        lIndex = link->epanetIndex();
    else
        lIndex = 0; //for deactivated links, lindex is set to zero
    errcode = ENsetcontrol(cIndex, cType, lIndex, setting, nIndex, level);
    if(errcode) checkError(errcode, "ONControl::setLink()");
    link_ = link;
}

double ONControl::linkSetting(void) const
{
    int errcode;
    int cIndex;
    int cType;
    int lIndex;
    float setting;
    int nIndex;
    float level;
    errcode = ENgetcontrol(epanetIndex(), &cType, &lIndex, &setting, &nIndex, &level );
    if(errcode) checkError(errcode, "ONControl::linkSetting()");
    return setting;
}

void ONControl::setLinkSetting(double linkSetting)
{
    int errcode;
    int cIndex = epanetIndex();
    int cType;
    int lIndex;
    float setting;
    int nIndex;
    float level;
    errcode = ENgetcontrol(cIndex, &cType, &lIndex, &setting, &nIndex, &level );
    if(errcode) checkError(errcode, "ONControl::setLinkSetting()");
    errcode = ENsetcontrol(cIndex, cType, lIndex, linkSetting, nIndex, level);
    if(errcode) checkError(errcode, "ONControl::setLinkSetting()");
}

ONNode* ONControl::node(void) const
{
    return node_;
}

void ONControl::setNode(ONNode* node)
{
    int errcode;
    int cIndex = epanetIndex();
    int cType;
    int lIndex;
    float setting;
    int nIndex;
    float level;
    errcode = ENgetcontrol(cIndex, &cType, &lIndex, &setting, &nIndex, &level );
    if(errcode) checkError(errcode, "ONControl::setNode()");
    if (node != 0) //for Time and System Time controls, Epanet sets nIndex = 0
        nIndex = node->epanetIndex();
    else
        nIndex = 0;
    errcode = ENsetcontrol(cIndex, cType, lIndex, setting, nIndex, level);
    if(errcode) checkError(errcode, "ONControl::setNode()");
    node_ = node;
}

double ONControl::trigger(void) const
{
    int errcode;
    int cType;
    int lIndex;
    float setting;
    int nIndex;
    float level;
    errcode = ENgetcontrol(epanetIndex(), &cType, &lIndex, &setting, &nIndex, &level );
    if(errcode) checkError(errcode, "ONControl::trigger()");
    return level;
}

void ONControl::setTrigger(double trigger)
{
    int errcode;
    int cIndex = epanetIndex();
    int cType;
    int lIndex;
    float setting;
    int nIndex;
    float level;
    errcode = ENgetcontrol(cIndex, &cType, &lIndex, &setting, &nIndex, &level );
    if(errcode) checkError(errcode, "ONControl::setTrigger()");
    errcode = ENsetcontrol(cIndex, cType, lIndex, setting, nIndex, trigger);
    if(errcode) checkError(errcode, "ONControl::setTrigger()");
}

