import pygame
import random
import database

#Intialize
database.intialise_db()
pygame.init()
pygame.mixer.init()
time=pygame.time.Clock()
screen=pygame.display.set_mode((1280,720))
pygame.display.set_caption('Hangman')
font = pygame.font.Font('Media/Fonts/abel-regular.ttf', 28)
font2 = pygame.font.Font('Media/Fonts/Raleway-MediumItalic.ttf', 38)

#Home screen elements
home_screen = pygame.image.load('Media/Images/home.png').convert()
textbox = pygame.image.load('Media/Images/textbox.png').convert_alpha()
user_text = pygame.Rect(560,305,165,55)
play_button = pygame.Rect(560,600,160,45)
username=''

#welcome screen elements
transition_screen = pygame.image.load('Media/Images/transition_screen.png').convert()


words = ['able', 'about', 'account', 'acid', 'across', 'act', 'addition', 'adjustment', 'advertisement', 'after', 'again', 'against', 'agreement', 'air', 'all', 'almost', 'among', 'amount', 'amusement', 'and', 'angle', 'angry', 'animal', 'answer', 'ant', 'any', 'apparatus', 'apple', 'approval', 'arch', 'argument', 'arm', 'army', 'art', 'as', 'at', 'attack', 'attempt', 'attention', 'attraction', 'authority', 'automatic', 'awake', 'baby', 'back', 'bad', 'bag', 'balance', 'ball', 'band', 'base', 'basin', 'basket', 'bath', 'be', 'beautiful', 'because', 'bed', 'bee', 'before', 'behaviour', 'belief', 'bell', 'bent', 'berry', 'between', 'bird', 'birth', 'bit', 'bite', 'bitter', 'black', 'blade', 'blood', 'blow', 'blue', 'board', 'boat', 'body', 'boiling', 'bone', 'book', 'boot', 'bottle', 'box', 'boy', 'brain', 'brake', 'branch', 'brass', 'bread', 'breath', 'brick', 'bridge', 'bright', 'broken', 'brother', 'brown', 'brush', 'bucket', 'building', 'bulb', 'burn', 'burst', 'business', 'but', 'butter', 'button', 'by', 'cake', 'camera', 'canvas', 'card', 'care', 'carriage', 'cart', 'cat', 'cause', 'certain', 'chain', 'chalk', 'chance', 'change', 'cheap', 'cheese', 'chemical', 'chest', 'chief', 'chin', 'church', 'circle', 'clean', 'clear', 'clock', 'cloth', 'cloud', 'coal', 'coat', 'cold', 'collar', 'colour', 'comb', 'come', 'comfort', 'committee', 'common', 'company', 'comparison', 'competition', 'complete', 'complex', 'condition', 'connection', 'conscious', 'control', 'cook', 'copper', 'copy', 'cord', 'cork', 'cotton', 'cough', 'country', 'cover', 'cow', 'crack', 'credit', 'crime', 'cruel', 'crush', 'cry', 'cup', 'cup', 'current', 'curtain', 'curve', 'cushion', 'damage', 'danger', 'dark', 'daughter', 'day', 'dead', 'dear', 'death', 'debt', 'decision', 'deep', 'degree', 'delicate', 'dependent', 'design', 'desire', 'destruction', 'detail', 'development', 'different', 'digestion', 'direction', 'dirty', 'discovery', 'discussion', 'disease', 'disgust', 'distance', 'distribution', 'division', 'do', 'dog', 'door', 'doubt', 'down', 'drain', 'drawer', 'dress', 'drink', 'driving', 'drop', 'dry', 'dust', 'ear', 'early', 'earth', 'east', 'edge', 'education', 'effect', 'egg', 'elastic', 'electric', 'end', 'engine', 'enough', 'equal', 'error', 'even', 'event', 'ever', 'every', 'example', 'exchange', 'existence', 'expansion', 'experience', 'expert', 'eye', 'face', 'fact', 'fall', 'false', 'family', 'far', 'farm', 'fat', 'father', 'fear', 'feather', 'feeble', 'feeling', 'female', 'fertile', 'fiction', 'field', 'fight', 'finger', 'fire', 'first', 'fish', 'fixed', 'flag', 'flame', 'flat', 'flight', 'floor', 'flower', 'fly', 'fold', 'food', 'foolish', 'foot', 'for', 'force', 'fork', 'form', 'forward', 'fowl', 'frame', 'free', 'frequent', 'friend', 'from', 'front', 'fruit', 'full', 'future', 'garden', 'general', 'get', 'girl', 'give', 'glass', 'glove', 'go', 'goat', 'gold', 'good', 'government', 'grain', 'grass', 'great', 'green', 'grey', 'grip', 'group', 'growth', 'guide', 'gun', 'hair', 'hammer', 'hand', 'hanging', 'happy', 'harbour', 'hard', 'harmony', 'hat', 'hate', 'have', 'he', 'head', 'healthy', 'hear', 'hearing', 'heart', 'heat', 'help', 'high', 'history', 'hole', 'hollow', 'hook', 'hope', 'horn', 'horse', 'hospital', 'hour', 'house', 'how', 'humour', 'I', 'ice', 'idea', 'if', 'ill', 'important', 'impulse', 'in', 'increase', 'industry', 'ink', 'insect', 'instrument', 'insurance', 'interest', 'invention', 'iron', 'island', 'jelly', 'jewel', 'join', 'journey', 'judge', 'jump', 'keep', 'kettle', 'key', 'kick', 'kind', 'kiss', 'knee', 'knife', 'knot', 'knowledge', 'land', 'language', 'last', 'late', 'laugh', 'law', 'lead', 'leaf', 'learning', 'leather', 'left', 'leg', 'let', 'letter', 'level', 'library', 'lift', 'light', 'like', 'limit', 'line', 'linen', 'lip', 'liquid', 'list', 'little', 'living', 'lock', 'long', 'look', 'loose', 'loss', 'loud', 'love', 'low', 'machine', 'make', 'male', 'man', 'manager', 'map', 'mark', 'market', 'married', 'mass', 'match', 'material', 'may', 'meal', 'measure', 'meat', 'medical', 'meeting', 'memory', 'metal', 'middle', 'military', 'milk', 'mind', 'mine', 'minute', 'mist', 'mixed', 'money', 'monkey', 'month', 'moon', 'morning', 'mother', 'motion', 'mountain', 'mouth', 'move', 'much', 'muscle', 'music', 'nail', 'name', 'narrow', 'nation', 'natural', 'near', 'necessary', 'neck', 'need', 'needle', 'nerve', 'net', 'new', 'news', 'night', 'no', 'noise', 'normal', 'north', 'nose', 'not', 'note', 'now', 'number', 'nut', 'observation', 'of', 'off', 'offer', 'office', 'oil', 'old', 'on', 'only', 'open', 'operation', 'opinion', 'opposite', 'or', 'orange', 'order', 'organization', 'ornament', 'other', 'out', 'oven', 'over', 'owner', 'page', 'pain', 'paint', 'paper', 'parallel', 'parcel', 'part', 'past', 'paste', 'payment', 'peace', 'pen', 'pencil', 'person', 'physical', 'picture', 'pig', 'pin', 'pipe', 'place', 'plane', 'plant', 'plate', 'play', 'please', 'pleasure', 'plough', 'pocket', 'point', 'poison', 'polish', 'political', 'poor', 'porter', 'position', 'possible', 'pot', 'potato', 'powder', 'power', 'present', 'price', 'print', 'prison', 'private', 'probable', 'process', 'produce', 'profit', 'property', 'prose', 'protest', 'public', 'pull', 'pump', 'punishment', 'purpose', 'push', 'put', 'quality', 'question', 'quick', 'quiet', 'quite', 'rail', 'rain', 'range', 'rat', 'rate', 'ray', 'reaction', 'reading', 'ready', 'reason', 'receipt', 'record', 'red', 'regret', 'regular', 'relation', 'religion', 'representative', 'request', 'respect', 'responsible', 'rest', 'reward', 'rhythm', 'rice', 'right', 'ring', 'river', 'road', 'rod', 'roll', 'roof', 'room', 'root', 'rough', 'round', 'rub', 'rule', 'run', 'sad', 'safe', 'sail', 'salt', 'same', 'sand', 'say', 'scale', 'school', 'science', 'scissors', 'screw', 'sea', 'seat', 'second', 'secret', 'secretary', 'see', 'seed', 'seem', 'selection', 'self', 'send', 'sense', 'separate', 'serious', 'servant', 'sex', 'shade', 'shake', 'shame', 'sharp', 'sheep', 'shelf', 'ship', 'shirt', 'shock', 'shoe', 'short', 'shut', 'side', 'sign', 'silk', 'silver', 'simple', 'sister', 'size', 'skin', 'skirt', 'sky', 'sleep', 'slip', 'slope', 'slow', 'small', 'smash', 'smell', 'smile', 'smoke', 'smooth', 'snake', 'sneeze', 'snow', 'so', 'soap', 'society', 'sock', 'soft', 'solid', 'some', 'son', 'song', 'sort', 'sound', 'soup', 'south', 'space', 'spade', 'special', 'sponge', 'spoon', 'spring', 'square', 'stage', 'stamp', 'star', 'start', 'statement', 'station', 'steam', 'steel', 'stem', 'step', 'stick', 'sticky', 'stiff', 'still', 'stitch', 'stocking', 'stomach', 'stone', 'stop', 'store', 'story', 'straight', 'strange', 'street', 'stretch', 'strong', 'structure', 'substance', 'such', 'sudden', 'sugar', 'suggestion', 'summer', 'sun', 'support', 'surprise', 'sweet', 'swim', 'system', 'table', 'tail', 'take', 'talk', 'tall', 'taste', 'tax', 'teaching', 'tendency', 'test', 'than', 'that', 'the', 'then', 'theory', 'there', 'thick', 'thin', 'thing', 'this', 'thought', 'thread', 'throat', 'through', 'through', 'thumb', 'thunder', 'ticket', 'tight', 'till', 'time', 'tin', 'tired', 'to', 'toe', 'together', 'tomorrow', 'tongue', 'tooth', 'top', 'touch', 'town', 'trade', 'train', 'transport', 'tray', 'tree', 'trick', 'trouble', 'trousers', 'true', 'turn', 'twist', 'umbrella', 'under', 'unit', 'up', 'use', 'value', 'verse', 'very', 'vessel', 'view', 'violent', 'voice', 'waiting', 'walk', 'wall', 'war', 'warm', 'wash', 'waste', 'watch', 'water', 'wave', 'wax', 'way', 'weather', 'week', 'weight', 'well', 'west', 'wet', 'wheel', 'when', 'where', 'while', 'whip', 'whistle', 'white', 'who', 'why', 'wide', 'will', 'wind', 'window', 'wine', 'wing', 'winter', 'wire', 'wise', 'with', 'woman', 'wood', 'wool', 'word', 'work', 'worm', 'wound', 'writing', 'wrong', 'year', 'yellow', 'yes', 'yesterday', 'you', 'young', 'Bernhard', 'Android']


def pickword(words):
    global answer
    answer=random.choice(words)
    return answer

def splitting(chosen_word):
    letters=dict()
    for i,x in enumerate(chosen_word):
        letters[i]=x
    return letters

def blank_word(letters):
    display=dict()
    display[0]=letters[0]
    for i in range(1,len(letters)):
        display[i]='_'
    return display
def correct_guess(guess,letters):
    global guessed
    for key,value in letters.items():
        if value==guess:
            display_blanks[key]=guess
            if guess not in guessed:
                pygame.mixer.Sound.play(correct_guess_music)
                guessed.append(guess)
    show=''
    for x in display_blanks.values():
        show= show+x+' '
    return show

x_image=pygame.image.load('Media/Images/x.png').convert_alpha()
x_rect=x_image.get_rect()
x_rect.center=(164,85)

x2_image=pygame.image.load('Media/Images/x.png').convert_alpha()
x2_rect=x2_image.get_rect()
x2_rect.center=(196,85)
def hang():
    if chance<8:
        pygame.draw.line(screen,(0,0,0),(180,0),(180,50),4)
    if chance<7:
        pygame.draw.circle(screen,(0,0,0),(180,90),40,4)
    if chance<6:
        pygame.draw.line(screen,(0,0,0),(180,130),(180,220),4)
    if chance<5:
        pygame.draw.line(screen,(0,0,0),(180,140),(120,180),4)
    if chance<4:
        pygame.draw.line(screen, (0, 0, 0), (180, 140), (240, 180), 4)
    if chance<3:
        pygame.draw.line(screen,(0,0,0),(180,220),(120,270),4)
    if chance<2:
        pygame.draw.line(screen, (0, 0, 0), (180, 220), (240, 270), 4)
    if chance<1:
        screen.blit(x_image,x_rect)
        screen.blit(x2_image,x2_rect)

def give_points(letters):
    global points
    if 4>=len(letters)>1:
        points=3
    elif 8>=len(letters)>=5:
        points=5
    elif len(letters)>8:
        points=8
    else:
        points=0
    return points


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
    global username,count
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_BACKSPACE:
            username=username[:-1]
            if count > 0:
                count -= 1
        else:
            username+=event.unicode

def process_username():
    global in_home,in_game
    if len(username) > 0:
        new_user = database.get_user(username)
        in_game = True
        in_home = False

        if new_user:
            welcome_text = 'Your username has been successfully registered.'
        else:
            welcome_text = (f"Welcome back {username}!")
        transition_page(welcome_text, 3000)


def transition_page(text,delay):
    while True:
        screen.blit(transition_screen, (0, 0))
        display_text = font2.render(text, True, (0, 0, 0))
        display_rect = display_text.get_rect()
        display_rect.center = (640, 360)
        screen.blit(display_text, display_rect)
        pygame.display.update()
        pygame.time.delay(delay)
        break
def home():
    global in_home, in_game, continue_game,count

    user_text_click_once=False
    user_text_click=False

    count=0

    while in_home:
        #display
        screen.blit(home_screen,(0,0))
        if user_text_click_once:
            screen.blit(textbox, (536, 305))

        username_copy = username[count:len(username)+1]
        display_username=font.render((username_copy),True,(0,0,0))
        username_rect=display_username.get_rect()

        if username_rect.right>165:
            count+=1

        screen.blit(display_username,(560,315))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_home = False
                continue_game=False


            elif event.type == pygame.MOUSEBUTTONDOWN:

                # If the user clicks on username button
                if pygame.Rect.colliderect(user_text,get_cursor()):
                    user_text_click_once=True
                    user_text_click=True
                elif not pygame.Rect.colliderect(user_text,get_cursor()):
                    user_text_click=False

                #If the user clicks on play button
                if pygame.Rect.colliderect(play_button,get_cursor()):
                    process_username()

            elif event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    process_username()
                elif user_text_click:
                    get_username(event)



        pygame.display.update()




#Gameplay elements
blank_screen=pygame.image.load('Media/Images/blank_background.png').convert()
guess_text=font2.render('Enter a letter to guess',True,(0,0,0))
guess_rect=guess_text.get_rect()
guess_rect.center = (640, 260)

display_blanks_font=pygame.font.Font('Media/Fonts/Raleway-SemiBoldItalic.ttf', 38)
rope_font=pygame.font.Font('Media/Fonts/Reeperbahn.ttf', 160)
won_font=pygame.font.Font('Media/Fonts/Reeperbahn.ttf', 120)

play_again_pic=pygame.image.load('Media/Images/play_again.png').convert_alpha()
play_again_rect=play_again_pic.get_rect()
play_again_rect.center=(470,550)

retry_pic=pygame.image.load('Media/Images/Retry.png').convert_alpha()
retry_rect=retry_pic.get_rect()
retry_rect.center=(470,550)

quit_pic=pygame.image.load('Media/Images/Quit.png').convert_alpha()
quit_rect=quit_pic.get_rect()
quit_rect.center=(850,550)

correct_guess_music=pygame.mixer.Sound('Media/Sound_effects/correct_guess.wav')
wrong_guess_music=pygame.mixer.Sound('Media/Sound_effects/invalid_selection.mp3')
game_over_music=pygame.mixer.Sound('Media/Sound_effects/game_over.wav')
winning_sound=pygame.mixer.Sound('Media/Sound_effects/winning.wav')

won_text = won_font.render('Congratulations! You\'ve Won.', True, (30, 255, 5))
won_rect = won_text.get_rect()
won_rect.center = (640, 200)

gameover_text = rope_font.render('Game Over!', True, (255, 20, 20))
gameover_rect = gameover_text.get_rect()
gameover_rect.center = (640, 220)

def gameplay():
    global display_blanks,in_game,continue_game,guessed,chance
    answer=pickword(words)
    letters=splitting(answer)
    display_blanks=blank_word(letters)
    show=''
    guessed=[]
    for x in display_blanks.values():
        show= show+x+' '
    display_blanks_text = display_blanks_font.render(show, True, (0, 0, 0))
    display_blanks_rect = display_blanks_text.get_rect()
    display_blanks_rect.center=(640,380)
    chance=8

    game_status=1
    given_points=False
    while in_game:
        screen.blit(blank_screen, (0, 0))


        if game_status==1:
            screen.blit(guess_text, guess_rect)
            display_blanks_text = display_blanks_font.render(show, True, (0, 0, 0))
            display_blanks_rect = display_blanks_text.get_rect()
            display_blanks_rect.center = (640, 380)
            screen.blit(display_blanks_text,display_blanks_rect)
            hang()
            pygame.display.update()

        elif game_status==0:
            pygame.mixer.Sound.play(game_over_music)

            hang()

            screen.blit(gameover_text, gameover_rect)

            answer_text = font2.render(f"The word was \"{answer}\"", True, (0, 0, 0))
            answer_rect = answer_text.get_rect()
            answer_rect.center = (640, 380)
            screen.blit(answer_text, answer_rect)

            screen.blit(retry_pic, retry_rect)
            screen.blit(quit_pic, quit_rect)
            pygame.display.update()

            lost_page = True
            while lost_page:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        lost_page=False
                        in_game = False
                        continue_game=False

                    elif pygame.Rect.colliderect(retry_rect,get_cursor()):
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            lost_page=False
                            in_game=False
                            continue_game=True

                    elif pygame.Rect.colliderect(quit_rect,get_cursor()):
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            lost_page=False
                            in_game=False
                            continue_game=False
                            transition_page('Thanks for playing!',2800)

        elif game_status==2:
            pygame.mixer.Sound.play(winning_sound)

            screen.blit(won_text, won_rect)

            answer_text = font2.render(f"The word was indeed \"{answer}\"", True, (0, 0, 0))
            answer_rect = answer_text.get_rect()
            answer_rect.center = (640, 320)
            screen.blit(answer_text, answer_rect)

            score_text = font2.render(f"You\'ve earned {points} points, your new total score is {new_total_score}.",True, (0, 0, 0))
            score_rect = score_text.get_rect()
            score_rect.center = (640, 390)
            screen.blit(score_text, score_rect)

            screen.blit(play_again_pic, play_again_rect)
            screen.blit(quit_pic, quit_rect)
            pygame.display.update()

            won_page=True
            while won_page:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        won_page=False
                        in_game = False
                        continue_game=False

                    elif pygame.Rect.colliderect(play_again_rect,get_cursor()):
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            won_page=False
                            in_game=False
                            continue_game=True

                    elif pygame.Rect.colliderect(quit_rect,get_cursor()):
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            won_page=False
                            in_game=False
                            continue_game=False
                            transition_page('Thanks for playing!', 2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                in_game = False
                continue_game=False

            elif chance>0:
                if event.type==pygame.KEYDOWN:
                    guess=event.unicode
                    if guess in letters.values():
                        show=correct_guess(guess,letters)
                    else:
                        chance-=1
                        pygame.mixer.Sound.play(wrong_guess_music)

            elif chance==0:
                game_status=0
        if display_blanks==letters and given_points is False:
            points=give_points(letters)
            new_total_score=database.update_score(username,points)
            game_status=2
            given_points=True
        pygame.display.update()

in_home = True
in_game = False
continue_game = True
home()
while continue_game:
    in_game=True
    gameplay()




