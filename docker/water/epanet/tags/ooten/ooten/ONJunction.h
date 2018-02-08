/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONJUNCTION.H - Definition of OOTEN ONJunction class

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

#ifndef ONJunctionH
#define ONJunctionH
//---------------------------------------------------------------------------

#include <cmath>
#include "ONNode.h"

using namespace std;

class ONJunction: public ONNode
{
    public:
        //constructors and destructors
        ONJunction(void);
        ONJunction(int enIndex, ONSystem* parent, ONPattern* demandPattern = 0);
        ONJunction(const ONJunction &o);
        virtual ONNode* clone(void);
        virtual ~ONJunction(void);

        //methods
        virtual elementTpe  type(void) const;
        double              baseDemand(void) const;
        void                setBaseDemand(double demand);
        ONPattern*          demandPattern(void) const;
        void                setDemandPattern(ONPattern* pattern);
        double              emitterCoeff(void) const;
        void                setEmitterCoeff(double coeff);
        double              demand(void) const;

    private:
        ONPattern* demandPattern_;
};

#endif
