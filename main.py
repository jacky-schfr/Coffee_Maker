import pygame

pygame.init()

BROWN = (128, 10, 10)
PORCELAIN = (240, 225, 205)
RED = (240, 128, 128)
GREY = (169, 169, 169)
TURQUOISE = (175, 238, 238)
VIOLET = (216, 191, 216)
BLUE = (65, 105, 225)
MILK_WHITE = (255, 255, 224)

WIDTH = 800
HEIGHT = 800

coffee_value = 0
foam_value = 0

animations = []

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Coffee-Maker")

run = True

clock = pygame.time.Clock()


class InputBox:
    def __init__(self, x, y, user_text, font_size):
        self.X = x
        self.Y = y
        self.user_text = user_text
        self.font_size = font_size

    def rectangle(self):
        return pygame.Rect(self.X, self.Y, 140, 40)

    def base_font(self):
        return pygame.font.Font(None, self.font_size)

    def surface(self):
        base_font = self.base_font()
        return base_font.render(self.user_text, True, BLUE)


start_txt = InputBox(50, 90, 'COFFEE', 40)
stop_txt = InputBox(633, 90, 'RESTART', 40)
foam_text = InputBox(320, 90, 'MILK-FOAM', 35)

while run:
    coffee_fill1 = 660 - coffee_value
    coffee_fill2 = 0 + coffee_value

    screen.fill(VIOLET)

    pygame.draw.rect(screen, PORCELAIN, [250, 300, 300, 400], 0)
    pygame.draw.rect(screen, PORCELAIN, [450, 370, 250, 250], 30)
    coffee = pygame.draw.rect(screen, BROWN, [270, coffee_fill1, 260, coffee_fill2], 0)
    milk = pygame.draw.rect(screen, MILK_WHITE, [270, (coffee_fill1 - foam_value), 260, 0 + foam_value], 0)
    startButton = pygame.draw.ellipse(screen, RED, [30, 30, 150, 150], 0)
    stopButton = pygame.draw.ellipse(screen, GREY, [620, 30, 150, 150], 0)
    foamButton = pygame.draw.ellipse(screen, TURQUOISE, [315, 30, 150, 150], 0)
    screen.blit(start_txt.surface(), start_txt.rectangle())
    screen.blit(stop_txt.surface(), stop_txt.rectangle())
    screen.blit(foam_text.surface(), foam_text.rectangle())
    pygame.display.flip()
    clock.tick(250)

    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

    if pygame.mouse.get_pressed()[0] and startButton.collidepoint(pygame.mouse.get_pos()) and coffee_value <= 280 \
            and (coffee_value + foam_value) <= 400:
        for coffee_value in coffee_fill1, coffee_fill2:
            coffee_value += 1

    if pygame.mouse.get_pressed()[0] and stopButton.collidepoint(pygame.mouse.get_pos()):
        for coffee_value in coffee_fill1, coffee_fill2:
            coffee_value = (coffee_value * 0)
            foam_value = (foam_value * 0)

    if pygame.mouse.get_pressed()[0] and foamButton.collidepoint(pygame.mouse.get_pos()) and coffee_value != 0 \
            and (coffee_value + foam_value) <= 400:
        for foam_value in milk:
            foam_value += 1

pygame.quit()
