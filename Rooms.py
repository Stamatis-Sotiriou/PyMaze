# {"room":[[wall_1], [wall_2], [wall_3], [wall_4], [wall_alltop], [wall_allbot], [wall_allleft], [wall_allright], [mid_top_wall]]}
                    #1     #2     #3     #4     #top   #bot   #left  #right #MT    #b_L   #b_R   #b_T   #b_B
room_dict = {         #1     #2     #3     #4     #top   #bot   #left  #right #MT    #b_L   #b_R   #b_T   #b_B    left,   right, up,    down
              "1"  :[[False, False, True,  False, True,  False, True,  False, False, False, False, False, False], [False, True,  False, True]],
              "2"  :[[False, False, True,  True,  True,  False, False, False, False, False, False, False, False], [True,  True,  False, True]],
              "3"  :[[True,  True,  True,  True,  False, False, False, False, True,  False, False, False, True ], [True,  True,  False, True]],
              "4"  :[[False, False, False, True,  True,  False, False, True,  False, False, False, False, False], [True,  False, False, True]],
              "5"  :[[False, True,  False, False, False, True,  True,  False, False, False, False, False, False], []],
              "6"  :[[True,  True,  True,  True,  False, False, False, False, False, True,  False, False, False], []],
              "7"  :[[True,  True,  True,  True,  False, False, False, False, False, False, False, False, False], []],
              "8"  :[[True,  False, False, True,  False, False, False, True,  False, False, False, False, False], []],
              "9"  :[[False, False, True,  False, True,  False, True,  False, False, False, False, False, False], []],
              "10" :[[True,  True,  True,  True,  False, False, False, False, False, False, False, False, False], []],
              "11" :[[True,  True,  True,  True,  False, False, False, False, False, True,  True,  False, True ], []],
              "12" :[[True,  True,  True,  True,  False, False, False, False, False, False, True,  False, False], []],
              "13" :[[False, False, False, False, False, False, True,  True,  False, False, False, False, True ], []],
              "14" :[[True,  True,  False, False, False, True,  True,  False, False, False, False, False, False], []],
              "15" :[[True,  True,  True,  True,  False, False, False, False, False, False, False, False, False], []],
              "16" :[[True,  False, False, True,  False, False, False, True,  False, False, False, False, False], []],
              "17" :[[False, True,  True,  False, False, False, True,  False, False, False, False, False, False], []],
              "18" :[[False, False, False, False, True,  True,  False, False, False, False, False, False, False], []],
              "19" :[[True,  True,  True,  True,  False, False, False, False, False, False, False, False, False], []],
              "20" :[[True,  False, False, False, False, True,  False, True, False,  False, False, False, False], []],
              "21" :[[True,  True,  True,  True,  False, False, False, False, False, True,  False, True,  False], []],
              "22" :[[False, False, True,  True,   True, False, False, False, False, False, False, False, False], []],
              "23" :[[True,  True,  True,  True,  False, False, False, False, False, False, False, False, False], []],
              "24" :[[False, False, False, True,  True,  False, False, True,  False, False, False, False, False], []],
              "25" :[[False, True,  False, False, False, True,  True,  False, False, False, False, False, False], []],
              "26" :[[True,  True,  False, False, False, True,  False, False, False, False, True,  False, False], []],
              "27" :[[True,  False, False, False, False, True,  False, True, False, False,  False, False, False], []],
              "28" :[[False, False, False, False, False, True,  True,  True,  False, False, False, False, False], []]
              }

cur_room = 3