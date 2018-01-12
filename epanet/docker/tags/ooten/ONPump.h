/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONPUMP.H - Definition of OOTEN ONPump class

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

#ifndef ONPumpH
#define ONPumpH
//---------------------------------------------------------------------------

#include "ONLink.h"
#include "ONCurve.h"

using namespace std;

class ONPump: public ONLink
{
    public:
        //constructors and destructors
        ONPump(void);
        ONPump(int enIndex, ONSystem* parent, ONNode* startNode, ONNode* endNode);
        ONPump(const ONPump &o);
        virtual ONLink* clone(void);
        virtual ~ONPump(void);

        //methods
        virtual elementTpe  type(void) const;
        ONCurve*            headCurve(void) const;
        void                setHeadCurve(ONCurve* headCurve);
        ONCurve*            efficiencyCurve(void) const;
        void                setEfficiencyCurve(ONCurve* effCurve);
        double              initialSpeed(void) const;
        void                setInitialSpeed(double setting);
        double              speed(void) const;
        void                setSpeed(double setting);
        double              energy(void) const;

    private:
        ONCurve* headCurve_;
        ONCurve* efficiencyCurve_;
};

#endif
