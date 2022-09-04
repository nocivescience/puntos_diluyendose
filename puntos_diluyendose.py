from manim import *
import itertools as it
class DilucionPoints(VMobject):
    CONFIG={
        'colors':[
            YELLOW,
            RED,
            GREEN,
            BLUE,
        ]
    }
    def __init__(self,**kwargs):
        VMobject.__init__(self,**kwargs)
        dots=self.add_dots()
        self.add(dots)
        self.add_invisible_circles()
    def add_dots(self):
        color=it.cycle(self.CONFIG['colors'])
        dots=self.dots=VGroup(*[
            Dot().set_color(next(color)) for _ in range(144)
        ]).arrange_in_grid(12,12,buff=.02)
        dots.set_height(3)
        dots.sort(lambda p:p[0])
        return dots
    def add_invisible_circles(self):
        circles=VGroup()
        for dot in self.dots:
            point=dot.get_center()
            radius=np.linalg.norm(point)
            circle=Circle(radius=radius)
            circle.fade(1)
            circle.rotate(angle_of_vector(point))
            circles.add(circle)
            self.add_updater_to_do(dot, circle)
        self.add(circles)
    def add_updater_to_do(self,dot,circle):
        dot.total_time=0
        radius=np.linalg.norm(dot.get_center())
        freq=.1+0.05*np.random.random()+.05/radius
        def  update(dot,dt):
            dot.total_time+=dt
            prop=(freq*dot.total_time)%1
            dot.move_to(circle.point_from_proportion(prop))
        dot.add_updater(update)
        return dot
class DilucionScene(Scene):
    def construct(self):
        points=DilucionPoints()
        self.add(points)
        self.wait(12)