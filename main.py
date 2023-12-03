import pygame

WIDTH = 600
background_color =  (245,205,200)

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH , WIDTH))
    pygame.display.set_caption("SUDOKU")
    
    
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                return 
    
    
main()
