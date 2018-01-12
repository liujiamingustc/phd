/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONPSV.H - Definition of OOTEN ONPSV (pressures sustaining valve) class

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

#ifndef ONPSVH
#define ONPSVH
//---------------------------------------------------------------------------

#include "ONValve.h"

using namespace std;

class ONPSV: public ONValve
{
    public:
        //constructors and destructors
        ONPSV(void);
        ONPSV(int enIndex, ONSystem* parent, ONNode* startNode, ONNode* endNode);
        ONPSV(ONPSV &o);
        virtual ONLink* clone(void);
        virtual ~ONPSV(void);

        //methods
        virtual elementTpe type(void) const;
};

#endif
