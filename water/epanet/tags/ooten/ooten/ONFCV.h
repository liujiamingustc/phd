/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONFCV.H - Definition of OOTEN ONFCV (flow control valve) class

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

#ifndef ONFCVH
#define ONFCVH
//---------------------------------------------------------------------------

#include "ONValve.h"

using namespace std;

class ONFCV: public ONValve
{
    public:
        //constructors and destructors
        ONFCV(void);
        ONFCV(int enIndex, ONSystem* parent, ONNode* startNode, ONNode* endNode);
        ONFCV(ONFCV &o);
        virtual ONLink* clone(void);
        virtual ~ONFCV(void);

        //methods
        virtual elementTpe type(void) const;
};

#endif
