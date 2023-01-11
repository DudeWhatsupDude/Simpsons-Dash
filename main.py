import pygame
from pygame import font
import sys
import player
import KillEffects
import math
import random
from particles import Particle 
pygame.init()

screen = pygame.display.set_mode((600,600))
font.init()
particlesin = []

Points = 0

background = pygame.image.load('Background(Fence&Sidewalk).png')
background = pygame.transform.scale(background, (600,600))

background2 = background

ScoreFont = font.Font('freesansbold.ttf', 32)
ScoreText = ScoreFont.render(f'Score:{Points}', True, (60,100,20))

ScoreTextRect = ScoreText.get_rect()
ScoreTextRect.center = (600 // 2, 50)

Player_image = pygame.image.load('Player(Homer).png')
Player_image = pygame.transform.scale(Player_image, (50,66))

Enemy = pygame.image.load('Obstacles(Flander(1Heart)).png')
Enemy = pygame.transform.scale(Enemy, (50,66))

ABE_ENEMY = pygame.image.load('Obstacles(Abe(2Heart).png')
ABE_ENEMY = pygame.transform.scale(ABE_ENEMY, (55,71))

Collectable = pygame.image.load('Collectables(Donut).png')
Collectable = pygame.transform.scale(Collectable, (30,30))

lives_heart = pygame.image.load('Heart.png')
lives_heart = pygame.transform.scale(lives_heart, (30,30))
lives_heart = pygame.transform.rotate(lives_heart, 45)

GameOverScreen = pygame.image.load('GAMEOVERSCREEN.png')
GameOverScreen = pygame.transform.scale(GameOverScreen, (600,600))

Powerup = pygame.image.load('PowerUp(DuffCan).png')
Powerup = pygame.transform.scale(Powerup, (30, 50))

Bart_Shield = pygame.image.load('Sheild(Bart).png')
Bart_Shield = pygame.transform.scale(Bart_Shield, (40, 80))

restart_button = pygame.image.load('RestartButton.png')
restart_button = pygame.transform.scale(restart_button, (50, 50))

endimg = pygame.image.load('PowerUp(DuffCan).png')
endimgframeone = pygame.transform.rotate(endimg, 5)
endimgframetwo = pygame.transform.rotate(endimg, 10)
endimgframethree = pygame.transform.rotate(endimg, 15)
endimgframefour = pygame.transform.rotate(endimg, 20)
endimgframefive = pygame.transform.rotate(endimg, 25)
endimgframesix = pygame.transform.rotate(endimg, 30)
endimgframeseven = pygame.transform.rotate(endimg, 35)
endimgframeeight = pygame.transform.rotate(endimg, 40)
endimgframenine = pygame.transform.rotate(endimg, 35)
endimgframeten = pygame.transform.rotate(endimg, 30)
endimgframeeleven = pygame.transform.rotate(endimg, 25)
endimgframetwelve = pygame.transform.rotate(endimg, 20)
endimgframethirteen = pygame.transform.rotate(endimg, 15)
endimgframefourteen = pygame.transform.rotate(endimg, 10)
endimgframefifteen = pygame.transform.rotate(endimg, 5)
endimgframesixteen = pygame.transform.rotate(endimg, 0)
endimgframeseventeen = pygame.transform.rotate(endimg, -5)
endimgframeeighteen = pygame.transform.rotate(endimg, -10)
endimgframenineteen = pygame.transform.rotate(endimg, -15)
endimgframetwenty = pygame.transform.rotate(endimg, -20)
endimgframetwentyone = pygame.transform.rotate(endimg, -25)
endimgframetwentytwo = pygame.transform.rotate(endimg, -30)
endimgframetwentythree = pygame.transform.rotate(endimg, -35)
endimgframetwentyfour = pygame.transform.rotate(endimg, -40)
endimgframetwentyfive = pygame.transform.rotate(endimg, -35)
endimgframetwentysix = pygame.transform.rotate(endimg, -30)
endimgframetwentyseven = pygame.transform.rotate(endimg, -25)
endimgframetwentyeight = pygame.transform.rotate(endimg, -20)
endimgframetwentynine = pygame.transform.rotate(endimg, -15)
endimgframethirty = pygame.transform.rotate(endimg, -10)
endimgframethirtyone = pygame.transform.rotate(endimg, -5)
endimgframethirtytwo = pygame.transform.rotate(endimg, 0)
CANDODAMAGE = True
invincibleTimer = 0
endingframeanim = [
  endimgframeone,
  endimgframetwo,
  endimgframethree,
  endimgframefour,
  endimgframefive,
  endimgframesix,
  endimgframeseven,
  endimgframeeight,
  endimgframenine,
  endimgframeten,
  endimgframeeleven,
  endimgframetwelve,
  endimgframethirteen,
  endimgframefourteen,
  endimgframefifteen,
  endimgframesixteen,
  endimgframeseventeen,
  endimgframeeighteen,
  endimgframenineteen,
  endimgframetwenty,
  endimgframetwentyone,
  endimgframetwentytwo,
  endimgframetwentythree,
  endimgframetwentyfour,
  endimgframetwentyfive,
  endimgframetwentysix,
  endimgframetwentyseven,
  endimgframetwentyeight,
  endimgframetwentynine,
  endimgframethirty,
  endimgframethirtyone,
  endimgframethirtytwo
]

KILLDONE = False

localPlayer = player.Player([50, 500], Player_image)

mainClock = pygame.time.Clock()

KILLEFFECTFRAME0 = pygame.image.load('NukePhotos/frame_00.png')
KILLEFFECTFRAME0 = pygame.transform.scale(KILLEFFECTFRAME0, (600,600))

KILLEFFECTFRAME1 = pygame.image.load('NukePhotos/frame_01.png')
KILLEFFECTFRAME1 = pygame.transform.scale(KILLEFFECTFRAME1, (600,600))

KILLEFFECTFRAME2 = pygame.image.load('NukePhotos/frame_02.png')
KILLEFFECTFRAME2 = pygame.transform.scale(KILLEFFECTFRAME2, (600,600))

KILLEFFECTFRAME3 = pygame.image.load('NukePhotos/frame_03.png')
KILLEFFECTFRAME3 = pygame.transform.scale(KILLEFFECTFRAME3, (600,600))

KILLEFFECTFRAME4 = pygame.image.load('NukePhotos/frame_04.png')
KILLEFFECTFRAME4 = pygame.transform.scale(KILLEFFECTFRAME4, (600,600))

KILLEFFECTFRAME5 = pygame.image.load('NukePhotos/frame_05.png')
KILLEFFECTFRAME5 = pygame.transform.scale(KILLEFFECTFRAME5, (600,600))

KILLEFFECTFRAME6 = pygame.image.load('NukePhotos/frame_06.png')
KILLEFFECTFRAME6 = pygame.transform.scale(KILLEFFECTFRAME6, (600,600))

KILLEFFECTFRAME7 = pygame.image.load('NukePhotos/frame_07.png')
KILLEFFECTFRAME7 = pygame.transform.scale(KILLEFFECTFRAME7, (600,600))

KILLEFFECTFRAME8 = pygame.image.load('NukePhotos/frame_08.png')
KILLEFFECTFRAME8 = pygame.transform.scale(KILLEFFECTFRAME8, (600,600))

KILLEFFECTFRAME9 = pygame.image.load('NukePhotos/frame_09.png')
KILLEFFECTFRAME9 = pygame.transform.scale(KILLEFFECTFRAME9, (600,600))

KILLEFFECTFRAME10 = pygame.image.load('NukePhotos/frame_10.png')
KILLEFFECTFRAME10 = pygame.transform.scale(KILLEFFECTFRAME10, (600,600))

KILLEFFECTFRAME11 = pygame.image.load('NukePhotos/frame_11.png')
KILLEFFECTFRAME11 = pygame.transform.scale(KILLEFFECTFRAME11, (600,600))

KILLEFFECTFRAME12 = pygame.image.load('NukePhotos/frame_12.png')
KILLEFFECTFRAME12 = pygame.transform.scale(KILLEFFECTFRAME12, (600,600))

KILLEFFECTFRAME13 = pygame.image.load('NukePhotos/frame_13.png')
KILLEFFECTFRAME13 = pygame.transform.scale(KILLEFFECTFRAME13, (600,600))

KILLEFFECTFRAME14 = pygame.image.load('NukePhotos/frame_14.png')
KILLEFFECTFRAME14 = pygame.transform.scale(KILLEFFECTFRAME14, (600,600))

KILLEFFECTFRAME15 = pygame.image.load('NukePhotos/frame_15.png')
KILLEFFECTFRAME15 = pygame.transform.scale(KILLEFFECTFRAME15, (600,600))

KILLEFFECTFRAME16 = pygame.image.load('NukePhotos/frame_16.png')
KILLEFFECTFRAME16 = pygame.transform.scale(KILLEFFECTFRAME16, (600,600))

KILLEFFECTFRAME17 = pygame.image.load('NukePhotos/frame_17.png')
KILLEFFECTFRAME17 = pygame.transform.scale(KILLEFFECTFRAME17, (600,600))

KILLEFFECTFRAME18 = pygame.image.load('NukePhotos/frame_18.png')
KILLEFFECTFRAME18 = pygame.transform.scale(KILLEFFECTFRAME18, (600,600))

KillEffect_frames = [KILLEFFECTFRAME0,
                    KILLEFFECTFRAME1,
                    KILLEFFECTFRAME2,
                    KILLEFFECTFRAME3,
                    KILLEFFECTFRAME4,
                    KILLEFFECTFRAME5,
                    KILLEFFECTFRAME6,
                    KILLEFFECTFRAME7,
                    KILLEFFECTFRAME8,
                    KILLEFFECTFRAME9,
                    KILLEFFECTFRAME10,
                    KILLEFFECTFRAME11,
                    KILLEFFECTFRAME12,
                    KILLEFFECTFRAME13,
                    KILLEFFECTFRAME14,
                    KILLEFFECTFRAME15,
                    KILLEFFECTFRAME16,
                    KILLEFFECTFRAME17,
                    KILLEFFECTFRAME18]

class LifeBar:
  def __init__(self, pos, graphic, lives=3):
    self.x = pos[0]
    self.y = pos[1]
    self.clones = lives
    self.myGraphic = graphic
    
  def loseLifes(self, life_lost):
    self.clones -= life_lost
    
  def render(self, display_surface):
    for clone in range(self.clones):
      display_surface.blit(self.myGraphic, (self.x + (clone * 40), self.y))
  def setLifes(self, l):
    self.clones = l


Restart_Button = restart_button
Restart_Button_Rect = Restart_Button.get_rect()

class Spike():
  def __init__(self, POS, extrainfo=None, doesKill=True, mygraphic=Collectable):
    self.x_pos = POS[0]
    self.y_pos = POS[1]
    self.graphics = mygraphic
    print(mygraphic)
    self.rect = self.graphics.get_rect()
    self.does_kill = doesKill
    self.show = True
    self.details = extrainfo
    self.INIT_x_pos = POS[0]
    self.INIT_y_pos = POS[1]
    self.INIT_graphics = mygraphic
    print(mygraphic)
    self.INIT_rect = self.graphics.get_rect()
    self.INIT_does_kill = doesKill
    self.INIT_show = True
    self.INIT_details = extrainfo
    
  def move(self,vel):
    self.x_pos += vel[0]
    self.y_pos += vel[1]
    
  def render(self, display_surface):
    self.rect.x = self.x_pos
    self.rect.y = self.y_pos
    if self.show:
      display_surface.blit(self.graphics, (self.x_pos, self.y_pos))

  def full_Reset(self):
    self.x_pos = self.INIT_x_pos
    self.y_pos = self.INIT_y_pos
    self.graphics = self.INIT_graphics
    self.rect = self.INIT_rect
    self.rect.x = self.x_pos
    self.rect.y = self.y_pos
    self.does_kill = self.INIT_does_kill
    self.show = self.INIT_show
    
class Button:
  def __init__(self, middle, xoff, yoff):
    self.middlex = middle[0]
    self.middley = middle[1]
    self.ishover = False
    self.x_offset = xoff
    self.y_offset = yoff

  def check_hover(self, mpos):
    if self.middlex - self.x_offset < mpos[0]:
      
      if self.middlex + self.x_offset > mpos[0]:
        #in rangex
        if self.middley + self.y_offset > mpos[1]:
          
          if self.middley - self.y_offset < mpos[1]:
            # in range y too.
            self.ishover = True
            return True
          else:
            
            self.ishover = False
            return False
        else:
          
          self.ishover = False
          return False
      else:
        
        self.ishover = False
        return False
    else:
      
      self.ishover = False
      return False

def genRandomLevel(Opts, lenopts):
  returnlist = []
  
  for i in range(lenopts):
    returnlist.append(Opts[random.randint(0, (len(Opts)-1))])
    
  return returnlist

Bart_ShieldRect = Bart_Shield.get_rect()
Bart_ShieldRect.x = 100
Bart_ShieldRect.y = localPlayer.y_pos

level = 1
gamemaps = [[Spike([700, 500],None,True, Enemy),
             Spike([350, 500],None,True, Enemy),
             Spike([500, 500],None, False, Collectable),
             Spike([350, 440],None, False, Collectable),
             Spike([1160, 420],None, False, Collectable),
             Spike([980, 500],None, True, Enemy),
             Spike([1530, 500],None, True, ABE_ENEMY),
             Spike([1530, 400],'Powerup', True, Powerup)]]

inGame_lifeBar = LifeBar([10,10], lives_heart, 5)
#gamemaps = [[genRandomLevel([[Spike([700, 500],True, Enemy),
#             Spike([350, 500],True, Enemy),
#             Spike([500, 500], False, Collectable),
#             Spike([350, 440], False, Collectable),],
#             [Spike([500, 500], False, Collectable),
#             Spike([350, 440], False, Collectable)]])]]

tickertickticktick = 0

speed = 4

for i in range(100):
  tickertickticktick += 1

  gamemaps[level-1].append(Spike([(tickertickticktick * 300) + random.randint(-50, 50) + 1600, 500],None, True, Enemy))
  if random.randint(0,2) == 1:
    gamemaps[level-1].append(Spike([(tickertickticktick * 300) + random.randint(-50, 50) + 1600 + 100, 450],None, False, Collectable))

def RESTARTPLAY(INGAME):
  print('initRestart')
  for LEVEL in INGAME:
    for OBJECT in LEVEL:
      OBJECT.full_Reset()
  inGame_lifeBar.setLifes(5)

class CustomizeAbleBar:
  def __init__(self, pos, out, color):
    self.x = pos[0]
    self.y = pos[1]
    self.out_x = out[0]
    self.out_y = out[1]
    self.color = color
  def _timegone(self):
    self.out_x -= 1

  def _timeleft(self, tl):
    self.out_x = tl
    
  def render(self, display_surface):
   # pygame.draw.rect(display_surface, (0,0,255), pygame.Rect(self.x-5, self.y-5, 210, self.out_y+5))
    pygame.draw.rect(display_surface, (255,0,0), pygame.Rect(self.x, self.y, 200, self.out_y))
    pygame.draw.rect(display_surface, self.color, pygame.Rect(self.x, self.y, self.out_x, self.out_y))
    
isButtonUp = False

DuffBar = CustomizeAbleBar([400, 15], [200, 25], (0, 255, 0))

pygame.mixer.music.load('BackgroundMusic.mp3')
pygame.mixer.music.play(-1)

bgmovement = 0
bg1add = 0
timesthrough = 0
start = False
PlayButton = Button([300,300], 60, 20)
PlayButtonRect = pygame.Rect(PlayButton.middlex-PlayButton.x_offset,PlayButton.middley-PlayButton.y_offset, PlayButton.x_offset*2, PlayButton.y_offset*2)
txxtfont = pygame.font.Font('freesansbold.ttf', 32)
txxt = txxtfont.render('Play', True, (255,255,255))
txxtRect = txxt.get_rect()
txxtRect.center = (PlayButtonRect.center[0],PlayButtonRect.center[1])

particles = []
particlecolors = [(255, 0, 0), (255,215,0), (255,69,0), (22,22,22), (0,255,30), (0,30,255)]

while not start:
  screen.fill((0,0,0))
  
  mx,my = pygame.mouse.get_pos()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
      isMouse = PlayButton.check_hover([mx,my])
      if isMouse:
        start = True
  for x in range(random.randint(2, 5)):
    particle = Particle(300, 300, random.randint(-20,20)/5, random.randint(-10, 10), random.randint(3, 5), random.choice(particlecolors),0)
  particles.append(particle)
  for particle in particles:
    particle.render(screen)
    if particle.radius <= 0:
      particles.remove(particle)
  
  pygame.draw.rect(screen, (21,71,52), PlayButtonRect)
  screen.blit(txxt,txxtRect)
  pygame.display.flip()
  
  
while True:
  bgmovement -= 4
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
      
    if event.type == pygame.KEYDOWN:
        
      if event.key == pygame.K_w:
          
        isButtonUp = True
          
      if event.key == pygame.K_UP:
          
        isButtonUp = True

      if event.key == pygame.K_SPACE:
        isButtonUp = True
        
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_w:
        isButtonUp = False
        
      if event.key == pygame.K_UP:
        isButtonUp = False
          
      if event.key == pygame.K_SPACE:
        isButtonUp = False

    if event.type == pygame.MOUSEBUTTONDOWN:
      isButtonUp = True
        
    if event.type == pygame.MOUSEBUTTONUP:
      isButtonUp = False
  if localPlayer.Alive:
    
    screen.fill((0,0,120))
    screen.blit(background, (0, 0))
    try:
      if bgmovement / timesthrough <= -600:
        
        bg1add += 600
        if timesthrough == 0:
          timesthrough += 1
        else:
          timesthrough += 1
        print(timesthrough)
        
    except:
      if bgmovement <= -600:
        bg1add += 600
        if timesthrough == 0:
          timesthrough += 1
        else:
          
          timesthrough += 1
        
    
          
    ticker = 0
    
    for part in gamemaps[level - 1]:
      part.render(screen)
      part.x_pos -= math.floor(speed)
      
      if part.does_kill:
        if part.show:
          if CANDODAMAGE:
            if part.rect.colliderect(localPlayer.rect):
              if part.graphics == ABE_ENEMY:
                if CANDODAMAGE:
                  inGame_lifeBar.loseLifes(2)
                  part.show = False
                else:
                  part.show = False
                
              if part.graphics == Enemy:
                if CANDODAMAGE:
                  inGame_lifeBar.loseLifes(1)
                  part.show = False
                else:
                  part.show = False
          else:
            if part.rect.colliderect(Bart_ShieldRect):
              part.show = False
            
            ticker = 0
          
      else:
        if part.rect.colliderect(localPlayer.rect):
          if part.show and part.details == None:
            Points += 10
            part.show = False
      if part.rect.colliderect(localPlayer.rect):
        if part.show and part.details == 'Powerup':
          CANDODAMAGE = False
          part.show = False
          DuffBar._timeleft(200)
          invincibleTimer = 200
    
    if inGame_lifeBar.clones <= 0:
      localPlayer.Alive = False
      pygame.mixer.music.load('ExplosionSound.mp3')
      pygame.mixer.music.play(1)

    localPlayer.render(screen)
    localPlayer.Apply_phisics(isButtonUp)
    
    ticker += 1
    
    Points += 0.02
    
    ScoreFont = font.Font('freesansbold.ttf', 32)
    ScoreText = ScoreFont.render(f'Score: {math.floor(Points)}', True, (60,100,20))
    
    ScoreTextRect = ScoreText.get_rect()
    ScoreTextRect.center = (600 // 2, 50)
    
    screen.blit(ScoreText, ScoreTextRect)

    if not CANDODAMAGE:

      Bart_ShieldRect = Bart_Shield.get_rect()
      
      Bart_ShieldRect.x = 100
      Bart_ShieldRect.y = localPlayer.y_pos
      
      screen.blit(Bart_Shield, (100,localPlayer.y_pos))
      
      invincibleTimer -= 1

      DuffBar._timegone()

      DuffBar.render(screen)

      screen.blit(Powerup, (490, 5))
      
    if invincibleTimer <= 0:
      CANDODAMAGE = True
    
    screen.blit(restart_button, (550,550))
    mx,my = pygame.mouse.get_pos()
    Restart_Button_Rect.x, Restart_Button_Rect.y = 550, 550
    
    if Restart_Button_Rect.collidepoint(mx, my):
      if isButtonUp:
        RESTARTPLAY(gamemaps)
        pygame.mixer.music.load('BackgroundMusic.mp3')
        pygame.mixer.music.play(-1)
      
  else:
    try:
      if not KILLDONE:
        KillEffects._play(KillEffect_frames[math.floor(ticker / 8)], screen, [0,0])
        ticker += 1
    except:
      KILLDONE = True
    if len(KillEffect_frames) < math.floor(ticker / 8):
      KILLDONE = True
    if math.floor((ticker - 20) / 6) > len(KillEffect_frames):
      screen.fill((60,60,120))
      KILLDONE = True

  if KILLDONE:
    f = open('highscore.txt', 'r')
    c_highscore = f.read()
    f.close()
    
    if Points > math.floor(int(c_highscore)):
      f = open('highscore.txt', 'a')
      f.truncate(0)
      f.close()
      f = open('highscore.txt','w')
      f.write(str(math.floor(int(Points))))
      f.close()
      c_highscore = math.floor(Points)
    screen.blit(GameOverScreen,(0,0))
    LoseFont = font.Font('freesansbold.ttf', 32)
    LoseText = LoseFont.render(f'Game over. Score: {math.floor(Points)}', True, (60,100,20))
    LosePercentangeText = LoseFont.render(f'highscore: {c_highscore}', True, (60,100,20))
    
    LoseTextRect = LoseText.get_rect()
    LosePercentangeTextRect = LosePercentangeText.get_rect()
    LosePercentangeTextRect.center = (600 // 2, 100)
    
    LoseTextRect.center = (600 // 2, 50)
    screen.blit(LosePercentangeText, LosePercentangeTextRect)
    screen.blit(LoseText, LoseTextRect)
    #particlesin.append(particles.Particle((localPlayer.x_pos,localPlayer.y_pos), (3456,110), (0,0), [3,0]))
    mx,my = pygame.mouse.get_pos()
    Restart_Button_Rect.x, Restart_Button_Rect.y = 550, 550
    screen.blit(Restart_Button, (550,550))
    if Restart_Button_Rect.collidepoint(mx, my):
      if isButtonUp:
        RESTARTPLAY(gamemaps)
        localPlayer.Alive = True
        KILLDONE = False
        speed = 4
        pygame.mixer.music.load('BackgroundMusic.mp3')
        pygame.mixer.music.play(-1)
    
  mainClock.tick(100)

  inGame_lifeBar.render(screen)
  
  for particle in particlesin:
    particle.render(screen)
    particle.Phisics()

  speed += 0.001
  
  pygame.display.flip()
