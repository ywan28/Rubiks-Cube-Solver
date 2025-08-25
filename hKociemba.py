import twophase.solver as sv
def cubeToString(cube):
    uSide = cube[0] + cube[1] + cube[2]
    rSide = cube[3][6:9] + cube[4][6:9] + cube[5][6:9]
    fSide = cube[3][3:6] + cube[4][3:6] + cube[5][3:6]
    dSide = cube[6] + cube[7] + cube[8]
    lSide = cube[3][:3] + cube[4][:3] + cube[5][:3]
    bSide = cube[3][9:12] + cube[4][9:12] + cube[5][9:12]
    return uSide + rSide + fSide + dSide + lSide + bSide
#SOLVED CUBE
'''
WWW
WWW
WWW
GGGRRRBBBOOO
GGGRRRBBBOOO
GGGRRRBBBOOO
YYY
YYY
YYY

One Turn Away:
WWW
WWW
WWW
RRRBBBOOOGGG
GGGRRRBBBOOO
GGGRRRBBBOOO
YYY
YYY
YYY

'''
solved = [
    '   UUU',
    '   UUU',
    '   UUU',
    'LLLFFFRRRBBB',
    'LLLFFFRRRBBB',
    'LLLFFFRRRBBB',
    '   DDD',
    '   DDD',
    '   DDD',
]

inputCube = []
for i in range(9):
    line = input()
    line = line.replace('W','U')
    line = line.replace('R', 'F')
    line = line.replace('G', 'L')
    line = line.replace('B', 'R')
    line = line.replace('O', 'B')
    line = line.replace('Y', 'D')
    inputCube.append(line)
inputString = cubeToString(inputCube)

solvedCube = 'UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB'
oneTurnAway = 'UUUUUUUUUFFFRRRRRRLLLFFFFFFDDDDDDDDDBBBLLLLLLRRRBBBBBB'
randomCube = 'DUUBULDBFRBFRRULLLBRDFFFBLURDBFDFDRFRULBLUFDURRBLBDUDL'
print(cubeToString(inputString))
print(sv.solve(inputString,0,1))