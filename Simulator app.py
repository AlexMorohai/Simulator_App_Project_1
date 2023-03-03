import pygame

# initialize pygame app

pygame.init()
# create Screen
screen = pygame.display.set_mode((800, 800))


# Input text Title program, customer order and title orders(wearhouse)
pygame.display.set_caption('pygame text!')
font = pygame.font.SysFont('timesnewroman', 25, italic=True, bold=True)
text = font.render('Simulator App', True, (83, 134, 139))
textrect = text.get_rect()
textrect.center = (440, 25)

# text customer
text_c = font.render('Customer order', True, (83, 134, 139))
textrect_c = text_c.get_rect()
textrect_c.center = (80, 780)


# Title and Icon
pygame.display.set_caption('SmartMarket_RoboSimulator')
icon = pygame.image.load('IconApp.png')

# set frame of icon
pygame.display.set_icon(icon)

# ShoppingCart

image = pygame.image.load("ShoppingCart.png")
# Define the initial position of the image
x, y = 0, 0

# Set the speed of the image
speed = 1


# OnlineShop Icon
OnlineShopImg_1 = pygame.image.load('OnlineShop_Icon.png')
onlineSX_1 = 50
onlineSY_1 = 700


def onlineshop(x, y):
    screen.blit(OnlineShopImg_1, (x, y))


# whearhouse 1
WhearhouseImg_1 = pygame.image.load('target.png')
targetX_1 = 250
targetY_1 = 100


def wearhouse_1(x, y):
    screen.blit(WhearhouseImg_1, (x, y))


font = pygame.font.SysFont('timesnewroman', 15, italic=True, bold=True)
text_1 = font.render('L1', True, (39, 64, 139))
textrect_1 = text_1.get_rect()
textrect_1.center = (285, 90)

# whearhouse 2
WhearhouseImg_2 = pygame.image.load('target.png')
targetX_2 = 350
targetY_2 = 100


def wearhouse_2(x, y):
    screen.blit(WhearhouseImg_2, (x, y))


font = pygame.font.SysFont('timesnewroman', 15, italic=True, bold=True)
text_2 = font.render('L2', True, (39, 64, 139))
textrect_2 = text_2.get_rect()
textrect_2.center = (385, 90)

# whearhouse 3
WhearhouseImg_3 = pygame.image.load('target.png')
targetX_3 = 450
targetY_3 = 100


def wearhouse_3(x, y):
    screen.blit(WhearhouseImg_2, (x, y))


font = pygame.font.SysFont('timesnewroman', 15, italic=True, bold=True)
text_3 = font.render('L3', True, (39, 64, 139))
textrect_3 = text_3.get_rect()
textrect_3.center = (485, 90)

# whearhouse 4
WhearhouseImg_4 = pygame.image.load('target.png')
targetX_4 = 550
targetY_4 = 100


def wearhouse_4(x, y):
    screen.blit(WhearhouseImg_2, (x, y))


font = pygame.font.SysFont('timesnewroman', 15, italic=True, bold=True)
text_4 = font.render('L4', True, (39, 64, 139))
textrect_4 = text_4.get_rect()
textrect_4.center = (585, 90)


# whearhouse 5
WhearhouseImg_5 = pygame.image.load('target.png')
targetX_5 = 250
targetY_5 = 200


def wearhouse_5(x, y):
    screen.blit(WhearhouseImg_2, (x, y))


font = pygame.font.SysFont('timesnewroman', 15, italic=True, bold=True)
text_5 = font.render('C1', True, (39, 64, 139))
textrect_5 = text_5.get_rect()
textrect_5.center = (285, 190)


# whearhouse 6
WhearhouseImg_6 = pygame.image.load('target.png')
targetX_6 = 350
targetY_6 = 200


def wearhouse_6(x, y):
    screen.blit(WhearhouseImg_2, (x, y))


font = pygame.font.SysFont('timesnewroman', 15, italic=True, bold=True)
text_6 = font.render('C2', True, (39, 64, 139))
textrect_6 = text_6.get_rect()
textrect_6.center = (385, 190)

# whearhouse 7
WhearhouseImg_7 = pygame.image.load('target.png')
targetX_7 = 450
targetY_7 = 200


def wearhouse_7(x, y):
    screen.blit(WhearhouseImg_2, (x, y))


font = pygame.font.SysFont('timesnewroman', 15, italic=True, bold=True)
text_7 = font.render('C3', True, (39, 64, 139))
textrect_7 = text_7.get_rect()
textrect_7.center = (485, 190)

# whearhouse 8
WhearhouseImg_8 = pygame.image.load('target.png')
targetX_8 = 550
targetY_8 = 200


def wearhouse_8(x, y):
    screen.blit(WhearhouseImg_2, (x, y))


font = pygame.font.SysFont('timesnewroman', 15, italic=True, bold=True)
text_8 = font.render('C4', True, (39, 64, 139))
textrect_8 = text_8.get_rect()
textrect_8.center = (585, 190)

# whearhouse 9
WhearhouseImg_9 = pygame.image.load('target.png')
targetX_9 = 250
targetY_9 = 300


def wearhouse_9(x, y):
    screen.blit(WhearhouseImg_2, (x, y))


font = pygame.font.SysFont('timesnewroman', 15, italic=True, bold=True)
text_9 = font.render('P1', True, (39, 64, 139))
textrect_9 = text_9.get_rect()
textrect_9.center = (285, 290)


# whearhouse 10
WhearhouseImg_10 = pygame.image.load('target.png')
targetX_10 = 350
targetY_10 = 300


def wearhouse_10(x, y):
    screen.blit(WhearhouseImg_2, (x, y))


font = pygame.font.SysFont('timesnewroman', 15, italic=True, bold=True)
text_10 = font.render('P2', True, (39, 64, 139))
textrect_10 = text_10.get_rect()
textrect_10.center = (385, 290)

# whearhouse 11
WhearhouseImg_11 = pygame.image.load('target.png')
targetX_11 = 450
targetY_11 = 300


def wearhouse_11(x, y):
    screen.blit(WhearhouseImg_2, (x, y))


font = pygame.font.SysFont('timesnewroman', 15, italic=True, bold=True)
text_11 = font.render('P3', True, (39, 64, 139))
textrect_11 = text_11.get_rect()
textrect_11.center = (485, 290)

# whearhouse 12
WhearhouseImg_12 = pygame.image.load('target.png')
targetX_12 = 550
targetY_12 = 300


def wearhouse_12(x, y):
    screen.blit(WhearhouseImg_2, (x, y))


font = pygame.font.SysFont('timesnewroman', 15, italic=True, bold=True)
text_12 = font.render('P4', True, (39, 64, 139))
textrect_12 = text_12.get_rect()
textrect_12.center = (585, 290)

# whearhouse 13
WhearhouseImg_13 = pygame.image.load('target.png')
targetX_13 = 250
targetY_13 = 400


def wearhouse_13(x, y):
    screen.blit(WhearhouseImg_2, (x, y))


font = pygame.font.SysFont('timesnewroman', 15, italic=True, bold=True)
text_13 = font.render('M1', True, (39, 64, 139))
textrect_13 = text_13.get_rect()
textrect_13.center = (285, 390)

# whearhouse 14
WhearhouseImg_14 = pygame.image.load('target.png')
targetX_14 = 350
targetY_14 = 400


def wearhouse_14(x, y):
    screen.blit(WhearhouseImg_2, (x, y))


font = pygame.font.SysFont('timesnewroman', 15, italic=True, bold=True)
text_14 = font.render('M2', True, (39, 64, 139))
textrect_14 = text_14.get_rect()
textrect_14.center = (385, 390)

# whearhouse 15
WhearhouseImg_15 = pygame.image.load('target.png')
targetX_15 = 450
targetY_15 = 400


def wearhouse_15(x, y):
    screen.blit(WhearhouseImg_2, (x, y))


font = pygame.font.SysFont('timesnewroman', 15, italic=True, bold=True)
text_15 = font.render('M3', True, (39, 64, 139))
textrect_15 = text_15.get_rect()
textrect_15.center = (485, 390)

# whearhouse 16
WhearhouseImg_16 = pygame.image.load('target.png')
targetX_16 = 550
targetY_16 = 400


def wearhouse_16(x, y):
    screen.blit(WhearhouseImg_2, (x, y))


font = pygame.font.SysFont('timesnewroman', 15, italic=True, bold=True)
text_16 = font.render('M4', True, (39, 64, 139))
textrect_16 = text_16.get_rect()
textrect_16.center = (585, 390)

# whearhouse 17
WhearhouseImg_17 = pygame.image.load('target.png')
targetX_17 = 250
targetY_17 = 500


def wearhouse_17(x, y):
    screen.blit(WhearhouseImg_2, (x, y))


font = pygame.font.SysFont('timesnewroman', 15, italic=True, bold=True)
text_17 = font.render('B1', True, (39, 64, 139))
textrect_17 = text_17.get_rect()
textrect_17.center = (285, 490)

# whearhouse 18
WhearhouseImg_18 = pygame.image.load('target.png')
targetX_18 = 350
targetY_18 = 500


def wearhouse_18(x, y):
    screen.blit(WhearhouseImg_2, (x, y))


font = pygame.font.SysFont('timesnewroman', 15, italic=True, bold=True)
text_18 = font.render('B2', True, (39, 64, 139))
textrect_18 = text_18.get_rect()
textrect_18.center = (385, 490)

# whearhouse 19
WhearhouseImg_19 = pygame.image.load('target.png')
targetX_19 = 450
targetY_19 = 500


def wearhouse_19(x, y):
    screen.blit(WhearhouseImg_2, (x, y))


font = pygame.font.SysFont('timesnewroman', 15, italic=True, bold=True)
text_19 = font.render('B3', True, (39, 64, 139))
textrect_19 = text_19.get_rect()
textrect_19.center = (485, 490)

# whearhouse 20
WhearhouseImg_20 = pygame.image.load('target.png')
targetX_20 = 550
targetY_20 = 500


def wearhouse_20(x, y):
    screen.blit(WhearhouseImg_2, (x, y))


font = pygame.font.SysFont('timesnewroman', 15, italic=True, bold=True)
text_20 = font.render('B4', True, (39, 64, 139))
textrect_20 = text_20.get_rect()
textrect_20.center = (585, 490)


# Game Loop for running then close it
running = True
while running:

    # RGB
    c = screen.fill((224, 238, 238))
    screen.blit(text, textrect)
    screen.blit(text_c, textrect_c)
    screen.blit(text_1, textrect_1)
    screen.blit(text_2, textrect_2)
    screen.blit(text_3, textrect_3)
    screen.blit(text_4, textrect_4)
    screen.blit(text_5, textrect_5)
    screen.blit(text_6, textrect_6)
    screen.blit(text_7, textrect_7)
    screen.blit(text_8, textrect_8)
    screen.blit(text_9, textrect_9)
    screen.blit(text_10, textrect_10)
    screen.blit(text_11, textrect_11)
    screen.blit(text_12, textrect_12)
    screen.blit(text_13, textrect_13)
    screen.blit(text_14, textrect_14)
    screen.blit(text_15, textrect_15)
    screen.blit(text_16, textrect_16)
    screen.blit(text_17, textrect_17)
    screen.blit(text_18, textrect_18)
    screen.blit(text_19, textrect_19)
    screen.blit(text_20, textrect_20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(image, (x, y))

    # update uploud icons
    onlineshop(onlineSX_1, onlineSY_1)
    wearhouse_1(targetX_1, targetY_1)
    wearhouse_2(targetX_2, targetY_2)
    wearhouse_3(targetX_3, targetY_3)
    wearhouse_4(targetX_4, targetY_4)
    wearhouse_5(targetX_5, targetY_5)
    wearhouse_6(targetX_6, targetY_6)
    wearhouse_7(targetX_7, targetY_7)
    wearhouse_8(targetX_8, targetY_8)
    wearhouse_9(targetX_9, targetY_9)
    wearhouse_10(targetX_10, targetY_10)
    wearhouse_11(targetX_11, targetY_11)
    wearhouse_12(targetX_12, targetY_12)
    wearhouse_13(targetX_13, targetY_13)
    wearhouse_14(targetX_14, targetY_14)
    wearhouse_15(targetX_15, targetY_15)
    wearhouse_16(targetX_16, targetY_16)
    wearhouse_17(targetX_17, targetY_17)
    wearhouse_18(targetX_18, targetY_18)
    wearhouse_19(targetX_19, targetY_19)
    wearhouse_20(targetX_20, targetY_20)
    pygame.display.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed



