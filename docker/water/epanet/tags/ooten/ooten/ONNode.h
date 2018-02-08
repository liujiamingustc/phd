/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONNODE.H - Definition of OOTEN ONNode class

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

#ifndef ONNodeH
#define ONNodeH
//---------------------------------------------------------------------------

#include "ONElement.h"
#include "ONPattern.h"

using namespace std;

class ONNode: public ONElement
{
    public:
        //enumerators
        enum sourceTpe {stConcentration, stMass, stSetPoint, stFlowPaced};

        //constructors and destructors
        ONNode(void);
        ONNode(int enIndex, ONSystem* parent);
        ONNode(const ONNode &o);
        virtual ONNode* clone(void);
        virtual ~ONNode(void);

        //methods
        virtual elementTpe  type(void) const;
        virtual string      id(void) const;
        double              elevation(void) const;
        void                setElevation(double elevation);
        double              initialQuality(void) const;
        void                setInitialQuality(double quality);
        double              sourceQuality(void) const;
        void                setSourceQuality(double quality);
        ONPattern*          sourcePattern(void) const;
        void                setSourcePattern(ONPattern* p);
        sourceTpe           sourceType(void) const;
        void                setSourceType(sourceTpe type);
        double              head(void) const;
        double              pressure(void) const;
        double              quality(void) const;
        double              sourceMass(void) const;

    private:
        ONPattern* sourcePattern_;
};


#endif
