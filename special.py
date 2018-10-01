# Special has a radius of 10 and will spawn Balls every 20 cycles.
# When the special is deleted, it will spawn an 10 balls.
# Specials have a speed of 4.
from prey import Prey
from ball import Ball
from hunter import Hunter
import model
class Special(Prey):
    spawn_rate = 50
    radius = 10
    def __init__(self,x,y):
        Prey.__init__(self,x,y,width=Special.radius*2,height=Special.radius*2,angle=0,speed=4)
        self.randomize_angle()
        self._x       = x
        self._y       = y
        self._color = '#9CFDFF'
        self.counter = 0
        
    def update(self):
        if self.counter == Special.spawn_rate:
            self.counter = 0 
            model.objects.add(Ball(self._x,self._y))
        self.counter += 1 
        self.move()
    
    



         
    def display(self,canvas):
       canvas.create_oval(self._x-Special.radius     , self._y-Special.radius,
                                self._x+Special.radius, self._y+Special.radius,
                                fill=self._color)
