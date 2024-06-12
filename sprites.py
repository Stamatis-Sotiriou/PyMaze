from GameSprite import *

player = Player((325, 100), (50,50), (0,100,0), 7)

wall_1 = Wall((0,0),     (275, 175), (0,0,0)) #cor, size, color
wall_2 = Wall((425,0),   (700, 175), (0,0,0))
wall_3 = Wall((425,325), (700, 500), (0,0,0))
wall_4 = Wall((0,325),   (275, 500), (0,0,0))

wall_alltop = Wall((0,0),   (700, 175), (0,0,0))
wall_allbot = Wall((0,325), (700, 500), (0,0,0))

wall_allleft = Wall((0,0),    (275, 500),  (0,0,0))
wall_allright = Wall((425,0), (700, 500),  (0,0,0))

wall_blockL = Wall((225, 175),  (50, 150), (0,0,0))
wall_blockR = Wall((425,175),   (50, 150), (0,0,0))
wall_blockT = Wall((275, 125),  (150, 50), (0,0,0))
wall_blockB = Wall((275,325),   (150, 50), (0,0,0))

mid_top_wall = Wall((275, 0), (150, 75), (0,0,0))

wall_group = [
            wall_1, wall_2, wall_3, wall_4, 
            wall_alltop, wall_allbot, wall_allleft, wall_allright, 
            mid_top_wall, 
            wall_blockL, wall_blockR, wall_blockT, wall_blockB
            ]

light_left  = Light([(100, 150), (100, 300)])
light_right = Light([(550, 150), (550, 300)])
light_up    = Light([(250, 100), (400, 100)])
light_down  = Light([(250, 400), (400, 400)])

light_group = [light_left, light_right, light_up, light_down]

key_13 = GameSprite((325,400), (50,50), (0,255,255), 1)
