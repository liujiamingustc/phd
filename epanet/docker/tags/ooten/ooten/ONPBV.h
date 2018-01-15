/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONPBV.H - Definition of OOTEN ONPBV (pressure breaker valve) class

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

#ifndef ONPBVH
#define ONPBVH
//---------------------------------------------------------------------------

#include "ONValve.h"

using namespace std;

class ONPBV: public ONValve
{
    public:
        //constructors and destructors
        ONPBV(void);
        ONPBV(int enIndex, ONSystem* parent, ONNode* startNode, ONNode* endNode);
        ONPBV(ONPBV &o);
        virtual ONLink* clone(void);
        virtual ~ONPBV(void);

        //methods
        virtual elementTpe type(void) const;
};

#endif
