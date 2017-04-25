import pygame

def draw_board(the_board):
    """ Draw a chess board with queens, from the_board. """

    pygame.init()
    colors = [(255,0,0), (0,255,0),(0,0,255)]    # Set up colors [red, black]

    n = len(the_board)         # This is an NxN chess board.
    surface_sz = 480           # Proposed physical surface size.
    sq_sz = surface_sz // n    # sq_sz is length of a square.
    surface_sz = n * sq_sz     # Adjust to exactly fit n squares.

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))
    ball = pygame.image.load('alien1.png')
    
    ball_offset = (sq_sz-ball.get_width()) // 2
    
    while True:
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break
        
        for row in range(n):
            c_indx = row % 3
            for col in range(n):
                the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                
                c_indx = (c_indx + 1) % 3
                
        for (col, row) in enumerate(the_board):
            surface.blit(ball,
                         (col*sq_sz+ball_offset,row*sq_sz+ball_offset))
        
        pygame.display.flip()
            
    pygame.quit()
        
if __name__ == '__main__':
    draw_board([0, 5, 3, 1, 6, 4, 2])    # 7 x 7 to test window size
    draw_board([6, 4, 2, 0, 5, 7, 1, 3])
    draw_board([9, 6, 0, 3, 10, 7, 2, 4, 12, 8, 11, 5, 1])  # 13 x 13
    draw_board([11, 4, 8, 12, 2, 7, 3, 15, 0, 14, 10, 6, 13, 1, 5, 9])