from asciimatics.screen import Screen, ManagedScreen
from time import sleep


class Gallow:
    '''This class draws the gallow on the screen and tracks the number of mistakes made
    '''
    # Variables used to determine the area to draw things
    x_pos: int
    y_pos: int
    width: int
    height: int

    # Variables used to determine state of the game
    misses: int

    def __init__(self, x_pos: int, y_pos: int, width: int, height: int):
        """
        :param x_pos: The highest position to start drawing
        :param y_pos: The left most position to start drawing
        :param width: The width to draw the gallow at (minimum 7)
        :param height: The height to draw the gallow at (minimum 4)
        """
        self.x_pos = x_pos
        self.y_pos = y_pos
        if width < 7:
            width = 7
        else:
            self.width = width
        if height < 4:
            self.height = 4
        else:
            self.height = height

        self.misses = 0

    def miss(self) -> bool:
        """
        :return: Returns true while the game can still progress after another miss
        """
        self.misses += 1
        return self.misses < 6

    def render(self, screen: Screen):
        """
        :param screen: The screen to draw the gallow on
        """
        screen.move(self.x_pos, self.y_pos+self.height)
        screen.draw(self.x_pos+self.width, self.y_pos+self.height)
        screen.move(self.x_pos+self.width//2, self.y_pos+self.height)
        screen.draw(self.x_pos+self.width//2, self.y_pos)
        screen.draw(self.x_pos+self.width+1, self.y_pos)
        screen.move(self.x_pos+self.width, self.y_pos+1)
        screen.draw(self.x_pos+self.width, self.y_pos+3, '|')


if __name__ == '__main__':
    with ManagedScreen() as screen:
        n = Gallow(5, 5, 10, 10)
        n.render(screen)
        screen.refresh()
        sleep(10)
