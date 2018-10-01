# Hunter is derived from the Mobile_Simulton/Pulsator classes: i.e., it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import model

class Hunter(Pulsator, Mobile_Simulton):
    dist = 200
    def __init__(self,x,y):
        Pulsator.__init__(self,x,y)
        Mobile_Simulton.__init__(self,x,y,width=self.get_dimension()[0],height=self.get_dimension()[1],angle=0,speed=5)
        self.randomize_angle()
    def update(self):
        eaten = Pulsator.update(self)
        s = model.find(lambda x: isinstance(x,Prey))
        for item in s:
            if self.distance((item._x,item._y)) <= Hunter.dist and item == min(s, key = lambda item: self.distance((item._x,item._y))):
                self.set_angle(atan2(item._y - self._y,item._x - self._x))
        self.move()
        return eaten