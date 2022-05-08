from configuration import *
import game_map
import agents
import ending

player_frame = [-1, "UP"]#-1 -> player stands, 0 -> first frame, 1 -> second frame, 2->third frame 3-> fourth frame; direction  

goes_right = False
goes_left = False
goes_up = False
goes_down = False

CANNOT_STAND_ON = ["E", "36", "37", "43", "44", "76", "84", "110", "111", "112", "121", "122", "123", "135", "144",  "163", "164", "165",
                   "178", "180", "205", "206", "207", "225", "240", "233", "342", "343", "344", "345", "370", "371", "372", "411", "412"
                   "441", "442", "465", "466"]
COLLISION_TAKING_LIFE = ["464","414", "413", "383", "387","427"]

def if_change(event):
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
            
def movement(player_x, player_y, list_of_events):
    global player_frame, goes_up, goes_left, goes_down, goes_right
    global player_img_width, player_img_height
    
    change_in_moving = False
    
    for event in list_of_events:
        if event.type == KEYDOWN or event.type == KEYUP: #potentially changing movement events
            if event.key in [K_UP, K_RIGHT, K_DOWN, K_LEFT]:
                change_in_moving = True
                if_change(event)
        
    if change_in_moving == False and (goes_up  or goes_left or goes_down or goes_right): #continue walking in previous direction
        player_frame[0] = (player_frame[0] + 1) % 3
               
    
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
    
    #bouncing from edges
            
    if player_x < 0:
        player_x = 5
    elif (player_x + player_img_width) > screen_width:
        player_x = screen_width  - player_img_width - 5
            
    if player_y < 0:
        player_y = 5
    elif (player_y + player_img_height) > (screen_height-40):
        player_y = (screen_height - 40) - player_img_height - 5
    
    filename = ""
    if player_frame[0] == -1:
        filename = "stand_" + player_frame[1].lower() + ".png"
    else:
        filename = "walk_" + player_frame[1].lower() + "_" + str(player_frame[0] + 1) + ".png" # 0 -> 1, 1 -> 2, 2->3, 3->4
        
    player_img = pygame.image.load("images/player/" + filename)
    player_img = pygame.transform.scale(player_img, (player_img_width,player_img_height)) #scalling, original character was too small 
    
    
    return player_x, player_y, player_img

def collision(player_x, player_y, map_name):
    global player_img_width, player_img_height
    global player_frame
    global CANNOT_STAND_ON
    
    collisions = game_map.check_what_under(player_x, player_y, map_name, player_img_width, player_img_height)
    
    if agents.collision_with_player(player_x, player_y, map_name):
        collisions += ",S"
    
    if map_name == "Motorway.txt":
        if game_map.collision_with_car(player_x, player_y):
            ending.death()
            return player_x, player_y, map_name, True
    
    for ID in collisions.split(","):
        if ID in CANNOT_STAND_ON:
            if player_frame[1] == "UP":
                player_y += 10
            elif player_frame[1] == "DOWN":
                player_y -= 10
            elif player_frame[1] == "RIGHT":
                player_x -= 10
            elif player_frame[1] == "LEFT":
                player_x += 10
        elif ID == "I": #IN warp
            player_x, player_y, map_name = game_map.warp_info(player_x, player_y, map_name, player_img_width, player_img_height)
        elif ID == "S":
            ending.caught()
            return player_x, player_y, map_name, True
        elif ID == "C":
            ending.good()
            return player_x, player_y, map_name, True
        elif ID in COLLISION_TAKING_LIFE:
            ending.death()
            return player_x, player_y, map_name, True
     

            
            
    return player_x, player_y, map_name, False
        
def status(map_name):
    pygame.draw.rect(screen, (217,217,214), [0,760,screen_width, 40])
    pygame.draw.line(screen, (0,0,0), (0,760), (screen_width, 760), width = 4)
    character_img = pygame.image.load("images/player/stand_down.png")
    character_img = pygame.transform.scale(character_img, (35,35))
    
    screen.blit(character_img, (0, 763))
    
    map_name = "".join(map_name.split(".")[:-1]).split("_")
    map_name = " ".join(map_name)
    
    style = pygame.font.SysFont("Arial", 20)
    
    name = style.render(map_name, True, (0,0,0))
    screen.blit(name, (100, 770))
    
    

    