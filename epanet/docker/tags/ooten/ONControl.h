/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONCONTROL.H - Definition of OOTEN ONControl class

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

#ifndef ONControlH
#define ONControlH
//---------------------------------------------------------------------------

#include "ONElement.h"
#include "ONNode.h"
#include "ONLink.h"

using namespace std;

class ONControl : public ONElement
{
    public:
        //enumerators
        enum controlTpe {ctLowLevel, ctHighLevel, ctTimer, ctTimeOfDay};

        //constructors and destructors
        ONControl(void);
        ONControl(int enIndex, ONSystem* parent, ONLink* link = 0, ONNode* node = 0);
        ONControl(const ONControl &o);
        virtual ONControl* clone(void);
        virtual ~ONControl(void);

        //methods
        virtual elementTpe  type(void) const;
        controlTpe          controlType(void);
        void                setControlType(controlTpe type);
        ONLink*             link(void) const;
        void                setLink(ONLink* link);
        double              linkSetting(void) const;
        void                setLinkSetting(double setting);
        ONNode*             node(void) const;
        void                setNode(ONNode* node);
        double              trigger(void) const;
        void                setTrigger(double pressure);

    private:
        ONLink* link_;
        ONNode* node_;
};

#endif
