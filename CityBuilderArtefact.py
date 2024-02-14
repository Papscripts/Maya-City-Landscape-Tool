import maya.cmds as cmds
import random
from functools import partial

cmds.select( all=True )
cmds.delete()


def clearScene(*args):
    cmds.select( all=True )
    cmds.delete()

  
def closeWindow(*args):
    cmds.deleteUI(mywindow, window=True)
     
def createLandscape(*args):
    cmds.polyPlane( n = 'landscape', sx=1, sy=1, w=10, h=10)
   
def getSliderValue(ctrlName):
    value = cmds.intSlider(ctrlName, q=True, value=True)
    return value
     
def setSubdivisions(slider,*args,**kwargs):
    value = getSliderValue(slider) 
    print(value)
    cmds.setAttr ("polyPlane1.subdivisionsWidth", value)
    cmds.setAttr ("polyPlane1.subdivisionsHeight", value)
 
    
def setPlaneSize(slider,*args,**kwargs):
    value = getSliderValue(slider)
    print(value)
    cmds.setAttr ("polyPlane1.width", value)
    cmds.setAttr ("polyPlane1.height", value)

def makeBuildings(*args, **kwargs):
    checktime = cmds.date()
    print('Before faces:')
    print (checktime)
    faces = cmds.polyEvaluate( f=True )
    print(faces)
    checktime = cmds.date()
    print('After faces:')
    print (checktime)
    for i in range (0, faces):
        cmds.delete(ch=True)
        size1 = random.random()
        while size1 < 0.2:
            size1 = random.random()
        size2 = random.random()
        while size2 < 0.2:
            size2 = random.random()
        checktime = cmds.date()
        print (checktime)
        cmds.polyExtrudeFacet('landscape.f[%s]'% i, kft=False, ltz=0, ls=(size1, size2, 0) )
        checktime = cmds.date()
        print (checktime)
        chance = random.randint(0,100)
        BigB = cmds.textField(BigBuildingChance, query=True, text=True)
        int_BigB = int(BigB) 
        if chance < int_BigB:
            print(i)
            height = random.randint(7,10)
            print (height)
            chance = random.randint(0,2)
            if chance == 1:
                size = random.random()
                while size < 0.4:
                    size = random.random()
            else:
                size = 1
            checktime = cmds.date()
            print (checktime)
            cmds.polyExtrudeFacet('landscape.f[%s]'% i, kft=False, ltz=height, ls=(size, size, 0) )
            checktime = cmds.date()
            print (checktime)
            chance = random.randint(0,100)
            spire = cmds.textField(SpireChance, query=True, text=True)
            int_spire = int(spire)
            if chance < int_spire:
                checktime = cmds.date()
                print (checktime)
                cmds.polyExtrudeFacet('landscape.f[%s]'% i, kft=False, ltz=height/2, ls=(0, 0, 0) )
                checktime = cmds.date()
                print (checktime)
            else:
                checktime = cmds.date()
                print (checktime)
                cmds.polyExtrudeFacet('landscape.f[%s]'% i, kft=False, ltz=height/2, ls=(size, size, 0) )
                checktime = cmds.date()
                print (checktime)
        else:
            print(i)
            height = random.randint(1,2)
            print (height)
            size = 1
            checktime = cmds.date()
            print (checktime)
            cmds.polyExtrudeFacet('landscape.f[%s]'% i, kft=False, ltz=height, ls=(size, size, 0) )
            checktime = cmds.date()
            print (checktime)
            chance = random.randint(0,100)
            height = random.randint(1,2)
            House = cmds.textField(HouseChance, query=True, text=True)
            int_house = int(House)
            if chance < int_house:
                chance = random.randint(0,2)
                if chance == 1:
                    checktime = cmds.date()
                    print (checktime)
                    cmds.polyExtrudeFacet('landscape.f[%s]'% i, kft=False, ltz=height, ls=(size, size/2, 0) )
                    checktime = cmds.date()
                    print (checktime)
                else:
                    checktime = cmds.date()
                    print (checktime)
                    cmds.polyExtrudeFacet('landscape.f[%s]'% i, kft=False, ltz=height, ls=(size/2, size, 0) )
                    checktime = cmds.date()
                    print (checktime)
            else:
                checktime = cmds.date()
                print (checktime)
                cmds.polyExtrudeFacet('landscape.f[%s]'% i, kft=False, ltz=height, ls=(size, size, 0) )
                checktime = cmds.date()
                print (checktime)    
     
if cmds.window('mywindow', exists=True):
    cmds.deleteUI('mywindow')
    
mywindow = cmds.window('mywindow', title='City Builder',sizeable=True)
cmds.columnLayout()
cmds.text( label='Create a Plane to Build Your City on', align='center' )
cmds.button(label='Create Landscape', w=120, h=30, command=createLandscape)
cmds.text( label=' ', align='center' )
cmds.text( label='Number of Subdivisions', align='center' )
mySlider = cmds.intSlider(min=1, max=32, value=0, step=1, dc = 'empty')
cmds.intSlider(mySlider, e=True, dc = partial(setSubdivisions, mySlider, x=1))
cmds.text( label='Plane Size', align='center' )
mySlider = cmds.intSlider(min=1, max=100, value=0, step=1, dc = 'empty')
cmds.intSlider(mySlider, e=True, dc = partial(setPlaneSize, mySlider, x=1))
cmds.text( label=' ', align='center' )
cmds.text( label='----------------------------------------------', align='center' )
cmds.text( label=' ', align='center' )
cmds.text( label='Buildings:', align='center' )
cmds.text( label=' ', align='center' )

cmds.text( label='Chance of a Big Building (%)', align='center' )
BigBuildingChance = cmds.textField()
cmds.text( label=' ', align='center' )

cmds.text( label='Chance of a Big Building having a Spire (%)', align='center' )
SpireChance = cmds.textField()
cmds.text( label=' ', align='center' )

cmds.text( label='Chance of a Small Building being a House (%)', align='center' )
HouseChance = cmds.textField()
cmds.text( label=' ', align='center' )

cmds.textField( BigBuildingChance, edit=True,tx = '5')
cmds.textField( SpireChance, edit=True,tx = '50')
cmds.textField( HouseChance, edit=True,tx = '50')

cmds.button(label='Build Buildings', w=120, h=30, command=makeBuildings)
cmds.button(label='Clear Scene', w=120, h=30, command=clearScene, bgc=[1,0,0])
cmds.button(label='Exit', w=120, h=30, command=closeWindow)
cmds.showWindow(mywindow)


    