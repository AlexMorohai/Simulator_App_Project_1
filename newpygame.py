import pygame

pygame.init()

# Set the width and height of the screen
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Load the image
image = pygame.image.load("ShoppingCart.png")
# Define the initial position of the image
x, y = 0, 0

# Set the speed of the image
speed = 1

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the image on the screen
    screen.blit(image, (x, y))

    # Update the display
    pygame.display.update()

    # Move the image
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
