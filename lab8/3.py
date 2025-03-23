import pygame

WIDTH, HEIGHT = 1200, 800
FPS = 90

draw = False
radius = 2
color = 'blue'
mode = 'pen'

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Paint')
clock = pygame.time.Clock()
screen.fill(pygame.Color('white'))
font = pygame.font.SysFont('None', 60)

def drawLine(screen, start, end, width, color):
    pygame.draw.line(screen, pygame.Color(color), start, end, width)

def drawCircle(screen, start, end, width, color):
    center = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)
    radius = max(abs(end[0] - start[0]), abs(end[1] - start[1])) // 2
    pygame.draw.circle(screen, pygame.Color(color), center, radius, width)

def drawRectangle(screen, start, end, width, color):
    rect = pygame.Rect(min(start[0], end[0]), min(start[1], end[1]), abs(end[0] - start[0]), abs(end[1] - start[1]))
    pygame.draw.rect(screen, pygame.Color(color), rect, width)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = 'rectangle'
            if event.key == pygame.K_c:
                mode = 'circle'
            if event.key == pygame.K_p:
                mode = 'pen'
            if event.key == pygame.K_e:
                mode = 'erase'
            if event.key == pygame.K_s:
                mode = 'square'
            if event.key == pygame.K_q:
                screen.fill(pygame.Color('white'))

            if event.key == pygame.K_1:
                color = 'black'
            if event.key == pygame.K_2:
                color = 'green'
            if event.key == pygame.K_3:
                color = 'red'
            if event.key == pygame.K_4:
                color = 'blue'
            if event.key == pygame.K_5:
                color = 'yellow'

        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
            start_pos = event.pos
            prev_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            draw = False
            end_pos = event.pos
            if mode == 'rectangle':
                drawRectangle(screen, start_pos, end_pos, radius, color)
            elif mode == 'circle':
                drawCircle(screen, start_pos, end_pos, radius, color)
            elif mode == 'square':
                size = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                rect = pygame.Rect(start_pos[0], start_pos[1], size, size)
                pygame.draw.rect(screen, pygame.Color(color), rect, radius)

        if event.type == pygame.MOUSEMOTION:
            if draw and mode == 'pen':
                drawLine(screen, prev_pos, event.pos, radius, color)
            elif draw and mode == 'erase':
                drawLine(screen, prev_pos, event.pos, radius, 'white')
            prev_pos = event.pos

    pygame.draw.rect(screen, pygame.Color('white'), (5, 5, 115, 75))
    renderRadius = font.render(str(radius), True, pygame.Color(color))
    screen.blit(renderRadius, (5, 5))

    pygame.display.flip()
    clock.tick(FPS)

