from configuration import *
import game_map

player_frame = [-1, "UP"]#-1 -> player stands, 0 -> first frame, 1 -> second frame, 2->third frame 3-> fourth frame; direction  

goes_right = False
goes_left = False
goes_up = False
goes_down = False

PERSON_CANNOT_STAND_ON = ["110", "111", "112", "121", "122", "123", "163", "164", "165", "178", "180",  "205", "206", "207" "370", "371", "372"]

def player_if_change(event):
    global player_frame,goes_up, goes_left, goes_down, goes_right
    if event.type == KEYDOWN and event.key == K_UP:
        goes_up = True
        goes_right = False
        goes_down = False
        goes_left = False
        
        player_frame = [0, "UP"]
    elif event.type == KEYDOWN and event.key == K_RIGHT:
        goes_up = False
        goes_right = True
        goes_down = False
        goes_left = False
        
        player_frame = [0, "RIGHT"]

    elif event.type == KEYDOWN and event.key == K_DOWN:
        goes_up = False
        goes_right = False
        goes_down = True
        goes_left = False
        player_frame = [0, "DOWN"]

    elif event.type == KEYDOWN and event.key == K_LEFT:
        goes_up = False
        goes_right = False
        goes_down = False
        goes_left = True
        
        player_frame = [0, "LEFT"]

        
    
    elif event.type == KEYUP and event.key in [K_UP, K_RIGHT, K_DOWN, K_LEFT]:
        goes_right = False
        goes_left = False
        goes_up = False
        goes_down = False
        
        player_frame[0] = -1
            
def player_movement(list_of_events, player_x, player_y, map_name):
    global player_frame, goes_up, goes_left, goes_down, goes_right
    global PERSON_CANNOT_STAND_ON
    
    change_in_move = False
    for x in list_of_events:
        if x.type == KEYDOWN or x.type == KEYUP:
            if x.key in [K_UP, K_RIGHT, K_DOWN, K_LEFT]:
                change_in_move = True
                player_if_change(x)
        
    if change_in_move == False and (goes_up  or goes_left or goes_down or goes_right): #continue walking in previous direction
        player_frame[0] = (player_frame[0] + 1) % 3
            
    
    filename = ""
    if player_frame[0] == -1:
        filename = "stand_" + player_frame[1].lower() + ".png"
    else:
        filename = "walk_" + player_frame[1].lower() + "_" + str(player_frame[0] + 1) + ".png" # 0 -> 1, 1 -> 2, 2->3, 3->4
        
    player_img = pygame.image.load("images/player/" + filename)
    player_img = pygame.transform.scale(player_img, (35,35)) #scalling, original charcter was too small
    
    player_img_width, player_img_height = player_img.get_size()
    
    
    #player_x, player_y -> left upper corner
    
    if player_frame[0] != -1: #player is walking
        if player_frame[1] == "UP":
            player_y -= 10
        elif player_frame[1] == "RIGHT":
            player_x += 10
        elif player_frame[1] == "DOWN":
            player_y += 10
        else:
            player_x -= 10

    #collision
    
    under, map_name, player_x, player_y, on_warp, is_game_finished = game_map.check_what_under(player_x, player_y, map_name,35,35)
    
    if is_game_finished == False:
        if on_warp == False:
            for ID in under.split(","):
                if ID in PERSON_CANNOT_STAND_ON:
                    if player_frame[1] == "UP":
                        player_y += 10
                    elif player_frame[1] == "DOWN":
                        player_y -= 10
                    elif player_frame[1] == "RIGHT":
                        player_x -= 10
                    elif player_frame[1] == "LEFT":
                        player_x += 10
                    
        
            #bouncing from edges
            
            if player_x < 0:
                player_x = 5
            elif (player_x + player_img_width) > screen_width:
                player_x = screen_width - player_img_width - 5
            
            if player_y < 0:
                player_y = 5
            elif (player_y + player_img_height) > screen_height:
                player_y = screen_height - player_img_height - 5
            
    return player_img, player_x, player_y, map_name, is_game_finished
        
def status(map_name, player_life):
    pygame.draw.rect(screen, (217,217,214), [0,760,screen_width, 40])
    pygame.draw.line(screen, (0,0,0), (0,760), (screen_width, 760), width = 4)
    character_img = pygame.image.load("images/player/stand_down.png")
    character_img = pygame.transform.scale(character_img, (35,35))
    
    left_x = 0
    
    for i in range(player_life):
        screen.blit(character_img, (left_x, 763))
        left_x += 40
    
    map_name = "".join(map_name.split(".")[:-1]).split("_")
    map_name = " ".join(map_name)
    
    style = pygame.font.SysFont("Arial", 20)
    
    left_x = 200
    name = style.render(map_name, True, (0,0,0))
    screen.blit(name, (left_x, 770))
    
    

    