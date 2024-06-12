from pygame import *
from GameSprite import Wall, Light
from Rooms import room_dict, cur_room
from sprites import *

def check_quit():
    for e in event.get():
        if e.type == QUIT:
            return False
    return True

# Init:
init()

window = display.set_mode((700, 500))
display.set_caption("Py Maze!")

# Clock:
clock = time.Clock()
FPS = 60

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
        Light.get_new_cor(light_group)

    Light.make_lights(window, light_group, room_dict[str(cur_room)])

    clock.tick(FPS)
    display.update()

    game = check_quit()
quit()