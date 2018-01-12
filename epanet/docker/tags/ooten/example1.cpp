/*
*******************************************************************
OOTEN: Object Oriented Toolkit for Epanet

EXAMPLE1.CPP - Main function implementing OOTEN Example 1

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

#include <iostream>
#include "ONSystem.h"

//---------------------------------------------------------------------------

#pragma argsused
int main(int argc, char* argv[])
{
    /*    EXAMPLE 1     */

    /*create a new instance of MyClassSystem */
    ONSystem mySystem;
    try
    {
        /* Open a new file in OOTEN and the hydraulics solver */
        mySystem.open("net1.inp", "net1.rpt", "");
        mySystem.openHydraulics();

        /* Find all the tanks in the network */
        vector<ONNode*> nodes = mySystem.nodes();
        vector<ONTank*> tanks;
        ONTank* aTank;
        for (unsigned int i = 0; i < nodes.size(); i++)
        {
            if (nodes[i]->type() == ONElement::etTank)
           {
               aTank = dynamic_cast<ONTank*>(nodes[i]);
               /* check that null pointer was not returned */
               if (!aTank) 
                   exit(1);
               tanks.push_back(aTank);
            }
        }

        /* Do hydraulic simulation and report results*/
        long simTime, stepLength;
        mySystem.initializeHydraulics(false, false);
        do
        {
            simTime = mySystem.runHydraulicSnapshot();
            cout << simTime << "\t";
            for (unsigned int i = 0; i < tanks.size(); i++)
                cout << tanks[i]->level() << "\t";
            cout << endl;
            stepLength = mySystem.nextHydraulicStep();
        }
        while (stepLength != 0);

        /*close the hydraulic system and OOTEN */
        mySystem.closeHydraulics();
        mySystem.close();
    }

    /*catch and handle any exceptions thrown in the code */
    catch(ONException e)
    {
        mySystem.close();
        cout << e.report() << endl;
    }

    string enter;
    cout << "Type quit to continue" <<endl;
    cin >> enter;

    exit(0);
}
//---------------------------------------------------------------------------

