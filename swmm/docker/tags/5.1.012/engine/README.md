Contents of this archive:

source5_1_012.zip
=================
Contains the source code for the computational engine
of SWMM 5.1.012. Consult the included Roadmap.txt file
for an overview of the various code modules.

makefiles.zip
=============
Contains `"make"` files for compiling the SWMM 5.1 engine
on Microsoft C++ 2010 and the GNU C compiler for Linux.


*INSTRUCTIONS FOR COMPILING THE COMMAND LINE VERSION OF SWMM 5*


USING THE GNU C/C++ COMPILER ON LINUX
-------------------------------------

1. Open the file `swmm5.c` in a text editor and make sure that the compiler directives at the top of the file read as follows:

	```c
	#define CLE
	//#define SOL
	//#define DLL
	```

2. Copy the file `"Makefile"` to the directory where the SWMM 5 `engine` source code files are located.

3. Open a console shell and navigate to the SWMM 5 engine source code directory.

4. Issue the command, to create an executable named swmm5.

	```bash
	make
	```


