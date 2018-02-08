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
JSON-MOEA class for save MOEA results into json file format.
"""

import os, json

import matplotlib as mpl
if os.environ.get('DISPLAY','') == '':
    # print('--py:Warning:: No display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt

import numpy as np
from matplotlib.pyplot import cm

class jsonMOEA(object):
    """jsonMOEA

    :param fileName: file name
    :param numVar: Number of Deciison Variables
    :param numPop: Number of Populations
    :param numCon: Number of Constrains
    :param numObj: Number of Objective Functions
    :param numGen: Number of Generations
    """
    def __init__(self, fileName, numVar, numPop, numCon, numObj, numGen):
        """

        :param fileName:
        :param numVar:
        :param numPop:
        :param numCon:
        :param numObj:
        :param numGen:
        :return:
        """
        self.fileName = fileName
        self.numPop = numPop
        self.numVar = numVar
        self.numCon = numCon
        self.numObj = numObj
        self.numGen = numGen

    def writeHeader(self):
        """

        :return:
        """
        outFile = open(self.fileName, "wt")
        outFile.write("{\n")
        outFile.write("\"generation\": [\n")
        outFile.close()

    def writeEnd(self):
        """

        :return:
        """
        outFile = open(self.fileName, "a")
        outFile.write("]\n}\n")
        outFile.close()

    def writePareto(self, individuals, igen):
        """

        :param individuals:
        :param igen:
        :return:
        """
        outFile = open(self.fileName, "a")
        outFile.write("    {\n")

        outFile.write("        \"variable\"   : [")
        outFile.write("[%.6f" % (individuals[0].variable[0]))
        for j in range(1, self.numVar):
            outFile.write(",%.6f" % (individuals[0].variable[j]))
        outFile.write("]")
        for i in range(1, self.numPop):
            outFile.write(",[%.6f" % (individuals[i].variable[0]))
            for j in range(1, self.numVar):
                outFile.write(",%.6f" % (individuals[i].variable[j]))
            outFile.write("]")
        outFile.write("],\n")

        outFile.write("        \"objective\"  : [[")
        outFile.write("[%.6f" % (individuals[0].fitness.values[0]))
        for j in range(1, self.numObj):
            outFile.write(",%.6f" % (individuals[0].fitness.values[j]))
        outFile.write("]")
        for i in range(1, self.numPop):
            outFile.write(",[%.6f" % (individuals[i].fitness.values[0]))
            for j in range(1, self.numObj):
                outFile.write(",%.6f" % (individuals[i].fitness.values[j]))
            outFile.write("]")
        outFile.write("]]")

        if self.numCon > 0:
            outFile.write(",")
        outFile.write("\n")

        if self.numCon > 0:
            outFile.write("        \"constraint\" : [")
            outFile.write("[%.6f" % (individuals[0].constraint[0]))
            for j in range(1, self.numCon):
                outFile.write(",%.6f" % (individuals[0].constraint[j]))
            outFile.write("]")
            for i in range(1, self.numPop):
                outFile.write(",[%.6f" % (individuals[i].constraint[0]))
                for j in range(1, self.numCon):
                    outFile.write(",%.6f" % (individuals[i].constraint[j]))
                outFile.write("]")
            outFile.write("]")
            outFile.write("\n")

        outFile.write("    }")
        if igen < self.numGen - 1:
            outFile.write(",")
        outFile.write("\n")

        outFile.close()

    def savePlot(self):
        with open(self.fileName) as data_file:
            data = json.load(data_file)

        gen = data["generation"]
        gen_tot = len(gen)

        color = iter(cm.gray(np.linspace(1, 0.1, gen_tot)))
        # color = iter(cm.rainbow(np.linspace(0,1,gen_tot)))
        for index, item in enumerate(gen):
            obj = item["objective"][0]
            obj_tot = len(obj)
            x = []
            y = []
            r = index / gen_tot
            g = index / gen_tot
            b = index / gen_tot

            for iobj in obj:
                x.append(iobj[0])
                y.append(iobj[1])

                # print '['+'\t'.join(map(str,iobj))+']'
            plt.plot(x, y, 'o', color=next(color), label=str(index))

        # minmax = [min(x), max(x), min(y), max(y)]

        plt.title('moea.json')
        plt.xlabel('obj1')
        # if minmax[0]==0.0 and minmax[1]==0.0:
        #     plt.xlim([minmax[0]-0.05,minmax[1]+0.05])
        # elif minmax[0]==0.0 and minmax[1]!=0.0:
        #     plt.xlim([minmax[0]-0.05,minmax[1]+0.05*abs(minmax[1])])
        # elif minmax[0]!=0.0 and minmax[1]==0.0:
        #     plt.xlim([minmax[0]-0.05*abs(minmax[0]),minmax[1]+0.05])
        # else:
        #     plt.xlim([minmax[0]-0.05*abs(minmax[0]),minmax[1]+0.05*abs(minmax[1])])
        # # plt.xlim([minmax[0]-0.05*abs(minmax[0]),minmax[1]+0.05*abs(minmax[1])])
        plt.ylabel('obj2')
        # if minmax[2]==0.0 and minmax[3]==0.0:
        #     plt.ylim([minmax[2]-0.05,minmax[3]+0.05])
        # elif minmax[2]==0.0 and minmax[3]!=0.0:
        #     plt.ylim([minmax[2]-0.05,minmax[3]+0.05*abs(minmax[3])])
        # elif minmax[2]!=0.0 and minmax[3]==0.0:
        #     plt.ylim([minmax[2]-0.05*abs(minmax[2]),minmax[3]+0.05])
        # else:
        #     plt.ylim([minmax[2]-0.05*abs(minmax[2]),minmax[3]+0.05*abs(minmax[3])])
        # # plt.ylim([minmax[2]-0.05*abs(minmax[2]),minmax[3]+0.05*abs(minmax[3])])
        plt.grid(True)
        # plt.legend(loc='best')
        plt.savefig(self.fileName+'.png')
        # plt.show()
        plt.clf()

    def plot_json(self):
        """

        :return:
        """
        with open(self.fileName) as data_file:
            data = json.load(data_file)

        gen = data["generation"]
        gen_tot = len(gen)

        color = iter(cm.gray(np.linspace(1, 0.1, gen_tot)))
        # color = iter(cm.rainbow(np.linspace(0,1,gen_tot)))
        for index, item in enumerate(gen):
            obj = item["objective"][0]
            obj_tot = len(obj)
            x = []
            y = []
            r = index / gen_tot
            g = index / gen_tot
            b = index / gen_tot

            for iobj in obj:
                x.append(iobj[0])
                y.append(iobj[1])

                # print '['+'\t'.join(map(str,iobj))+']'
            plt.plot(x, y, 'o', color=next(color), label=str(index))

        minmax = [min(x), max(x), min(y), max(y)]

        plt.title('moea.json')
        plt.xlabel('obj1')
        if minmax[0]==0.0 and minmax[1]==0.0:
            plt.xlim([minmax[0]-0.05,minmax[1]+0.05])
        elif minmax[0]==0.0 and minmax[1]!=0.0:
            plt.xlim([minmax[0]-0.05,minmax[1]+0.05*abs(minmax[1])])
        elif minmax[0]!=0.0 and minmax[1]==0.0:
            plt.xlim([minmax[0]-0.05*abs(minmax[0]),minmax[1]+0.05])
        else:
            plt.xlim([minmax[0]-0.05*abs(minmax[0]),minmax[1]+0.05*abs(minmax[1])])
        # plt.xlim([minmax[0]-0.05*abs(minmax[0]),minmax[1]+0.05*abs(minmax[1])])
        plt.ylabel('obj2')
        if minmax[2]==0.0 and minmax[3]==0.0:
            plt.ylim([minmax[2]-0.05,minmax[3]+0.05])
        elif minmax[2]==0.0 and minmax[3]!=0.0:
            plt.ylim([minmax[2]-0.05,minmax[3]+0.05*abs(minmax[3])])
        elif minmax[2]!=0.0 and minmax[3]==0.0:
            plt.ylim([minmax[2]-0.05*abs(minmax[2]),minmax[3]+0.05])
        else:
            plt.ylim([minmax[2]-0.05*abs(minmax[2]),minmax[3]+0.05*abs(minmax[3])])
        # plt.ylim([minmax[2]-0.05*abs(minmax[2]),minmax[3]+0.05*abs(minmax[3])])
        plt.grid(True)
        # plt.legend(loc='best')
        plt.show()
