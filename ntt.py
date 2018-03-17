#Not this time!
#defend your komfort
#bartek banaś
#25.02.2018

from livewires import games
import random

games.init(screen_width=1200, screen_height=660, fps=60)

class Condom(games.Sprite):
    img=games.load_image("condom.bmp")
    delay=100
    def __init__(self,x,y):
        super(Condom,self).__init__(image=Condom.img,x=x,y=y)

        self.scoore=games.Text(value=0,
                                   color=(211,23,45),
                                   size=80,
                                   right=games.screen.width-65,
                                   top=30,
                                   is_collideable=False)
        games.screen.add(self.scoore)


    def update(self):
        self.x=games.mouse.x
        self.y=games.mouse.y
        Condom.delay-=1
        self.scoore_txt=games.screen.width-55
        if self.bottom>games.screen.height:
            self.bottom=games.screen.height
        if self.top<0:
            self.top=0
        if self.right>games.screen.width:
            self.right=games.screen.width
        if self.left<games.screen.width/2:
            self.left=games.screen.width/2
        if not Condom.delay:
            the_sperm=Sperm(x=0,y=random.randint(20,games.screen.height-20))
            games.screen.add(the_sperm)
            Condom.delay=random.randint(50,80)
        for catched in self.overlapping_sprites:
            catched.destr()
            self.scoore.value+=1
            
        
class Sperm(games.Sprite):
    img=games.load_image("spore.bmp")
    speed=3
    direct=(True,False)
    def __init__(self,x,y):
        super(Sperm,self).__init__(image=Sperm.img,x=x,y=y,)
        self.dire=random.choice(Sperm.direct)
        if self.dire:
            self.dy=-Sperm.speed
        else:
            self.dy=Sperm.speed

    def update(self):
        self.change_dy=random.randrange(200)
        if self.change_dy==0:
            self.dy=-self.dy
        self.dx=Sperm.speed
        if self.bottom > games.screen.height or self.top<0:
            self.dy=-self.dy
        if games.mouse.x - self.x<=15:
            self.dx+=2

    def destr(self):
        self.destroy()

    

def main():
    the_condom=Condom(x=1100,y=games.screen.height/2)
    games.screen.add(the_condom)
    games.mouse.is_visible=False
    games.screen.mainloop()


main()
