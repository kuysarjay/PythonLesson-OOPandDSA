# A third-party module is a module created by other developers.
# It is not included with Python by default and must be installed
    # using pip before it can be imported into a program.

# The list of the main pip activities looks as follows:    
    # pip help operation – shows a brief description of pip;
    # pip list – shows a list of the currently installed packages;
    # pip show package_name – shows package_name info including the package's dependencies;
    # pip search anystring – searches through PyPI directories in order to find packages whose names contain anystring;
    # pip install name – installs name system-wide (expect problems when you don't have administrative rights);
    # pip install --user name – installs name for you only; no other platform user will be able to use it;
    # pip install -U name – updates a previously installed package;
    # pip uninstall name – uninstalls a previously installed package.
    
import pygame

run = True
width = 400
height = 100

pygame.init()

screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame",True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2,
                   (height - text.get_height()) // 2))

pygame.display.flip()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT\
            or event.type == pygame.MOUSEBUTTONUP\
                or event.type == pygame.KEYUP:
                    run = False

