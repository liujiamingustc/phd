//---- GPL ---------------------------------------------------------------------
//
// Copyright (C)  Stichting Deltares, 2011-2016.
//
// This program is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation version 3.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program.  If not, see <http://www.gnu.org/licenses/>.
//
// contact: delft3d.support@deltares.nl
// Stichting Deltares
// P.O. Box 177
// 2600 MH Delft, The Netherlands
//
// All indications and logos of, and references to, "Delft3D" and "Deltares"
// are registered trademarks of Stichting Deltares, and remain the property of
// Stichting Deltares. All rights reserved.
//
//------------------------------------------------------------------------------
// $Id: neftyp.h 5717 2016-01-12 11:35:24Z mourits $
// $HeadURL: https://svn.oss.deltares.nl/repos/delft3d/tags/6686/src/tools_gpl/vs/packages/vs/include/neftyp.h $

#ifndef _NEFTYP_INCLUDED
    enum STORAGE_TYPE {DBLCMPL, COMPLEX, DOUBLE, FLOAT, INT, SHORT, \
                       BOOL, BOOLSHRT, CHAR, UNDEF} ;
        typedef enum STORAGE_TYPE NfDtp;
#   define _NEFTYP_INCLUDED
#endif