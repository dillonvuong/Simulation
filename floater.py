# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
import random


class Floater(Prey): 
    radius = 5 # used in this class only; never changes
    def __init__(self,x,y):
        Prey.__init__(self,x,y,width=Floater.radius*2,height=Floater.radius*2,angle=0,speed=5)
        self.randomize_angle()
        self._x       = x
        self._y       = y
        self._image = PhotoImage(file='ufo.gif')

    
    def update(self):
        x = random.random()
        if x < 0.3:
            rand_speed = random.uniform(-.5,.5)
            rand_angle = random.uniform(-.5,.5)
            a = self._speed + rand_speed
            if a > 7:
                a = 7
            elif a < 3:
                a = 3
            b = self._angle + rand_angle
            self.set_velocity(a,b)   
        self.move()
        

         
    def display(self,the_canvas):
        the_canvas.create_image(*self.get_location(),image=self._image)
