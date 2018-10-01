# Black_Hole is derived from Simulton: i.e., it updates by finding and removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey
import model


class Black_Hole(Simulton):
    radius = 10
    def __init__(self,x,y):
        Simulton.__init__(self,x,y, width = Black_Hole.radius*2, height = Black_Hole.radius*2)
        self._x       = x
        self._y       = y
        self._color = '#000000'
        
    def update(self):
        eaten = model.find(lambda s: isinstance(s,Prey) and self.contains(s.get_location()))
        for s in eaten:
            model.remove(s)
        return eaten
    
    def contains(self,xy):
        z = self.distance(xy)
        return z < self.get_dimension()[0]/2

        
                
        
    

         
    def display(self,canvas):
        z = self.get_dimension()
        canvas.create_oval(self._x-z[0]/2      , self._y-z[0]/2,
                                self._x+z[0]/2, self._y+z[0]/2,
                                fill=self._color)
