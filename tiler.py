import numpy
import bisect
# import pyqtgraph as pg

TC = \
[[2,2,2,2,2,1,2,0,1,2,2,2,2,2,2,2,2,2], 
 [3,2,1,1,2,3,1,0,3,2,2,2,2,1,3,2,3,1],
 [2,3,2,2,2,1,3,2,1,2,2,3,1,2,2,2,2,2],
 [2,2,2,1,1,1,2,1,0,2,2,3,2,2,2,2,2,3],
 [2,2,0,3,2,3,1,2,3,3,2,1,3,2,2,2,2,2],
 [2,1,3,2,1,2,3,2,1,3,2,2,2,2,3,2,2,2],
 [2,1,1,1,2,2,2,1,1,1,2,3,2,3,2,2,3,1],
 [0,2,2,2,2,2,2,3,2,2,2,2,2,3,2,2,1,2],
 [2,2,2,2,2,3,2,2,1,1,1,2,1,2,3,2,2,3],
 [2,2,2,2,2,1,3,2,3,1,1,3,2,2,3,1,2,2],
 [2,2,2,2,3,3,2,2,2,3,1,1,2,2,2,1,2,2],
 [2,2,1,1,3,3,1,2,1,1,3,1,2,2,2,1,2,2],
 [2,2,3,2,0,2,2,2,2,2,3,1,1,2,2,1,2,2],
 [2,3,2,3,2,2,2,2,1,2,2,2,2,1,2,2,0,2],
 [2,2,3,2,3,2,2,2,1,1,1,3,2,2,1,3,2,2],
 [2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,3,2,0],
 [2,1,2,2,2,2,2,3,2,2,2,2,2,3,2,2,1,1],
 [2,3,2,1,2,2,2,2,1,1,2,2,2,2,2,3,3,2]]
types=18
grid = [0]*types
grid_h = 4
grid_v = 4

for d in range(types):
    grid[d]=[[[] for i in range(grid_h)] for j in range(grid_v)]
    grid[d][2][2]=[20]
    for a in range(types):
        if TC[d][a] != 2 or TC[a][d] != 2:
            grid[d][TC[d][a]][TC[a][d]] += [a]

def printGrid(mat):
    block_size = 25
    blank = " "*block_size
    print("\n  "+"0:"+" "*(block_size-2)+
                 "1:"+" "*(block_size-2)+
                 "2:"+" "*(block_size-2)+
                 "3:"+" "*(block_size-2))
    for i in range(len(mat)):
        row = ""
        for j in range(len(mat[i])):
            if len(mat[i][j])>0:
                block = ""
                for k in range(len(mat[i][j])):
                    block += "."+ str(mat[i][j][k])
                row += block + (block_size-len(block))*" "
            else:
                row += blank
        print(str(i)+":"+row)

branch = [[[] for i in range(6)] for j in range(types)]
for ref in range(types):
    for comp in range(types):
        if ref == comp:
            continue
        if len(grid[ref][0][1])*len(grid[comp][3][0])+\
           len(grid[ref][0][2])*len(grid[comp][3][1])+\
           len(grid[ref][0][3])*len(grid[comp][3][2]) == 0:
            branch[ref][0] += [comp]
        if len(grid[ref][0][3])*len(grid[comp][1][0])+\
          +len(grid[ref][1][3])*len(grid[comp][2][0])+\
          +len(grid[ref][2][3])*len(grid[comp][3][0]) == 0:
            branch[ref][1] += [comp]
        if len(grid[ref][2][2])*len(grid[comp][0][0])+\
           len(grid[ref][2][3])*len(grid[comp][0][1])+\
           len(grid[ref][3][2])*len(grid[comp][1][0])+\
           len(grid[ref][3][3])*len(grid[comp][1][1]) == 0:
            branch[ref][2] += [comp]
        if len(grid[ref][3][0])*len(grid[comp][0][1])+\
           len(grid[ref][3][1])*len(grid[comp][0][2])+\
           len(grid[ref][3][2])*len(grid[comp][0][3]) == 0:
            branch[ref][3] += [comp]
        if len(grid[ref][1][0])*len(grid[comp][0][3])+\
           len(grid[ref][2][0])*len(grid[comp][1][3])+\
           len(grid[ref][3][0])*len(grid[comp][2][3]) == 0:
            branch[ref][4] += [comp]
        if len(grid[ref][0][0])*len(grid[comp][2][2])+\
           len(grid[ref][0][1])*len(grid[comp][2][3])+\
           len(grid[ref][1][0])*len(grid[comp][3][2])+\
           len(grid[ref][1][1])*len(grid[comp][3][3]) == 0:
            branch[ref][5] += [comp]
#TODO remove self from branch list

class Tarr:
    compat = branch
    indexed = [0,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1]
    names = ["nor", "fig", "fly", "poi", "gro", "roc", "bug", "gho", "ste", "fir", "wat", "gra", "ele", "psy", "ice", "dra", "dar", "fai"]
    types = 18
    @staticmethod
    def printCompat():
        for i in range(len(Tarr.compat)):
            print(str(i) + ": " + Tarr.names[i])
            for j in range(len(Tarr.compat[i])):
                print("   " + str(j) + ": " + str(Tarr.compat[i][j]))
                names = "    "
                for k in range(len(Tarr.compat[i][j])):
                    names += " " + Tarr.names[Tarr.compat[i][j][k]]
                print(names)
    @staticmethod
    def inArray(hay,need):
        i = bisect.bisect_left(hay, need)
        if i != len(hay) and hay[i] == need:
            return True
        return False
    def __init__(self):
        self.pos = 0
        self.arr = [0]*Tarr.types
        self.arr[0] = -1
        self.base = [0]*Tarr.types
        self.occ = [0]*Tarr.types
        self.solution = False
    @classmethod
    def from_arr(cls,startArr,startPos):
        ret = cls()
        if len(startArr) < types:
            ret.arr = startArr + [0]*(types-len(startArr))
        elif len(startArr) > types:
            ret.arr = startArr[:types]
        else:
            ret.arr = startArr[:]
        ret.pos = startPos
        ret.base = [0]*Tarr.types
        ret.occ = [0]*Tarr.types
        for i in range(startPos):
            if Tarr.indexed[i]:
                ret.base[i] = Tarr.compat[ret.base[i-1]][1][ret.arr[i]]
            else:
                ret.base[i] = ret.arr[i]
            ret.occ[ret.base[i]] = 1
        return ret
    def printDebug(self):
        print("\npos: " + str(self.pos) + "\na: " + str(self.arr) + "\no: " + str(self.occ) + "\nb: " + str(self.base))
        Tarr.printNames(self.base)
    def print(self,label="",quality=16):
        if self.pos>quality or self.solution:
            cutoff = types if self.solution else self.pos
            print(label +"\n"+
                (Tarr.names[self.base[0]]  if cutoff >  0 else "") +" "+
                (Tarr.names[self.base[3]]  if cutoff >  3 else "") +" "+
                (Tarr.names[self.base[6]]  if cutoff >  6 else "") +" "+
                (Tarr.names[self.base[9]]  if cutoff >  9 else "") +" "+
                (Tarr.names[self.base[12]] if cutoff > 12 else "") +" "+
                (Tarr.names[self.base[15]] if cutoff > 15 else "") +"\n"+("*" if self.solution else str(self.pos)) +" "+
                (Tarr.names[self.base[2]]  if cutoff >  2 else "") +" "+
                (Tarr.names[self.base[5]]  if cutoff >  5 else "") +" "+
                (Tarr.names[self.base[8]]  if cutoff >  8 else "") +" "+
                (Tarr.names[self.base[11]] if cutoff > 11 else "") +" "+
                (Tarr.names[self.base[14]] if cutoff > 14 else "") +" "+
                (Tarr.names[self.base[17]] if cutoff > 17 else "") +"\n"+
                (Tarr.names[self.base[1]]  if cutoff >  1 else "") +" "+
                (Tarr.names[self.base[4]]  if cutoff >  4 else "") +" "+
                (Tarr.names[self.base[7]]  if cutoff >  7 else "") +" "+
                (Tarr.names[self.base[10]] if cutoff > 10 else "") +" "+
                (Tarr.names[self.base[13]] if cutoff > 13 else "") +" "+
                (Tarr.names[self.base[16]] if cutoff > 16 else "") +"\n")
    def isCompat(self,node,val):
        if node%3 == 1 and (val == 4 or val == 16 or val == 17):
            return False
        elif node%3 == 0 and (val == 12 or val == 13 or val == 15):
            return False
        elif node <= 1:
            return True
        elif node == 2:
            return self.inArray(Tarr.compat[self.base[0]][3],val)
        elif node%3 == 0:
            return self.inArray(Tarr.compat[self.base[node-3]][2],val)
        else:
            return self.inArray(Tarr.compat[self.base[node-3]][2],val) and self.inArray(Tarr.compat[self.base[node-2]][3],val)
    def inc(self):
        self.solution = False
        if Tarr.indexed[self.pos]:
            src = Tarr.compat[self.base[self.pos-1]][1]
            ix = self.arr[self.pos]+1
            while ix < len(src):
                if not self.occ[src[ix]] and self.isCompat(self.pos,src[ix]):
                    if self.pos < types-1:
                        self.arr[self.pos] = ix
                        self.base[self.pos] = src[ix]
                        self.occ[src[ix]] = 1
                        self.pos += 1
                        self.arr[self.pos] = -1
                    else:
                        self.arr[self.pos] = ix
                        self.base[self.pos] = src[ix]
                        self.solution = True
                    break
                ix += 1
            if ix == len(src):
                self.pos -= 1
                self.occ[self.base[self.pos]]=0
        else:
            cur = self.arr[self.pos]+1
            while cur < Tarr.types:
                if not self.occ[cur] and self.isCompat(self.pos,cur):
                    self.arr[self.pos] = cur
                    self.base[self.pos] = cur
                    self.occ[cur] = 1
                    self.pos += 1
                    self.arr[self.pos] = -1 #TODO solution check here too
                    break
                cur += 1
            if cur == Tarr.types:
                if self.pos > 0:
                    self.pos -= 1   
                    self.occ[self.base[self.pos]]=0
                else:
                    return False
        return True
#TODO: Order
#TODO: Immutable

Tarr.printCompat()
#arr1 = Tarr.from_arr([0, 1, 2, 5, 2, 7, 8, 16, 6, 3, 17, 11, 11, 8, -1, -1, -1, -1],14)
#arr1 = Tarr.from_arr([0, 7, 12, -1],3)
'''
arr1 = Tarr.from_arr([0, 7, 12,-1],3)
for i in range(2000000):
    arr1.inc()
    arr1.print(label = str(i),quality = 20)
arr1.print(label = "last",quality = 0)
print(str(arr1.arr)+","+str(arr1.pos))
'''