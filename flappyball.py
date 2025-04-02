import pgzrun
TITLE="Flappy Ball"
WIDTH=500
HEIGHT=510
gravity=500 #pixel per second
class Ball():
    def __init__(self, x, y, vx, vy, clr, r):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.clr=clr
        self.r=r
    def draw(self):
        screen.draw.filled_circle((self.x,self.y), self.r, self.clr)

balls=[]
ball1=Ball(100,1,100,0,"blue",50)
ball2=Ball(120,40,120,0,"red",20)
ball3=Ball(32,54,90,0,"green",30)
ball4=Ball(45,70,67,0,"yellow",20)
ball5=Ball(20,90,67,0,"pink",20)

def draw():
    screen.clear()
    ball1.draw()
    ball2.draw()
def update(dt):
    initialyvelocity=ball1.vy
    print(ball1.y)
    ball1.vy+=gravity*dt
    ball1.y+=(initialyvelocity+ball1.vy)*0.5*dt
    if ball1.y > HEIGHT-ball1.r:
        ball1.y=HEIGHT-ball1.r
        ball1.vy=-ball1.vy*0.9
    initialvelocity1=ball2.vy
    print(ball2.y)
    ball2.vy+=gravity*dt
    ball2.y+=(initialvelocity1+ball2.vy)*0.5*dt
    if ball2.y > HEIGHT-ball2.r:
        ball2.y = HEIGHT-ball2.r
        ball2.vy=-ball2.vy*0.6

pgzrun.go()