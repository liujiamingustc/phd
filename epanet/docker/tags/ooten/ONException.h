/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONEXCEPTION.H - Definition of OOTEN ONException class

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

#ifndef ONExceptionH
#define ONExceptionH
//---------------------------------------------------------------------------

#include <string>

using namespace std;

class ONException
{
    public:
        //constructors and destructors
        ONException(void);
        ONException(string message, string origin = "unknown");
        ONException(const ONException &o);
        ~ONException(void);

        //methods
        string  message(void) const;
        string  origin(void) const;
        virtual string report(void) const;

    protected:
        void    setMessage(string message);
        void    setOrigin(string origin);

    private:
        string message_;
        string origin_;
};

#endif
