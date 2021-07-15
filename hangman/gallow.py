from asciimatics.screen import Screen, ManagedScreen
from time import sleep


class Gallow:
    '''This class draws the gallow on the screen and tracks the number of mistakes made
    '''
    # Variables used to determine the area to draw things
    row: int
    col: int
    width: int
    height: int

    # Variables used to determine state of the game
    misses: int

    def __init__(self, row: int, col: int, width: int, height: int):
        """
        :param row: The highest position to start drawing
        :param col: The left most position to start drawing
        :param width: The width to draw the gallow at (minimum 14)
        :param height: The height to draw the gallow at (minimum 11)
        """
        self.row = row
        self.col = col
        if width < 14:
            self.width = 14
        else:
            self.width = width
        if height < 11:
            self.height = 11
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
        :param screen: The screen to draw the scene
        """
        self.draw_gallow(screen)
        self.draw_human(screen)

    def draw_gallow(self, screen: Screen):
        """
        :param screen: The screen to draw the gallow on
        """
        rope = self.height - 6 - 2
        rope = rope // 2 + rope % 2

        screen.move(self.row, self.col+self.height)
        screen.draw(self.row+self.width+1, self.col+self.height, '0')
        screen.move(self.row+self.width//2, self.col+self.height)
        screen.draw(self.row+self.width//2, self.col, '|')
        screen.draw(self.row+self.width-3, self.col, '-')
        screen.move(self.row+self.width-3, self.col+1)
        screen.draw(self.row+self.width-3, self.col+rope, '|', thin=True)

    def draw_human(self, screen: Screen):
        """
        :param screen: The screen to draw the human
        """
        middleBody = self.row + self.width-3
        rope = self.height - 6 - 2
        rope = rope // 2 + rope % 2

        if self.misses > 0:
            screen.print_at("/▔\\", middleBody-1, self.col+rope)
            screen.print_at("\\_/", middleBody-1, self.col+rope+1)
            if self.misses > 1:
                screen.move(middleBody, self.col+rope+2)
                screen.draw(middleBody, self.col+rope+5, '|')
                if self.misses > 2:
                    screen.print_at('\\', middleBody+1, self.col+rope+2)
                    screen.print_at('\\', middleBody+2, self.col+rope+3)
                    if self.misses > 3:
                        screen.print_at('/', middleBody-1, self.col+rope+2)
                        screen.print_at('/', middleBody-2, self.col+rope+3)
                        if self.misses > 4:
                            screen.print_at('\\', middleBody+1, self.col+rope+5)
                            screen.print_at('\\', middleBody+2, self.col+rope+6)
                            if self.misses > 5:
                                screen.print_at('/', middleBody-1, self.col+rope+5)
                                screen.print_at('/', middleBody-2, self.col+rope+6)


if __name__ == '__main__':
    with ManagedScreen() as screen:
        n1 = Gallow(5, 5, 14, 11)
        n1.render(screen)
        screen.refresh()
        sleep(2)
        n1.misses = 10
        n1.render(screen)
        n2 = Gallow(5, 17, 14, 11)
        n2.render(screen)
        n3 = Gallow(20, 5, 15, 22)
        n3.miss()
        n3.miss()
        n3.render(screen)
        screen.refresh()
        sleep(10)
