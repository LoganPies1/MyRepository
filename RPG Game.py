from gamelib import*
import random
game=Game(800,800,"BunnyGame",1.4)

titlescreen=Image("logo2.png",game)
bg=Image("forest1.png",game)
game.setBackground(bg)
titlescreen.resizeTo(game.width,game.height)
bg.resizeTo(800,800)
house=Image("house.png",game)
house.moveTo(150,558)
house.resizeBy(-60)
sCoin=Animation("SecretCarrotCoin.png",6,game,937/6,156)
sCoin.moveTo(-700,550)
sCoin.resizeBy(-60)
titlescreen=Image("titlescreen.png",game)
bg=Image("forest1.png",game)
game.setBackground(bg)
titlescreen.resizeTo(game.width,game.height)
bg.resizeTo(800,800)
house=Image("house.png",game)
house.moveTo(150,558)
house.resizeBy(-60)
sCoin=Animation("SecretCarrotCoin.png",6,game,937/6,156)
sCoin.moveTo(-700,550)
sCoin.resizeBy(-60)
animationinc=Image("animationinc.png",game)
buny=Animation("bunnys.png",6,game,396/6,89)
buny.resizeBy(100)
buny.moveTo(400,300)
blackscreen=Image("blackscreen.jpg",game)
blackscreen.resizeTo(800,800)
f=Font(white,50,blue)
ff=Font(black,75)
firstscreen=Image("storyboard.png",game)
firstscreen.resizeTo(800,800)
end=Image("end.jpg",game)
endsong=Sound("endS.wav",2)
plasma=Image("plasmaball.png",game)
end.resizeTo(game.width,game.height)

#Player stuff
playerL=Animation("bunnyL.png",6,game,396/6,89)
playerR=Animation("bunnyR.png",6,game,395/6,88)
playerL.moveTo(200,550)
playerL.setSpeed(1,0)
playerR.moveTo(200,550)
playerR.setSpeed(1,0)
playerL.visible=False
playerR.visible=True

#Jumping stuff/variables
jumping=False
landed=False
factor=1
scrollx=(0)
px=(0)
house.health=100
lvl=1
eRemains=(lvl*5)+5+1



#music
song=Sound("snailhouse.wav",1)



game.over=False

p=[]
for index in range((lvl*5)+5+1):
    p.append(Animation("pL.png",1,game,73,65))
for index in range((lvl*5)+5+1):
    x=(scrollx+randint(1000,1500))
    y=656
    p[index].moveTo(x,y)
    p[index].setSpeed(3,90)

goon=[]
for index in range((lvl*5)+5+1):
    goon.append(Animation("GoonL.png",9,game,2400/3,1800/3))
for index in range((lvl*5)+5+1):
    goon[index].resizeBy(-75)
    goon[index].setSpeed(2,90)
    goon[index].moveTo(random.randint(1500,2500),653)

#loading screen
while not game.over:
    game.processInput()
    blackscreen.draw()
    buny.draw()
    animationinc.draw()
    game.drawText("Loading...",325,500,f)
    if game.time<1:
        game.over=True
    game.update(60)
    game.displayTime()
game.over=False

#TitleScreen
while not game.over:
    game.processInput()
    firstscreen.draw()
    titlescreen.draw()
    if keys.Pressed[K_p]:
        titlescreen.visible=False
    if keys.Pressed[K_SPACE]:
        game.over=True
    if keys.Pressed[K_o]:
        titlescreen.visible=True
    game.update(20)

game.over=False



#Game
while not game.over:
    game.processInput()
    bg.draw()
    game.scrollBackground("right",0)
    house.draw()
    playerR.draw()
    playerL.draw() 
    sCoin.draw()
    song.play()
    #Level/Enemy counter
    if eRemains==0 or eRemains<0:
        lvl+=1
        game.drawText("lvl:"+str(lvl),0,0)
        p[index].visible=True
        eRemains=(lvl*5)+5
        for index in range((lvl*5)+5+1):
            p.append(Animation("pL.png",1,game,73,65))
        for index in range((lvl*5)+5+1):
            x=(scrollx+randint(1000,1500))
            y=656
            p[index].moveTo(x,y)
            p[index].setSpeed(3,90)

    for index in range((lvl*5)+5+1):
        p[index].move()
        px+=5

    #PlayerMovement/Jump/Scrollx
    if playerR.y<650:
        landed=False
    else:
        landed=True
    if keys.Pressed[K_w] and landed and not jumping:
        jumping=True
    if jumping:
        playerL.y -=27*factor
        playerR.y -=27*factor
        factor*=.95
        landed = False
    if factor < .18:
            jumping = False
            factor = 1
    if not landed:
        playerL.y+=10
        playerR.y+=10
        
    if keys.Pressed[K_a]:
        game.scrollBackground("right",5)
        playerR.visible=False
        playerL.visible=True
        house.moveTo(scrollx+150,558)
        p[index].moveTo(scrollx+px+1000,650)
        p[index].visible=True
        sCoin.moveTo(scrollx-700,500)
        for index in range((lvl*5)+5+1):      
            p[index].draw()
            p[index].x+=5
        scrollx+=5
        playerL.draw()
        
    if keys.Pressed[K_d]:
        game.scrollBackground("left",5)
        playerL.visible=False
        playerR.visible=True
        house.moveTo(scrollx+150,558)
        p[index].moveTo(scrollx+px+1000,650)
        p[index].visible=True
        sCoin.moveTo(scrollx-700,500)
        for index in range((lvl*5)+5+1):
            p[index].draw()
            p[index].x-=5
        scrollx-=5
        playerR.draw()

        #Pancake Logic
    for index in range((lvl*5)+5+1):
        if p[index].collidedWith(house):
            house.health-=1
            p[index].moveTo(random.randint(2000,2500),656)
            p[index].draw()
            eRemains-=1
        if house.health==0:
            game.over=True
        if p[index].collidedWith(playerR,"rectangle"):
            p[index].moveTo(random.randint(2000,2500),656)
            eRemains-=1
            
        if p[index].collidedWith(playerL,"rectangle"):
            p[index].moveTo(random.randint(2000,2500),656)
            eRemains-=1
    game.drawText("House Health:"+str(house.health),house.x,house.y)
    game.drawText("Level:"+str(lvl),0,0)

    if house.health==0:
        game.over=True
    if house.health<0:
        game.over=True
    
            
    #game.drawText("scrollx:"+str(scrollx),playerR.x,playerR.y-30)
    #game.drawText("Ypos:"+str(playerR.y),playerR.x,playerR.y-40)
    #game.drawText("eRemains:"+str(eRemains),playerR.x,playerR.y-50)

        
        
    
        
    game.update(20)
game.over=False
while not game.over:
    game.processInput()
    endsong.play()
    end.draw()  
    game.drawText("game over",400,300,ff)
    game.drawText("you tried",410,600,ff)
    game.drawText("Press [SPACE] to Exit the game",20,700,f)
    if keys.Pressed[K_SPACE]:
        game.over=True
    
            
    game.update(30)
game.over=False
game.quit()    
