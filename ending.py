from configuration import *
import time

t1 = time.time()
t2 = t1 + 55
def death():
    global t1,t2
    
    if t2 - t1 > 47:
        pygame.mixer.music.load("music/dark-atmospheric.mp3")
        pygame.mixer.music.play()
        t1 = time.time()
    
    key_pressed = False
    
    while key_pressed == False:
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    key_pressed = True
                    break
    
        screen.fill((0,0,0)) #black background    
        
        style = pygame.font.SysFont("Arial", 30)
        
        text = style.render("Year 2091, aerial city of GAFAMpolis", True, (255,255,255))
        screen.blit(text, (300,20))
        
        text = style.render("Monarchy of GAFAM", True, (255,255,255))
        screen.blit(text, (320,70))
        
        style = pygame.font.SysFont("Arial", 20)
        
        text= style.render("A year since memorable events passed.", True, (255,255,255))
        screen.blit(text, (10,200))

        text= style.render("GAFAM found your limp body and used it to cow citizens.", True, (255,255,255))
        screen.blit(text, (10,230))

        text= style.render("Rebels still tried to fight, but with no advocacy from people, they gave up.", True, (255,255,255))
        screen.blit(text, (10,260))
        
        text= style.render("Now nothing could stop GAFAM.", True, (255,255,255))
        screen.blit(text, (10,290))
        
        text= style.render("Slavery, surveillance, violence - these are signs of our times.", True, (255,255,255))
        screen.blit(text, (10,310))
        
        text= style.render("A new era set in - Degradation of Human.", True, (255,255,255))
        screen.blit(text, (10,340))
        
        text = style.render("THE DEATH END", True, (255,255,255))
        screen.blit(text, (10, 380))
        
        text = style.render("Press SPACE to continue..." , True, (255,255,255))
        screen.blit(text, (0, 750))

        pygame.display.update()
        
        t2 = time.time()

def caught():
    
    global t1,t2
    
    if t2 - t1 > 44:
        pygame.mixer.music.load("music/rain-sounds-ambulance-siren-distant.mp3")
        pygame.mixer.music.play()
        t1 = time.time()
    
    key_pressed = False
    
    while key_pressed == False:
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                 if event.key == K_SPACE:
                    key_pressed = True
                    break
        screen.fill((0,0,0)) #black background    
        
        style = pygame.font.SysFont("Arial", 30)
        
        text = style.render("Year 2091, earth", True, (255,255,255))
        screen.blit(text, (300,20))
        
        style = pygame.font.SysFont("Arial", 20)
        
        text= style.render("A year since memorable events passed.", True, (255,255,255))
        screen.blit(text, (10,200))

        text= style.render("Unnamed rabble-rouser from Technopolis was sentenced to deportation to earth.", True, (255,255,255))
        screen.blit(text, (10,230))
        
        text= style.render("Thanks to some kind of miracle he didn't die like many do.", True, (255,255,255))
        screen.blit(text, (10,260))
        
        text= style.render("Instead his DNA mutated and he became Abomination.", True, (255,255,255))
        screen.blit(text, (10,290))
        
        text= style.render("But it was not GAFAM's win.", True, (255,255,255))
        screen.blit(text, (10,320))
        
        text = style.render("The Abomination became exemplar for citizens who started street fighting.", True, (255,255,255))
        screen.blit(text, (10, 350))
        
        text = style.render("The result is still unknown as GAFAM disconnected radio connection with other cities...", True, (255,255,255))
        screen.blit(text, (10, 380))
        
        text = style.render("THE CAUGHT END", True, (255,255,255))
        screen.blit(text, (10, 410))
        
        text = style.render("Press SPACE to continue..." , True, (255,255,255))
        screen.blit(text, (0, 750))

        pygame.display.update()
        
        t2 = time.time()


def good():
    
    global t1,t2
    
    if t2 - t1 > 51:
        pygame.mixer.music.load("music/positive-happy-background.mp3")
        pygame.mixer.music.play()
        t1 = time.time()
    
    key_pressed = False
    
    while key_pressed == False:
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    key_pressed = True
                    break
    
        screen.fill((0,0,0)) #black background    
        
        style = pygame.font.SysFont("Arial", 30)
        
        text = style.render("Year 2091, aerial city of Technopolis", True, (255,255,255))
        screen.blit(text, (300,20))
        
        text = style.render("District of free people", True, (255,255,255))
        screen.blit(text, (320,70))
        
        style = pygame.font.SysFont("Arial", 20)
        
        text= style.render("A year since memorable events passed.", True, (255,255,255))
        screen.blit(text, (10,200))

        text= style.render("Unnamed liberator released citizens from GAFAM's yoke.", True, (255,255,255))
        screen.blit(text, (10,230))
        
        text= style.render("The event later named The Great Liberation triggered strikes in other cities.", True, (255,255,255))
        screen.blit(text, (10,260))
        
        text= style.render("Companies were forced to evacuate themselves from cities.", True, (255,255,255))
        screen.blit(text, (10,290))
        
        text= style.render("A new era set in - Era of Freedom.", True, (255,255,255))
        screen.blit(text, (10,320))
        
        text = style.render("THE GOOD END", True, (255,255,255))
        screen.blit(text, (10, 350))
        
        text = style.render("Press SPACE to continue..." , True, (255,255,255))
        screen.blit(text, (0, 750))

        pygame.display.update()
        
        t2 = time.time()