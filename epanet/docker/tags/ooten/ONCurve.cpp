/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONCURVE.CPP - Implementation of OOTEN ONCurve class

VERSION:    1.00beta
DATE:       13 June 2003
AUTHOR:     JE van Zyl
            Rand Afrikaans University
            Johannesburg
            South Africa
            jevz@ing.rau.ac.za

*******************************************************************


*///---------------------------------------------------------------------------

#pragma hdrstop

#include "ONCurve.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)


ONCurve::ONCurve(void) {}

ONCurve::ONCurve(int enIndex, ONSystem* parent) : ONElement(enIndex, parent) {}

ONCurve::ONCurve(const ONCurve &o) : ONElement(o.epanetIndex(), o.parent()) {}

ONCurve* ONCurve::clone(void)
{
    return new ONCurve(*this);
}

ONCurve::~ONCurve(void) {}

ONElement::elementTpe ONCurve::type(void) const
{
    return etCurve;
}

string ONCurve::id(void) const
{
    char* idc = new char[15];
    int errcode;
    errcode = ENgetcurveid(epanetIndex(), idc);
    if(errcode) checkError(errcode, "ONCurve::id()");
    string id(idc);
    return id;
}

ONCurve::ONPoint ONCurve::dataPoint(int index) const
{
    int errcode;
    float x, y;
    errcode = ENgetcurvepoint(epanetIndex(), index+1, &x, &y);
    if(errcode) checkError(errcode, "ONCurve::dataPoint()");
    return ONCurve::ONPoint(x, y);
}

vector<ONCurve::ONPoint> ONCurve::dataPoints(void) const
{
    vector<ONPoint> v;
    int ln, errcode;
    float x, y;
    ln = size();
    for (int i = 1; i <= ln; i++)
    {
        errcode = ENgetcurvepoint(epanetIndex(), i, &x, &y);
        if(errcode) checkError(errcode, "ONCurve::dataPoints()");
        v.push_back(ONCurve::ONPoint(x, y));
    }
    return v;
}

void ONCurve::setDataPoint(int index, const ONCurve::ONPoint &datapoint)
{
    int errcode;
    errcode = ENsetcurvepoint(epanetIndex(), index+1, datapoint.first, datapoint.second);
    if(errcode) checkError(errcode, "ONCurve::setDataPoint()");
}

void ONCurve::setDataPoints(const vector<ONPoint> &values)
{
    int errcode;
    int n;
    n = values.size();
    float *x = new float[n];
    float *y = new float[n];
    for (int i = 0; i < n; i++)
    {
        x[i] = values[i].first;
        y[i] = values[i].second;
    }
    errcode = ENsetcurve(epanetIndex(), x, y, n);
    delete[] x;
    delete[] y;
    if(errcode) checkError(errcode, "ONCurve::setDataPoints()");
}

int ONCurve::size(void) const
{
    int len;
    int errcode;
    errcode = ENgetcurvelen(epanetIndex(), &len);
    if(errcode) checkError(errcode, "ONCurve::length()");
    return len;
}


