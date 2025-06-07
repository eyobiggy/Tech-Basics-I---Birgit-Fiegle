import pygame
import random

class Object:

    def __init__(self, _x, _y, img):
        self._x = _x
        self._y = _y
        self.img = img

    def draw(self):
        screen.blit(self.img, (self.pos_x, self.pos_y))

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_position(self):
        return (self._x, self._y)

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def set_position(self, x, y):
        self._x = x
        self._y = y

class PuzzlePiece(Object):

    def __init__(self, _x, _y, _width, _height, img, piece_id, _selected):
        super().__init__(_x, _y, img)
        self._id = piece_id
        self._selected = False
        self._width = _width
        self._height = _height

    def get_id(self):
        return self._id

    def is_selected(self):
        return self._selected

    def set_selected(self, _selected):
        self._selected = _selected

    def toggle_selected(self):
        self._selected = not self._selected

    def move(self,dx,dy):
        new_x = self.get_x() + dx
        new_y = self.get_y() + dy
        self.set_position(new_x, new_y)

    def contains (self, x, y):
        return (self.get_x() <= x <= self.get_x() + self._width) and \
               (self.get_y() <= y <= self.get_y() + self._height)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,700))
        pygame.display.set_caption('puzzle game :)')

        pp1 = pygame.image.load("puzzle pictures/01.jpeg").convert_alpha()
        pp2 = pygame.image.load("puzzle pictures/02.jpeg").convert_alpha()
        pp3 = pygame.image.load("puzzle pictures/03.jpeg").convert_alpha()
        pp4 = pygame.image.load("puzzle pictures/04.jpeg").convert_alpha()
        pp5 = pygame.image.load("puzzle pictures/05.jpeg").convert_alpha()
        pp6 = pygame.image.load("puzzle pictures/06.jpeg").convert_alpha()
        pp7 = pygame.image.load("puzzle pictures/07.jpeg").convert_alpha()
        pp8 = pygame.image.load("puzzle pictures/08.jpeg").convert_alpha()
        pp9 = pygame.image.load("puzzle pictures/09.jpeg").convert_alpha()

        self.clock = pygame.time.Clock()
        self.running = True

        self.pieces = [
            PuzzlePiece(random.randint(30,1170),random.randint(30, 670),179,166,pp1,1, False),
            PuzzlePiece(random.randint(30,1170),random.randint(30,670),179,166,pp2,2, False),
            PuzzlePiece(random.randint(30,1170),random.randint(30, 670), 179, 166, pp3, 3, False),
            PuzzlePiece(random.randint(30,1170),random.randint(30, 670), 179, 166, pp4, 4, False),
            PuzzlePiece(random.randint(30,1170),random.randint(30, 670), 179, 166, pp5, 5, False),
            PuzzlePiece(random.randint(30,1170),random.randint(30, 670), 179, 166, pp6, 6, False),
            PuzzlePiece(random.randint(30,1170),random.randint(30, 670), 179, 166, pp7, 7, False),
            PuzzlePiece(random.randint(30,1170),random.randint(30, 670), 179, 166, pp8, 8, False),
            PuzzlePiece(random.randint(30,1170),random.randint(30, 670), 179, 166, pp9, 9, False)
        ]
        self.selected_piece = None

    def run(self):
        while self.running:
            self.clock.tick(20)
            self.handle_events()

            keys = pygame.key.get_pressed()
            if self.selected_piece:
                if keys[pygame.K_LEFT]:
                    self.selected_piece.move(-3,0)
                if keys[pygame.K_RIGHT]:
                    self.selected_piece.move(3,0)
                if keys[pygame.K_UP]:
                    self.selected_piece.move(0,-3)
                if keys[pygame.K_DOWN]:
                    self.selected_piece.move(0,3)

            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                self.handle_mouse_click(x,y)

            elif event.type == pygame.KEYDOWN:
                self.handle_keypress(event.key)

    def handle_mouse_click(self, x, y):
        for piece in self.pieces:
            if piece.contains(x, y):
                if self.selected_piece:
                    self.selected_piece.set_selected(False)
                self.selected_piece = piece
                piece.set_selected(True)
                break

    def handle_keypress(self, key):
        if key == pygame.K_LEFT:
            self.selected_piece.move(-1, 0)
        elif key == pygame.K_RIGHT:
            self.selected_piece.move(1, 0)
        elif key == pygame.K_UP:
            self.selected_piece.move(0, -1)
        elif key == pygame.K_DOWN:
            self.selected_piece.move(0, 1)

    def draw(self):
        self.screen.fill((255, 255, 255))
        for piece in self.pieces:
            self.screen.blit(piece.img, piece.get_position())
            if piece.is_selected():
                pygame.draw.rect(self.screen, (255,0,0),(piece.get_x(), piece.get_y(),piece._width, piece._height),3)
        pygame.display.flip()

if __name__ == "__main__":
    game = Game()
    game.run()

### INSTRUCTIONS ###
# use the mouse to select a puzzle piece
# use the arrow keys to move a selected puzzle piece up, down, left or right



### I used Chat GBT to:
# debug
# help me find a good code structure for my idea
# make parts of the PuzzlePiece class and the Game class, mainly when it comes to the mouseclick parts
# find out how to keep a piece moving when a key is pressed longer