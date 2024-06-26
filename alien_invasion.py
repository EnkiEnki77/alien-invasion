# Its important to write a description of what youre trying to accomplish with your program so you have a 
# general direction to go starting out. YOu can refine later.

# Used to exit the game when player quits
import sys

# Contains functionality to make a game
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self) -> None:
        """Initialize the game and create game resources"""
        # Initializes the background settings required for pygame to work properly
        pygame.init()
        self.clock = pygame.time.Clock()

        self.bg_color = (130, 140, 170)

        # Creates a display window. (1200, 800) is a tuple that defines the dimensions of the window. 
        # We assign the display window to the attribute self.screen so its available in all methods of the class.
        # The object assigned here is called a surface which is something we can display game eleemnts on. Each game
        # element is also its own surface.
        # When we start the game animation loop these surfaces will be redrawn on each iteration of the loop, so we can
        # update the screen based on user input. 
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
    
    # The game is controlled by the run_game method. It contains a while loop that runs continually.
    # The while loop contains an event loop and code that manages screen updates. An event is an action the user performs
    # while playing the game. 
    # To make our program respond to events we write an event loop that listens for events and takes appropriate action 
    # depending on the events that occur
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse events. This is an event loop.   
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    # Make game instance and run the game
    ai = AlienInvasion()
    ai.run_game()