from configuration import *

def show():
    options = [(800,400), (800,600)] #coordinates for coursor
    coursor_pos = 0 #index
    
    while True:
        for event in pygame.event.get():
            window_closed = to_finish(event)
            if window_closed:
                return False
            
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    coursor_pos -= 1
                    coursor_pos %= len(options)
                elif event.key == K_DOWN:
                    coursor_pos += 1
                    coursor_pos %= len(options)
                elif event.key == K_SPACE:
                    if coursor_pos == 0:
                        return True
                    else:
                        return False
        
        screen.fill((255,255,255))
        
        #background
        background = pygame.image.load("images/menu_background.jpg")
        pygame.transform.scale(background, (screen_width,screen_height))
        screen.blit(background, (0,0))
        
        #showing title
        style = pygame.font.SysFont("Arial", 70, bold = True)
        title = style.render("MEGAWARPS", True, (255,0,0)) # red
        screen.blit(title, (320, 200))
        
        #options
        style = pygame.font.SysFont("Arial", 60, bold = True)
        
        new_game = style.render("New  game", True, (255, 100, 0))
        screen.blit(new_game, (340,400))
        
        exit_opt = style.render("Exit", True, (255, 100, 0))
        screen.blit(exit_opt, (340,600))
        
        #coursor
        
        coursor = style.render("<--", True, (255,0,0))
        screen.blit(coursor, options[coursor_pos])
        
        pygame.display.update()
        clock.tick(15)
    
    return True
    
    
    
