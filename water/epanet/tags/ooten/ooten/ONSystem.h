/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONSYSTEM.H - Definition of OOTEN ONSystem class

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

#define DLLE __declspec(dllexport) __stdcall

#ifndef ONSystemH
#define ONSystemH
//---------------------------------------------------------------------------

#include <vector>
#include <cmath>

#include "ONException.h"
#include "ONENException.h"
#include "ONObject.h"
#include "ONElement.h"
#include "ONPattern.h"
#include "ONCurve.h"
#include "ONNode.h"
#include "ONLink.h"
#include "ONControl.h"
#include "ONJunction.h"
#include "ONTank.h"
#include "ONReservoir.h"
#include "ONPipe.h"
#include "ONPump.h"
#include "ONValve.h"
#include "ONPRV.h"
#include "ONTCV.h"
#include "ONPSV.h"
#include "ONGPV.h"
#include "ONPBV.h"
#include "ONFCV.h"

using namespace std;

class ONSystem: public ONObject
{
    public:
        //enumerators
        enum flowUnitsTpe    {futCFS, futGPM, futMGD, futIMGD, futAFD,
                                 futLPS, futLPM, futMLD, futCMH, futCMD};
        enum qualityTpe      {qtNone, qtChemical, qtAge, qtTrace};
        enum statisticsTpe   {stNone, stAverage, stMinimum, stMaxium, stRange};
        enum statusReportTpe {srtNone, srtNormal, srtFull};

        //constructors and destructors
        ONSystem(void);
        ONSystem(const ONSystem &o);
        virtual ~ONSystem(void);

        //hydraulic options attributes
        flowUnitsTpe        flowUnits(void) const;
        double              maxTrials(void) const;
        void                setMaxTrials(double trials);
        double              accuracy(void) const;
        void                setAccuracy(double accuracy);
        double              qualityTolerance(void) const;
        void                setQualityTolerance(double tolerance);
        double              emitterExponent(void) const;
        void                setEmitterExponent(double exponent);
        double              demandMultiplier(void) const;
        void                setDemandMultiplier(double multiplier);
        void                setStatusReportType(statusReportTpe status);

        //time options attributes
        long                simulationDuration(void) const;
        void                setSimulationDuration(long duration);
        long                hydraulicTimeStep(void) const;
        void                sethydraulicTimeStep(long timestep);
        long                qualityTimeStep(void) const;
        void                setQualityTimeStep(long timestep);
        long                patternTimeStep(void) const;
        void                setPatternTimeStep(long timestep);
        long                patternStartTime(void) const;
        void                setPatternStartTime(long starttime);
        long                reportTimeStep(void) const;
        void                setReportTimeStep(long timestep);
        long                reportStartTime(void) const;
        void                setReportStartTime(long starttime);
        long                ruleTimeStep(void) const;
        void                setRuleTimeStep(long timestep);
        statisticsTpe       statistics(void) const;
        void                setStatistics(statisticsTpe type);
        long                noOfReportingPeriods(void) const;

        //quality options atributes
        qualityTpe          qualityParameter(void) const;
        ONNode*             traceNode(void) const;
        void                setQualityParameters(qualityTpe type,
                            string chemName="", string chemUnits="",
                            ONNode* tracenode=0);

        //run a full simulation
        void                epanetSimulation(string inputFile, string reprtFile,
                                string outputFile = "",
                                void (*progressFunc)(char*) = 0);

        //open and close toolkit
        void                open(string inputFile, string reportFile,
                                string outputFile = "");
        void                close(void);
        int                 noOfNodes(void) const;
        int                 noOfTanks(void) const;
        int                 noOfLinks(void) const;
        int                 noOfPatterns(void) const;
        int                 noOfCurves(void) const;
        int                 noOfControls(void) const;

        //query methods
        ONNode*             node(string id) const;
        ONLink*             link(string id) const;
        ONPattern*          pattern(string id) const;
        ONCurve*            curve(string id) const;
        ONNode*             node(unsigned int onIndex) const;
        ONLink*             link(unsigned int onIndex) const;
        ONPattern*          pattern(unsigned int onIndex) const;
        ONCurve*            curve(unsigned int onIndex) const;
        ONControl*          control(unsigned int onIndex) const;
        vector<ONLink*>     links(void) const;
        vector<ONNode*>     nodes(void) const;
        vector<ONPattern*>  patterns(void) const;
        vector<ONCurve*>    curves(void) const;
        vector<ONControl*>  controls(void) const;

        //result file methods
        void                saveHydraulicsFile(string fileName);
        void                loadHydraulicsFile(string fileName);

        //hydraulic simulation methods
        void                solveHydraulics(void);
        void                openHydraulics(void);
        void                initializeHydraulics(bool initialFlows, bool saveResults);
        long                runHydraulicSnapshot(void);
        long                nextHydraulicStep(void);
        void                closeHydraulics(void);

        //quality simulation methods
        void                solveQuality(void);
        void                openQuality(void);
        void                initializeQuality(bool saveResults);
        long                runQualitySnapshot(void);
        long                nextQualityStep(void);
        long                stepQuality(void);
        void                closeQuality(void);

        //reporting methods
        void                saveHydraulicsOutputFile(void);
        void                saveInputFile(string fileName);
        void                writeReport(void);
        void                resetReportFormat(void);
        void                setReportFormat(string command);
        int                 epanetVersion() const;
        string              ootenVersion() const;

    private:
        const string       onVersion_;
        vector<ONNode*>    nodes_;
        vector<ONLink*>    links_;
        vector<ONPattern*> patterns_;
        vector<ONCurve*>   curves_;
        vector<ONControl*> controls_;
        void destroy(void);
};


#endif
