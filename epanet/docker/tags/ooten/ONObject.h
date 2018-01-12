/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONOBJECT.H - Definition of OOTEN ONObject class

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

#ifndef ONObjectH
#define ONObjectH
//---------------------------------------------------------------------------

#include <string>
extern "C"
{
#include "toolkit_on.h"
}
#include "ONENException.h"

using namespace std;

class ONObject
{
    public:
        //constructors and destructors
        ONObject(void);
        ONObject(const ONObject &o);
        virtual ~ONObject(void);

        //methods
        void checkError(int errcode, string origin) const;
};

#endif
