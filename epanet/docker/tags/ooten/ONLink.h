/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

ONLINK.H - Definition of OOTEN ONLink class

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

#ifndef ONLinkH
#define ONLinkH
//---------------------------------------------------------------------------

#include "ONElement.h"
#include "ONNode.h"

using namespace std;

class ONLink : public ONElement
{
    public:
        //constructors and destructors
        ONLink(void);
        ONLink(int enIndex, ONSystem* parent, ONNode* startNode, ONNode* endNode);
        ONLink(const ONLink &o);
        virtual ONLink* clone(void);
        virtual ~ONLink(void);

        //methods
        virtual elementTpe  type(void) const;
        virtual string      id(void) const;
        ONNode*             startNode(void) const;
        ONNode*             endNode(void) const;
        bool                initialStatus(void) const;
        void                setInitialStatus(bool status);
        double              flowrate(void) const;
        double              headloss(void) const;
        bool                status(void) const;
        void                setStatus(bool status);

    private:
        ONNode* startNode_;
        ONNode* endNode_;
};

#endif
