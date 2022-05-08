from configuration import *

game_map = {}
cars = []

def prepare_game_map():
    import os, random
    from collections import deque
    
    global game_map
    global tile_width, tile_height
    
    possible_places = os.listdir("maps/independent")
    
    possible_places.remove("Rebels'_HQ.txt") #starting location
    possible_places.remove("The_Core.txt") #final location
    
    to_process = deque()
    
    to_process.append("Rebels'_HQ.txt")
    
    how_many_places_to_include = min(len(possible_places), random.randint(10, 1000))
        
    while len(to_process) > 0:
        
        actual = to_process.popleft()
        game_map[actual] = {}
        
        
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
                                    game_map[actual][(x * tile_width,y * tile_height)] = ((x_cord * tile_width, y_cord * tile_height), place_to_connect)
                                    to_process.append(place_to_connect)
                                    break
                        
                        how_many_places_to_include -= 1
                    
                    else:
                        already_used = []
                        for a in game_map.keys():
                            for b in game_map[a].values():
                                already_used.append(b)
                                
                        #to ensure player cannot be teleported to the same place by using warps in particular place
                        
                        for w in game_map[actual].keys():
                            if game_map[actual][w][1] in already_used:
                                already_used.remove(game_map[actual][w][1])
                        
                        if len(already_used) > 1: #there are more locations than only actual
                            chosen = ((0,0), actual)
                            while chosen[1] == actual:
                                chosen = random.choice(already_used)
                                
                            game_map[actual][(x * tile_width,y * tile_height)] = chosen
                        else: #warp to begin of the game
                            game_map[actual][(x * tile_width ,y * tile_height)] = ((280,120), "Rebels'_HQ.txt",)    
    
    #connecting one of places to the final location

    visited_places = ["Rebels'_HQ.txt"]
    
    Q = deque()
    
    Q.append("Rebels'_HQ.txt")
    
    while len(Q) > 0:
        act_pos = Q.popleft()
        for warp in game_map[act_pos].keys():
            if game_map[act_pos][warp][1] not in visited_places:
                Q.append(game_map[act_pos][warp][1])
                visited_places.append(game_map[act_pos][warp][1])
    
    chosen_loc = "Rebels'_HQ.txt"
    while chosen_loc == "Rebels'_HQ.txt":
        chosen_loc = random.choice(visited_places)
    
    game_map[chosen_loc][random.choice(list(game_map[chosen_loc].keys()))] = ((120,720), "The_Core.txt")
    
def warp_info(x,y,map_name, img_width, img_height):
    global game_map
    global screen_width, screen_height
    global tile_width, tile_height
    
    object_rect = Rect(x, y, img_width, img_height)
    for warp in list(game_map[map_name].keys()):
        warp_rect = Rect(warp[0], warp[1], tile_width, tile_height)
        if pygame.Rect.colliderect(object_rect, warp_rect):
            return game_map[map_name][warp][0][0], game_map[map_name][warp][0][1], game_map[map_name][warp][1]
    return 0,0, "Error" #never should be executed

def check_what_under(x, y, map_name, img_width, img_height):
    global tile_width, tile_height
    
    #reading map
    file = open("maps/independent/" + map_name, "r")
    data = file.read()
    data = data.split()
    file.close()

    MAP = []
    ind = -1
    for element in data:
        if element == "B": #every line begins with B
            MAP.append([])
            ind += 1
        else:
            #element -> tile(s) ID
            MAP[ind].append(element)
    
    collision_with = "TBD"
    
    object_rect = Rect(x, y, img_width, img_height)
    
    for row in range(len(MAP)):
        if (row + 1) * tile_height < y or row * tile_height > y + img_height:
            continue
        
        for column in range(len(MAP[row])):
            
            if (column + 1) * tile_width < x or column * tile_width > x + img_width:
                continue

            tile_rect = Rect(column * tile_width, row * tile_height, tile_width, tile_height)
            if pygame.Rect.colliderect(object_rect, tile_rect):
                collision_with += "," + MAP[row][column]  
    
    return collision_with

def draw_area(map_name):
    global screen_height, screen_width
    global tile_width, tile_height
    
    #reading map
    file = open("maps/independent/" + map_name, "r")
    data = file.read()
    data = data.split()
    file.close()

    MAP = []
    ind = -1
    for element in data:
        if element == "B": #every line begins with B
            MAP.append([])
        else:
            #element -> tile(s) ID
            MAP[ind].append(element)
    
    for y in range(screen_height // tile_height):
        if y > len(MAP) - 1:
            break
        for x in range(screen_width // tile_width):
            if x > len(MAP[y]) - 1:
                break
            if MAP[y][x] == "TBD":
                continue
            for z in MAP[y][x].split(","):
                if z == "TBD":
                    continue
                tile = pygame.image.load("images/tiles/" + z + ".png")
                tile = pygame.transform.scale(tile, (tile_width, tile_height))
                screen.blit(tile,(tile_width * x, tile_height * y ))

    if map_name == "Motorway.txt":
        draw_cars()
    


def draw_cars():
    global cars, screen_height, screen_width
    import random
    
    if len(cars) < 5:
        cars.append([random.choice([410, 414,464]), random.choice([80, 120, 200, 240, 440, 480, 560,600, 800, 840, 920, 960]), 0, random.randint(10, 20)])
    
    for car in cars:
        front = pygame.image.load("images/tiles/" + str(car[0]) + ".png")
        if car[0] == 410:
            back = pygame.image.load("images/tiles/383.png")
        elif car[0] == 414:
            back = pygame.image.load("images/tiles/387.png")
        elif car[0] == 464:
            back = pygame.image.load("images/tiles/437.png")
        
        front = pygame.transform.scale(front, (40,40))
        back = pygame.transform.scale(back, (40,40))
        
        screen.blit(front, (car[1], car[2]))
        screen.blit(back, (car[1], car[2] - 40))
        
        car[2] += car[3]
        
        if car[2] >= screen_height:
            cars.remove(car)
def collision_with_car(player_x, player_y):
    global cars
    global player_img_height, player_img_width
    
    player_rect = Rect(player_x, player_y, player_img_width, player_img_height)
    
    for c in cars:
        car_rect = Rect(c[1], c[2], 40, 40)
        if pygame.Rect.colliderect(player_rect, car_rect):
            return True
    return False