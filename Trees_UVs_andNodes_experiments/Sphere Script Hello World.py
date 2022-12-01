import maya.cmds as mc

def ball_party(value = 5):
    for i in range(value):
        sphereName = mc.polySphere(r = 1, sx = 20, sy = 20, ax = (0,1,0), cuv = 2, ch = False)
        print(sphereName[0])
        
ball_party(value =  15)

# def getR()