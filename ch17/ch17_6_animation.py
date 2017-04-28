import pygame
import time

def main():
    import random
    rng = random.Random()   # Instantiate a generator
    my_clock = pygame.time.Clock()
    
    pygame.init()    # Prepare the PyGame module for use
    colors = [(255,0,0), (255,255,255)]
    all_sprites = []      # Keep a list of all sprites in the game

    the_board = list(range(8))
    rng.shuffle(the_board)
    n = len(the_board)         # This is an NxN chess board.
    surface_sz = 480           # Proposed physical surface size.
    sq_sz = surface_sz // n    # sq_sz is length of a square.
    surface_sz = n * sq_sz     # Adjust to exactly fit n squares.

    # Create the surface of (width, height), and its window.
    surface = pygame.display.set_mode((surface_sz, surface_sz))
    

    # Load an image to draw. Substitute your own.
    # PyGame handles gif, jpg, png, etc. image types.
    ball = pygame.image.load("alien1.png")
    ball_offset = (sq_sz-ball.get_width()) // 2


    # Create a sprite object for each queen, and populate our list.
    for (col, row) in enumerate(the_board):
        a_queen = QueenSprite(ball,
                   (col*sq_sz+ball_offset, row*sq_sz+ball_offset))
        all_sprites.append(a_queen)
    
    # Load the sprite sheet
    duke_sprite_sheet = pygame.image.load("duke_spritesheet.png")
    
    # Instantiate two duke instances, put them on the chessboard
    duke1 = DukeSprite(duke_sprite_sheet,(sq_sz*2, 0))
    duke2 = DukeSprite(duke_sprite_sheet,(sq_sz*5, sq_sz))
    
    # Add them to the list of sprites which our game loop manages
    all_sprites.append(duke1)
    all_sprites.append(duke2)
    
    # Create a font for rendering text
    my_font = pygame.font.SysFont('Courier', 16)

    frame_count = 0
    frame_rate = 0
    t0 = time.clock()

    
    while True:

        # Look for an event from keyboard, mouse, joystick, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:   # Window close button clicked?
            break                    # Leave game loop
        if ev.type == pygame.KEYDOWN:   # Only print if it is interesting!
            key = ev.dict['key']
            if key == 27:
                break
            if key == ord('r'):
                colors[0] = (255, 0, 0)
            elif key == ord('g'):
                colors[0] = (0,255,0)
            elif key == ord('b'):
                colors[0] = (0,0,255)
            
        if ev.type == pygame.MOUSEBUTTONDOWN:
            posn_of_click = ev.dict['pos']
            for sprite in all_sprites:
                if sprite.contains_point(posn_of_click):
                    sprite.handle_click()
                    break
        # Do other bits of logic for the game here
        frame_count += 1
        if frame_count % 500 == 0:
            t1 = time.clock()
            frame_rate = 500 / (t1-t0)
            t0 = t1


        for row in range(n):           # Draw each row of the board.
            c_indx = row % 2           # Alternate starting color
            for col in range(n):       # Run through cols drawing squares
                the_square = (col*sq_sz, row*sq_sz, sq_sz, sq_sz)
                surface.fill(colors[c_indx], the_square)
                # Now flip the color index for the next square
                c_indx = (c_indx + 1) % 2
        
        # Ask every sprite to update itself.
        for sprite in all_sprites:
            sprite.update()
            
        # Ask every sprite to draw itself.
        for sprite in all_sprites:
            sprite.draw(surface)

        # Make a new surface with an image of the text
        the_text = my_font.render('Frame = {0},  rate = {1:.2f} fps'
                  .format(frame_count, frame_rate), True, (0,0,0))
        # Copy the text surface to the main surface
        surface.blit(the_text, (10, 10))

        # Now that everything is drawn, put it on display!
        pygame.display.flip()
        my_clock.tick(60)  # Waste time so that frame rate becomes 60 fps
        
    pygame.quit()

class QueenSprite:

    def __init__(self, img, target_posn):
        """ Create and initialize a queen for this
            target position on the board
        """
        self.gravity = 0.98
        self.image = img
        self.target_posn = target_posn
        (x, y) = target_posn
        self.posn = (x, 0)      # Start ball at top of its column
        self.y_velocity = 0     #    with zero initial velocity

    def update(self):
        self.y_velocity += self.gravity
        (x, y) = self.posn
        new_y_posn = y + self.y_velocity
        (target_x, target_y) = self.target_posn
        dist_to_go = target_y - new_y_posn
        if dist_to_go < 0:
            self.y_velocity = -0.6*self.y_velocity
            new_y_posn = target_y      # Move back above floor

        self.posn = (x, new_y_posn)
    
    def contains_point(self, pt):
          """ Return True if my sprite rectangle contains point pt """
          (my_x, my_y) = self.posn
          my_width = self.image.get_width()
          my_height = self.image.get_height()
          (x, y) = pt
          return ( x >= my_x and x < my_x + my_width and
                   y >= my_y and y < my_y + my_height)        

    def handle_click(self):
        self.y_velocity += 0.5*self.y_velocity
    
    def draw(self, target_surface):
        target_surface.blit(self.image, self.posn)

class DukeSprite:

    def __init__(self, img, target_posn):
        self.image = img
        self.posn = target_posn
        self.anim_frame_count = 0
        self.curr_patch_num = 0

    def update(self):
        if self.anim_frame_count > 0:
            self.anim_frame_count = (self.anim_frame_count + 1 ) % 60
            self.curr_patch_num = self.anim_frame_count // 6

    def draw(self, target_surface):
        patch_rect = (self.curr_patch_num * 50, 0,
                        50, self.image.get_height())
        target_surface.blit(self.image, self.posn, patch_rect)
    
    def handle_click(self):
        if self.anim_frame_count == 0:
            self.anim_frame_count = 5

    def contains_point(self, pt):
          """ Return True if my sprite rectangle contains point pt """
          (my_x, my_y) = self.posn
          my_width = self.image.get_width() / 10
          my_height = self.image.get_height()
          (x, y) = pt
          return ( x >= my_x and x < my_x + my_width and
                   y >= my_y and y < my_y + my_height)        
          

main()