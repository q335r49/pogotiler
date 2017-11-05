import numpy
import bisect

TC = \
[[2, 2, 2, 2, 2, 1, 2, 0, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2],
 [3, 2, 1, 1, 2, 3, 1, 0, 3, 2, 2, 2, 2, 1, 3, 2, 3, 1],
 [2, 3, 2, 2, 2, 1, 3, 2, 1, 2, 2, 3, 1, 2, 2, 2, 2, 2],
 [2, 2, 2, 1, 1, 1, 2, 1, 0, 2, 2, 3, 2, 2, 2, 2, 2, 3],
 [2, 2, 0, 3, 2, 3, 1, 2, 3, 3, 2, 1, 3, 2, 2, 2, 2, 2],
 [2, 1, 3, 2, 1, 2, 3, 2, 1, 3, 2, 2, 2, 2, 3, 2, 2, 2],
 [2, 1, 1, 1, 2, 2, 2, 1, 1, 1, 2, 3, 2, 3, 2, 2, 3, 1],
 [0, 2, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 3, 2, 2, 1, 2],
 [2, 2, 2, 2, 2, 3, 2, 2, 1, 1, 1, 2, 1, 2, 3, 2, 2, 3],
 [2, 2, 2, 2, 2, 1, 3, 2, 3, 1, 1, 3, 2, 2, 3, 1, 2, 2],
 [2, 2, 2, 2, 3, 3, 2, 2, 2, 3, 1, 1, 2, 2, 2, 1, 2, 2],
 [2, 2, 1, 1, 3, 3, 1, 2, 1, 1, 3, 1, 2, 2, 2, 1, 2, 2],
 [2, 2, 3, 2, 0, 2, 2, 2, 2, 2, 3, 1, 1, 2, 2, 1, 2, 2],
 [2, 3, 2, 3, 2, 2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 0, 2],
 [2, 2, 3, 2, 3, 2, 2, 2, 1, 1, 1, 3, 2, 2, 1, 3, 2, 2],
 [2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 3, 2, 0],
 [2, 1, 2, 2, 2, 2, 2, 3, 2, 2, 2, 2, 2, 3, 2, 2, 1, 1],
 [2, 3, 2, 1, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 2, 3, 3, 2]]
types = 18
grid = [0]*types
grid_h = 4
grid_v = 4

for d in range(types):
    grid[d] = [[[] for i in range(grid_h)] for j in range(grid_v)]
    grid[d][2][2] = [20]
    for a in range(types):
        if TC[d][a] != 2 or TC[a][d] != 2:
            grid[d][TC[d][a]][TC[a][d]] += [a]

def printGrid(mat):
    block_size = 25
    blank = " "*block_size
    print("\n"+
          "0:"+" "*(block_size-2)+
          "1:"+" "*(block_size-2)+
          "2:"+" "*(block_size-2)+
          "3:"+" "*(block_size-2))
    for i in range(len(mat)):
        row = ""
        for j in range(len(mat[i])):
            if len(mat[i][j]) > 0:
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
    names = ["nor", "fig", "fly", "poi", "gro", "roc",
             "bug", "gho", "ste", "fir", "wat", "gra",
             "ele", "psy", "ice", "dra", "dar", "fai", "___"]
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
    def match(hay, need):
        i = bisect.bisect_left(hay, need)
        if i != len(hay) and hay[i] == need:
            return True
        return False
    def __init__(self):
        self.pos = 0
        self.arr = [Tarr.types] * Tarr.types
        self.ord = list(range(types))
        self.slots = len(self.ord)
        self.occ = [0] * Tarr.types
        self.overflow = False
    def startat(pos, arr, order):
        self.ord = order
        self.arr = arr
        self.slots = len(self.ord)
        self.pos = pos
        for i in range(self.pos):
            self.occ[self.arr[self.ord[self.pos]]] = 1
    def printDebug(self):
        print("\npos: " + str(self.pos) +
              "\narr: " + str(self.arr) +
              "\nocc: " + str(self.occ) +
              "\nimm: " + str(self.imm) +
              "\nord: " + str(self.ord))
    def print(self, label=""):
        print(label +"\n"+ \
              Tarr.names[self.arr[0]] + " "+
              Tarr.names[self.arr[3]] + " "+
              Tarr.names[self.arr[6]] + " "+
              Tarr.names[self.arr[9]] + " "+
              Tarr.names[self.arr[12]]+" "+
              Tarr.names[self.arr[15]]+"\n" + str(self.pos) + " " +
              Tarr.names[self.arr[2]] +" "+
              Tarr.names[self.arr[5]] +" "+
              Tarr.names[self.arr[8]] +" "+
              Tarr.names[self.arr[11]]+" "+
              Tarr.names[self.arr[14]]+" "+
              Tarr.names[self.arr[17]]+"\n" +
              Tarr.names[self.arr[1]] +" "+
              Tarr.names[self.arr[4]] +" "+
              Tarr.names[self.arr[7]] +" "+
              Tarr.names[self.arr[10]]+" "+
              Tarr.names[self.arr[13]]+" "+
              Tarr.names[self.arr[16]]+"\n")
    def fits(self, node, val):
        if node%3 == 1 and (val == 4 or val == 16 or val == 17):
            return False
        elif node%3 == 0 and (val == 12 or val == 13 or val == 15):
            return False
        elif node == 0:
            if (self.arr[3] == Tarr.types or self.match(self.compat[self.arr[3]][5], val)) and \
               (self.arr[2] == Tarr.types or self.match(self.compat[self.arr[2]][3], val)):
                return True
            return False
        elif node == 1:
            if (self.arr[2] == Tarr.types or self.match(self.compat[self.arr[2]][4], val)) and \
               (self.arr[4] == Tarr.types or self.match(self.compat[self.arr[4]][5], val)):
                return True
            return False
        elif node == 2:
            if (self.arr[0] == Tarr.types or self.match(self.compat[self.arr[0]][3], val)) and \
               (self.arr[3] == Tarr.types or self.match(self.compat[self.arr[3]][4], val)) and \
               (self.arr[5] == Tarr.types or self.match(self.compat[self.arr[5]][5], val)) and \
               (self.arr[4] == Tarr.types or self.match(self.compat[self.arr[4]][0], val)) and \
               (self.arr[1] == Tarr.types or self.match(self.compat[self.arr[1]][1], val)):
                return True
            return False
        elif node == 3:
            if (self.arr[6] == Tarr.types or self.match(self.compat[self.arr[6]][5], val)) and \
               (self.arr[5] == Tarr.types or self.match(self.compat[self.arr[5]][0], val)) and \
               (self.arr[2] == Tarr.types or self.match(self.compat[self.arr[2]][1], val)) and \
               (self.arr[0] == Tarr.types or self.match(self.compat[self.arr[0]][2], val)):
                return True
            return False
        elif node == 4:
            if (self.arr[2] == Tarr.types or self.match(self.compat[self.arr[2]][3], val)) and \
               (self.arr[5] == Tarr.types or self.match(self.compat[self.arr[5]][4], val)) and \
               (self.arr[7] == Tarr.types or self.match(self.compat[self.arr[7]][5], val)) and \
               (self.arr[1] == Tarr.types or self.match(self.compat[self.arr[1]][2], val)):
                return True
            return False
        elif node == 5:
            if (self.arr[3] == Tarr.types or self.match(self.compat[self.arr[3]][3], val)) and \
               (self.arr[6] == Tarr.types or self.match(self.compat[self.arr[6]][4], val)) and \
               (self.arr[8] == Tarr.types or self.match(self.compat[self.arr[8]][5], val)) and \
               (self.arr[7] == Tarr.types or self.match(self.compat[self.arr[7]][0], val)) and \
               (self.arr[4] == Tarr.types or self.match(self.compat[self.arr[4]][1], val)) and \
               (self.arr[2] == Tarr.types or self.match(self.compat[self.arr[2]][2], val)):
                return True
            return False
        elif node == 6:
            if (self.arr[9] == Tarr.types or self.match(self.compat[self.arr[9]][5], val)) and \
               (self.arr[8] == Tarr.types or self.match(self.compat[self.arr[8]][0], val)) and \
               (self.arr[5] == Tarr.types or self.match(self.compat[self.arr[5]][1], val)) and \
               (self.arr[3] == Tarr.types or self.match(self.compat[self.arr[3]][2], val)):
                return True
            return False
        elif node == 7:
            if (self.arr[5] == Tarr.types or self.match(self.compat[self.arr[5] ][3], val)) and \
               (self.arr[8] == Tarr.types or self.match(self.compat[self.arr[8] ][4], val)) and \
               (self.arr[10]== Tarr.types or self.match(self.compat[self.arr[10]][5], val)) and \
               (self.arr[4] == Tarr.types or self.match(self.compat[self.arr[4] ][2], val)):
                return True
            return False
        elif node == 8:
            if (self.arr[6] == Tarr.types or self.match(self.compat[self.arr[6] ][3], val)) and \
               (self.arr[9] == Tarr.types or self.match(self.compat[self.arr[9] ][4], val)) and \
               (self.arr[11]== Tarr.types or self.match(self.compat[self.arr[11]][5], val)) and \
               (self.arr[10]== Tarr.types or self.match(self.compat[self.arr[10]][0], val)) and \
               (self.arr[7] == Tarr.types or self.match(self.compat[self.arr[7] ][1], val)) and \
               (self.arr[5] == Tarr.types or self.match(self.compat[self.arr[5] ][2], val)):
                return True
            return False
        elif node == 9:
            if (self.arr[12]== Tarr.types or self.match(self.compat[self.arr[12]][5], val)) and \
               (self.arr[11]== Tarr.types or self.match(self.compat[self.arr[11]][0], val)) and \
               (self.arr[8] == Tarr.types or self.match(self.compat[self.arr[8] ][1], val)) and \
               (self.arr[6] == Tarr.types or self.match(self.compat[self.arr[6] ][2], val)):
                return True
            return False
        elif node == 10:
            if (self.arr[8] == Tarr.types or self.match(self.compat[self.arr[8] ][3], val)) and \
               (self.arr[11]== Tarr.types or self.match(self.compat[self.arr[11]][4], val)) and \
               (self.arr[13]== Tarr.types or self.match(self.compat[self.arr[13]][5], val)) and \
               (self.arr[7] == Tarr.types or self.match(self.compat[self.arr[7] ][2], val)):
                return True
            return False
        elif node == 11:
            if (self.arr[9] == Tarr.types or self.match(self.compat[self.arr[9 ]][3], val)) and \
               (self.arr[12]== Tarr.types or self.match(self.compat[self.arr[12]][4], val)) and \
               (self.arr[14]== Tarr.types or self.match(self.compat[self.arr[14]][5], val)) and \
               (self.arr[13]== Tarr.types or self.match(self.compat[self.arr[13]][0], val)) and \
               (self.arr[10]== Tarr.types or self.match(self.compat[self.arr[10]][1], val)) and \
               (self.arr[8] == Tarr.types or self.match(self.compat[self.arr[8 ]][2], val)):
                return True
            return False
        elif node == 12:
            if (self.arr[15]== Tarr.types or self.match(self.compat[self.arr[15]][5], val)) and \
               (self.arr[14]== Tarr.types or self.match(self.compat[self.arr[14]][0], val)) and \
               (self.arr[11]== Tarr.types or self.match(self.compat[self.arr[11]][1], val)) and \
               (self.arr[9] == Tarr.types or self.match(self.compat[self.arr[9] ][2], val)):
                return True
            return False
        elif node == 13:
            if (self.arr[11]== Tarr.types or self.match(self.compat[self.arr[11]][3], val)) and \
               (self.arr[14]== Tarr.types or self.match(self.compat[self.arr[14]][4], val)) and \
               (self.arr[16]== Tarr.types or self.match(self.compat[self.arr[16]][5], val)) and \
               (self.arr[10]== Tarr.types or self.match(self.compat[self.arr[10]][2], val)):
                return True
            return False
        elif node == 14:
            if (self.arr[12]== Tarr.types or self.match(self.compat[self.arr[12]][3], val)) and \
               (self.arr[15]== Tarr.types or self.match(self.compat[self.arr[15]][4], val)) and \
               (self.arr[17]== Tarr.types or self.match(self.compat[self.arr[17]][5], val)) and \
               (self.arr[16]== Tarr.types or self.match(self.compat[self.arr[16]][0], val)) and \
               (self.arr[13]== Tarr.types or self.match(self.compat[self.arr[13]][1], val)) and \
               (self.arr[11]== Tarr.types or self.match(self.compat[self.arr[11]][2], val)):
                return True
            return False
        elif node == 15:
            if (self.arr[17]== Tarr.types or self.match(self.compat[self.arr[17]][0], val)) and \
               (self.arr[14]== Tarr.types or self.match(self.compat[self.arr[14]][1], val)) and \
               (self.arr[12]== Tarr.types or self.match(self.compat[self.arr[12]][2], val)):
                return True
            return False
        elif node == 16:
            if (self.arr[14]== Tarr.types or self.match(self.compat[self.arr[14]][3], val)) and \
               (self.arr[17]== Tarr.types or self.match(self.compat[self.arr[17]][4], val)) and \
               (self.arr[13]== Tarr.types or self.match(self.compat[self.arr[13]][2], val)):
                return True
            return False
        elif node == 17:
            if (self.arr[15]== Tarr.types or self.match(self.compat[self.arr[15]][3], val)) and \
               (self.arr[16]== Tarr.types or self.match(self.compat[self.arr[16]][1], val)) and \
               (self.arr[14]== Tarr.types or self.match(self.compat[self.arr[14]][2], val)):
                return True
            return False
    def inc(self):
            if self.pos == self.slots:
                self.pos -= 1
            tile = self.arr[self.ord[self.pos]]
            if tile == self.types:
                tile = 0
            else:
                tile += 1
            while tile < self.types:
                if self.occ[tile] or not self.fits(self.pos,tile):
                    tile += 1
                else:
                    break
            if tile == self.types:
                if self.pos == 0:
                    self.overflow = True
                else:
                    self.pos -= 1
                    self.occ[self.arr[self.ord[self.pos]]] = 0
                return
            self.occ[tile] = 1
            self.arr[self.ord[self.pos]] = tile
            self.pos += 1
            if self.pos < self.slots:
                 self.arr[self.ord[self.pos]] = self.types

#Tarr.printCompat()
seq1 = Tarr()
for i in range(100):
    seq1.print()
    seq1.inc()
