import pygame

#Intialize
pygame.init()
screen=pygame.display.set_mode((1280,720))
pygame.display.set_caption('Hangman')
font = pygame.font.Font('freesansbold.ttf', 32)

#Home screen elements
home_screen = pygame.image.load('home.png').convert()
user_text = pygame.Rect(560,305,165,55)
play_button = pygame.Rect(560,600,160,45)
username=''

def get_cursor():
    cursor_pos=pygame.mouse.get_pos()
    var=0
    for i in cursor_pos:
        if var==0:
            x=i
        else:
            y=i
        var+=1
    cursor=pygame.Rect(x,y,5,5)
    return cursor


def get_username(event):
    global username
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_BACKSPACE:
            username+='\b'
        else:
            username+=event.unicode


def home():

    in_home = True
    user_text_click=False
    while in_home:
        screen.blit(home_screen,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_home = False


            elif event.type == pygame.MOUSEBUTTONDOWN:

                # If the user clicks on username button
                if pygame.Rect.colliderect(user_text,get_cursor()):
                    user_text_click=True
                elif not pygame.Rect.colliderect(user_text,get_cursor()):
                    user_text_click=False

                #If the user clicks on play button
                if pygame.Rect.colliderect(play_button,get_cursor()):
                    print('success')

            elif user_text_click:
                get_username(event)
                print(username)






        pygame.display.update()

home()


