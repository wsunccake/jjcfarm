#!/usr/bin/env python
#
# modified date: 2011/09/14
#

import math

class poscarAtom:
    def __init__(self, element, x, y, z, X_Dynamic="F", Y_Dynamic="F", Z_Dynamic="F"):

        self.setElement(element)
        self.setCoordinate(x, y, z)
        # F: Freeze, T: Translate
        self.setDynamic(X_Dynamic, Y_Dynamic, Z_Dynamic)

    def setElement(self, element):
        self._element_ = element

    def setCoordinate(self, xCoordinate, yCoordinate, zCoordinate):
        self._xCoordinate_ = xCoordinate
        self._yCoordinate_ = yCoordinate
        self._zCoordinate_ = zCoordinate

    def setDynamic(self, xDynamic, yDynamic, zDynamic):
        self._xDynamic_ = xDynamic
        self._yDynamic_ = yDynamic
        self._zDynamic_ = zDynamic

    def getElement(self):
        return self._element_

    def getCoordinate(self):
        return (self._xCoordinate_, self._yCoordinate_, self._zCoordinate_)

    def getDynamic(self):
        return (self._xDynamic_, self._yDynamic_, self._zDynamic_)
    
    def __add__(self, atom):
        x, y, z = atom.getCoordinate()
        X = self._xCoordinate_ + x
        Y = self._yCoordinate_ + y
        Z = self._zCoordinate_ + z
        newAtom = poscarAtom(self._element_, X, Y, Z,
                             self._xDynamic_, self._yDynamic_, self._zDynamic_)
        return newAtom
        
    def __sub__(self, atom):
        x, y, z = atom.getCoordinate()
        X = self._xCoordinate_ - x
        Y = self._yCoordinate_ - y
        Z = self._zCoordinate_ - z
        newAtom = poscarAtom(self._element_, X, Y, Z,
                             self._xDynamic_, self._yDynamic_, self._zDynamic_)
        return newAtom
    
    def __mul__(self, value):
        X = self._xCoordinate_ * value
        Y = self._yCoordinate_ * value
        Z = self._zCoordinate_ * value
        newAtom = poscarAtom(self._element_, X, Y, Z,
                             self._xDynamic_, self._yDynamic_, self._zDynamic_)
        return newAtom
        
    def __div__(self, value):
        X = self._xCoordinate_ / value
        Y = self._yCoordinate_ / value
        Z = self._zCoordinate_ / value
        newAtom = poscarAtom(self._element_, X, Y, Z,
                             self._xDynamic_, self._yDynamic_, self._zDynamic_)
        return newAtom
    
    def distane(self, atom):
        x, y, z = atom.getCoordinate()
        X = x - self._xCoordinate_
        Y = y - self._yCoordinate_
        Z = z - self._zCoordinate_
        D = math.sqrt(X * X + Y * Y + Z * Z)
        return (D, X, Y, Z)
      
class poscarElement:
    def __init__(self, t, n):
        self.setType(t)
        self.setNumber(n)
        
    def setType(self, t):
        self._Type_ = t
        
    def getType(self):
        return self._Type_
    
    def setNumber(self, n):
        self._Number_ = n
    
    def getNumber(self):
        return self._Number_

class POSCAR:
    def __init__(self, filename=None, comment=None, lattice_constat=1.0,
                 vector1=(1.0, 0.0, 0.0), vector2=(0.0, 1.0, 0.0), vector3=(0.0, 0.0, 1.0),
                 select="Selective", coordinate="Cartesian"):
        # setup filename
        if filename is None:
            self.setFilename("")
        else:
            self.setFilename(filename)
        
        # setup comment
        if comment is None:
            self.setComment("Comment line")
        else:
            self.setComment(comment)
            
        # setup lattice constant
        self.setLatticeConstant(lattice_constat)
        
        # setup lattice vector
        self._LatticeVectors_ = [vector1, vector2, vector3]
        
        # setup SelectiveMode
        self.setSelectiveMode(select)
        
        # set upCoorndinate Type
        self.setCoorndinateType(coordinate)
        
        
        self._Elements_ = []
        self._Atoms_ = []
        pass

    def setFilename(self, filename):
        self._FileName_ = filename
        
    def getFilename(self):
        return self._FileName_
    
    def setComment(self, comment):
        self._Comment_ = comment
        
    def getComment(self):
        return self._Comment_
    
    def setLatticeConstant(self, lattice_constat):
        self._LatticeConstant_ = lattice_constat
        
    def getLatticeConstant(self):
        return self._LatticeConstant_
    
    def setLatticeVector(self, index, vector):
        v1 = self._LatticeVectors_[0]
        v2 = self._LatticeVectors_[1]
        v3 = self._LatticeVectors_[2]
        if index == 0:
            v1 = vector
        elif index == 1:
            v2 = vector
        else:
            v3 = vector
        self._LatticeVectors_ = [v1, v2 , v3]

    def getLatticeVector(self, index):
        return self._LatticeVectors_[index]
    
    def setSelectiveMode(self, mode):
        self._SelectiveMode_ = mode
        
    def getSelectiveMode(self):
        return self._SelectiveMode_
    
    def setCoorndinateType(self, coordinate):
        self._CoorndinateType_ = coordinate
        
    def getCoorndinateType(self):
        return self._CoorndinateType_

    def readFile(self, filename):
        self.setFilename(filename)
        f = open(self._FileName_)
        # setup comment
        self.setComment(f.readline().rstrip())
        
        # setup lattice constant
        self.setLatticeConstant(float(f.readline().rstrip()[0]))
        
        # setup lattice vector
        for i in range(3):
            l = f.readline().rstrip()
            v = (float(l.split()[0]), float(l.split()[1]), float(l.split()[2]))
            self.setLatticeVector(i, v)
            
        # setup number of element type 
        l = f.readline()
        for n in l.split():
            e = poscarElement("", int(n))
            self._Elements_.append(e)
        
        # setup selective mode and coordinate type
        l = f.readline().rstrip()
        if l.split()[0][0].upper() == "S":
            # setup coordinate type
            self._SelectiveMode_ = l
            l = f.readline().rstrip()
            # cartesian coordinates
            if l.split()[0][0].upper() == 'C':
                self._CoorndinateType_ = l
            # cartesian coordinates
            elif l.split()[0][0].upper() == 'K':
                self._CoorndinateType_ = l
            # direct/fractional coordinates)
            elif l.split()[0][0].upper() == 'D':
                self._CoorndinateType_ = l
            else:
                pass
                
        # setup atom coordinate
        for l in f.readlines():
            if len(l.split()) < 3:
                a = poscarAtom("", float(l.split()[0]), float(l.split()[1]), float(l.split()[2]))
            else:
                a = poscarAtom("", float(l.split()[0]), float(l.split()[1]), float(l.split()[2]),
                                   l.split()[3], l.split()[4], l.split()[5])
            self._Atoms_.append(a)
        
        f.close()
        
    def writePOSCAR(self, filename=None):
        format1 = '''%s
%.10f
%+14.10f %+14.10f %+14.10f
%+14.10f %+14.10f %+14.10f
%+14.10f %+14.10f %+14.10f
'''
        output1 = format1 % (self._Comment_, self._LatticeConstant_,
                        self._LatticeVectors_[0][0], self._LatticeVectors_[0][1], self._LatticeVectors_[0][2],
                        self._LatticeVectors_[1][0], self._LatticeVectors_[1][1], self._LatticeVectors_[1][2],
                        self._LatticeVectors_[2][0], self._LatticeVectors_[2][1], self._LatticeVectors_[2][2])

        output2 = ""
        for e in self._Elements_:
            output2 = output2 + " %i" % (e._Number_)
        output2 = output2 + "\n"  

        if self._SelectiveMode_ is None:
            output3 = "%s\n" % (self._CoorndinateType_)
            for a in self._Atoms_:
                output3 = output3 + "%+14.10f %+14.10f %+14.10f\n" % a.getCoordinate()
        else:
            output3 = "%s\n%s\n" % (self._SelectiveMode_, self._CoorndinateType_)
            for a in self._Atoms_:
                output3 = output3 + "%+14.10f %+14.10f %+14.10f" % a.getCoordinate() + "  %s %s %s\n" % a.getDynamic()
        
        # setup output
        if filename == None:
            print output1 + output2 + output3
        else:
            f = open(filename, "wb")
            f.write(output1 + output2 + output3)
            f.close()

    def equalLattice(self, poscar):
        if self._LatticeConstant_ == poscar._LatticeConstant_ and self._LatticeVectors_ == poscar._LatticeVectors_:
            return True
        return False
        
    def equalElement(self, poscar):
        if len(self._Elements_) == len(poscar._Elements_):
            for i in range(len(self._Elements_)):
                if self._Elements_[i]._Number_ != poscar._Elements_[i]._Number_:
                    return False 
            return True
        return False
        
    def splitPOSCAR(self, poscar, npart=2):
        if npart <= 1:
            print "npart must be gather than 1"
            return

        if self.equalElement(poscar) and self.equalLattice(poscar):
            increment = []
            for i in range(len(self._Atoms_)):
                increment.append((poscar._Atoms_[i] - self._Atoms_[i]) / (npart - 1))
            poscarList = []
            for i in range(npart):
                newposcar = POSCAR("POSCAR" + str(i), self._Comment_, self._LatticeConstant_,
                                   self._LatticeVectors_[0], self._LatticeVectors_[1], self._LatticeVectors_[2],
                                   self._SelectiveMode_, self._CoorndinateType_)
                newposcar._Elements_ = self._Elements_
                for j in range(len(increment)):
                    newposcar._Atoms_.append(self._Atoms_[j] + increment[j] * i)
                poscarList.append(newposcar)
            return poscarList
    
        
if __name__ == "__main__":
    import sys
    import os
    import getopt
    
    def checkFile(f):
        if os.path.exists(f):
            return os.path.abspath(f)
        print "File: " + f + " didn't exist."
        sys.exit(2)
        return False
    
    if os.path.basename(os.path.abspath(sys.argv[0])) == "splitPOSCAR" or os.path.basename(os.path.abspath(sys.argv[0])) == "splitPOSCAR.py":
        def usage():
            print '''splitPOSCAR -i initial_POSCAR -f final_POSCAR [-n 4] [-d outdir]
'''
        try:
            opt_list, args = getopt.getopt(sys.argv[1:], 'i:f:n:d:h')
        except getopt.GetoptError, err: 
            print str(err)
            usage()
            sys.exit(2)
        
        initial = None
        final = None
        npart = None
        outdir = None
        tool = "scan"
        help_flag = False
        for o, a in opt_list: 
            if o in ('-i'): 
                initial = checkFile(a)
            elif o in ("-f"): 
                final = checkFile(a)
            elif o in ("-n"): 
                npart = int(a)
            elif o in ("-d"): 
                outdir = os.path.abspath(a)
            elif o in ("-t"): 
                tool = a 
            elif o in ("-h"): 
                help_flag = True 

        if help_flag:
            usage() 
            sys.exit(2)
    
        if initial is None:
            print "Input initial poscar: " 
            initial = checkFile(sys.stdin.readline().rstrip())
         
        if final is None:
            print "Input final poscar: " 
            final = checkFile(sys.stdin.readline().rstrip())

        if npart is None:
            print "Input number of split: " 
            npart = int(sys.stdin.readline().rstrip())
        
        if outdir is None:
            outdir = os.getcwd()
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        
            os.chdir(outdir)
    
            '''
    initial = "/Users/kam/AAA/ttt/POSCAR00"
    final = "/Users/kam/AAA/ttt/POSCAR09"
    npart = 5
'''
    
        poscar0 = POSCAR()
        poscar0.readFile(initial)
        poscar1 = POSCAR()
        poscar1.readFile(final)

        poscarList = poscar0.splitPOSCAR(poscar1, npart)
    
        for i in range(len(poscarList)):
            d = "%02i" % (i)
            if not os.path.exists(d):
                os.mkdir(d)
                poscarList[i].writePOSCAR(os.path.join(d, "POSCAR"))
                if os.name != "nt":
                    os.symlink(os.path.join(d, "POSCAR"), "POSCAR" + d)
#            for p in poscarList:
#            p.writePOSCAR(p.getFilename())
    else:
        pass


