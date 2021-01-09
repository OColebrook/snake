"""
 Snake Game template, using classes.

 Derived from:
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

"""

import pygame
import random

# --- Globals ---
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (169,169,169)

#done
global done
done = False
global Game_Over


# Screen size
height = 700
width = 600

# Margin between each segment
segment_margin = 3

# Set the width and height of each snake segment
segment_width = min(height, width) / 40 - segment_margin
segment_height = min(height, width) / 40 - segment_margin

# Set initial speed
x_change = segment_width + segment_margin
y_change = 0


class Snake():
    """ Class to represent one snake. """

    # Constructor
    def __init__(self):
        self.segments = []

        self.spriteslist = pygame.sprite.Group()

        for i in range(15):
            x = (segment_width + segment_margin) * 30 - (segment_width + segment_margin) * i
            y = (segment_height + segment_margin) * 2
            segment = Segment(x, y)
            self.segments.append(segment)
            self.spriteslist.add(segment)


    def move(self):

        # Figure out where new segment will be
        x = self.segments[0].rect.x + x_change
        y = self.segments[0].rect.y + y_change

        # Don't move off the screen

        if 0 <= x <= width - segment_width and 0 <= y <= height - segment_height:
            # Insert new segment into the list
            segment = Segment(x, y)
            self.segments.insert(0, segment)
            self.spriteslist.add(segment)
            # Get rid of last segment of the snake
            # .pop() command removes last item in list
            old_segment = self.segments.pop()
            self.spriteslist.remove(old_segment)



        else:
            print("done")
            return False



    def grow(self, by_size=1):
        # we grow against self.direction
        # so if we're moving up, the tail grows down
        x = self.segments[-1].rect.x
        y = self.segments[-1].rect.y

        if direction == 'up':
            y = self.segments[-1].rect.y + segment_height
        elif direction == 'down':
            y = self.segments[-1].rect.y - segment_height
        elif direction == 'left':
            x += self.segments[-1].rect.x + segment_width
        elif direction == 'right':
            x = self.segments[-1].rect.x - segment_width




        for i in range(by_size):
            # new body part needs to be added at the tail-position

            self.segments.append(Segment(x, y))





class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of a snake. """

    # Constructor
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)

        # Set top-left corner of the bounding rectangle to be the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class enemy_Snake():
    """ Class to represent the enemy snake. """

    # Constructor
    def __init__(self):
        self.segments = []
        self.spriteslist = pygame.sprite.Group()
        self.enemy_moves = 0
        self.x_change = 1
        self.y_change = 1
        for i in range(8):
            x = (segment_width + segment_margin) * 35 - (segment_width + segment_margin) * i
            y = (segment_height + segment_margin) * 20
            segment = enemy_Segment(x, y)
            self.segments.append(segment)
            self.spriteslist.add(segment)

    def move(self):


        if self.enemy_moves == 8:
            direction2 = random.randint(0, 4)
            if direction2 == 1:
                self.x_change = (segment_width + segment_margin) * -1
                self.y_change = 0
                self.enemy_moves = 0


            if direction2 == 2:
                self.x_change = (segment_width + segment_margin)
                self.y_change = 0
                self.enemy_moves = 0


            if direction2 == 3:
                self.x_change = 0
                self.y_change = (segment_height + segment_margin) * -1
                self.enemy_moves = 0


            if direction2 == 4:
                self.x_change = 0
                self.y_change = (segment_height + segment_margin)
                self.enemy_moves = 0

        else:
            self.enemy_moves = self.enemy_moves + 1


        # Figure out where new segment will be
        x = self.segments[0].rect.x + self.x_change
        y = self.segments[0].rect.y + self.y_change

        # Don't move off the screen

        if 0 <= x <= width - segment_width and 0 <= y <= height - segment_height:
            # Insert new segment into the list
            segment = enemy_Segment(x, y)
            self.segments.insert(0, segment)
            self.spriteslist.add(segment)
            # Get rid of last segment of the snake
            # .pop() command removes last item in list
            old_segment = self.segments.pop()
            self.spriteslist.remove(old_segment)



        else:
            if self.segments[-1].rect.x <= 100 or self.segments[0].rect.x <= 100:
                direction2 = 4
                self.enemy_moves = 8

            if self.segments[-1].rect.x >= 400 or self.segments[0].rect.x >= 400:
                direction2 =  3
                self.enemy_moves = 8

            if self.segments[-1].rect.y <= 100 or self.segments[0].rect.y <= 100:
                direction2 = random.randint(1,2)
                self.enemy_moves = 8

            if self.segments[-1].rect.y >= 400 or self.segments[0].rect.y >= 400:
                direction2 = random.randint(1,2)
                self.enemy_moves = 8






class enemy_Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of a snake. """

    # Constructor
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(GREY)

        # Set top-left corner of the bounding rectangle to be the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Food():
    """ Class to represent food. """

    # Constructor
    def __init__(self):
        self.food = []
        self.spriteslist = pygame.sprite.Group()

        for i in range(20):
            x = random.randrange(100,500)
            y = random.randrange(100,500)
            food = Food_item(x, y)
            self.food.append(food)
            self.spriteslist.add(food)

    def replenish(self):
        for i in range(20):
            x = random.randrange(100, 500)
            y = random.randrange(100, 500)
            food = Food_item(x, y)
            hit_snake = pygame.sprite.spritecollide(food, my_snake.segments, True)
            if hit_snake:
                print("already in list")

            else:
                self.food.append(food)
                self.spriteslist.add(food)




class Food_item(pygame.sprite.Sprite):

    # Constructor
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(GREEN)

        # Set top-left corner of the bounding rectangle to be the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Obs():
    """ Class to represent food. """

    # Constructor
    def __init__(self):
        self.obs = []
        self.spriteslist = pygame.sprite.Group()

        for i in range(10):
            x = random.randrange(100,500)
            y = random.randrange(100,500)
            obs = Obs_item(x, y)
            self.obs.append(obs)
            self.spriteslist.add(obs)

class Obs_item(pygame.sprite.Sprite):

    # Constructor
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(RED)

        # Set top-left corner of the bounding rectangle to be the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y






# Call this function so the Pygame library can initialize itself
pygame.init()


# Create a 600x600 sized screen
screen = pygame.display.set_mode([width, height])

# Set the title of the window
pygame.display.set_caption('Snake Game')

# Create an initial snake
my_snake = Snake()
my_food = Food()
my_obs = Obs()
my_enemy = enemy_Snake()




#set score and food items:

score = 0
fooditemcount = 20
global direction
global Game_Over
Game_Over = False


clock = pygame.time.Clock()
done = False

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Set the direction based on the key pressed
        # We want the speed to be enough that we move a full
        # segment, plus the margin.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (segment_width + segment_margin) * -1
                y_change = 0
                direction = "left"

            if event.key == pygame.K_RIGHT:
                x_change = (segment_width + segment_margin)
                y_change = 0
                direction = "right"


            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (segment_height + segment_margin) * -1
                direction = "up"

            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (segment_height + segment_margin)
                direction = "down"






    # move snake one step
    my_snake.move()
    my_enemy.move()


    #my_snake.self_collide()



    if my_snake.move() == False:
        Game_Over = True


    hit_list = pygame.sprite.spritecollide(my_snake.segments[0],my_food.spriteslist, True)

    if hit_list:
        print("food")
        fooditemcount = fooditemcount - 1
        score = score + 1
        my_snake.grow()

    if fooditemcount == 5:
        my_food.replenish()
        fooditemcount = fooditemcount+ 25
        print(score)

    hit_list2 = pygame.sprite.spritecollide(my_snake.segments[0], my_obs.spriteslist, True)
    if hit_list2:
        Game_Over = True

    hit_list3 = pygame.sprite.spritecollide(my_snake.segments[0], my_enemy.spriteslist, True)
    if hit_list3:
        Game_Over = True

    hit_list4 = pygame.sprite.spritecollide(my_snake.segments[0], my_snake.segments[2:], False)
    if hit_list4:
        Game_Over = True

    hit_list5 = pygame.sprite.spritecollide(my_enemy.segments[0], my_obs.spriteslist, False)
    if hit_list5:
        my_enemy.enemy_moves = 8





    # -- Draw everything
    # Clear screen
    screen.fill(BLACK)
    my_snake.spriteslist.draw(screen)
    my_food.spriteslist.draw(screen)
    my_obs.spriteslist.draw(screen)
    my_enemy.spriteslist.draw(screen)
    pygame.draw.rect(screen, BLUE, (0, 600, 600, 100))
    pygame.font.init()
    font = pygame.font.SysFont("comicsansms", 28)

    # create an image (Surface) of the text
    text = font.render('Score = ' + str(score), True, (WHITE))
    # get the bounding box for the image get the bounding box for the image
    textrect = text.get_rect()
    # set the position set the position
    textrect.centerx = 300
    textrect.centery = 650
    screen.blit(text, textrect)

    while Game_Over == True:
        screen.fill(BLACK)
        pygame.draw.rect(screen, BLUE, (0, 600, 600, 100))
        font = pygame.font.SysFont("comicsansms", 28)

        # create an image (Surface) of the text
        text = font.render(("Game Over"), True, (WHITE))

        # get the bounding box for the image get the bounding box for the image
        textrect = text.get_rect()
        # set the position set the position
        textrect.centerx = 300
        textrect.centery = 650
        screen.blit(text, textrect)
        font = pygame.font.SysFont("comicsansms", 28)

        # create an image (Surface) of the text
        text = font.render('Score = ' + str(score), True, (WHITE))

        # get the bounding box for the image get the bounding box for the image
        textrect = text.get_rect()
        # set the position set the position
        textrect.centerx = 300
        textrect.centery = 675
        screen.blit(text, textrect)
        break






    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(1)

pygame.quit()