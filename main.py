import pygame
from defs import *
from pipe import PipeCollection
from bird import BirdCollection

def update_label(data, title, font, x, y, gameDisplay):
    label = font.render('{} {}'.format(title, data), 1, DATA_FONT_COLOR)
    gameDisplay.blit(label, (x, y))
    return y

def update_data_labels(gameDisplay, dt, game_time, score, highest_score, num_iterations, num_alive, font):
    y_pos = 2
    gap = 20
    x_pos = 10
    y_pos = update_label(round(1000/dt, 2), 'FPS', font, x_pos, y_pos + gap, gameDisplay)
    y_pos = update_label(round(game_time/1000, 2), 'Game Time', font, x_pos, y_pos + gap, gameDisplay)
    y_pos = update_label(score, 'Score', font, x_pos, y_pos + gap, gameDisplay)
    y_pos = update_label(highest_score, 'Highest Score', font, x_pos, y_pos + gap, gameDisplay)
    y_pos = update_label(num_iterations, 'Iterations', font, x_pos, y_pos + gap, gameDisplay)
    y_pos = update_label(num_alive, 'Birds alive ', font, x_pos, y_pos + gap, gameDisplay)


def update_score(pipes, score):
    closest_pipe = DISPLAY_W * 2
    for p in pipes:
            if p.pipe_type == PIPE_UPPER and p.rect.right < closest_pipe and p.rect.right > 181:
                closest_pipe = p.rect.right

    # print('Closest Pipe: ', closest_pipe)
    # print('Bird: ', alive_bird.rect.left)
    if(closest_pipe <= 184):
        score += 1

    return score

def update_highest_score(score, highest_score):
    if score > highest_score:
        highest_score = score

    return highest_score

def run_game():

    SCORE = 0
    HIGHEST_SCORE = 0

    pygame.init() #initialize pygame
    gameDisplay = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
    pygame.display.set_caption('Learn to Fly')

    running = True
    bgImg = pygame.image.load(BG_FILENAME)
    pipes = PipeCollection(gameDisplay)
    birds = BirdCollection(gameDisplay)

    pipes.create_new_set()

    label_font = pygame.font.SysFont("monospace", DATA_FONT_SIZE)

    clock = pygame.time.Clock()
    dt = 0
    game_time = 0
    num_iterations = 1

    #pipe section
    #pi = Pipe(gameDisplay, DISPLAY_W, 300, PIPE_LOWER)

    while running:

        dt = clock.tick(FPS)
        game_time += dt

        gameDisplay.blit(bgImg, (0, 0)) #Draw the background image at (0, 0) point


        #Event Section 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                running = False
        
        pipes.update(dt)
        num_alive = birds.update(dt, pipes.pipes)

        if num_alive == 0:
            SCORE = 0
            pipes.create_new_set()
            game_time = 0
            birds.evolve_population()
            num_iterations += 1

        SCORE = update_score(pipes.pipes, SCORE)
        HIGHEST_SCORE = update_highest_score(SCORE, HIGHEST_SCORE)

        update_data_labels(gameDisplay, dt, game_time, SCORE, HIGHEST_SCORE, num_iterations, num_alive, label_font)

        pygame.display.update() #update the display for every iteration


if __name__ == "__main__":
    run_game()