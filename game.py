# Ben Cohen fxa6my
# Ada Zhang abz2mf


# This project was made possible with the use of gamebox, which is the original
# work of Luther Tychonievich.

# See the code under "Final product work" for the final code and for an explanation
# on how to play the game.

# CP1 work
# GENERAL DESCRIPTION
# This is a typical game of dodgeball. Player is located at bottom of screen
# and dodges balls by moving horizontally left or right. Balls come down vertically
# from top of screen.

# REQUIRED FEATURES
# 1. User Input
#     - Left: moves player left
#     - Right: moves player right
# 2. Game Over
#     - Player gets hit by a ball, Health Bar goes down by 1
#     - show Game Over when Health Bar runs out
# 3. Small Enough Window
#     - Game window will be 800 x 600
#     - camera = gamebox.Camera(800,600)
# 4. Graphics/Images
#     - Player: from_image(x, y, filename_or_url)
#     - Dodgeballs: from_circle(x, y, color, radius, *args)
#     - Background: all black

# OPTIONAL FEATURES
# 1. Health Bar
#     - you lose after getting hit 3 times by dodgeball
#     - bar starts with 3 and decreases each time you get hit
# 2. Sprite Animation
#     - many dodgeballs of different colors
# 3. Collectibles
#     - player can collect a "coin" to get a life back
#     - not to exceed 3 lives
# 4. Multiple Levels
#     - dodgeballs come faster with each level
#     - more dodgeballs at each level

# CP2 work

"""import pygame
import gamebox
import random # for different ball colors and enemy positions

camera = gamebox.Camera(800,600)
bounds = [gamebox.from_color(400,0,"black",800,1),
          gamebox.from_color(400,600,"black",800,1),
          gamebox.from_color(0,300,"black",1,600),
          gamebox.from_color(800,300,"black",1,600)]

hp = 3
hp_bar_position_x = 75
hp_bar_outline = gamebox.from_color(hp_bar_position_x,25,"white",55,30)
# outer box for hp bar
hp_bar_inside = gamebox.from_color(hp_bar_position_x,25,"black",50,25)
hp_label = gamebox.from_text(hp_bar_position_x-25,25,"HP:",24,"red")
# inside background color for hp bar. will have the same dimensions as a full
# hp bar, and when some of the hp is depleted, this is behind it. Covers up
# the white from hp_bar_outline except for the edges.
court_line = gamebox.from_color(400,325,"dark red",800,5)
char = gamebox.from_color(400,500,"blue",25,50)
# can be replaced with something other than a square if wanted
char_movespeed = 5

enemies = []
enemy_movespeed = 5
enemy = gamebox.from_color(random.randint(100,700),random.randint(100,250),"red",25,50)
enemy_balls = []

# html hex codes are a '#' sign followed by 6 letters or numbers from 0-9 and A-F.

# the first 2 characters measure from down to up, with the second character cycling
# through 0-9 and then A-F, and the first character changing once for each time the
# second character changes, like how one minute passes after each cycle of 60
# seconds. We don't want the first character to be from 0-6 or else it will be
# too dark to see against the black background.
# the last 4 characters cycle through similarly from right to left and based on
# some other factors, like different colors, but we're not going to worry about
# constraints on this since making them not dark is our main priority.
# Using this information, we can assign randomly generated numbers to the values
# of 7-9 and A-F for the first character and 0-9 + A-F for the other ones.
character1 = str(random.randint(7,15))
characters_list = [character1]
for i in range(1,6):
  other = str(random.randint(0,15))
  characters_list.append(other)

random_colors_html_code = "#"
for each in characters_list:
  if each == "10":
    each = "A"
  elif each == "11":
    each = "B"
  elif each == "12":
    each = "C"
  elif each == "13":
    each = "D"
  elif each == "14":
    each = "E"
  elif each == "15":
    each = "F"
  random_colors_html_code += each
colorful_ball = gamebox.from_circle(current_pos_x,current_pos_y,random_colors_html_code,10)
# move this to within the loop for creating balls when done.
# needs the enemies current position, which will be in a for loop for each enemy
# and will need a counter for time, where each ball spawns within a random time
# using random.randint.


player_balls = []

level = 1
level_display = gamebox.from_text(700,25,"Level: " + str(level),36,"yellow")
top_separator = gamebox.from_color(400,50,"white",800,1)

screen_things = [hp_bar_outline,hp_bar_inside,court_line,char,level_display,
                 top_separator]
# variable name above can be changed, couldn't think of the word for these things

game_on = False

def tick(keys):
  global game_on
  global hp
  global level
  camera.clear("black")
  for each in screen_things:
    camera.draw(each)

  if pygame.K_SPACE in keys:
    game_on = True
  if game_on == False:
    camera.draw(gamebox.from_text(400,200,"GAME TITLE",36,"white"))
    camera.draw(gamebox.from_text(400,250,"Press the spacebar to start",24,"white"))

  if game_on == True:
    if pygame.K_UP in keys:
      char.y -= char_movespeed
    if pygame.K_DOWN in keys:
      char.y += char_movespeed
    if pygame.K_LEFT in keys:
      char.x -= char_movespeed
    if pygame.K_RIGHT in keys:
      char.x += char_movespeed

      enemies = enemies.append(enemy)
      for each in enemies:

        camera.draw(each)

  char.move_to_stop_overlapping(court_line)
  for bound in bounds:
    char.move_to_stop_overlapping(bound)
    for each in enemies:
      each.move_to_stop_overlapping(bound)
      each.move_to_stop_overlapping(court_line)


  hp_red_bar = gamebox.from_color((hp_bar_position_x + hp_bar_position_x/3*hp)/2,25,"red",(hp_bar_position_x-25)/3*hp,25)
  camera.draw(hp_red_bar)
  # could also look into using heart sprites rather than a bar, but either's fine

  camera.display()

ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)"""

# Final product work

# Changes from initial CP1 ideas:
# 1) In addition to the different colors for the balls, just in case that
# did not satisfy the requirement for sprite animations, we made it so that the
# food items have sprite animations where they switch back and forth between
# different foods every 0.5 seconds.
# 2) Additionally, the feature of colleting coins has been changed to collecting
# food items since there was some difficulty in having Python correctly access certain spritesheets.
# 3) Another change is that our player character has been generated using
# from_color instead of from_image, although we did use from_image for the food items.
# 4) In addition to dodgeballs increasing in movespeed at each level and there
# being more dodgeballs at each level (since the number of enemies increases by 5
# each level), the enemies also get faster in speed, and health items spawn less
# frequently (an additional second for each level).

# Game instructions:
# Move with the arrow keys, throw a ball with d. If you throw the ball while moving
# left or right, it will go at an angle to the left or the right, respectively.
# You cannot move past the middle court line (as is the rule in dodgeball), and
# neither can your opponents. Hit the opponents with dodgeballs to eliminate them,
# and once you eliminate all from the field, you proceed to the next level, which
# has even more opponents. If you get hit, you lose 1 hp (health/hit point), and
# you start with 3 hp. If you drop to 0 hp, the game is over. You can collect food
# items that will spawn in near the back of your opponents' side by hitting them
# with one of your dodgeballs.
# Have fun!

import pygame
import gamebox
import random  # for different ball colors and enemy positions

camera = gamebox.Camera(800, 600)  # create camera and bounds
left_bound = gamebox.from_color(0, 300, "black", 1, 600)
right_bound = gamebox.from_color(800, 300, "black", 1, 600)
top_bound = gamebox.from_color(400, 0, "black", 800, 1)
bottom_bound = gamebox.from_color(400, 600, "black", 800, 1)
top_separator = gamebox.from_color(400, 50, "white", 800, 1)
bounds = [top_bound,
          bottom_bound,
          left_bound,
          right_bound,
          top_separator]

hp = 3  # create health bar
hp_bar_pos_x = 75
hp_bar_width = 50
hp_bar_side_distance_from_lbound = hp_bar_pos_x - (hp_bar_width / 2)
hp_bar_outline = gamebox.from_color(hp_bar_pos_x, 25, "white", 55, 30)
# outer box for hp bar
hp_bar_inside = gamebox.from_color(hp_bar_pos_x, 25, "black", hp_bar_width, 25)
hp_label = gamebox.from_text(hp_bar_pos_x - 25, 25, "HP:", 24, "red")
# inside background color for hp bar. will have the same dimensions as a full
# hp bar, and when some of the hp is depleted, this is behind it. Covers up
# the white from hp_bar_outline except for the edges.
court_line = gamebox.from_color(400, 325, "dark red", 800, 5)
char = gamebox.from_color(400, 500, "blue", 25, 50)
# can be replaced with something other than a square if wanted
char_movespeed = 5

enemies = []
enemy_movespeed = 5
enemy_balls = {}
player_balls = {}

game_over_text = gamebox.from_text(400, 200, "GAME OVER", 60, "red", bold=True)

level = 0
level_display = gamebox.from_text(700, 25, "Level: " + str(level), 36, "yellow")

screen_things = [hp_bar_outline, hp_bar_inside, court_line, char, top_separator]
# removing level_display from the list screen_things got it to properly update

game_on = False
enemy_ball_count = 0
player_ball_count = 30
food_count = 0
foods = {}
food_shift_count = 0
food_sprite_sheet_url = "https://axelpale.github.io/openmoji-sprites/png/food-drink-00.png"
food_sprite_sheet = gamebox.load_sprite_sheet(food_sprite_sheet_url, 8, 16)
item_number = 0
angle_pb = 0


def random_color():  # create dodgeballs
    # html hex codes are a '#' sign followed by 6 letters or numbers from 0-9 and A-F.

    # the first 2 characters measure from down to up, with the second character cycling
    # through 0-9 and then A-F, and the first character changing once for each time the
    # second character changes, like how one minute passes after each cycle of 60
    # seconds. We don't want the first character to be from 0-6 or else it will be
    # too dark to see against the black background.
    # the last 4 characters cycle through similarly from right to left and based on
    # some other factors, like different colors, but we're not going to worry about
    # constraints on this since making them not dark is our main priority.
    # Using this information, we can assign randomly generated numbers to the values
    # of 7-9 and A-F for the first character and 0-9 + A-F for the other ones.
    character1 = str(random.randint(7, 15))
    characters_list = [character1]
    for i in range(1, 6):
        other = str(random.randint(0, 15))
        characters_list.append(other)

    random_colors_html_code = "#"
    for each_c in characters_list:
        # each_c stands for each character
        if each_c == "10":
            each_c = "A"
        elif each_c == "11":
            each_c = "B"
        elif each_c == "12":
            each_c = "C"
        elif each_c == "13":
            each_c = "D"
        elif each_c == "14":
            each_c = "E"
        elif each_c == "15":
            each_c = "F"
        random_colors_html_code += each_c
    return random_colors_html_code


def tick(keys):
    global game_on
    global hp
    global level
    global enemy_ball_count
    global player_ball_count
    global food_count
    global foods
    global food_shift_count
    global item_number
    global enemies
    global enemy_balls
    global player_balls
    global angle_pb
    global level_display

    camera.clear("black")
    for each in screen_things:
        camera.draw(each)

    if pygame.K_SPACE in keys and hp != 0:
        game_on = True
    if game_on == False and hp != 0:
        camera.draw(gamebox.from_text(400, 200, "DODGEBALL", 36, "white"))
        camera.draw(
            gamebox.from_text(400, 250, "Press space to start, d to throw (throws in direction of movement)", 24,
                              "white"))
    # pressing d while not moving left or right makes the ball go straight up.
    # pressing d while moving left makes it go up and left.
    # pressing d while moving right makes it go up and right

    if game_on == True:
        # the player can move after pressing space to start the game
        if pygame.K_UP in keys:
            char.y -= char_movespeed
        if pygame.K_DOWN in keys:
            char.y += char_movespeed
        if pygame.K_LEFT in keys:
            char.x -= char_movespeed
        if pygame.K_RIGHT in keys:
            char.x += char_movespeed
        if player_ball_count >= 30:
            # the player ball count is a timer that prevents the player from firing multiple
            # balls within a short time frame. >= 30 means the player can fire a ball
            # at a maximum of 1 per second. It then gets reset to 0 when d is pressed.
            if pygame.K_d in keys:
                player_ball_count = 0
                # pressing d throws a ball. If they're moving left or right while throwing,
                # the ball is angled to the left or right, and if not, it goes straight up.
                regular_ball = gamebox.from_circle(char.x, char.y, random_color(), 10)
                if pygame.K_LEFT in keys:
                    angle = 1
                elif pygame.K_RIGHT in keys:
                    angle = 2
                else:
                    angle = 0
                player_balls[regular_ball] = angle

        enemy_ball_count += 1
        player_ball_count += 1
        food_count += 1
        food_shift_count += 1
        if food_shift_count == 30:
            food_shift_count = 0
        # this is used later in the "if food_count == 270 + 30*level" clause

        deleting_keys_list_pb = []
        for each_pb, angle in player_balls.items():
            # this was moved from out of the for each_e in enemies loop because it was
            # causing the balls to go faster when more enemies were alive since it would
            # then run through more enemies and cause the position to be changed more frequently
            camera.draw(each_pb)
            each_pb.speedy = 10
            each_pb.y -= each_pb.speedy
            each_pb.speedx = 10
            if angle == 1:  # goes to the top left, 22.5 degrees
                each_pb.x -= 0.5 * each_pb.speedx
            elif angle == 2:  # goes to the top right, 22.5 degrees
                each_pb.x += 0.5 * each_pb.speedx
            elif angle == 0:  # goes straight up
                each_pb.x += 0
            if each_pb.touches(left_bound):
                player_balls[each_pb] = 2
            if each_pb.touches(right_bound):
                player_balls[each_pb] = 1
            if each_pb.touches(top_separator):
                deleting_keys_list_pb.append(each_pb)
                # if it hits a side wall, it bounces off in the other direction

        deleting_keys_list_eb = []
        # an explanation for the use of these lists along with the deleting keys list
        # for food items is farther down near the bottom where the deletion process occurs
        if enemies == []:
            # when all enemies have been eliminated, it goes to the next level
            level += 1
            level_display = gamebox.from_text(700, 25, "Level: " + str(level), 36, "yellow")
            # the level display is added again within the ticks function so it can be updated
            for i in range(level * 5):
                enemy = gamebox.from_color(random.randint(100, 700), random.randint(100, 250), "red", 25, 50)
                enemies.append(enemy)
                # at the beginning of each level, an amount of enemies are spawned equal
                # to 5 times the level. At level 1, there are 5 enemies, at level 5, there
                # are 25, etc.
                # the enemy variable is put here so it's randomized for each enemy
        camera.draw(level_display)
        if enemies != []:
            # if there are enemies present, this is active
            for each_e in enemies:
                camera.draw(each_e)
                # each_e stands for each enemy
                # this runs through the enemy list to give attributes to each enemy in the list
                for each_b in bounds:
                    # each_b stands for each bound
                    each_e.move_to_stop_overlapping(each_b)
                each_e.speedx = level
                each_e.speedy = level
                each_e.x += random.randint(-each_e.speedx, each_e.speedx)
                each_e.y += random.randint(-each_e.speedy, each_e.speedy)
                # these two lines above help to randomize their movement, although it will
                # likely be the case that enemies stay in a general area since their chance
                # of going to the right is equal to their chance of going to the left, and
                # the same with up and down.
                for each_pb in player_balls.keys():
                    # each_pb stands for each player ball
                    if each_pb.touches(each_e):
                        enemies.remove(each_e)
                        deleting_keys_list_pb.append(each_pb)
                if enemy_ball_count == 45:
                    # enemy dodgeballs spawn in every 1.5 seconds
                    enemy_ball_count = 0
                    for each_e in enemies:
                        # a dodgeball is thrown by each enemy at their location.
                        colorful_ball = gamebox.from_circle(each_e.x, each_e.y, random_color(), 10)
                        enemy_balls[colorful_ball] = random.randint(0, 2)
            for each_eb, angle in enemy_balls.items():
                # each_eb stands for each enemy ball
                each_eb.speedy = 3 + (level / 2)
                each_eb.y += each_eb.speedy
                each_eb.speedx = 3 + (level / 2)
                # the enemy balls have a speed that increases with level, and they travel
                # downwards with that speed and to the sides with half of that speed if
                # assigned to go at an angle.
                if angle == 1:  # goes to the bottom left, 22.5 degrees
                    each_eb.x -= 0.5 * each_eb.speedx
                elif angle == 2:  # goes to the bottom right, 22.5 degrees
                    each_eb.x += 0.5 * each_eb.speedx
                elif angle == 0:  # goes straight down
                    each_eb.x += 0
                if each_eb.touches(left_bound):
                    enemy_balls[each_eb] = 2
                if each_eb.touches(right_bound):
                    enemy_balls[each_eb] = 1
                if each_eb.touches(bottom_bound):
                    deleting_keys_list_eb.append(each_eb)
                # if an enemy ball hits a wall, it changes its angle to bounce off it.
                # if an enemy ball hits the bottom of the screen, it is deleted.
                camera.draw(each_eb)
                if each_eb.touches(char):
                    deleting_keys_list_eb.append(each_eb)
                    hp -= 1
                    # this makes hp go down if an enemy ball hits the player, and the enemy
                    # ball disappears too

        char.move_to_stop_overlapping(court_line)
        for bound in bounds:
            char.move_to_stop_overlapping(bound)
            for each in enemies:
                each.move_to_stop_overlapping(bound)
                each.move_to_stop_overlapping(court_line)
        # this prevents the player from crossing the middle line and from going off
        # the sides of the screen anywhere

        if food_count == 270 + 30 * level:
            # at level 1, this is 300, which means one food item spawns every 10 seconds.
            # +30*level adds a second for each level up you go
            food_count = 0
            food = gamebox.from_image(random.randint(10, 790), 100, food_sprite_sheet[1])
            foods[food] = random.randint(1, 5)
            camera.draw(food)
        for each_f, item_number in foods.items():
            # this is the code for alternating between sprites for the food items. Each
            # of the 5 randomly generated possible food items shift between 2 sprites
            # every half second, as seen by 0 to 14 and 15 to 29 when this is running at 30 fps.
            if item_number == 1:  # alternates between slice of cake and full cake
                if 0 <= food_shift_count <= 14:
                    each_f = gamebox.from_image(each_f.x, each_f.y, food_sprite_sheet[93])
                elif 15 <= food_shift_count <= 29:
                    each_f = gamebox.from_image(each_f.x, each_f.y, food_sprite_sheet[94])
            if item_number == 2:  # alternates between ice cream and cupcake
                if 0 <= food_shift_count <= 14:
                    each_f = gamebox.from_image(each_f.x, each_f.y, food_sprite_sheet[95])
                elif 15 <= food_shift_count <= 29:
                    each_f = gamebox.from_image(each_f.x, each_f.y, food_sprite_sheet[88])
            if item_number == 3:  # alternates between green apple and red apple
                if 0 <= food_shift_count <= 14:
                    each_f = gamebox.from_image(each_f.x, each_f.y, food_sprite_sheet[8])
                elif 15 <= food_shift_count <= 29:
                    each_f = gamebox.from_image(each_f.x, each_f.y, food_sprite_sheet[9])
            if item_number == 4:  # alternates between ice cream in cup with or without topping
                if 0 <= food_shift_count <= 14:
                    each_f = gamebox.from_image(each_f.x, each_f.y, food_sprite_sheet[90])
                elif 15 <= food_shift_count <= 29:
                    each_f = gamebox.from_image(each_f.x, each_f.y, food_sprite_sheet[89])
            if item_number == 5:  # alternates between croissant and baguette
                if 0 <= food_shift_count <= 14:
                    each_f = gamebox.from_image(each_f.x, each_f.y, food_sprite_sheet[34])
                elif 15 <= food_shift_count <= 29:
                    each_f = gamebox.from_image(each_f.x, each_f.y, food_sprite_sheet[35])
            camera.draw(each_f)

        deleting_keys_list_food = []
        for each_f, item_number in foods.items():
            for each_pb in player_balls.keys():
                if each_pb.touches(each_f):
                    deleting_keys_list_pb.append(each_pb)
                    deleting_keys_list_food.append(each_f)
                    if hp < 3:  # restores 1 hp for hitting a food item unless you're at full hp
                        hp += 1
        for hit_food in deleting_keys_list_food:
            del foods[hit_food]
        for hit_pb in deleting_keys_list_pb:
            del player_balls[hit_pb]
        for hit_eb in deleting_keys_list_eb:
            del enemy_balls[hit_eb]
            # the dictionaries were having trouble since deleting keys during iteration causes
        # problems, so instead, the keys that were hit/hit something were saved to a list for
        # reference, and then right outside of the for loop the keys (and their values)
        # from the dictionary are deleted using the list as a reference

    hp_red_bar = gamebox.from_color(
        ((hp_bar_side_distance_from_lbound + 2 * hp_bar_width) / 2 - hp_bar_side_distance_from_lbound) * (
                    hp / 3) + hp_bar_side_distance_from_lbound,
        25, "red", hp_bar_width * hp / 3, 25)
    # the code above may seem somewhat complicated, but what it's doing is only changes
    # to the x position and the width since both change as hp is reduced. The width
    # is just proportional to the amount of health left, and since the hp is reduced
    # by 1/3 each time, this means it is multiplied by hp/3 (a variable for maximum
    # hp could technically be in place of the 3 just like how some other variables are
    # used despite changes not being made midway through the project, but having 3 health
    # was pretty definitive, whereas things like the hp bar position was not).
    # the x position of the red bar is slightly more complicated. It also involves
    # multiplying by hp/3 at one point, but before that calculations have to be done
    # to make it from 0 to 50 max instead of 50 to 100 max since it's hard to reduce
    # by fractions when there's an extra 50 complicating things (this is then added back
    # at the end).
    camera.draw(hp_red_bar)
    # could also look into using heart sprites rather than a bar, but either's fine

    if hp == 0:
        game_on = False
        camera.draw(game_over_text)
        # if your health hits 0, the game is over.

    camera.display()


ticks_per_second = 30
gamebox.timer_loop(ticks_per_second, tick)