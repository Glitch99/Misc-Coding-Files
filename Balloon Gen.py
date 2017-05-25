## Outcome Three ##


class Balloon(object):
    
    def __init__(self,radius,colour):
        
        self.radius = float(radius)
        self.colour = str(colour)
        
    def getRadius(self):
        return self.radius
    
    def getColour(self):
        return self.colour 
    
    def __str__ (self):
        return "The balloon has a radius of %s, and it is %s. " % (self.radius,self.colour)
    
class testBalloon(Balloon):
    
    def __init__(self, radius, colour):
        Balloon.__init__(self,radius,colour)
        
        
        
b1 = testBalloon("4.0", "Blue")
b2 = testBalloon("1.0", "Purple")
b3 = testBalloon("3.0","Yellow")        

print("For balloon b1 :",b1)
print("For balloon b2 :",b2)
print("For balloon b3 :",b3)