from configuration import *
import player
import menu
import intro
import game_map
import agents
import time

user_chose_new_game = menu.show()

if user_chose_new_game == True:
    
    #show intro
    intro.show()
    
    #prepare game map
    game_map.prepare_game_map()
    
    #starting positions
    player_x = 50
    player_y = 600
    
    #first map
    act_map = "Rebels'_HQ.txt"
    
    
    is_running = True
    
    t1 = time.time()
    t2 = t1 + 50
    
    
    while is_running:
        
        if(t2 - t1) > 46:
            pygame.mixer.music.load("music/dramatic-action-background.mp3")
            pygame.mixer.music.play()
            t1 = time.time()
            
        
        #clear screen
        screen.fill((255,255,255))
        
        #store list of events
        list_of_events = []
        for event in pygame.event.get():
            if to_finish(event):
                is_running = False
                break
            list_of_events.append(event)
        
        player_x, player_y, player_img = player.movement(player_x, player_y, list_of_events)
        agents.move(player_x, player_y, act_map)
        player_x, player_y, act_map, is_game_finished = player.collision(player_x, player_y, act_map)
        
        if is_game_finished:
            is_running = False
            break
        
        game_map.draw_area(act_map)
        screen.blit(player_img, (player_x,player_y))
        agents.draw(act_map)
        
        player.status(act_map)
        
        pygame.display.update()
        
        clock.tick(15)
        
        t2 = time.time()
        previous_map = act_map
    
    
sys.exit()
pygame.quit()



