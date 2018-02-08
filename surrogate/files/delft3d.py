# MIT License
#
# Copyright (c) 2016 Daily Actie
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Author: Quan Pan <quanpan302@hotmail.com>
# License: MIT License
# Create: 2016-12-02

# 0 --py:Success::
# 1 --py:Warning::
# 2 --py:Error::
# --py:Start::['+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+']
# --py:End::  ['+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+']
# --py:Test::

"""
Delft3D classes for all Delft3D generated result files.
naming system: [method:read,write][software:Flow,Waq][file:Map,His]
"""

import os
import sys

import struct

class Delft3D(object):
    """Delft3D class

    :param gridFname: delft3D water quality grid file name
    :param mapFname: delft3D water quality map file name
    """
    def __init__(self, gridFname, mapFname):
        """

        :return:
        """
        self.gridFname = gridFname
        self.nrow = 0
        self.ncol = 0
        self.gridX = []
        self.gridY = []
        self.gridIndex = []

        self.mapFname = mapFname
        self.fileSize = os.path.getsize(mapFname)
        self.nseg = -1
        self.nvar = -1
        self.ntime = -1
        self.varlist = []
        self.timlist = []
        self.headOffset = -1
        self.blockOffset = -1

        self.iseg = 0
        self.ivar = 0
        self.itime = [-1,-1]

        # print '--py:Test:: Delft3D.gridFname: '+self.gridFname
        # print '--py:Test:: Delft3D.mapFname: '+self.mapFname

    def initWaqMap(self):
        """initWaqMap
        initiate read Delft3D Water quality model map file.
        open('b') is important -> binary
        file.read(1), 8 bits is 1 byte.

        Map file structure: [row,column]::

            character(len=40) : moname(4) [4,40]
            integer : self.nvar, self.nseg [1,4],[1,4]
            ntime = int(real(fileSize -4*40 -2*4 -self.nvar*20) / real(4+4*self.nvar*self.nseg))

            character(len=20) : self.varlist(self.nvar) [self.nvar,20]

            valmap(ntime,self.nseg,nresult)
            tempValMap(self.nvar, self.nseg) [self.nvar, self.nseg, 4]
            do k=1,ntime
                read (mapfID) maptime [1,4]
                read (mapfID) ((tempValMap(i,j),i=1,self.nvar),j=1,self.nseg)
                do j=1,nresult
                    valmap(k,:,j) = tempValMap(iseg(j),1:self.nseg)
                end do
            end do

        :return: fileContent
        """

        moname = []

        with open(self.mapFname, mode='rb') as file:
            for i in range(0,4):
                moname.append(file.read(40).strip())
            self.nvar = struct.unpack('i',file.read(4))[0]
            self.nseg = struct.unpack('i',file.read(4))[0]
            self.ntime = int((self.fileSize -4*40 -2*4 -self.nvar*20)/(4+4*self.nvar*self.nseg))
            self.headOffset = 4*40 + 2*4 + self.nvar*20
            self.blockOffset = self.nvar*self.nseg*4

            for i in range(0,self.nvar):
                self.varlist.append(file.read(20).strip())
            # print self.varlist

            # data = [[[None for k in range(self.ntime)] for j in range(self.nvar)] for i in range(self.nseg)]
            for k in range(0,self.ntime):
                self.timlist.append(struct.unpack('i',file.read(4))[0])
                # print '--py:Test:: '+'self.timlist:\t'+str(self.timlist[k])

                file.seek(self.nseg*self.nvar*4,1)
                # for i in range(0,self.nseg):
                #     for j in range(0,self.nvar):
                #         data[i][j][k] = struct.unpack('f',file.read(4))[0]

        return moname,\
               self.varlist,\
               self.timlist,\
               self.nseg,\
               self.nvar,\
               self.ntime

    def getWaqGrid(self):
        """readWaqGrid

        :return:
        """
        with open(self.gridFname, mode='r') as file:
            for line in file:
                self.nrow += 1
                rowIndex = [int(elt.strip()) for elt in line.split('\t')]
                self.ncol = len(rowIndex)
                # in alternative, if you need to use the file content as numbers
                # inner_list = [int(elt.strip()) for elt in line.split(',')]
                self.gridIndex.append(rowIndex)
                self.gridX.append([float(i) if rowIndex[i]>0 else 0.0 for i in range(self.ncol)])
                self.gridY.insert(0,[float(self.nrow-1) for y in range(self.ncol)])

        # file = open(self.gridFname+'-index','w')
        # strIndex = 'row\tcol\tindex\n'
        # file.write(strIndex)
        # for j in range(self.ncol):
        #     for i in range(self.nrow-1,-1,-1):
        #         if self.gridIndex[i][j]>0:
        #             strIndex = str(self.nrow-i)+'\t'+str(j+1)+'\t'+str(self.gridIndex[i][j])+'\n'
        #             file.write(strIndex)
        # file.close()

        return self.nrow,\
               self.ncol,\
               self.gridX,\
               self.gridY,\
               self.gridIndex

    def getWaqMapDataAtOffset(self,iseg=0,ivar=0,itime=0):
        """

        :param iseg:
        :param ivar:
        :param itime:
        :return:
        """
        self.chkError(i=iseg,n=self.nseg,s='segment')
        self.chkError(i=ivar,n=self.nvar,s='variable')
        self.chkError(i=itime,n=self.ntime,s='time')
        self.iseg = iseg
        self.ivar = ivar
        self.itime[0] = itime

        with open(self.mapFname, mode='rb') as file:
            file.seek(self.headOffset,0)

            file.seek((self.blockOffset+4)*itime,1)
            self.itime[1] = struct.unpack('i',file.read(4))[0]
            file.seek((iseg*self.nvar+ivar)*4,1)
            data = struct.unpack('f',file.read(4))[0]

        return data

    def getWaqMapDataAtTime(self,itime=0):
        """

        :param itime:
        :return:
        """
        self.chkError(i=itime,n=self.ntime,s='time')
        self.iseg = -1
        self.ivar = -1
        self.itime[0] = itime

        # data = [[ None for j in range(self.nvar)] for i in range(self.nseg)]
        data = [[[None for k in range(1)] for j in range(self.nvar)] for i in range(self.nseg)]
        with open(self.mapFname, mode='rb') as file:
            file.seek(self.headOffset,0)

            file.seek((self.blockOffset+4)*itime,1)
            self.itime[1] = struct.unpack('i',file.read(4))[0]
            for i in range(0,self.nseg):
                for j in range(0,self.nvar):
                    data[i][j][0] = struct.unpack('f',file.read(4))[0]

        return data

    def getWaqMapDataAtSegment(self,iseg=0):
        """

        :param iseg:
        :return:
        """
        self.chkError(i=iseg,n=self.nseg,s='segment')
        self.iseg = iseg
        self.ivar = -1
        self.itime = [-1,-1]

        # data = [[ None for j in range(self.ntime)] for i in range(self.nvar)]
        data = [[[None for k in range(self.ntime)] for j in range(self.nvar)] for i in range(1)]
        with open(self.mapFname, mode='rb') as file:
            file.seek(self.headOffset,0)

            # file.seek((self.blockOffset+4)*itime,1)
            for k in range(self.ntime):
                file.seek(4,1)
                file.seek(iseg*self.nvar*4,1)
                for j in range(self.nvar):
                    data[0][j][k] = struct.unpack('f',file.read(4))[0]
                file.seek((self.nseg-iseg-1)*self.nvar*4,1)

        return data

    def getWaqMapDataAtVariable(self,ivar=0):
        """

        :param ivar:
        :return:
        """
        self.chkError(i=ivar,n=self.nvar,s='variable')
        self.iseg = -1
        self.ivar = ivar
        self.itime = [-1,-1]

        # data = [[ None for j in range(self.ntime)] for i in range(self.nseg)]
        data = [[[None for k in range(self.ntime)] for j in range(1)] for i in range(self.nseg)]
        with open(self.mapFname, mode='rb') as file:
            file.seek(self.headOffset,0)

            # file.seek((self.blockOffset+4)*itime,1)
            for k in range(self.ntime):
                file.seek(4,1)
                for i in range(self.nseg):
                    file.seek(ivar*4,1)
                    data[i][0][k] = struct.unpack('f',file.read(4))[0]
                    file.seek((self.nvar-ivar-1)*4,1)

        return data

    def getWaqMapDataAtVariableTime(self,ivar=0,itime=0):
        """

        :param ivar:
        :param itime:
        :return:
        """
        self.chkError(i=ivar,n=self.nvar,s='variable')
        self.chkError(i=itime,n=self.ntime,s='time')
        self.iseg = -1
        self.ivar = ivar
        self.itime[0] = itime

        # data = [[ None for j in range(self.ntime)] for i in range(self.nseg)]
        data = [[None for j in range(1)] for i in range(self.nseg)]
        with open(self.mapFname, mode='rb') as file:
            file.seek(self.headOffset,0)

            file.seek((self.blockOffset+4)*itime,1)
            self.itime[1] = struct.unpack('i',file.read(4))[0]
            for i in range(self.nseg):
                file.seek(ivar*4,1)
                data[i][0] = struct.unpack('f',file.read(4))[0]
                file.seek((self.nvar-ivar-1)*4,1)

        return data

    def getWaqMapMaxDataAtVariableTime(self,ivar=0,itime=0):
        pass

    def saveFigMap(self,ivar=0,itime=0):
        """

        :param ivar:
        :param itime:
        :return:
        """
        pass

    def saveFigHis(self,ivar=0,iseg=0):
        """

        :param ivar:
        :param iseg:
        :return:
        """
        pass

    def chkError(self,i=0,n=0,s='empty'):
        """

        :param i: index of check variable
        :param n: total amount of check variable
        :param s: string of check variable
        :return:
        """
        icode = 0
        if i >= n:
            message = '--py:Test:: Delft3D.Error: '+s+' '+str(i)+' > '+str(n)
            print message
            icode = 101
            self.msgError(icode,message)


        # return icode,message

    def msgError(self,icode,message):
        """

        :param icode:
        :param message:
        :return:
        """
        if icode >= 0:
            sys.exit(message)

