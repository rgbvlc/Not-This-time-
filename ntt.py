#name=Not this time
#author=rgbvlc bartek.b133@wp.pl
#info=simple game in pygame, livewires
#           save your future!
#status=unfinished
#final version= ~ 2018
#todo= new graphisc, animations, main menu, levels, sound and music

from livewires import games
import random#,menu

games.init(screen_width=1200, screen_height=660, fps=60)

#the_menu=menu.Menu()
class Condom(games.Sprite):
    img=games.load_image("condom.bmp")
    delay=100
    speed=5
    def __init__(self,x,y):
        super(Condom,self).__init__(image=Condom.img,x=x,y=y)
        self.xy_pos=self.position
        print(self.xy_pos)
        self.scoore=games.Text(value=0,
                                   color=(211,23,45),
                                   size=80,
                                   right=games.screen.width-65,
                                   top=30,
                                   is_collideable=False)
        games.screen.add(self.scoore)


    def update(self):
        """self.x=games.mouse.x
        self.y=games.mouse.y"""
        if games.keyboard.is_pressed(games.K_UP):
            self.y-=Condom.speed
        if games.keyboard.is_pressed(games.K_DOWN):
            self.y+=Condom.speed
        if games.keyboard.is_pressed(games.K_LEFT):
            self.x-=Condom.speed
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.x+=Condom.speed
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
            the_sperm=Sperm(x=0,y=random.randint(20,games.screen.height-20),enemy_position=self.xy_pos[1])
            games.screen.add(the_sperm)
            Condom.delay=random.randint(50,80)
        for catched in self.overlapping_sprites:
            catched.destr()
           # the_menu.clear()
            """the_menu.set_title(text="siema",colors=(23,66,9),size=86,top=50,left=400)
            the_menu.set_bg("imag.bmp")
            the_menu.set_music("intro.wav")
            #the_menu.button(img="btt.bmp",place=(400,300))
            bbb=menu.Sprite("btt.bmp","quit",400,300)
            games.screen.add(bbb)"""
            self.scoore.value+=1
             
class Sperm(games.Sprite):
    ID="sperm"
    img=games.load_image("sperm.png")
    img2=games.load_image("sperm2.png")
    speed=3
    ang=1
    animate_delay=10
    direct=(True,False)
    images_list=(img,img2)
    def __init__(self,x,y,enemy_position):
        super(Sperm,self).__init__(image=Sperm.img,x=x,y=y)
        self.dire=random.choice(Sperm.direct)
        print(self.enemy_position)
        if self.dire:
            self.dy=-Sperm.speed
            Sperm.ang=-1
        else:
            self.dy=Sperm.speed
            Sperm.ang=1

    def update(self):
        Sperm.animate_delay-=1
        if Sperm.animate_delay==0:
            self.new_image=random.choice(Sperm.images_list)
            self.set_image(self.new_image)
            Sperm.animate_delay=10
        self.change_dy=random.randrange(100)
        if self.change_dy==0:
            self.dy=-self.dy
            Sperm.ang=-Sperm.ang
            if Sperm.ang<0:
                self.set_angle(20)
            else:
                self.set_angle(-20)
        self.dx=Sperm.speed
        if self.bottom > games.screen.height or self.top<0:
            self.dy=-self.dy
        if self.left>=games.screen.width:
            self.destr()
        self.condom_xposition(self.enemy_position)

    def condom_xposition(self,pos):
        if self.pos-self.x<=0:
            self.dx+=5
        if self.pos-self.x==30:
            self.dy*=(-1)
        
    
    def destr(self):
        self.destroy()

def main():
    bg=games.load_image("background.png")
    games.screen.background=bg
    the_condom=Condom(x=1100,y=games.screen.height/2)
    games.screen.add(the_condom)
    games.mouse.is_visible=False
    #games.screen.event_grab=True
    games.screen.mainloop()

main()
