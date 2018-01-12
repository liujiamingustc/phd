/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONENEXCEPTION.H - Definition of OOTEN ONENException class

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

#ifndef ONENExceptionH
#define ONENExceptionH
//---------------------------------------------------------------------------

extern "C"
{
#include "toolkit_on.h"
}
#include "ONException.h"

using namespace std;

class ONENException : ONException
{
    public:
        //constructors and destructors
        ONENException(void);
        ONENException(int errcode, string origin = "unknown");
        ONENException(const ONENException &o);
        ~ONENException(void);

        //methods
        virtual string  report(void) const;
};


#endif
