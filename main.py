import pygame
import 


WIDTH =550
background_color =  (251,247,245)

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH , WIDTH))
    pygame.display.set_caption("SUDOKU")
    
    win.fill(background_color)
    
    for i in range(0 ,10) :
        if(i%3 ==0 ):
            pygame.draw.line(win , (0,0 ,0) , (50+ 50*i , 50  ) , (50 + 50*i ,500),6)
            pygame.draw.line(win , (0,0 ,0) , ( 50 , 50+ 50*i  ) , (500  ,50 + 50*i),6)
             
            
            
        pygame.draw.line(win , (0,0 ,0) , (50+ 50*i , 50  ) , (50 + 50*i ,500),2)
        pygame.draw.line(win , (0,0 ,0) , ( 50 , 50+ 50*i  ) , (500  ,50 + 50*i),2)
    pygame.display.update()  
    
    
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT : suduko.py
                pygame.quit()
                return 
    
    
main()