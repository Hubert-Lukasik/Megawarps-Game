from configuration import *

def show():
    
    key_pressed = False
    
    while key_pressed == False:
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                key_pressed = True
                break
    
        screen.fill((0,0,0)) #black background    
        
        style = pygame.font.SysFont("Arial", 30)
        
        text = style.render("Year 2090, aerial city of Technopolis", True, (255,255,255))
        screen.blit(text, (300,20))
        
        text = style.render("District under GAFAM governance", True, (255,255,255))
        screen.blit(text, (320,70))
        
        style = pygame.font.SysFont("Arial", 20)
        
        text= style.render("Since 3rd technological war, humankind has moved out to aerial cities to finally experience peace.", True, (255,255,255))
        screen.blit(text, (7,200))

        text= style.render("The cities consist of many small pieces floating in the air.", True, (255,255,255))
        screen.blit(text, (7,230))
        
        text= style.render("To travel efficiently in the city, people built teleporters called warps.", True, (255,255,255))
        screen.blit(text, (7,260))
        
        text= style.render("The warps are under steady inspection conducted by the Engineers.", True, (255,255,255))
        screen.blit(text, (7,290))
        
        text= style.render("Originally only citizens were Engineeers.", True, (255,255,255))
        screen.blit(text, (7,320))
        
        text = style.render("Unfortunately, big companies brought cities under their spheres of control.", True, (255,255,255))
        screen.blit(text, (7, 350))
        
        text = style.render("Since then they have full control on warps which they eagerly use to compete with other enterprises", True, (255,255,255))
        screen.blit(text, (7, 380))
        
        text = style.render("or to simply irritate citizens. Normal people are clearly disadvanteged, but they have no choice - earth is too", True, (255,255,255))
        screen.blit(text, (7, 410))
        
        text = style.render("much polluted and irradiated to live there. But now everythig may change...", True, (255,255,255))
        screen.blit(text, (7, 440))
        
        text = style.render("Rebels to whom you belong came to know that today directions to where warps lead would be changed", True, (255,255,255))
        screen.blit(text, (7, 470))
        
        text = style.render("to cause chaos in communication. This may be a chance for you to get to The Core where warps are controlled.", True, (255,255,255))
        screen.blit(text, (7, 500))

        text = style.render("Normally the only warp there is located in impossibly well-guarded GAFAM's HQ.", True, (255,255,255))
        screen.blit(text, (7, 530))
        
        text = style.render("But knowing thoughtlessness and incompetence of the city Engineer, one of the warps will surely lead to The Core", True, (255,255,255))
        screen.blit(text, (5, 560))
        
        text = style.render("Also because of above mentioned reasons, warps can lead even to another dimensions!", True, (255,255,255))
        screen.blit(text, (7, 590))
        
        text = style.render("Rebels assigned YOU this dangerous task!", True, (255,255,255))
        screen.blit(text, (7, 620))
        
        text = style.render("Try get to The Core avoiding company's agents (they can see you if you are not further then 3 tiles from them)" , True, (255,255,255))
        screen.blit(text, (7, 650))
        
        text = style.render("and other dangers. You have one chance! Good luck!" , True, (255,255,255))
        screen.blit(text, (7, 680))
        
        
        text = style.render("Press any key to continue..." , True, (255,255,255))
        screen.blit(text, (7, 750))

        pygame.display.update()