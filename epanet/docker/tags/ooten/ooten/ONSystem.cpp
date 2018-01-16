/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONSYSTEM.CPP - Implementation of OOTEN ONSystem class

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

#pragma hdrstop

#include "ONSystem.h"
//---------------------------------------------------------------------------

#pragma package(smart_init)

ONSystem::ONSystem(void) : onVersion_("1.00beta")
{}

ONSystem::ONSystem(const ONSystem &o)
{
    unsigned int i;
    for (i = 0; i<o.nodes_.size(); i++)
        nodes_.push_back(o.nodes_[i]->clone());
    for (i = 0; i<o.links_.size(); i++)
        links_.push_back(o.links_[i]->clone());
    for (i = 0; i<o.patterns_.size(); i++)
        patterns_.push_back(o.patterns_[i]->clone());
    for (i = 0; i<o.curves_.size(); i++)
        curves_.push_back(o.curves_[i]->clone());
    for (i = 0; i<o.controls_.size(); i++)
        controls_.push_back(o.controls_[i]->clone());
}

void ONSystem::destroy(void)
{
    unsigned int i;
    for (i = 0; i<nodes_.size(); i++) 
        delete nodes_[i];
    for (i = 0; i<links_.size(); i++)
        delete links_[i];
    for (i = 0; i<patterns_.size(); i++)
        delete patterns_[i];
    for (i = 0; i<curves_.size(); i++)
        delete curves_[i];
    for (i = 0; i<controls_.size(); i++)
        delete controls_[i];
    nodes_.clear();
    links_.clear();
    patterns_.clear();
    curves_.clear();
    controls_.clear();
}

ONSystem::~ONSystem(void)
{
    destroy();
}

ONSystem::flowUnitsTpe ONSystem::flowUnits(void) const
{
    int units;
    int errcode;
    errcode = ENgetflowunits(&units);
    if(errcode) checkError(errcode, "ONSystem::flowUnits()");
    return static_cast<ONSystem::flowUnitsTpe> (units);
}

double ONSystem::maxTrials(void) const
{
    float value;
    int errcode;
    errcode = ENgetoption(EN_TRIALS, &value);
    if(errcode) checkError(errcode, "ONSystem::noOfTrials()");
    return value;
}

void ONSystem::setMaxTrials(double trials)
{
    int errcode;
    errcode = ENsetoption(EN_TRIALS, trials);
    if(errcode) checkError(errcode, "ONSystem::setNumberOfTrials()");
}

double ONSystem::accuracy(void) const
{
    float value;
    int errcode;
    errcode = ENgetoption(EN_ACCURACY, &value);
    if(errcode) checkError(errcode, "ONSystem::accuracy()");
    return value;
}

void ONSystem::setAccuracy(double accuracy)
{
    int errcode;
    errcode = ENsetoption(EN_ACCURACY, accuracy);
    if(errcode) checkError(errcode, "ONSystem::setAccuracy()");
}

double ONSystem::qualityTolerance(void) const
{
    float value;
    int errcode;
    errcode = ENgetoption(EN_TOLERANCE, &value);
    if(errcode) checkError(errcode, "ONSystem::qualityTolerance()");
    return value;
}

void ONSystem::setQualityTolerance(double tolerance)
{
    int errcode;
    errcode = ENsetoption(EN_TOLERANCE, tolerance);
    if(errcode) checkError(errcode, "ONSystem::setQualityTolerance()");
}

double ONSystem::emitterExponent(void) const
{
    float value;
    int errcode;
    errcode = ENgetoption(EN_EMITEXPON, &value);
    if(errcode) checkError(errcode, "ONSystem::emitterExponent()");
    return value;
}

void ONSystem::setEmitterExponent(double exponent)
{
    int errcode;
    errcode = ENsetoption(EN_EMITEXPON, exponent);
    if(errcode) checkError(errcode, "ONSystem::setEmitterExponent()");
}

double ONSystem::demandMultiplier(void) const
{
    float value;
    int errcode;
    errcode = ENgetoption(EN_DEMANDMULT, &value);
    if(errcode) checkError(errcode, "ONSystem::demandMultiplier()");
    return value;
}

void ONSystem::setDemandMultiplier(double multiplier)
{
    int errcode;
    errcode = ENsetoption(EN_DEMANDMULT, multiplier);
    if(errcode) checkError(errcode, "ONSystem::setDemandMultiplier()");
}

void ONSystem::setStatusReportType(statusReportTpe status)
{
    int errcode;
    errcode = ENsetstatusreport(status);
    if(errcode) checkError(errcode, "ONSystem::setStatusReporting()");
}

long ONSystem::simulationDuration(void) const
{
    long value;
    int errcode;
    errcode = ENgettimeparam(EN_DURATION, &value);
    if(errcode) checkError(errcode, "ONSystem::simulationDuration()");
    return value;
}

void ONSystem::setSimulationDuration(long duration)
{
    int errcode;
    errcode = ENsettimeparam(EN_DURATION, duration);
    if(errcode) checkError(errcode, "ONSystem::setSimulationDuration()");
}

long ONSystem::hydraulicTimeStep(void) const
{
    long value;
    int errcode;
    errcode = ENgettimeparam(EN_HYDSTEP, &value);
    if(errcode) checkError(errcode, "ONSystem::hydraulicTimeStep()");
    return value;
}

void ONSystem::sethydraulicTimeStep(long timestep)
{
    int errcode;
    errcode = ENsettimeparam(EN_HYDSTEP, timestep);
    if(errcode) checkError(errcode, "ONSystem::sethydraulicTimeStep()");
}

long ONSystem::qualityTimeStep(void) const
{
    long value;
    int errcode;
    errcode = ENgettimeparam(EN_QUALSTEP, &value);
    if(errcode) checkError(errcode, "ONSystem::qualityTimeStep()");
    return value;
}

void ONSystem::setQualityTimeStep(long timestep)
{
    int errcode;
    errcode = ENsettimeparam(EN_QUALSTEP, timestep);
    if(errcode) checkError(errcode, "ONSystem::setQualityTimeStep()");
}

long ONSystem::patternTimeStep(void) const
{
    long value;
    int errcode;
    errcode = ENgettimeparam(EN_PATTERNSTEP, &value);
    if(errcode) checkError(errcode, "ONSystem::patternTimeStep()");
    return value;
}

void ONSystem::setPatternTimeStep(long timestep)
{
    int errcode;
    errcode = ENsettimeparam(EN_PATTERNSTEP, timestep);
    if(errcode) checkError(errcode, "ONSystem::setPatternTimeStep()");
}

long ONSystem::patternStartTime(void) const
{
    long value;
    int errcode;
    errcode = ENgettimeparam(EN_PATTERNSTART, &value);
    if(errcode) checkError(errcode, "ONSystem::patternStartTime()");
    return value;
}

void ONSystem::setPatternStartTime(long starttime)
{
    int errcode;
    errcode = ENsettimeparam(EN_PATTERNSTART, starttime);
    if(errcode) checkError(errcode, "ONSystem::setPatternStartTime()");
}

long ONSystem::reportTimeStep(void) const
{
    long value;
    int errcode;
    errcode = ENgettimeparam(EN_REPORTSTEP, &value);
    if(errcode) checkError(errcode, "ONSystem::reportTimeStep()");
    return value;
}

void ONSystem::setReportTimeStep(long timestep)
{
    int errcode;
    errcode = ENsettimeparam(EN_REPORTSTEP, timestep);
    if(errcode) checkError(errcode, "ONSystem::setReportTimeStep()");
}

long ONSystem::reportStartTime(void) const
{
    long value;
    int errcode;
    errcode = ENgettimeparam(EN_REPORTSTART, &value);
    if(errcode) checkError(errcode, "ONSystem::reportStartTime()");
    return value;
}

void ONSystem::setReportStartTime(long starttime)
{
    int errcode;
    errcode = ENsettimeparam(EN_REPORTSTART, starttime);
    if(errcode) checkError(errcode, "ONSystem::setReportStartTime()");
}

long ONSystem::ruleTimeStep(void) const
{
    long value;
    int errcode;
    errcode = ENgettimeparam(EN_RULESTEP, &value);
    if(errcode) checkError(errcode, "ONSystem::ruleTimeStep()");
    return value;
}

void ONSystem::setRuleTimeStep(long timestep)
{
    int errcode;
    errcode = ENsettimeparam(EN_RULESTEP, timestep);
    if(errcode) checkError(errcode, "ONSystem::setRuleTimeStep()");
}

ONSystem::statisticsTpe ONSystem::statistics(void) const
{
    long value;
    int errcode;
    errcode = ENgettimeparam(EN_STATISTIC, &value);
    if(errcode) checkError(errcode, "ONSystem::statistics()");
    return static_cast<ONSystem::statisticsTpe> (value);
}

void ONSystem::setStatistics(ONSystem::statisticsTpe type)
{
    int errcode;
    errcode = ENsettimeparam(EN_STATISTIC, type);
    if(errcode) checkError(errcode, "ONSystem::setStatistics()");
}

long ONSystem::noOfReportingPeriods(void) const
{
    long value;
    int errcode;
    errcode = ENgettimeparam(EN_PERIODS, &value);
    if(errcode) checkError(errcode, "ONSystem::noOfReportingPeriods()");
    return value;
}

void ONSystem::epanetSimulation(string inputFile, string reportFile, string outputFile, void (* progressFunc)(char*))
{
    int errcode;
    char* inputfile = new char[inputFile.length()+1];
    char* reportfile = new char[reportFile.length()+1];
    char* outputfile = new char[outputFile.length()+1];

    std::strcpy(inputfile, inputFile.c_str());
    std::strcpy(reportfile, reportFile.c_str());
    std::strcpy(outputfile, outputFile.c_str());

    errcode = ENepanet(inputfile, reportfile, outputfile, progressFunc);
    if(errcode) checkError(errcode, "ONSystem::epanetSimulation()");

    delete[] inputfile;
    delete[] reportfile;
    delete[] outputfile;
}

vector<ONLink*> ONSystem::links(void) const
{
    return links_;
}

vector<ONNode*> ONSystem::nodes(void) const
{
    return nodes_;
}

vector<ONPattern*> ONSystem::patterns(void) const
{
    return patterns_;
}

vector<ONCurve*> ONSystem::curves(void) const
{
    return curves_;
}

vector<ONControl*> ONSystem::controls(void) const
{
    return controls_;
}

ONSystem::qualityTpe ONSystem::qualityParameter(void) const
{
    int value;
    int errcode;
    int traceNode;
    errcode = ENgetqualtype(&value, &traceNode);
    if(errcode) checkError(errcode, "ONSystem::qualityParameter()");
    return static_cast<ONSystem::qualityTpe> (value);
}

ONNode* ONSystem::traceNode(void) const
{
    int value;
    int errcode;
    int traceNodeEnIndex;
    errcode = ENgetqualtype(&value, &traceNodeEnIndex);
    if(errcode) checkError(errcode, "ONSystem::qualityParameter()");
    if (traceNodeEnIndex <= 0)
        return nodes_[traceNodeEnIndex-1];
    else
        return 0;
}

void ONSystem::setQualityParameters(ONSystem::qualityTpe type, string chemName,
            string chemUnits, ONNode* tracenode)
{
    int errcode;
    string traceId;
    if (tracenode)
        traceId = tracenode->id();
    else
        traceId = "";
    char* node = new char[traceId.length()+1];
    char* chemname = new char[chemName.length()+1];
    char* chemunits = new char[chemUnits.length()+1];
    std::strcpy(node, traceId.c_str());
    std::strcpy(chemname, chemName.c_str());
    std::strcpy(chemunits, chemUnits.c_str());
    errcode = ENsetqualtype(type, chemname, chemunits, node);
    if(errcode) checkError(errcode, "ONSystem::setQualityParameter()");
    delete[] node;
    delete[] chemname;
    delete[] chemunits;
}

void ONSystem::open(string inputFile, string reportFile, string outputFile)
{
    int errcode;
    int i, count, type;
    char* inputfile = new char[inputFile.length()+1];
    char* reportfile = new char[reportFile.length()+1];
    char* outputfile = new char[outputFile.length()+1];

    std::strcpy(inputfile, inputFile.c_str());
    std::strcpy(outputfile, outputFile.c_str());
    std::strcpy(reportfile, reportFile.c_str());
    errcode = ENopen(inputfile, reportfile, outputfile);
    if(errcode) checkError(errcode, "ONSystem::open()");
    delete[] inputfile;
    delete[] reportfile;
    delete[] outputfile;
    destroy();

    //get patterns
    errcode = ENgetcount(EN_PATCOUNT, &count);
    if(errcode) checkError(errcode, "ONSystem::open()");
    for (i = 1; i<=count; i++)
    {
        patterns_.push_back(new ONPattern(i, this));
    }

    //get curves
    errcode = ENgetcount(EN_CURVECOUNT, &count);
    if(errcode) checkError(errcode, "ONSystem::open()");
    for (i = 1; i<=count; i++)
    {
        curves_.push_back(new ONCurve(i, this));
    }

    //get nodes
    errcode = ENgetcount(EN_NODECOUNT, &count);
    if(errcode) checkError(errcode, "ONSystem::open()");
    for (i = 1; i<=count; i++)
    {
        errcode = ENgetnodetype(i, &type);
        if(errcode) checkError(errcode, "ONSystem::open()");
        switch (type)
        {
            case EN_JUNCTION:
                {
                    float value;
                    errcode = ENgetnodevalue(i, EN_PATTERN, &value);
                    if(errcode) checkError(errcode, "ONSystem::open()");
                    //Epanet returns default pattern if no pattern is set. However, if no valid
                    //default pattern is specified, Epanet returns 0
                    ONPattern* patt;
                    if (value != 0)
                        patt = patterns_[(floor(value))-1];
                    else
                        patt = 0;
                    ONJunction* onj = new ONJunction(i, this, patt);
                    nodes_.push_back(onj);
                    break;
                }
            case EN_RESERVOIR:
                {
                    ONReservoir* onr = new ONReservoir(i, this);
                    nodes_.push_back(onr);
                    break;
                }
            case EN_TANK:
                {
                    float value;
                    errcode = ENgetnodevalue(i, EN_TANKCURVE, &value);
                    if(errcode) checkError(errcode, "ONSystem::open()");
                    ONTank* ont = new ONTank(i, this);
                    if (value != 0)
                        ont->setVolumeCurve(curves_[(floor(value))-1]);
                    else
                        ont->setVolumeCurve(0);
                    nodes_.push_back(ont);
                    break;
                }
            default:  throw ONException("Illegal node type", "ONSystem::open()");
        }

        // set node's source pattern
        float value;
        errcode = ENgetnodevalue(i, EN_SOURCEPAT, &value);
        if (errcode != 251)
        {
            if (value < 1) throw ONException("Illegal index value", "ONSystem::open()");
            if(errcode) checkError(errcode, "ONSystem::open()");
            ONNode* onn = nodes_[nodes_.size()-1];
            onn->setSourcePattern(patterns_[(int)value -1]);
        }
    }

    //get links
    errcode = ENgetcount(EN_LINKCOUNT, &count);
    if(errcode) checkError(errcode, "ONSystem::open()");
    for (i = 1; i<=count; i++)
    {
        //get start and end nodes
        int fromEni, toEni;
        errcode = ENgetlinknodes(i, &fromEni, &toEni);
        if(errcode) checkError(errcode, "ONSystem::open()");
        //create pipe
        errcode = ENgetlinktype(i, &type);
        if(errcode) checkError(errcode, "ONSystem::open()");
        switch (type)
        {
            case EN_CVPIPE:
                {
                    ONPipe* onp = new ONPipe(i, this, nodes_[fromEni-1], nodes_[toEni-1]);
                    links_.push_back(onp);
                    break;
                }
            case EN_PIPE:
                {
                    ONPipe* onp = new ONPipe(i, this, nodes_[fromEni-1], nodes_[toEni-1]);
                    links_.push_back(onp);
                    break;
                }
            case EN_PUMP:
                {
                    ONPump* onp = new ONPump(i, this, nodes_[fromEni-1], nodes_[toEni-1]);
                    float value;
                    errcode = ENgetlinkvalue(i, EN_PUMPHCURVE, &value);
                    if(errcode) checkError(errcode, "ONSystem::open()");
                    if (value != 0)
                        onp->setHeadCurve(curves_[(floor(value))-1]);
                    else
                        onp->setHeadCurve(0);
                    errcode = ENgetlinkvalue(i, EN_PUMPECURVE, &value);
                    if(errcode) checkError(errcode, "ONSystem::open()");
                    if (value != 0)
                        onp->setEfficiencyCurve(curves_[(floor(value))-1]);
                    else
                        onp->setEfficiencyCurve(0);
                    links_.push_back(onp);
                    break;
                }
            case EN_PRV:
                {
                    ONPRV* onp = new ONPRV(i, this, nodes_[fromEni-1], nodes_[toEni-1]);
                    links_.push_back(onp);
                    break;
                }
            case EN_PSV:
                {
                    ONPSV* onp = new ONPSV(i, this, nodes_[fromEni-1], nodes_[toEni-1]);
                    links_.push_back(onp);
                    break;
                }
            case EN_PBV:
                {
                    ONPBV* onp = new ONPBV(i, this, nodes_[fromEni-1], nodes_[toEni-1]);
                    links_.push_back(onp);
                    break;
                }
            case EN_FCV:
                {
                    ONFCV* onf = new ONFCV(i, this, nodes_[fromEni-1], nodes_[toEni-1]);
                    links_.push_back(onf);
                    break;
                }
            case EN_TCV:
                {
                    ONTCV* ont = new ONTCV(i, this, nodes_[fromEni-1], nodes_[toEni-1]);
                    links_.push_back(ont);
                    break;
                }
            case EN_GPV:
                {
                    ONGPV* ong = new ONGPV(i, this, nodes_[fromEni-1], nodes_[toEni-1]);
                    links_.push_back(ong);
                    break;
                }
            default:  throw ONException("Illegal link type", "ONSystem::open()");
        }
    }

    //get simple controls
    errcode = ENgetcount(EN_CONTROLCOUNT, &count);
    if(errcode) checkError(errcode, "ONSystem::open()");
    for (i = 1; i<=count; i++)
    {
        int cType, lIndex, nIndex;
        float level, setting;
        errcode = ENgetcontrol(i, &cType, &lIndex, &setting, &nIndex, &level);
        if(errcode) checkError(errcode, "ONControl::type()");
        ONLink* link;
        if (lIndex) //for deactivated controls, Epanet sets lIndex = 0
            link = links_[lIndex-1];
        else
            link = 0;
        ONNode* node;
        if (nIndex) //for Time and System Time controls, Epanet sets nIndex = 0
            node = nodes_[nIndex-1];
        else
            node = 0;
        controls_.push_back(new ONControl(i, this, link, node));
    }
}

void ONSystem::close(void)
{
    int errcode;
    errcode = ENclose();
    if(errcode) checkError(errcode, "ONSystem::close()");
}

int ONSystem::noOfNodes(void) const
{
    int count;
    int errcode;
    errcode = ENgetcount(EN_NODECOUNT, &count);
    if(errcode) checkError(errcode, "ONSystem::noOfNodes()");
    return count;
}

int ONSystem::noOfTanks(void) const
{
    int count;
    int errcode;
    errcode = ENgetcount(EN_TANKCOUNT, &count);
    if(errcode) checkError(errcode, "ONSystem::noOfTanks()");
    return count;
}

int ONSystem::noOfLinks(void) const
{
    int count;
    int errcode;
    errcode = ENgetcount(EN_LINKCOUNT, &count);
    if(errcode) checkError(errcode, "ONSystem::noOfLinks()");
    return count;
}

int ONSystem::noOfPatterns(void) const
{
    int count;
    int errcode;
    errcode = ENgetcount(EN_PATCOUNT, &count);
    if(errcode) checkError(errcode, "ONSystem::noOfPatterns()");
    return count;
}

int ONSystem::noOfCurves(void) const
{
    int count;
    int errcode;
    errcode = ENgetcount(EN_CURVECOUNT, &count);
    if(errcode) checkError(errcode, "ONSystem::noOfCurves()");
    return count;
}

int ONSystem::noOfControls(void) const
{
    int count;
    int errcode;
    errcode = ENgetcount(EN_CONTROLCOUNT, &count);
    if(errcode) checkError(errcode, "ONSystem::noOfControls()");
    return count;
}

ONNode* ONSystem::node(string id) const
{
    int index;
    int errcode;
    char* cname = new char[id.length()+1];
    std::strcpy(cname, id.c_str());
    errcode = ENgetnodeindex(cname, &index);
    delete[] cname;
    if(errcode) checkError(errcode, "ONSystem::node()");
    return nodes_[index-1];
}

ONLink* ONSystem::link(string id) const
{
    int index;
    int errcode;
    char* cname = new char[id.length()+1];
    std::strcpy(cname, id.c_str());
    errcode = ENgetlinkindex(cname, &index);
    delete[] cname;
    if(errcode) checkError(errcode, "ONSystem::link()");
    return links_[index-1];
}

ONPattern* ONSystem::pattern(string id) const
{
    int index;
    int errcode;
    char* cname = new char[id.length()+1];
    std::strcpy(cname, id.c_str());
    errcode = ENgetpatternindex(cname, &index);
    delete[] cname;
    if(errcode) checkError(errcode, "ONSystem::pattern()");
    return patterns_[index-1];
}

ONCurve* ONSystem::curve(string id) const
{
    int index;
    int errcode;
    char* cname = new char[id.length()+1];
    std::strcpy(cname, id.c_str());
    errcode = ENgetcurveindex(cname, &index);
    delete[] cname;
    if(errcode) checkError(errcode, "ONSystem::curve()");
    return curves_[index-1];
}

ONNode* ONSystem::node(unsigned int onIndex) const
{
    if (onIndex >= nodes_.size())
        throw ONException("Invalid index specified", "ONSystem::node()");
    return nodes_[onIndex];
}

ONLink* ONSystem::link(unsigned int onIndex) const
{
    if (onIndex >= links_.size())
        throw ONException("Invalid index specified", "ONSystem::link()");
    return links_[onIndex];
}

ONPattern* ONSystem::pattern(unsigned int onIndex) const
{
    if (onIndex >= patterns_.size())
        throw ONException("Invalid index specified", "ONSystem::pattern()");
    return patterns_[onIndex];
}

ONCurve* ONSystem::curve(unsigned int onIndex) const
{
    if (onIndex >= curves_.size())
        throw ONException("Invalid index specified", "ONSystem::curve()");
    return curves_[onIndex];
}

ONControl* ONSystem::control(unsigned int onIndex) const
{
    if (onIndex >= controls_.size())
        throw ONException("Invalid index specified", "ONSystem::control()");
    return controls_[onIndex];
}

void ONSystem::saveHydraulicsFile(string fileName)
{
    int errcode;
    char* fname = new char[fileName.length()+1];
    std::strcpy(fname, fileName.c_str());
    errcode = ENsavehydfile(fname); 
    delete[] fname;
    if(errcode) checkError(errcode, "ONSystem::saveResultFile()");
}

void ONSystem::loadHydraulicsFile(string fileName)
{
    int errcode;
    char* fname = new char[fileName.length()+1];
    std::strcpy(fname, fileName.c_str());
    errcode = ENusehydfile(fname); 
    delete[] fname;
    if(errcode) checkError(errcode, "ONSystem::loadResultFile()");
}

void ONSystem::solveHydraulics(void)
{
    int errcode;
    errcode = ENsolveH();
    if(errcode) checkError(errcode, "ONSystem::solveHydraulics()");
}

void ONSystem::openHydraulics(void)
{
    int errcode;
    errcode = ENopenH();
    if(errcode) checkError(errcode, "ONSystem::openHydraulics()");
}

void ONSystem::initializeHydraulics(bool initializeFlows, bool saveResults)
{
    int errcode;
    if (initializeFlows)
    {
        if (saveResults)
            errcode = ENinitH(11);
        else
            errcode = ENinitH(10);
    }
    else
    {
        if (saveResults)
            errcode = ENinitH(01);
        else
            errcode = ENinitH(00);
    }

    if(errcode) checkError(errcode, "ONSystem::initializeHydraulics()");
}


long ONSystem::runHydraulicSnapshot(void)
{
    int errcode;
    long clock;
    errcode = ENrunH(&clock);
    if(errcode) checkError(errcode, "ONSystem::runHydraulicSnapshot()");
    return clock;
}

long ONSystem::nextHydraulicStep(void)
{
    int errcode;
    long clock;
    errcode = ENnextH(&clock);
    if(errcode) checkError(errcode, "ONSystem::nextHydraulicStep()");
    return clock;
}

void ONSystem::closeHydraulics(void)
{
    int errcode;
    errcode = ENcloseH();
    if(errcode) checkError(errcode, "ONSystem::closeHydraulics()");
}

void ONSystem::solveQuality(void)
{
    int errcode;
    errcode = ENsolveQ();
    if(errcode) checkError(errcode, "ONSystem::solveQuality()");
}

void ONSystem::openQuality(void)
{
    int errcode;
    errcode = ENopenQ();
    if(errcode) checkError(errcode, "ONSystem::openQuality()");
}

void ONSystem::initializeQuality(bool saveResults)
{
    int errcode;
    int flag = 0;
    if (saveResults) flag = 1;
    errcode = ENinitQ(flag);
    if(errcode) checkError(errcode, "ONSystem::initializeQuality()");
}

long ONSystem::runQualitySnapshot(void)
{
    int errcode;
    long clock;
    errcode = ENrunQ(&clock);
    if(errcode) checkError(errcode, "ONSystem::runQualitySnapshot()");
    return clock;
}

long ONSystem::nextQualityStep(void)
{
    int errcode;
    long clock;
    errcode = ENnextQ(&clock);
    if(errcode) checkError(errcode, "ONSystem::nextQualityStep()");
    return clock;
}

long ONSystem::stepQuality(void)
{
    int errcode;
    long clock;
    errcode = ENstepQ(&clock);
    if(errcode) checkError(errcode, "ONSystem::stepQuality()");
    return clock;
}

void ONSystem::closeQuality(void)
{
    int errcode;
    errcode = ENcloseQ();
    if(errcode) checkError(errcode, "ONSystem::closeQuality()");
}

void ONSystem::saveHydraulicsOutputFile(void)
{
    int errcode;
    errcode = ENsaveH();
    if(errcode) checkError(errcode, "ONSystem::saveHydraulics()");
}

void ONSystem::saveInputFile(string fileName)
{
    int errcode;
    char* fname = new char[fileName.length()+1];
    std::strcpy(fname, fileName.c_str());
    errcode = ENsaveinpfile(fname); 
    delete[] fname;
    if(errcode) checkError(errcode, "ONSystem::saveInputFile()");
}

void ONSystem::writeReport(void)
{
    int errcode;
    errcode = ENreport();
    if(errcode) checkError(errcode, "ONSystem::writeReport()");
}

void ONSystem::resetReportFormat(void)
{
    int errcode;
    errcode = ENresetreport();
    if(errcode) checkError(errcode, "ONSystem::resetReportFormatting()");
}

void ONSystem::setReportFormat(string command)
{
    int errcode;
    char* cmd = new char[command.length()+1];
    std::strcpy(cmd, command.c_str());
    errcode = ENsetreport(cmd);
    delete[] cmd;
    if(errcode) checkError(errcode, "ONSystem::setReportFormat()");
}

int ONSystem::epanetVersion(void) const
{
    int ver;
    int errcode;
    errcode = ENgetversion(&ver);
    if(errcode) checkError(errcode, "ONSystem::epanetVersion()");
    return ver;
}

string ONSystem::ootenVersion(void) const
{
    return onVersion_;
}
