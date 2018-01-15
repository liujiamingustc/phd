/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONOBJECT.CPP - Implementation of OOTEN ONObject class

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

#include "ONObject.h"
//---------------------------------------------------------------------------

#pragma package(smart_init)

ONObject::ONObject(void) {}

ONObject::ONObject(const ONObject &o) {}

ONObject::~ONObject(void) {}

void ONObject::checkError(int errcode, string origin) const
{
    if (errcode > 100)
    {
        ONENException e = ONENException(errcode, origin);
        throw(e); //EN error code = 0 means no error; EN error code < 100 means warning; Warnings are ignored
    }
}

