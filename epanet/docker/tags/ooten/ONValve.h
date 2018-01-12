/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONVALVE.H - Definition of OOTEN ONValve class

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

#ifndef ONValveH
#define ONValveH
//---------------------------------------------------------------------------

#include "ONLink.h"

using namespace std;

class ONValve: public ONLink
{
    public:
        //constructors and destructors
        ONValve(void);
        ONValve(int enIndex, ONSystem* parent, ONNode* startNode, ONNode* endNode);
        ONValve(const ONValve &o);
        virtual ONLink* clone(void);
        virtual ~ONValve(void);

        //methods
        virtual elementTpe  type(void) const;
        bool                initialSetting(void) const;
        void                setInitialSetting(bool setting);
        bool                setting(void) const;
        void                setSetting(bool setting);
};

#endif
