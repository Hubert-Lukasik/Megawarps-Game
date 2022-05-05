from configuration import *
import player
import menu
import intro
import game_map

screen.fill((255,255,255))

game_map.prepare_locations()

start_game = menu.show()

if start_game:
    
    if skip_intro == False:
        intro.show()
    
    player_x = 50
    player_y = 600
    act_map = "Professor's_house.txt"
    
    player_life = 3
    
    is_running = True
    while is_running:
        screen.fill((255,255,255))
        list_of_events = []
        for event in pygame.event.get():
            if to_finish(event):
                is_running = False
                break
            list_of_events.append(event)
        
        player_img, player_x, player_y, act_map, is_game_finished = player.player_movement(list_of_events, player_x, player_y, act_map)
        
        if is_game_finished:
            is_running = False
            break
        
        
        game_map.draw_area(act_map)
        screen.blit(player_img, (player_x,player_y))
        
        
        player.status(act_map, player_life)
        
        pygame.display.update()
        clock.tick(15)
    
    
    if is_game_finished:
        import time
        screen.fill((0,255,0))
        pygame.display.update()
        time.sleep(0)
        sys.exit()
        

pygame.quit()



