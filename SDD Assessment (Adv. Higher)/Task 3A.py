class balloon():
    def __init__(self,r,c):
        self.colour = c
        self.radius = r
    
    def getRadius():
        return self.radius
    
    def getColour():
        return self.colour
    


def testBalloon():
    
    b1 = balloon(4.0,"blue")   
    b2 = balloon(1.0,"purple")
    b3 = balloon(3.0,"yellow")
    
    displayData(b1)
    displayData(b2)
    displayData(b3)
    
def showBalloonData(d):
    print("The radius of the balloon is %d" %d.radius + ", and the colour is %s" %d.colour + ".")

testBalloon()