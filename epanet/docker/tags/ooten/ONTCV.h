/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONTCV.H - Definition of OOTEN ONTCV (throttle control valve) class

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

#ifndef ONTCVH
#define ONTCVH
//---------------------------------------------------------------------------

#include "ONValve.h"

using namespace std;

class ONTCV: public ONValve
{
    public:
        //constructors and destructors
        ONTCV(void);
        ONTCV(int enIndex, ONSystem* parent, ONNode* startNode, ONNode* endNode);
        ONTCV(ONTCV &o);
        virtual ONLink* clone(void);
        virtual ~ONTCV(void);

        //methods
        virtual elementTpe type(void) const;
};

#endif
