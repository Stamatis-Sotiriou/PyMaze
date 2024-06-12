from pygame import *
from GameSprite import Wall, Light
from Rooms import room_dict, cur_room
from sprites import player, wall_group, light_group, key_13


def check_quit():
    for e in event.get():
        if e.type == QUIT:
            return False
    return True


for light in light_group:
    light.init()


# Init:
init()

window = display.set_mode((700, 500))
display.set_caption("Py Maze!")

# Font
font = font.Font('freesansbold.ttf', 30)
#room_text = font.render('ROOM', False, (0,0,255))
text = "Pick \nup"
key_text = font.render(text, False, (0,0,255))

# Clock:
clock = time.Clock()
FPS = 30

counter = 0

# ----- Main ----- #
game = True
while game:
    window.fill((70,22,22))

    if counter == 0:
        Light.get_new_cor(light_group)
        counter += 1

    player.show(window)
    player.update()
 
    Wall.make_wall(window, wall_group, room_dict[str(cur_room)])
    Wall.collision(wall_group, player)

    temp = player.next_room()
    if temp != None:
        cur_room += temp
        
        for light in light_group:
            light.init()
        Light.get_new_cor(light_group)

    if cur_room == 2:
        key_13.show(window)
        key_13.update()
            
        if player.on_key(key_13):
            window.blit(key_text, (100, 100))

    Light.make_lights(window, light_group, room_dict[str(cur_room)])

    
    room_text = font.render(str(cur_room), False, (0,0,255))
    window.blit(room_text, (625, 450))

    clock.tick(FPS)
    display.update()

    game = check_quit()
quit()
