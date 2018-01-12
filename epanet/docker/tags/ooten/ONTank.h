/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONTANK.H - Definition of OOTEN ONTank class

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

#ifndef ONTankH
#define ONTankH
//---------------------------------------------------------------------------

#include "ONNode.h"
#include "ONCurve.h"

using namespace std;

class ONTank: public ONNode
{
    public:
        //constructors and destructors
        ONTank(void);
        ONTank(int enIndex, ONSystem* parent);
        ONTank(const ONTank &o);
        virtual ONNode* clone(void);
        virtual ~ONTank(void);

        //methods
        virtual elementTpe  type(void) const;
        virtual ONCurve*    volumeCurve(void) const;
        virtual void        setVolumeCurve(ONCurve* volCurve);
        virtual double      initialLevel(void) const;
        virtual void        setInitialLevel(double level);
        virtual double      level(void) const;

    private:
        ONCurve* volumeCurve_;
};

#endif
