/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONPRV.H - Definition of OOTEN ONPRV (pressure reducing valve) class

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

#ifndef ONPRVH
#define ONPRVH
//---------------------------------------------------------------------------

#include "ONValve.h"

using namespace std;

class ONPRV: public ONValve
{
    public:
        //constructors and destructors
        ONPRV(void);
        ONPRV(int enIndex, ONSystem* parent, ONNode* startNode, ONNode* endNode);
        ONPRV(ONPRV &o);
        virtual ONLink* clone(void);
        virtual ~ONPRV(void);

        //methods
        virtual elementTpe type(void) const;
};

#endif
