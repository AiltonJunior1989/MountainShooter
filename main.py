import pygame

print('Setup start')
pygame.init()
print('Setup end')
window = pygame.display.set_mode(size=(600, 480))

while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # close window
            quit()  # end game
