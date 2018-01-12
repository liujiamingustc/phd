/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONPATTERN.H - Definition of OOTEN ONPattern class

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

#ifndef ONPatternH
#define ONPatternH
//---------------------------------------------------------------------------

#include <vector>
#include "ONElement.h"

using namespace std;

class ONPattern: public ONElement
{
    public:
        //constructors and destructors
        ONPattern(void);
        ONPattern(int enIndex, ONSystem* parent);
        ONPattern(const ONPattern &o);
        virtual ONPattern* clone(void);
        virtual ~ONPattern(void);

        // methods
        virtual elementTpe  type(void) const;
        virtual string      id(void) const;
        vector<double>      values(void) const;
        void                setValues(vector<double> values);
        int                 size(void) const;
        double              value(int period) const;
};

#endif
