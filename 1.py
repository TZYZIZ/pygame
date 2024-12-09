import sys
import pygame


def draw_x(screen):
    screen.fill((0, 0, 0))


    x1, x2 = 0, screen.get_width()
    y1, y2 = 0, screen.get_height()


    color = pygame.Color(255, 255, 255)
    pygame.draw.line(screen, color, (x1, y1), (x2, y2), 5)
    pygame.draw.line(screen, color, (x1, y2), (x2, y1), 5)


def get_size(data):
    try:
        w, h = [int(x) for x in data.split()]
        if w < 60 or h < 10:
            w, h = 500, 500
    except Exception:
        print("«Неправильный формат ввода»")
        sys.exit()
    return w, h


if __name__ == '__main__':
    pygame.init()
    width, height = get_size(input())
    size = width, height
    screen = pygame.display.set_mode(size)
    draw_x(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:

        pygame.display.flip()

    sys.exit()
