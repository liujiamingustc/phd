/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONPIPE.H - Definition of OOTEN ONPipe class

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

#ifndef ONPipeH
#define ONPipeH
//---------------------------------------------------------------------------

#include "ONLink.h"

using namespace std;

class ONPipe: public ONLink
{
    public:
        //constructors and destructors
        ONPipe(void);
        ONPipe(int enIndex, ONSystem* parent, ONNode* startNode, ONNode* endNode);
        ONPipe(const ONPipe &o);
        virtual ONLink* clone(void);
        virtual ~ONPipe(void);

        //methods
        virtual elementTpe  type(void) const;
        double              initialRoughness(void) const;
        void                setInitialRoughness(double setting);
        double              diameter(void) const;
        void                setDiameter(double diameter);
        double              length(void) const;
        void                setLength(double length);
        double              roughness(void) const;
        void                setRoughness(double coeff);
        double              minorLossCoeff(void) const;
        void                setMinorLossCoeff(double coeff);
        double              bulkCoeff(void) const;
        void                setBulkCoeff(double coeff);
        double              wallCoeff(void) const;
        void                setWallCoeff(double coeff);
        double              velocity(void) const;
};

#endif
