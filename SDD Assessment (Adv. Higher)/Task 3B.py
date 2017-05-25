
class countdown():
        
    def keepCounting(self,CurCount):
        if CurCount <= 5:
            print("The dog has rounded up %s sheep" %CurCount )
            c.keepCounting(CurCount + 1)
        else:
            print("And then went home for tea!")

        
    def start(self,startingValue):
        c.keepCounting(startingValue)


c = countdown()

c.start(1)