/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONEXCEPTION.CPP - Implementation of OOTEN ONException class

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

#include "ONException.h"

//---------------------------------------------------------------------------

#pragma package(smart_init)

ONException::ONException(void)
{
    message_="Unknown";
    origin_="Unknown";
}

ONException::ONException(string message, string origin)
{
    message_=message;
    origin_ = origin;
}

ONException::ONException(const ONException &o)
{
    message_ = o.message();
    origin_ = o.origin();
}

ONException::~ONException(void){}

string ONException::message(void) const
{
    return message_;
}

string ONException::origin(void) const
{
    return origin_;
}

string ONException::report(void) const
{
    string messg = "Exception thrown at " + origin_ + " : " + message_;
    return messg;
}

void ONException::setMessage(string message)
{
    message_ = message;
}

void ONException::setOrigin(string origin)
{
    origin_ = origin;
}