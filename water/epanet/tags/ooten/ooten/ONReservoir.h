/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONRESERVOIR.H - Definition of OOTEN ONReservoir class

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

#ifndef ONReservoirH
#define ONReservoirH
//---------------------------------------------------------------------------

#include "ONTank.h"

using namespace std;

class ONReservoir: public ONTank
{
    public:
        //constructors and destructors
        ONReservoir(void);
        ONReservoir(int enIndex, ONSystem* parent);
        ONReservoir(const ONReservoir &o);
        virtual ONNode* clone(void);
        virtual ~ONReservoir(void);

        // methods
        virtual elementTpe  type(void) const;
        virtual ONCurve*    volumeCurve(void) const; //function has no effect since reservoirs don't use volume curves
        virtual void        setVolumeCurve(ONCurve* volCurve); //function has no effect since reservoirs don't use volume curves
        double              totalHead(void) const;  //returns reservoir variable 'elevation'
        void                setTotalHead(double head);  //sets reservoir variable 'elevation'
        virtual double      initialLevel(void) const;  //function has no effect - use ONReservoir::totalHead()
        virtual void        setInitialLevel(double level);  //function has no effect - use ONReservoir::setTotalHead()
        virtual double      level(void) const;  //function has no effect - use ONReservoir::totalHead()
};

#endif
