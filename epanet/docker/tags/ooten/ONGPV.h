/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONGPV.H - Definition of OOTEN ONGPV (general purpose valve) class

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

#ifndef ONGPVH
#define ONGPVH
//---------------------------------------------------------------------------

#include "ONValve.h"

using namespace std;

class ONGPV: public ONValve
{
    public:
        //constructors and destructors
        ONGPV(void);
        ONGPV(int enIndex, ONSystem* parent, ONNode* startNode, ONNode* endNode);
        ONGPV(ONGPV &o);
        virtual ONLink* clone(void);
        virtual ~ONGPV(void);

        //methods
        virtual elementTpe type(void) const;
};

#endif
