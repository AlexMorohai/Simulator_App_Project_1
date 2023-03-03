import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
image1 = pygame.image.load('ShoppingCart.png')
image2 = pygame.image.load('ShoppingCart_empty.png')
image1_pos = (0, 0)
image2_pos = (100, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # get input coordinates from the user
    coords_input = input("Enter ten coordinates separated by commas (x1, y1, x2, y2, x3, y3, x4, y4, x5, y5): ")
    x1, y1, x2, y2, x3, y3, x4, y4, x5, y5 = map(int, coords_input.split(','))
    speed = x5  # speed of image movement

    # calculate the direction vector and distance between the starting and destination positions of image1
    dir_vec1 = pygame.math.Vector2(x2 - x1, y2 - y1)
    distance1 = dir_vec1.length()

    # calculate the direction vector and distance between the starting and destination positions of image2
    dir_vec2 = pygame.math.Vector2(x4 - x3, y4 - y3)
    distance2 = dir_vec2.length()

    # move image1 towards its destination position using linear interpolation
    if distance1 > 0:
        dir_vec1.normalize_ip()
        image1_pos += dir_vec1 * min(distance1, speed)

    # move image2 towards its destination position using linear interpolation
    if distance2 > 0:
        dir_vec2.normalize_ip()
        image2_pos += dir_vec2 * min(distance2, speed)

    # draw both images at their current positions
    screen.blit(image1, image1_pos)
    screen.blit(image2, image2_pos)

    pygame.display.update()