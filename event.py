import pygame
pygame.init()
screen=pygame.display.set_mode((500,500))
screen.fill("white")
class Circle():
    def __init__(self, pos, clr, r, w):
        self.pos=pos
        self.clr=clr
        self.r=r
        self.w=w
    def draw(self):
        self.cir=pygame.draw.circle(screen,self.clr, self.pos, self.r,self.w)
    def grow(self, w):
        self.r+=w
        self.cir=pygame.draw.circle(screen,self.clr, self.pos, self.r,self.w)
circle1=Circle((80,100),"pink",50,5)
while True:
    for e in pygame.event.get():
        if e.type==pygame.MOUSEBUTTONDOWN:
            print("mouseclick")
            circle1.draw()
            pygame.display.update()
        elif e.type==pygame.MOUSEBUTTONUP:
            print("mouserelease")
            circle1.grow(5)
            pygame.display.update()
        elif e.type==pygame.MOUSEMOTION:
            print("mousemotion")
            c=Circle(pygame.mouse.get_pos(), "lightblue", 5,5)
            c.draw()
            pygame.display.update()
