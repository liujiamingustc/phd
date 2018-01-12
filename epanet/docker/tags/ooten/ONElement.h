/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONELEMENT.H - Definition of OOTEN ONElement class

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

#ifndef ONElementH
#define ONElementH
//---------------------------------------------------------------------------

#include "ONObject.h"

class ONSystem;

class ONElement : public ONObject
{
    public:
        //enumerators
        enum elementTpe {etElement, etNode, etLink, etPattern, etCurve, etControl,
                etJunction, etTank, etReservoir, etPipe, etPump,
                etValve, etFCV, etGPV, etPBV, etPRV, etPSV, etTCV};

        //constructors and destructors
        ONElement(void);
        ONElement(int enIndex, ONSystem* parent);
        ONElement(const ONElement &o);
        virtual ~ONElement(void);

        //methods
        virtual elementTpe  type(void) const;
        virtual string      id(void) const;
        int                 epanetIndex(void) const;
        ONSystem*           parent(void) const;

    private:
        ONSystem* parent_;
        int       enIndex_; //Epanet index
};

#endif
