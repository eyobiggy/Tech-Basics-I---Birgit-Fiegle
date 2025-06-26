import pygame

# button class
class Button:
    def __init__(self, rect, text, font, default_color, hover_color, text_color=(0, 0, 0)):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = font
        self.default_color = default_color
        self.hover_color = hover_color
        self.text_color = text_color

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.default_color
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        text_surf = self.font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

# setup
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Generative Art Project GUI")
clock = pygame.time.Clock()

# colours and font
BG_COLOR = (30, 30, 30)
FONT = pygame.font.SysFont("arial", 24)
TEXT_FONT = pygame.font.SysFont("arial", 22)
TEXT_COLOR = (255, 255, 255)

# create the button
button = Button(
    rect=(300, 250, 200, 60),
    text="Generate",
    font=FONT,
    default_color=(100, 100, 255),
    hover_color=(170, 170, 255),
    text_color=(0, 0, 0)
)

# text if clicked
show_message = False
message_text = "This button will be part of my final project.\nWhen everything is done, it will generate an abstract artwork."

# main loop
running = True
while running:
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if button.is_clicked(event):
            show_message = True

    # draw button
    button.draw(screen)

    # show text when button is clicked
    if show_message:
        lines = message_text.split('\n')
        for i, line in enumerate(lines):
            rendered = TEXT_FONT.render(line, True, TEXT_COLOR)
            screen.blit(rendered, (WIDTH // 2 - rendered.get_width() // 2, 350 + i * 30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

### this button will be part of my final project - a part of code where I could include all the requirements for the weekly assignment.
### later it will generate an abstract artwork, this code is just to demonstrate