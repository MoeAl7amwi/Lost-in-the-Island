import pygame, time, random ,Image,math,sys
from Background import LevelBackground
import Enemies
import Character


pygame.init()
screen = pygame.display.set_mode((1000,700))
screen_rect = screen.get_rect()
screen_height = screen.get_height()
screen_width = screen.get_width()


bg_img = pygame.image.load("bg.png")
bg_scale = pygame.transform.scale(bg_img, (1000,700))
bg_rect =bg_scale.get_rect()

invList = []
invAdded = pygame.font.Font('BlackNorth.ttf', 30)
inv = invAdded.render("Item added to inventory", True, (0,0,0))

bg_img = LevelBackground(screen.get_width,screen.get_height,"bgimg.jpg")
bg_img = LevelBackground(screen.get_width,screen.get_height,"bgimg.jpg")
font = pygame.font.Font('DangerNight.ttf', 70)
font1 = pygame.font.Font('DangerNight.ttf', 55)
ariel = pygame.font.Font('Ariel.ttf', 65)
ariel1 = pygame.font.Font('Ariel.ttf', 25)
ariel2 = pygame.font.Font('Ariel.ttf', 18)


plane = Image.image(850,630, "airplane.png", 90, 70)
gate = Image.image(317,485, "mysteriousGate.png", 55,55)
cave = Image.image(190, 550, "cave.png", 75, 105)
light = Image.image(715, 110, "mysteriousLight.png", 40, 40)
hole = Image.image(825, 350, "hole.png", 75,75)
apple = Image.image(228, 128, "apple.png", 60, 60)
mountain = Image.image(725, 35, "mountain.png", 90, 130)
house = Image.image(570, 265, "mysteriousHouse.png", 90,110)
boy = Image.image(325,550,"male.png", 200,200)
girl = Image.image(625, 550, "girl_char.png", 200,200)
water = Image.image(525, 0, "water.png", 60,60)
spear = Image.image(475, 0, "spear.png", 50,75)
knife = Image.image(500, 400, "knife.png", 60,60)

dragon2 = Enemies.Dragon(250,250,300)
dragon2.rect.x = 460
dragon2.rect.y = 10

finalBoss2 = Enemies.FinalBoss(130,130,500, "mysteriousMan.png")
magicBall2 = Enemies.MagicBall(10,50)
arrow2 = Character.Arrow(50, 30)
finalBoss2.rect.x = 415
finalBoss2.rect.y = 250


all_sprites = pygame.sprite.Group()
web_group = pygame.sprite.Group()
spider = Enemies.Spider(100, 50, all_sprites, web_group)
all_sprites.add(spider)



magicBall_group = pygame.sprite.Group()

arrow_group = pygame.sprite.Group()

Level1img = LevelBackground(screen.get_width,screen.get_height,"Level1.jpg")
Level2img = LevelBackground(screen.get_width, screen.get_height, "level2.png")
Level3img = LevelBackground(screen.get_width,screen.get_height,"Level3.png")
Level4img = LevelBackground(screen.get_width,screen.get_height,"Level4.png")
planeInside = LevelBackground(screen.get_width,screen.get_height,"planeInside.png")



fire_sprites = pygame.sprite.Group()

#intro animation
FPS = 60
clock = pygame.time.Clock()
plane_img = Image.image(100, 50, "plane1.png", 200,200)
plane_speed = 5
island_img = Image.image(850,525, "island.png", 200,200)
plane_speedx = 2
plane_speedy = -1
plane_x = 0
plane_y = 50
sky_img = LevelBackground(screen.get_width,screen.get_height, "sky.png")
def intro():
    global plane_x, plane_y
    
    # draw the background
    sky_img.draw(screen) # sky blue color
    
    # update and draw the plane
    plane_x += plane_speedx
    plane_y -= plane_speedy
    if plane_x > screen_width:
        # draw the crashed plane
        crashed_plane_image = pygame.image.load("crashed_plane.png")
        screen.blit(crashed_plane_image, (0, 200))
        # set the plane back to its starting position
        plane_x = 0
        plane_y = screen_height / 2

    screen.blit(plane_img.scale, (plane_x,plane_y))

    # draw the island
    screen.blit(island_img.scale, (island_img.rect))

    # update the display
    pygame.display.update()

    # set the FPS
    clock.tick(FPS)
Mchar = Character.girl("Alice",100,90, 650)
inventoryDisplayed = False

player_health = 100
rockLevelBlock = Image.image(660,360,"boulder.png",80,80)
bushLevelBlock = Image.image(480,250,"bush.png",60,60)
treeLevelBlock = Image.image(710,150,"tree.png",100,100)

level2Block = True
level3Block = True
level4Block = True

def start():
    screen.fill((0,0,0))
    welcome_text = font.render("Welcome to the Island", True, (255,255,255))
    choose_text = font1.render("Choose your character", True, ((255,255,255)) )
    startbg = LevelBackground(screen.get_width, screen.get_height, "startscreen.png")
    startbg.draw(screen)
    screen.blit(welcome_text, (250, 75))
    screen.blit(choose_text, (300, 350))
    screen.blit(boy.scale, boy.rect)
    screen.blit(girl.scale, girl.rect)
    pygame.display.flip()
    time.sleep(0.05)
    
def levelIntro(*description):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if spider.rect.collidepoint(event.pos):
                        spider_health -= 5
                    elif start1.rect.collidepoint(event.pos):
                        return "true"
            startbg = LevelBackground(screen.get_width, screen.get_height, "startscreen.png")
            startbg.draw(screen)
            start = ariel.render("Click start to begin the level", True , (255,255,255))
            desc = ariel2.render(description[0], True, (255,255,255))
            desc1 = ariel2.render(description[1], True, (255,255,255))
            desc2 =  ariel2.render(description[2], True, (255,255,255))
            start1 = Image.image(500, 550, "start.png", 150, 100)
            screen.blit(start, (140,100))
            screen.blit(desc, (200,300))
            screen.blit(desc1, (250,325))
            screen.blit(desc2, (325,350))
            screen.blit(start1.scale, start1.rect)

            pygame.display.flip()
            time.sleep(0.05)
def displayInventory():
        
        screen.fill((55, 80, 52))
        inventory = ariel.render("Inventory",True,(255,255,255))
        escape = ariel1.render("Press esc to exit Inventory", True, (255,255,255))
        inv_bg = LevelBackground(screen.get_width, screen.get_height, "loading.jpg")
        inventoryback = Image.image(650,400, "inventory.png",500,100)
        inventoryback1 = Image.image(650, 500, "inventory.png", 500,100)
        fist = Image.image(455,400, "fist.png",70,70)
        knife = Image.image(590,400, "knife.png",70,70)
        spear = Image.image(700,400, "spear.png",75,75)
        star = Image.image(825, 400, "star.png", 70,70)
        bow = Image.image(455,500, "bow.png",70,70)

        inv_bg.draw(screen)
        screen.blit(escape, (500,200))
        screen.blit(inventory, (550, 100) )
        Mchar_inv = pygame.transform.scale(Mchar.scale, (300,300))
        screen.blit(Mchar_inv, (30,200))
        screen.blit(inventoryback.scale,inventoryback.rect)
        screen.blit(inventoryback1.scale, inventoryback1.rect)
        screen.blit(fist.scale,fist.rect)
        for inv in invList:
            if inv == "knife":
                screen.blit(knife.scale,knife.rect)
            if inv == "spear":
                screen.blit(spear.scale, spear.rect)
            if inv == "star":
                screen.blit(star.scale, star.rect)
            if inv == "bow":
                screen.blit(bow.scale, bow.rect)

        pygame.display.flip()
        time.sleep(0.05)

def renderGameover():
    font = pygame.font.Font("DangerNight.ttf", 36)
    text = font.render("Game Over", True, (255, 255, 255))
    quit = font.render("Quit", True, (255, 255, 255))
    quit_rect = quit.get_rect(center = (200,screen.get_height()+150))
    con = font.render("Restart", True, (255, 255, 255))
    con_rect = con.get_rect(center = (screen.get_width()-200,screen.get_height()+150))



    text_rect = text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))
    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)
    screen.blit(con, con_rect)
    screen.blit(quit, quit_rect)

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if con_rect.collidepoint(pygame.mouse.get_pos()):
                    return " return"
                elif quit_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    return "quit"
    
            

def renderCharacter():
    scavenge = invAdded.render("Scavenge Plane", True, ((255,255,255)) )
    levelOne = invAdded.render("Level 1", True, ((255,255,255)) )
    levelTwo = invAdded.render("Level 2", True, ((255,255,255)) )
    levelThree = invAdded.render("Level 3", True, ((255,255,255)) )
    levelFour = invAdded.render("Level 4", True, ((255,255,255)) )
    screen.blit(bg_scale, bg_rect)
    Mchar.draw(screen)
    screen.blit(plane.scale, plane.rect)
    screen.blit(gate.scale, gate.rect)
    screen.blit(cave.scale, cave.rect)
    screen.blit(light.scale, light.rect)
    screen.blit(hole.scale, hole.rect)
    screen.blit(apple.scale, apple.rect)
    screen.blit(mountain.scale, mountain.rect)
    screen.blit(house.scale, house.rect)
    screen.blit(scavenge, (775,560))
    screen.blit(levelOne, (150,480))
    screen.blit(levelTwo, (825,310))
    screen.blit(levelThree, (690,35))
    screen.blit(levelFour, (570,240))
    if level2Block:
        screen.blit(rockLevelBlock.scale,rockLevelBlock.rect)
    if level3Block:
        screen.blit(treeLevelBlock.scale,treeLevelBlock.rect)
    if level4Block:
        screen.blit(bushLevelBlock.scale,bushLevelBlock.rect)
    pygame.display.flip()
    time.sleep(0.05)
spider_speed = 10
def renderlevel1():
    player_health = 80
    spider_health = 100
    shelter = Image.image(950, 50, "shelter.png", 160, 125)
    water = Image.image(525, 0, "water.png", 60,60)
    spear = Character.Spear(10, "spear.png")
    water_speed = 5
    spear_speed = 5
    again = Image.image(500, 650, "playagain.png", 300, 180)
    player_text = ariel1.render("Player Health", True, (255,255,255))
    spider_text = ariel1.render("Spider Health", True, (255,255,255))
    inv_text = ariel1.render("Items added to inventory", True, (255,255,255))
    knife = Image.image(Mchar.rect.x + Mchar.rect.width/2,Mchar.rect.y + Mchar.rect.height/2,"knife.png",20,20)
    Mchar.moveChar(500, 650)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if spider.rect.collidepoint(event.pos) and Mchar.rect.colliderect(spider.rect):
                    spider_health -= 5
            
        Level1img.draw(screen)
        Mchar.draw(screen)
        screen.blit(shelter.scale, shelter.rect)
        all_sprites.draw(screen)
        all_sprites.update(screen_height)
        pygame.draw.rect(screen, (255,0,0),(10,685,100*2,7.5))
        pygame.draw.rect(screen, (0,255,0), (10,685, player_health*2, 7.5))
        pygame.draw.rect(screen, (255,0,0),(10,35,100*2,7.5))
        pygame.draw.rect(screen, (0,255,0), (10,35, spider_health*2, 7.5))
        screen.blit(player_text, (28, 655) )
        screen.blit(spider_text, (28,10))
        charMove()
        if Mchar.rect.left < 0:
            Mchar.rect.left = 0
        elif Mchar.rect.right > screen.get_width():
            Mchar.rect.right = screen.get_width()
        if Mchar.rect.top < 0:
            Mchar.rect.top = 0
        elif Mchar.rect.bottom > screen.get_height() - 50:
            Mchar.rect.bottom = screen.get_height() - 50
        
    
        if Mchar.rect.y < 160:
            Mchar.rect.y = 160

        knife.rect.x = Mchar.rect.x + Mchar.rect.width/2
        knife.rect.y = Mchar.rect.y + Mchar.rect.height/2
        screen.blit(knife.scale,knife.rect)
        for web in web_group:
            if(Mchar.rect.colliderect(web.rect)):
                player_health-=5
                web_group.remove(web)
        
        if player_health <= 0:
            bg = LevelBackground(screen.get_width, screen.get_height, "gameover.jpg")
            bg.draw(screen)
            screen.blit(again.scale, again.rect)    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if again.rect.collidepoint(event.pos):
                    return "failed"
        if spider_health <= 0:
            for sprite in all_sprites:
                sprite.kill()
            water.rect.y += water_speed  
            spear.rect.y += spear_speed
            if spear.rect.y >= 125:  
                spear.rect.y = 125
            if water.rect.y >= 125:  
                water.rect.y = 125
            screen.blit(water.scale, water.rect)
            screen.blit(spear.scale, spear.rect)
        if Mchar.rect.colliderect(water.rect):
            invList.append("spear")
            screen.blit(inv_text, (500, 259))
            Mchar.inventory.add_weapon(spear)
            time.sleep(2)
            return "passed"
        
           

        pygame.display.flip()
        time.sleep(0.05)
all_sprites = pygame.sprite.Group()
spider = Enemies.Spider(100, 50, all_sprites, web_group)
all_sprites.add(spider)
    
def renderlevel2():
    all_sprites1=pygame.sprite.Group()
    slime_group = pygame.sprite.Group()
    centipede2 = Enemies.Centipede(100,50,all_sprites1,slime_group)
    all_sprites1.add(centipede2)
    player_health = 100
    centipede_health = 200
    aid = Image.image(525, 0, "aid.png", 60,60)
    bow = Character.Spear(5, "star.png")
    aid_speed = 5
    bow_speed = 5
    again = Image.image(500, 650, "playagain.png", 300, 180)
    player_text = ariel1.render("Player Health", True, (255,255,255))
    centipede_text = ariel1.render("Centipede Health", True, (255,255,255))
    inv_text = ariel1.render("Items added to inventory", True, (255,255,255))
    spear = Image.image(Mchar.rect.x + Mchar.rect.width/2,Mchar.rect.y + Mchar.rect.height/2,"spear.png",40,40)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Mchar.rect.colliderect(centipede2.rect):
                    centipede_health -= 5
                
        Level2img.draw(screen)
        Mchar.draw(screen)
        all_sprites1.draw(screen)
        all_sprites1.update(screen_height)
        pygame.draw.rect(screen, (255,0,0),(10,685,100*2,7.5))
        pygame.draw.rect(screen, (0,255,0), (10,685, player_health*2, 7.5))
        pygame.draw.rect(screen, (255,0,0),(10,35,200*2,7.5))
        pygame.draw.rect(screen, (0,255,0), (10,35, centipede_health*2, 7.5))
        screen.blit(player_text, (28, 655) )
        screen.blit(centipede_text, (28,10))
        charMove()

        if Mchar.rect.left < 0:
            Mchar.rect.left = 0
        elif Mchar.rect.right > screen.get_width():
            Mchar.rect.right = screen.get_width()
        if Mchar.rect.top < 0:
            Mchar.rect.top = 0
        elif Mchar.rect.bottom > screen.get_height() - 50:
            Mchar.rect.bottom = screen.get_height() - 50

        if Mchar.rect.y < 160:
            Mchar.rect.y = 160

        spear.rect.x = Mchar.rect.x + Mchar.rect.width/2
        spear.rect.y = Mchar.rect.y + Mchar.rect.height/2
        screen.blit(spear.scale,spear.rect)
        for slime in slime_group:
            if(Mchar.rect.colliderect(slime.rect)):
                player_health-=5
                slime_group.remove(slime)

        
        if player_health <= 0:
            bg = LevelBackground(screen.get_width, screen.get_height, "gameover.jpg")
            bg.draw(screen)
            again = Image.image(500, 650, "playagain.png", 300, 180)
            screen.blit(again.scale, again.rect)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if again.rect.collidepoint(event.pos):
                    return "failed"
        if centipede_health <= 0:
            for centipede in all_sprites1:
                centipede.kill()
            aid.rect.y += aid_speed  
            bow.rect.y += bow_speed
            if bow.rect.y >= 125:  
                bow.rect.y = 125
            if aid.rect.y >= 125:  
                aid.rect.y = 125
            screen.blit(aid.scale, aid.rect)
            screen.blit(bow.scale, bow.rect)
        if Mchar.rect.colliderect(aid.rect):
            invList.append("star")
            screen.blit(inv_text, (500, 259))
            Mchar.inventory.add_weapon(bow)
            time.sleep(2)
            return "passed"

        pygame.display.flip()
        time.sleep(0.05)


def renderlevel3():
  

    dragon2 = Enemies.Dragon(250,250,300)
    dragon2.rect.x = 460
    dragon2.rect.y = 10
  
    player_text = ariel1.render("Player Health", True, (255,255,255))
    spider_text = ariel1.render("Dragon Health", True, (255,255,255))

    fire_sprites = dragon2.create_fire_sprites(460,10,4)
    # Define initial velocity and direction for dragon2
    dragonspeed = 5
    dragondirection = math.pi / 4  # 45 degrees in radians
    velocity_x = dragonspeed * math.cos(dragondirection)
    velocity_y = dragonspeed * math.sin(dragondirection)
    Mchar.rect.x = screen_width - 100
    Mchar.rect.y = screen_height- 40

    loot = Image.image(screen.get_width()-200,50,"bow.png",30,30)
    
    firespeed = 5
    for fire in fire_sprites:
        firedirection = random.uniform(0, 2*math.pi)  # Random angle in radians
        firevelocity_x = firespeed * math.cos(firedirection)
        firevelocity_y = firespeed * math.sin(firedirection)
        fire.velocity = pygame.math.Vector2(firevelocity_x, firevelocity_y)

    last_attack_time = time.time()
    projectiles = pygame.sprite.Group()

    dragonfiretimer = time.time()
    again = Image.image(500, 650, "playagain.png", 300, 180)

    dragonAttackTimer = 0
    level3run =True
    click = True
    while level3run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and click:  # left mouse button
                    x, y = Mchar.rect.center  # get center of character
                    mx, my = pygame.mouse.get_pos()  # get mouse position
                    direction = pygame.math.Vector2(mx - x, my - y).normalize()  # calculate direction
                    projectile = Character.Projectile(x, y, 10)
                    projectile.direction = direction
                    projectiles.add(projectile)
                
        Level3img.draw(screen)
        Mchar.draw(screen)
        dragon2.update()
        dragon2.draw(screen)
        fire_sprites.draw(screen)
        charMove()
         

        pygame.draw.rect(screen, (255,0,0),(10,685,100,7.5))
        pygame.draw.rect(screen, (0,255,0), (10,685, Mchar.health, 7.5))
        pygame.draw.rect(screen, (255,0,0),(10,35,100*3,7.5))
        pygame.draw.rect(screen, (218,112,214), (10,35, dragon2.health, 7.5))
        screen.blit(player_text, (28, 655) )
        screen.blit(spider_text, (28,10))

        dragon2.rect.x += velocity_x
        dragon2.rect.y += velocity_y

        # Bounce dragon2 off the edges of the screen
        if dragon2.rect.x < 0 or dragon2.rect.x > screen_width - dragon2.rect.width:
            velocity_x = -velocity_x
        if dragon2.rect.y < 0 or dragon2.rect.y > screen_height - dragon2.rect.height:
            velocity_y = -velocity_y
        
        
        def moveFireSprites():
            firespeed = 5
            for fire in fire_sprites:
                firedirection = random.uniform(0, 2*math.pi)  # Random angle in radians
                firevelocity_x = firespeed * math.cos(firedirection)
                firevelocity_y = firespeed * math.sin(firedirection)
                fire.velocity = pygame.math.Vector2(firevelocity_x, firevelocity_y)

        for fire in fire_sprites:
                fire.rect.x += fire.velocity.x
                fire.rect.y += fire.velocity.y

                 # Bounce fire sprites off the edges of the screen
                if fire.rect.x <= 0 or fire.rect.x >= screen.get_width()- fire.rect.width:
                    fire.velocity.x = -fire.velocity.x 
                if fire.rect.y <= 0 or fire.rect.y >= screen.get_height()-fire.rect.height:
                    fire.velocity.y = -fire.velocity.y
                if Mchar.rect.colliderect(fire.rect):
                    fire_sprites.remove(fire)
                    fire.kill()
                    Mchar.health = Mchar.health - 5
                    print("Char health", Mchar.health)
                    
        if Mchar.rect.colliderect(dragon2.rect):
            if time.time() - last_attack_time >= 3:
                dragonAttackTimer = 0
                Mchar.health = Mchar.health - 10
                print("character health", Mchar.health)
                last_attack_time = time.time()
                
        
        if Mchar.health <= 0:
            click = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if again.rect.collidepoint(event.pos):
                    return "failed"
            bg = LevelBackground(screen.get_width(), screen.get_height(), "gameover.jpg")
            bg.draw(screen)
            screen.blit(again.scale, again.rect)
        
        if Mchar.rect.y <= 0:
            Mchar.rect.y += 50
        if Mchar.rect.x <= 0:
            Mchar.rect.x +=50
        if Mchar.rect.y >= screen.get_height():
            Mchar.rect.y -= 50
        if Mchar.rect.x >= screen.get_width():
            Mchar.rect.x -= 50
        if time.time()-dragonfiretimer >= 4:
            for i in range(2):
                sprite = Enemies.FireSprite(dragon2.rect.x,dragon2.rect.y)
                fire_sprites.add(sprite)
                moveFireSprites()
                dragonfiretimer = time.time()
        if dragon2.health <= 0:
            dragon2.rect.x = 1000
            dragon2.rect.y = 1000
            dragon2.remove()
            for fire in fire_sprites:
                fire.kill()
            loot = Image.image(570,80,"bow.png",100,100)
            screen.blit(loot.scale,loot.rect)
            if Mchar.rect.colliderect(loot.rect):
                invList.append("bow")
                return "passed"


        for projectile in projectiles:
            projectile.draw(screen)
            projectile.update()

            # check if projectile is off screen
            if not screen.get_rect().colliderect(projectile.rect):
                projectiles.remove(projectile)
                projectile.kill()

            # check for collision with dragon
            if projectile.rect.colliderect(dragon2.rect):
                damage = Mchar.selectedWeapon.damage
                dragon2.health -= 5
                projectiles.remove(projectile)
                projectile.kill()
                print("dragon hit!")
                if dragon2.health == 250:
                    for i in range(5):
                        sprite = Enemies.FireSprite(dragon2.rect.x,dragon2.rect.y)
                        fire_sprites.add(sprite)
                        moveFireSprites()
                if dragon2.health == 200:
                    for i in range(5):
                        sprite = Enemies.FireSprite(dragon2.rect.x,dragon2.rect.y)
                        fire_sprites.add(sprite)
                        moveFireSprites()
                if dragon2.health == 150:
                    for i in range(5):
                        sprite = Enemies.FireSprite(dragon2.rect.x,dragon2.rect.y)
                        fire_sprites.add(sprite)
                        moveFireSprites()
                if dragon2.health == 100:
                    for i in range(5):
                        sprite = Enemies.FireSprite(dragon2.rect.x,dragon2.rect.y)
                        fire_sprites.add(sprite)
                        moveFireSprites()
            
        pygame.display.flip()
        time.sleep(0.005)


def renderlevel4():
    player_health = 200
    boss_health = 130
    teleport_delay = 0  
    magic_ball_timer = 0
    magic_ball_delay = 1000 
    Mchar.rect.y = screen_height/2 - 10
    baby = Image.image(970, 50, "baby.png", 70, 70)
    again = Image.image(500, 650, "playagain.png", 300, 180)
    last_attack_time = 0
    
    while True:
        # Check if it's time to fire magic ball
        

       
        
        if magic_ball_timer <= 0:
            magicBall_group.add(finalBoss2.create_bullet())
            magic_ball_timer = magic_ball_delay 
        else:
            magic_ball_timer -= clock.tick(60)  


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN  and time.time() - last_attack_time >= 1:
                if event.key == pygame.K_SPACE:
                    arrow_group.add(Mchar.create_arrow())
                    last_attack_time = time.time()
               
        
            for arrow in arrow_group:
                if finalBoss2.rect.colliderect(arrow.rect):
                    boss_health -= 10
                    arrow.kill()
                  

        for magic_ball in magicBall_group:
            randTime = random.randint(5, 45)
            magic_ball.rect.x -= randTime
            if Mchar.rect.colliderect(magic_ball.rect):
                player_health -= 12
                magic_ball.kill()
            


        Level4img.draw(screen)
        Mchar.draw(screen)
        finalBoss2.draw(screen)
        screen.blit(baby.scale, baby.rect)

        player_text = ariel1.render("Player Health", True, (255,255,255))
        boss_text = ariel1.render("Boss Health", True, (255,255,255))
        pygame.draw.rect(screen, (255,0,0),(10,685,200*2,7.5))
        pygame.draw.rect(screen, (0,255,0), (10,685, player_health*2, 7.5))
        pygame.draw.rect(screen, (255,0,0),(10,35,130*2,7.5))
        pygame.draw.rect(screen, (0,255,0), (10,35, boss_health*2, 7.5))
        screen.blit(player_text, (28, 655))
        screen.blit(boss_text, (28,10))

    
        if boss_health <= 0:
            for magicBall in magicBall_group:
                magicBall.kill()
            final = LevelBackground(screen.get_width, screen.get_height, "final.jpg")
            final.draw(screen)
        else: 
            Mchar.rect.x = 15
            if teleport_delay <= 0:
                finalBoss2.teleport(screen.get_width()-130, screen.get_height()-130)
                teleport_delay = 550
            else:
                teleport_delay -= 50 
            

        if player_health <= 0:
            bg1 = LevelBackground(screen.get_width, screen.get_height, "gameover.jpg")
            bg1.draw(screen)
            screen.blit(again.scale, again.rect)
            for magicBall in magicBall_group:
                magicBall.kill()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if again.rect.collidepoint(event.pos):
                    return "failed"
        if Mchar.rect.colliderect(baby.rect):
            return "passed"
        
        
        if Mchar.rect.left < 0:
            Mchar.rect.left = 0
        elif Mchar.rect.right > screen.get_width():
            Mchar.rect.right = screen.get_width()
        if Mchar.rect.top < 60:
            Mchar.rect.top = 60
        elif Mchar.rect.bottom > screen.get_height() - 55:
            Mchar.rect.bottom = screen.get_height() - 55
        
        charMove()
        time.sleep(0.05)
        
      
        arrow_group.draw(screen)
        arrow_group.update()
        magicBall_group.draw(screen)
        magicBall_group.update()
        pygame.display.flip()
    

def scavangePlane():
    Mchar.charPosition(500, 650)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        planeInside.draw(screen)
        Mchar.draw(screen)
        screen.blit(knife.scale, knife.rect)
        charMove()
        time.sleep(0.05)
        pygame.display.flip()
        if Mchar.rect.colliderect(knife.rect):
            invList.append("knife")
            return "true"

def charMove():
    arrow = pygame.key.get_pressed()
    if arrow[pygame.K_a]:
        Mchar.moveChar(-char_speed,0) 
        flipped_image = pygame.transform.flip(Mchar.image, True, False) 
        Mchar.image = flipped_image
    elif arrow[pygame.K_d]:
        Mchar.moveChar(char_speed,0)
    elif arrow[pygame.K_w]:
        Mchar.moveChar(0, -char_speed)
    elif arrow[pygame.K_s]:        
        Mchar.moveChar(0,char_speed)
    if arrow[pygame.K_a] and arrow[pygame.K_w]:
        Mchar.moveChar(-char_speed/4,-char_speed/4) 
        flipped_image = pygame.transform.flip(Mchar.image, True, False) 
        Mchar.image = flipped_image
    if arrow[pygame.K_a] and arrow[pygame.K_s]:
        Mchar.moveChar(-char_speed/4,char_speed/4) 
    if arrow[pygame.K_d] and arrow[pygame.K_w]:
        Mchar.moveChar(char_speed/4,-char_speed/4)
    if arrow[pygame.K_d] and arrow[pygame.K_s]:
        Mchar.moveChar(char_speed/4, char_speed/4)

char_speed = 10
running = True
execute = False
starts = True
executegirl = False
in_battle = False
introd = True
levelCollide = True
Level1 = True
Level2 = True
Level3 = True
Level4 = True
collisions = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bound1 = pygame.Rect(295,345,315,90)
    bound2 = pygame.Rect(345, 475, 248, 110)
    bound3 = pygame.Rect(200, 580, 248, 50)
    bound4 = pygame.Rect(210, 265, 85, 265)
    bound5 = pygame.Rect(660, 390, 130, 70)
    bound6 = pygame.Rect(605, 150, 85, 200)
    bound7 = pygame.Rect(740, 80, 140, 250)
    bound8 = pygame.Rect(255, 155, 355, 55)
    bound9 = pygame.Rect(205, 35, 480, 80)
    bound10 = pygame.Rect(290, 275, 240, 70)
    bound11 = pygame.Rect(135, 120, 75, 145)

    if Mchar.rect.colliderect(bound1):
        Mchar.rect.y = 425
    elif Mchar.rect.colliderect(bound2):
        Mchar.rect.y = 425
    elif Mchar.rect.colliderect(bound3):
        Mchar.rect.y = 530
    elif Mchar.rect.colliderect(bound4):
        Mchar.rect.x = 295
    elif Mchar.rect.colliderect(bound5):
        Mchar.rect.x = 615
    elif Mchar.rect.colliderect(bound6):
        Mchar.rect.x = 690
    elif Mchar.rect.colliderect(bound7):
        Mchar.rect.x = 690
    elif Mchar.rect.colliderect(bound8):
        Mchar.rect.y = 100
    elif Mchar.rect.colliderect(bound9):
        Mchar.rect.y = 105
    elif Mchar.rect.colliderect(bound10):
        Mchar.rect.y = 205
    elif Mchar.rect.colliderect(bound11):
        Mchar.rect.x = 205
    if Mchar.rect.colliderect(rockLevelBlock.rect) and level2Block:
        Mchar.rect.x -= 15
        Mchar.rect.y +=15
        

    if Mchar.rect.colliderect(treeLevelBlock.rect) and level3Block:
        Mchar.rect.y += 15
    if Mchar.rect.colliderect(bushLevelBlock.rect) and level4Block:
        Mchar.rect.x -= 15

    if Mchar.rect.colliderect(apple.rect):
        apple.rect.y=10000 
        apple_text = invAdded.render("Health Boosted!", True, (255,255,255))
        start_time = pygame.time.get_ticks()
            # Display the image for 3 seconds
        while pygame.time.get_ticks() - start_time < 1000:
                screen.blit(apple_text, (25,50))
                pygame.display.flip()

    if Mchar.rect.colliderect(light.rect):
        light.rect.y = 10000
        light_text = invAdded.render("Speed Boosted!", True, (255,255,255))
        start_time = pygame.time.get_ticks()
            # Display the image for 3 seconds
        while pygame.time.get_ticks() - start_time < 1000:
                screen.blit(light_text, (25,50))
                pygame.display.flip()
    if Mchar.rect.colliderect(gate.rect):
        gate.rect.y = 10000
        gate_text = invAdded.render("Health Decreased!",True,(255,255,255))
        start_time = pygame.time.get_ticks()
            # Display the image for 3 seconds
        while pygame.time.get_ticks() - start_time < 1000:
                screen.blit(gate_text, (25,50))
                pygame.display.flip()

    charMove()
    arrow = pygame.key.get_pressed()
    if arrow[pygame.K_TAB]:
        displayInventory()
        starts = False
        execute = False
    elif arrow[pygame.K_ESCAPE]:
        execute = True
        starts = False
   
    if starts:
        start()
        if event.type== pygame.MOUSEBUTTONDOWN:
            if boy.rect.collidepoint(event.pos):
                Mchar = Character.boy("Joseph", 100, 780, 600)
                execute = True
                starts = False
            elif girl.rect.collidepoint(event.pos):
                Mchar = Character.girl("Alice",100, 780, 600)
                execute = True
                starts = False
    if execute:
        renderCharacter()
    if event.type== pygame.MOUSEBUTTONDOWN:
        if water.rect.collidepoint(event.pos):
            Level1 = False
            execute = True
    
    if Mchar.rect.colliderect(plane.rect):
        collisions = False
        execute = False
        Level1 = False
        Level2 = False
        Level3 = False
        level4 = False
        result = scavangePlane() 
        if result == "true":
            start_time = pygame.time.get_ticks()

            # Display the image for 3 seconds
            while pygame.time.get_ticks() - start_time < 1000:
                screen.blit(inv, (350, 100))
                pygame.display.flip()
            Mchar.charPosition(700, 360)
            Level1 = True
            execute = True
            Level2 = True
            Level3 = True
            Level4 = True
    if Mchar.rect.colliderect(cave.rect) and Level1:
        execute = False
        Level2 = False
        Level3 = False
        Level4 = False
        result = levelIntro("This is level 1, Defeat the giant Spider by avoiding its speed changing spider webs! " ,
        "Get close to the spider and use your mouse to click on it to deal damage ",
        "Defeat the Spider and claim your rewards")
        if result == "true":
            Mchar.charPosition(50 , 600)
            result1 = renderlevel1()
            if result1 ==  "passed":
                level2Block = False
                Mchar.charPosition(180, 525)
                Level1 = False
                execute = True
                Level2 = True
                Level3 = True
                Level4 = True
            elif result1 =="failed":
                starts = True
                Level1 = True
                Level2 = True
                Level3 = True
                Level4 = True

    if Mchar.rect.colliderect(hole.rect) and Level2:
        execute = False
        Level1 = False
        Level3 = False
        Level4 = False
        result = levelIntro("This is the 2nd level, the centipede is twice as strong and is able to move across the map! " ,
        "Use your spear to attack the centipede while avoiding his slime ",
        "Defeat the Centipede and receive items for your inventory")
        if result == "true":
            Mchar.charPosition(50 , 650)
            result2 = renderlevel2()
            if result2 ==  "passed":
                level3Block = False
                Mchar.charPosition(700, 360)
                Level1 = False
                execute = True
                Level2 = False
                Level3 = True
                Level4 = True
            elif result2 =="failed":
                starts = True
                Level1 = True
                Level2 = True
                Level3 = True
                Level4 = True
    if Mchar.rect.colliderect(house.rect) and Level4:
        execute = False
        Level1 = False
        Level2 = False
        Level3 = False
        result4 = levelIntro("This is the fourth and last level, Defeat the mysterious man by avoiding his magic balls and damagin him with your arrows" ,
        "Use the space bar to shoot the arrows. ",
        "Defeat the man and get your child back!")
        if result4 == "true":
            Mchar.charPosition(50 , 650)
            result4 = renderlevel4()
            if result4 ==  "passed":
                Mchar.charPosition(700, 360)
                Level1 = False
                execute = True
                Level2 = False
                Level3 = False
                Level4 = False
                level2Block = False
            elif result4 =="failed":
                starts = True
                Level1 = True
                Level2 = True
                Level3 = True
                Level4 = True
                
    if Mchar.rect.colliderect(hole.rect) and Level2:
        renderlevel2()
        execute = False
        Level1 = False
        Level3 = False
        Level4 = False
        
    if Mchar.rect.colliderect(mountain) and Level3:
        execute = False
        Level2 = False
        Level1 = False
        Level4 = False
        result = levelIntro("This is level 3, Defeat the dragon by avoiding its fireballs and its bites." ,
        "Use your mouse to click and shoot your slingshot at the dragon. ",
        "Defeat the dragon and claim your rewards")
        if result == "true":
            Mchar.charPosition(50 , 650)
            result1 = renderlevel3()
            if result1 ==  "passed":
                level4Block = False
                Mchar.charPosition(700, 360)
                Level3 = False
                execute = True
                Level1 = False
                Level2 = False
                Level4 = True
                level4Block = False
            elif result1 =="failed":
                starts = True
                Level1 = True
                Level2 = True
                Level3 = True
                Level4 = True
       
    if Mchar.rect.colliderect(house) and Level4:
        renderlevel4()
        execute = False
        in_battle = True
        Level1 = False
        Level2 = False
        Level3 = False

pygame.quit()