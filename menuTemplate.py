# Pygame Template File
# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame

pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)
RED = (200, 50, 0)
BRIGHT_RED = (255, 50, 0)
BLUE = (0, 115, 200)
BRIGHT_BLUE = (0, 115, 255)
ORANGE = (255, 150, 0)

# Open a new window
# The window is defined as (width, height), measured in pixels
SCREENWIDTH = 800
SCREENHEIGHT = 600

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Button")

# --- Text elements

# Define text for title of game
fontTitle = pygame.font.Font('freesansbold.ttf', 60)
textSurfaceTitle = fontTitle.render('My Awesome Game!', True, BLACK) 
textRectTitle = textSurfaceTitle.get_rect()
textRectTitle.center = (SCREENWIDTH/2, SCREENHEIGHT/6) # place the centre of the text

# Button's font
font = pygame.font.Font ('Comic Sans MS.ttf', 24)

# Play button 
textFacePlay = font.render ("Play", True, BLACK)
textRectPlay = textFacePlay.get_rect()
textRectPlay.center = (SCREENWIDTH/2, SCREENHEIGHT/3 + 25)

# Options button
textFaceOptions = font.render ("Options", True, BLACK)
textRectOptions = textFaceOptions.get_rect()
textRectOptions.center = (SCREENWIDTH/2, SCREENHEIGHT/2 + 25)

# Quit button
textFaceQuit = font.render ("Quit", True, BLACK)
textRectQuit = textFaceQuit.get_rect()
textRectQuit.center = (SCREENWIDTH/2, SCREENHEIGHT * 2/3 + 25)


# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # Get mouse location
    mouse = pygame.mouse.get_pos()
    #print(mouse) # Uncomment to see mouse position in shell

    # Check if mouse is pressed
    click = pygame.mouse.get_pressed()
    #print(click) # Uncomment to see mouse buttons clicked in shell
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(WHITE)

    # Queue shapes to be drawn
    
    # Buttons
    # Play button
    pygame.draw.rect(screen, GREEN, (SCREENWIDTH/2-50, SCREENHEIGHT/3, 100, 50))

     # Options button
    pygame.draw.rect (screen, BLUE, (SCREENWIDTH/2 - 50, SCREENHEIGHT/2, 100, 50))

    # Quit button
    pygame.draw.rect (screen, RED, (SCREENWIDTH/2 - 50, SCREENHEIGHT * 2/3, 100, 50))


    # Text
    screen.blit(textSurfaceTitle, textRectTitle)
    screen.blit (textFacePlay, textRectPlay)
    screen.blit (textFaceOptions, textRectOptions)
    screen.blit (textFaceQuit, textRectQuit)

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
