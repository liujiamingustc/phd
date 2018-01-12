/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONENEXCEPTION.CPP - Implementation of OOTEN ONENException class

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

#include "ONENException.h"

//---------------------------------------------------------------------------

#pragma package(smart_init)

ONENException::ONENException(void) : ONException() {}

ONENException::ONENException(int errcode, string origin) : ONException("", origin)
{
    errcode=errcode;
    char message[1024];
    int error;
    error=ENgeterror(errcode, message, 1023);
    if (error!=0)
        setMessage("Error could not be retrieved from Epanet. Error code = " + errcode);
    else
    {
        string messg(message);
        setMessage(messg);
    }
}

ONENException::ONENException(const ONENException &o)
{

    setOrigin(o.origin());
    setMessage(o.message());
}

ONENException::~ONENException(void){}

string ONENException::report(void) const
{
    string messg = "Epanet exception thrown at " + origin() + " : " + message();
    return messg;
}
