from configuration import *
import game_map

#tile in row (counting from 0), tile in collumn (counting from 0),direction
positions = {"Rebels'_HQ.txt" : [[50,50,"R"]], "Big_fountain.txt" : [[700, 50, "L"]], "Car_park.txt" : [[600, 200, "R"], [700, 600, "L"]], "The_Core.txt" : [], "Motorway.txt" : []}
AGENT_CANNOT_STAND_ON = ["I", "37","43", "76", "84", "110", "111", "112", "121", "122", "123", "135", "144", "163", "164", "165", "178", "180",  "205", "206", "207", "225", "240", "233", "342", "370", "371", "372"]

def is_proper_move(x, y, map_name):
    global agent_img_width, agent_img_height
    
    if x < 0 or x > screen_width:
        return False
    if y < 0 or y > screen_height - 40:
        return False
    
    under = game_map.check_what_under(x,y,map_name,agent_img_width, agent_img_height)
    
    for ID in under.split(","):
        if ID in AGENT_CANNOT_STAND_ON:
            return False
    return True

def move(player_x, player_y, map_name):
    global positions
    import random,math
    global tile_width, tile_height
    
    agent_step = 5
    agent_run = 7
    if positions[map_name] != []:
        moving = -2
        #checking distance to player
        for agent in positions[map_name]:
            if math.sqrt(abs(player_x - agent[0]) ** 2 + abs(player_y - agent[1]) ** 2) <= 120: #40 -> width and height of tile
                moving = -1
                if player_x > agent[0]:
                    agent[0] += agent_run
                    if is_proper_move(agent[0], agent[1], map_name):
                        agent[2] = "R"
                    else:
                        agent[0] -= agent_run
                else:
                    agent[0] -= agent_run
                    if is_proper_move(agent[0], agent[1], map_name):
                        agent[2] = "L"
                    else:
                        agent[0] += agent_run
                    
                
                if player_y > agent[1]:
                    agent[1] += agent_run
                    if not is_proper_move(agent[0], agent[1], map_name):
                        agent[1] -= agent_run
                else:
                    agent[1] -= agent_run
                    if not is_proper_move(agent[0], agent[1], map_name):
                        agent[1] += agent_run
        
        if moving == -2:      
            moving = random.randint(0, len(positions[map_name]) - 1)
            
        for ind in range(len(positions[map_name])):
            if ind != moving:
                positions[map_name][ind][2] = random.choice(["R","L"])
            else:
                new_y = -500
                new_x = -300
                while not is_proper_move(new_x, new_y, map_name):
                    x_shift = random.choice([-1 * agent_step,0, agent_step])
                    new_x = positions[map_name][ind][0] + x_shift
                    new_y = positions[map_name][ind][1] + random.choice([-1 * agent_step, 0, agent_step])
                
                positions[map_name][ind][0] = new_x
                positions[map_name][ind][1] = new_y
                
                if x_shift < 0:
                    positions[map_name][ind][2] = "L"
                else:
                    positions[map_name][ind][2] = "R"

                
def draw(map_name):
    global positions
    global agent_img_width, agent_img_height
    
    if positions[map_name] != []:
        
        for agent in positions[map_name]:
            if agent == []:
                continue
            img = pygame.image.load("images/tiles/S_" + agent[2] + ".png")
            img = pygame.transform.scale(img, (agent_img_width, agent_img_height))
            screen.blit(img, (agent[0], agent[1]))
        
def collision_with_player(player_x, player_y, map_name):
    global positions
    global player_img_width, player_img_height
    global agent_img_width, agent_img_height
    
    if positions[map_name] != []:
        
        player_rect = Rect(player_x, player_y, player_img_width, player_img_height)
        
        
        for agent in positions[map_name]:
            agent_rect = Rect(agent[0], agent[1], agent_img_width, agent_img_height)
            if pygame.Rect.colliderect(player_rect, agent_rect):
                return True
    return False
        