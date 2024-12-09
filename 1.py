import sys
import pygame


def draw_rect(screen):
    screen.fill((0, 0, 0))
    x1, y1 = 1, 1
    w, h = screen.get_width() - 2, screen.get_height() - 2


    color = pygame.Color('red')
    pygame.draw.rect(screen, color, (x1, y1, w, h), 0)


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
    draw_rect(screen)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:

        pygame.display.flip()

    sys.exit()
