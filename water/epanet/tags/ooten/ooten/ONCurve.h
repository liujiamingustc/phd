/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONCURVE.H - Definition of OOTEN ONCurve class

VERSION:    1.00beta
DATE:       13 June 2003
AUTHOR:     JE van Zyl
            Rand Afrikaans University
            Johannesburg
            South Africa
            jevz@ing.rau.ac.za

*******************************************************************

*///---------------------------------------------------------------------------

#ifndef ONCurveH
#define ONCurveH
//---------------------------------------------------------------------------

#include <vector>
#include <utility>
#include "ONElement.h"

using namespace std;

class ONCurve: public ONElement
{
    public:
        //enumerators
        enum curveTpe {ctVolume, ctPump, ctEfficiency, ctHeadloss};

        //type defines
        typedef  pair<double, double> ONPoint;

        //constructors and destructors
        ONCurve(void);
        ONCurve(int enIndex, ONSystem* parent);
        ONCurve(const ONCurve &o);
        virtual ONCurve* clone(void);
        virtual ~ONCurve(void);

        //methods
        virtual elementTpe  type(void) const;
        virtual string      id(void) const;
        ONPoint             dataPoint(int index) const;
        void                setDataPoint(int index, const ONPoint &datapoint);
        vector<ONPoint>     dataPoints(void) const;
        void                setDataPoints(const vector<ONPoint> &values);
        int                 size(void) const;
};

#endif
