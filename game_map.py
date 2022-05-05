from configuration import *

locations = {}

def prepare_locations():
    import os, random
    from collections import deque
    
    global locations
    
    possible_places = os.listdir("maps/independent")
    
    possible_places.remove("Professor's_house.txt") #starting location
    possible_places.remove("The_Core.txt") #final location
    
    to_process = deque()
    
    to_process.append("Professor's_house.txt")
    
    how_many_places_to_include = min(len(possible_places), random.randint(10, 1000))
    
    
    loops = [] #list of locations connected to earlier used locations, it will be useful to connect one of them to the final location
    
    while len(to_process) > 0:
        
        actual = to_process.popleft()
        locations[actual] = {}
        
        
        file = open("maps/independent/" + actual, "r")
        data = file.read()
        data = data.split()
        file.close()

        map_of_actual = []
        ind = -1
        for element in data:
            if element == "B": #every line begins with B
                map_of_actual.append([])
                ind += 1
            else:
                #element -> tile(s) ID
                map_of_actual[ind].append(element)
                
        for y in range(len(map_of_actual)):
            for x in range(len(map_of_actual[y])):
                if (map_of_actual[y][x] == "I"):
                    if how_many_places_to_include > 0:
                        place_to_connect = random.choice(possible_places)
                        possible_places.remove(place_to_connect)
                        file = open("maps/independent/" + place_to_connect, "r")
                        place_to_connect_description = file.read()
                        place_to_connect_description = place_to_connect_description.split()
                        file.close()
                        
                        map_of_place_to_connect = []
                        ind = -1
                        for element in place_to_connect_description:
                            if element == "B": #every line begins with B
                                map_of_place_to_connect.append([])
                                ind += 1
                            else:
                                #element -> tile(s) ID
                                map_of_place_to_connect[ind].append(element) 
                         
                        for y_cord in range(len(map_of_place_to_connect)):
                            for x_cord in range(len(map_of_place_to_connect[y_cord])):
                                if map_of_place_to_connect[y_cord][x_cord] == "O": #found out warp
                                    locations[actual][(x,y)] = (place_to_connect, (x_cord, y_cord))
                                    to_process.append(place_to_connect)
                                    break
                        
                        how_many_places_to_include -= 1
                    
                    else:
                        already_used = []
                        for a in locations.keys():
                            for b in locations[a].values():
                                already_used.append(b)
                        
                        if len(already_used) > 1: #there are more locations than only actual
                            chosen = (actual, (0,0))
                            while chosen[0] == actual:
                                chosen = random.choice(already_used)
                                
                            locations[actual][(x,y)] = chosen
                        else: #warp to begin of the game
                            locations[actual][(x,y)] = ("Professor's_house.txt", (7,3))
                        
                        loops.append((actual, (x,y)))
    
    
    #connecting one of places to the final location
    
    if len(loops) > 0:
        chosen = random.choice(loops)
        locations[chosen[0]][chosen[1]] = ("The_Core.txt", (0,19))
    else: # I don't have loops
        # I don't want to connect final location with starting location
        chosen_place = "Professor's_house.txt"
        while chosen_place == "Professor's_house.txt":
            chosen_place = random.choice(list(locations.keys()))
        chosen_warp = random.choise(list(locations[chosen_place].keys()))
        
        locations[chosen_place][chosen_warp] = ("The_Core.txt", (0,19))

        
    

def warp_info(y,x,map_name):
    global locations
    tile_width, tile_height = 40, 40
    return locations[map_name][(x,y)][0], locations[map_name][(x,y)][1][0] * tile_width, locations[map_name][(x,y)][1][1] * tile_height
        

def check_what_under(player_x, player_y, map_name, img_width, img_height):
    #reading map
    file = open("maps/independent/" + map_name, "r")
    data = file.read()
    data = data.split()
    file.close()

    game_map = []
    ind = -1
    for x in data:
        if x == "B": #every line begins with B
            game_map.append([])
            ind += 1
        else:
            #x -> tile(s) ID
            game_map[ind].append(x)
    
    tile_width, tile_height = 40,40
    
    
    under = "TBD"
    
    player_rect = Rect(player_x, player_y, img_width, img_height)
    
    on_warp = False
    is_game_finished = False
    
    for y in range(len(game_map)):
        if (y + 1) * tile_height < player_y or y * tile_height > player_y + img_height:
            continue
        
        for x in range(len(game_map[y])):
            
            if (x + 1) * tile_width < player_x or x * tile_width > player_x + img_width:
                continue

            tile_rect = Rect(x * tile_width, y * tile_height, tile_width, tile_height)
            if pygame.Rect.colliderect(player_rect, tile_rect):
                under += "," + game_map[y][x]
                if game_map[y][x] == "I":
                    map_name, player_x, player_y = warp_info(y,x,map_name)
                    on_warp = True
                elif game_map[y][x] == "E": #end of game
                    is_game_finished = True
                
    return under, map_name, player_x, player_y, on_warp, is_game_finished
    
def draw_area(map_name):
    global screen_height, screen_width

    #reading map
    file = open("maps/independent/" + map_name, "r")
    data = file.read()
    data = data.split()
    file.close()

    game_map = []
    ind = -1
    for x in data:
        if x == "B": #every line begins with B
            game_map.append([])
        else:
            #x -> tile(s) ID
            game_map[ind].append(x)


    tile_width, tile_height = 40,40
    
    for y in range(screen_height // tile_height):
        if y > len(game_map) - 1:
            break
        for x in range(screen_width // tile_width):
            if x > len(game_map[y]) - 1:
                break
            if game_map[y][x] == "TBD":
                continue
            for z in game_map[y][x].split(","): 
                tile = pygame.image.load("images/tiles/" + z + ".png")
                tile = pygame.transform.scale(tile, (tile_width, tile_height))
                screen.blit(tile,(tile_width * x, tile_height * y ))


    

 