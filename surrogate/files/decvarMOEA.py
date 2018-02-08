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
decvar-MOEA class for save MOEA Decision Variables into json file format.
"""

import os, json

import numpy as np

class decvarMOEA(object):

    def __init__(self, varDir, casePref, numVar, numPop, numCon, numObj, numGen):
        """decvarMOEA

        :param varDir:
        :param casePref: 't' for 'test'
        :param numVar:
        :param numPop:
        :param numCon:
        :param numObj:
        :param numGen:
        :return:
        """
        # # Method 1
        # # fileName = 'variable/surrogate'/g00000000_dv.json
        # self.fileName = self.varDir + '/' + "g%08d" % igen + self.fileExt
        # self.varDir = varDir
        # self.casePref = casePref
        # self.icase = 0
        # self.fileExt = '_dv.json'
        # self.fileName = ''

        # # Method 2
        # fileName = 'variable/surrogate'/'t'00000001.txt
        self.varDir = varDir
        self.casePref = casePref
        self.icase = 0
        self.fileExt = '.txt'
        self.fileName = ''

        self.numPop = numPop
        self.numVar = numVar
        self.numCon = numCon
        self.numObj = numObj
        self.numGen = numGen


    def writeHeader(self, igen):
        """writeHeader

        :return:
        """
        # # Method 1
        # self.fileName = self.varDir + '/' + "g%08d" % igen + self.fileExt
        # print '--py:Test:: ' + 'decvarMOEA.writeHeader'

        # outFile = open(self.fileName, "wt")
        # outFile.write("{\n")
        # outFile.write("\"variable\":[\n")
        # outFile.close()

        # # Method 2
        pass

    def writeEnd(self):
        """writeEnd

        :return:
        """
        # # Method 1
        # print '--py:Test:: ' + 'decvarMOEA.writeEnd'

        # outFile = open(self.fileName, "a")
        # outFile.write("]\n}\n")
        # outFile.close()

        # # Method 2
        pass

    def writeDecVar(self, variable, ipop):
        """

        :param variable:
        :param igen:
        :return:
        """
        # # Method 1
        # self.icase += 1
        # caseName = self.casePref+"%08d" % self.icase
        #
        # outFile = open(self.fileName, "a")
        # outFile.write("  { \""+caseName+"\" : ["+','.join(map("{:.5f}".format, variable))+"] }")
        # if ipop < self.numPop - 1:
        #     outFile.write(",")
        # outFile.write("\n")
        # outFile.close()

        # # Method 2
        self.icase += 1
        self.fileName = self.varDir + '/' + self.casePref+"%08d" % self.icase+self.fileExt
        # print '--py:Test:: ' + 'decvarMOEA.writeDecVar( Pop: '+str(ipop)+' ) '+self.fileName

        outFile = open(self.fileName, "wt")
        outFile.write('\t'.join(map("{:.5f}".format, variable)))
        outFile.write("\n")
        outFile.close()
