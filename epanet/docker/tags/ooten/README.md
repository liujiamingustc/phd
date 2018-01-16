# ooten

OOTEN - Object-Oriented Toolkit for EPANET

Like the EPANET sources, the OOTEN sources are Public Domain.

See [epanet.de](http://epanet.de/en/ooten/index.html) for more information.

## Contents of OOTEN.ZIP

This archive contains the source code for OOTEN (Object-
Oriented Toolkit for EpaNet), as well as the EPANET 2 
source code. 

OOTEN is based on the EPANET Programmers Toolkit, and 
incorporates all the functionality of the EPANET 
Programmers Toolkit in an object-oriented shell. It also
adds functionality that is currently not available in the
EPANET Programmers Toolkit. 

EPANET is written in ANSI-compatible C and OOTEN in ANSI
C++. OOTEN was developed using Borland C++ Builder version 
6.0, but should compile with any ANSI C and C++ compatible
compiler. no visual components, such as windows, are
referenced in the OOTEN source code.

The files included in OOTEN.ZIP are listed below in the
following categories:

	- Help files
	- EPANET source code files 
	- OOTEN source code files
	- Example Borland C++ Builder project files



## HELP FILES

The following files are included to provide help for users
of OOTEN:

	README.TXT  -- this file
	OOTEN.HLP   -- a help file for using OOTEN



## EPANET SOURCE CODE FILES

The following standard EPANET source files (C-code) are 
included in this archive:

	INPUT1.C  -- controls processing of input data
	INPUT2.C  -- reads data from input file
	INPUT3.C  -- parses individual lines of input data
	INPFILE.C -- saves modified input data to a text file
	RULES.C   -- implements rule-based control of piping system
	HYDRAUL.C -- computes extended period hydraulic behavior
	QUALITY.C -- tracks transport & fate of water quality
	OUTPUT.C  -- handles transfer of data to and from binary files
	REPORT.C  -- handles reporting of results to text file
	SMATRIX.C -- sparse matrix linear equation solver routines
	MEMPOOL.C -- memory pool management routines
	HASH.C    -- hash table routines

Also included are the following standard EPANET header files:

	FUNCS.H    -- prototypes of all other functions
	TYPES.H    -- declaration of global constants and data structures
	VARS.H     -- declaration of global variables
	HASH.H     -- header file for hash table routines
	MEMPOOL.H  -- header file for memory pool routines
	ENUMSTXT.H -- string constants for enumerated types
	TEXT.H     -- declaration of all other string constants

The following EPANET source code file (C-code) was altered, but
retains all its original functionality. To differentiate altered
EPANET source code files from standard ones, the altered files are
saved with a `'_on'` extension.

	EPANET_ON.C  -- main module providing supervisory control.

The following EPANET header code file was altered, but retains all 
its original functionality. To differentiate altered EPANET source 
code files from standard ones, the altered files are saved with a `'_on'` 
extension.

	TOOLKIT_ON.H  -- function prototypes of Toolkit functions 

The comments at the top of each file lists the date when the latest
update was made, and these updates can be located in the code by
searching for the keywords `"/*** Updated"`.

Other useful documentation that can be consulted includes the EPANET
Programmers Toolkit Help file and the EPANET Version 2 Users Manual.

Changes to standard EPANET files can be located in the code by searching
for the keyword `"jevz"`.


## OOTEN SOURCE CODE FILES

The following ANSI C++ OOTEN source code files are included in this 
archive:

	ONOBJECT.CPP      -- implementation of the OOTEN class ONObject
	ONOBJECT.H        -- definition of the OOTEN class ONObject (top most class)
	ONSYSTEM.CPP      -- implementation of the OOTEN class ONSystem
	ONSYSTEM.H        -- definition of the OOTEN class ONSystem
	ONELEMENT.CPP     -- implementation of the OOTEN class ONElement
	ONELEMENT.H       -- definition of the OOTEN class ONElement
	ONNODE.CPP        -- implementation of the OOTEN class ONNode
	ONNODE.H          -- definition of the OOTEN class ONNode
	ONLINK.CPP        -- implementation of the OOTEN class ONLink
	ONLINK.H          -- definition of the OOTEN class ONLink
	ONPATTERN.CPP     -- implementation of the OOTEN class ONPattern
	ONPATTERN.H       -- definition of the OOTEN class ONPattern
	ONCURVE.CPP       -- implementation of the OOTEN class ONCurve
	ONCURVE.H         -- definition of the OOTEN class ONCurve
	ONCONTROL.CPP     -- implementation of the OOTEN class ONControl
	ONCONTROL.H       -- definition of the OOTEN class ONControl
	ONJUNCTION.CPP    -- implementation of the OOTEN class ONJunction
	ONJUCTION.H       -- definition of the OOTEN class ONJunction
	ONTANK.CPP        -- implementation of the OOTEN class ONTank
	ONTANK.H          -- definition of the OOTEN class ONTank
	ONRESERVOIR.CPP   -- implementation of the OOTEN class ONReservoir
	ONRESERVOIR.H     -- definition of the OOTEN class ONReservoir
	ONPIPE.CPP        -- implementation of the OOTEN class ONPipe
	ONPIPE.H          -- definition of the OOTEN class ONPipe
	ONPUMP.CPP        -- implementation of the OOTEN class ONPump
	ONPUMP.H          -- definition of the OOTEN class ONPump
	ONVALVE.CPP       -- implementation of the OOTEN class ONValve
	ONVALVE.H         -- definition of the OOTEN class ONValve
	ONFVC.CPP         -- implementation of the OOTEN class ONFVC
	ONFVC.H           -- definition of the OOTEN class ONFVC (flow control valve)
	ONGPV.CPP         -- implementation of the OOTEN class ONGPV
	ONGPV.H           -- definition of the OOTEN class ONGPV (general purpose valve)
	ONPBV.CPP         -- implementation of the OOTEN class ONPBV 
	ONPBV.H           -- definition of the OOTEN class ONPBV (pressure breaker valve)
	ONPRV.CPP         -- implementation of the OOTEN class ONPRV
	ONPRV.H           -- definition of the OOTEN class ONPRV (pressure reducing valve)
	ONPSV.CPP         -- implementation of the OOTEN class ONPSV
	ONPSV.H           -- definition of the OOTEN class ONPSV (pressure sustaining valve)
	ONTCV.CPP         -- implementation of the OOTEN class ONTCV
	ONTCV.H           -- definition of the OOTEN class ONTCV (throttle control valve)
	ONEXCEPTION.CPP   -- implementation of the OOTEN class ONException
	ONEXCEPTION.H     -- definition of the OOTEN class ONException
	ONENEXCEPTION.CPP -- implementation of the OOTEN class ONENException
	ONENEXCEPTION.H   -- definition of the OOTEN class ONENException


## BORLAND C++ BUILDER PROJECT FILES

The following Borland Builder C++ Builder (version 6.0) project
files are included in this archive as an example of how to implement
OOTEN in Borland C++ Builder:

	OOTEN.BPR       -- Borland C++ Builder project file
	OOTEN.BPF       -- Borland C++ Builder support file
	OOTEN.RES       -- Borland C++ Builder resources file
	EXAMPLE1.CPP    -- implementation of example 1 defined in help - contains main() function
	NET1.INP        -- example EPANET input file - used in EXAMPLE1.CPP


## Build program

```bash
$ git clone https://github.com/quanpan302/phd.git
$ cd epanet/tags/ooten
$ mkdir -p build
$ cd build
$ cmake ..
$ make
$ cd ../
```