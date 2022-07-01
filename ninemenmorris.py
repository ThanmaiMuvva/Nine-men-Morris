import pygame
import math
pygame.init()

#Screen
WIDTH = 650
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Nine Men's Morris")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SKY_BLUE = (135,205,235)
GREEN = (0,200,0)

# Images
WHITE_IMAGE = pygame.transform.scale(pygame.image.load("imagewhite.png"), (550, 450))
BLACK_IMAGE = pygame.transform.scale(pygame.image.load("imageblack.png"), (300, 200))

# Fonts
END_FONT = pygame.font.SysFont('courier', 40)

def display_message(content):
    pygame.time.delay(500)
    win.fill(SKY_BLUE)
    end_text = END_FONT.render(content, 1, BLACK)
    win.blit(end_text, ((WIDTH - end_text.get_width()) // 2, (WIDTH - end_text.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(1000)


def draw_grid():
    pygame.draw.line(win, RED, (25,25), (625,25), 3)
    pygame.draw.line(win, RED, (125,125), (525,125), 3)
    pygame.draw.line(win, RED, (225,225), (425,225), 3)
    pygame.draw.line(win, RED, (225,425), (425,425), 3)
    pygame.draw.line(win, RED, (125,525), (525,525), 3)
    pygame.draw.line(win, RED, (25,625), (625,625), 3)
    pygame.draw.line(win, RED, (25,325), (225,325), 3)
    pygame.draw.line(win, RED, (425,325), (625,325), 3)

    pygame.draw.line(win, RED, (25,25), (25,625), 3)
    pygame.draw.line(win, RED, (125,125), (125,525), 3)
    pygame.draw.line(win, RED, (225,225), (225,425), 3)
    pygame.draw.line(win, RED, (425,225), (425,425), 3)
    pygame.draw.line(win, RED, (525,125), (525,525), 3)
    pygame.draw.line(win, RED, (625,25), (625,625), 3)
    pygame.draw.line(win, RED, (325,25), (325,225), 3)
    pygame.draw.line(win, RED, (325,425), (325,625), 3)

def initialize_grid():
    x = 0
    y = 0
    game_array =[[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None]] 
    for i in range(8):
        if (i ==0 or i==3 or i == 5):
            x =25
        elif (i ==1 or i == 6):
            x = 325
        elif (i == 2 or i == 4 or i == 7):
            x = 625
        if (i == 0 or i == 1 or i== 2):
            y =25
        elif(i== 3 or i == 4):
            y = 325
        elif (i==5 or i==6 or i==7):
            y = 625
        game_array[0][i] = (x,y,"",True)
    for i in range(8):
        if (i ==0 or i==3 or i == 5):
            x =125
        elif (i ==1 or i == 6):
            x = 325
        elif (i == 2 or i == 4 or i == 7):
            x = 525
        if (i == 0 or i == 1 or i== 2):
            y =125
        elif(i== 3 or i == 4):
            y = 325
        elif (i==5 or i==6 or i==7):
            y = 525
        game_array[1][i] = (x,y,"",True)
    for i in range(8):
        if (i ==0 or i==3 or i == 5):
            x =225
        elif (i ==1 or i == 6):
            x = 325
        elif (i == 2 or i == 4 or i == 7):
            x = 425
        if (i == 0 or i == 1 or i== 2):
            y =225
        elif(i== 3 or i == 4):
            y = 325
        elif (i==5 or i==6 or i==7):
            y = 425
        game_array[2][i] = (x,y,"",True)    
    return game_array

def click(game_array):
    global black_turn, white_turn,images,count_white,count_black
    m_x,m_y = pygame.mouse.get_pos()
    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x, y, char,can_play = game_array[i][j]
            dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
            if dis < 20 and can_play:
                if black_turn:  
                    images.append((x, y, BLACK_IMAGE))
                    count_black +=1
                    black_turn = False
                    white_turn = True
                    game_array[i][j] = (x, y, 'black',False)

                elif white_turn: 
                    images.append((x, y, WHITE_IMAGE))
                    count_white +=1
                    black_turn = True
                    white_turn = False
                    game_array[i][j] = (x, y, 'white',False)
            elif dis < 20 and not can_play:
                if black_turn:
                    if (x,y,BLACK_IMAGE) in images:
                        images.remove((x,y,BLACK_IMAGE))
                    game_array[i][j] = (x,y,'',True)
                elif white_turn:
                    if (x,y,WHITE_IMAGE) in images:
                        images.remove((x,y,WHITE_IMAGE))
                    game_array[i][j] = (x,y,'',True)

def click2(game_array):
    global black_turn, white_turn,images,count_white,count_black
    surrounding = [[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None]]
    surrounding[0][0] = [game_array[0][1],game_array[0][3]]
    surrounding[0][1] = [game_array[0][0],game_array[0][2],game_array[1][1]]
    surrounding[0][2] = [game_array[0][1],game_array[0][4]]
    surrounding[0][3] = [game_array[0][0],game_array[0][5],game_array[1][3]]
    surrounding[0][4] = [game_array[0][2],game_array[0][7],game_array[1][4]]
    surrounding[0][5] = [game_array[0][3],game_array[0][6]]
    surrounding[0][6] = [game_array[0][5],game_array[0][7],game_array[1][6]]
    surrounding[0][7] = [game_array[0][4],game_array[0][6]]
    surrounding[1][0] = [game_array[1][1],game_array[1][3]] 
    surrounding[1][1] = [game_array[1][0],game_array[1][2],game_array[0][1],game_array[2][1]]
    surrounding[1][2] = [game_array[1][1],game_array[1][4]]
    surrounding[1][3] = [game_array[1][0],game_array[1][5],game_array[0][3],game_array[2][3]]
    surrounding[1][4] = [game_array[1][2],game_array[1][7],game_array[0][4],game_array[2][4]]
    surrounding[1][5] = [game_array[1][3],game_array[1][6]]
    surrounding[1][6] = [game_array[1][5],game_array[1][7],game_array[0][6],game_array[2][6]]
    surrounding[1][7] = [game_array[1][4],game_array[1][6]]
    surrounding[2][0] = [game_array[2][1],game_array[2][4]]
    surrounding[2][1] = [game_array[2][0],game_array[2][2],game_array[1][1]]
    surrounding[2][2] = [game_array[2][1],game_array[2][4]]
    surrounding[2][3] = [game_array[2][0],game_array[2][5],game_array[1][3]]
    surrounding[2][4] = [game_array[2][2],game_array[2][7],game_array[1][4]]
    surrounding[2][5] = [game_array[2][3],game_array[2][6]]
    surrounding[2][6] = [game_array[2][5],game_array[2][7],game_array[1][6]]
    surrounding[2][7] = [game_array[2][4],game_array[2][6]]
    m1_x,m1_y = pygame.mouse.get_pos()
    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x, y, char,can_play = game_array[i][j]
            dis = math.sqrt((x - m1_x) ** 2 + (y - m1_y) ** 2)
            if dis < 20 :
                if game_array[i][j][2] == 'black' and black_turn:
                    for k in range(len(surrounding[i][j])):
                        if surrounding[i][j][k][2] == "":
                            pygame.draw.circle(win, RED, (surrounding[i][j][k][0],surrounding[i][j][k][1]),20)
                            pygame.display.update()
                        
                elif game_array[i][j][2] == "white" and white_turn:
                    for k in range(len(surrounding[i][j])):
                        if surrounding[i][j][k][2] == "":
                            pygame.draw.circle(win, RED, (surrounding[i][j][k][0],surrounding[i][j][k][1]),20)
                            pygame.display.update()
        
def click3(game_array):
    global black_turn,white_turn,images
    m2_x ,m2_y = pygame.mouse.get_pos()
    if white_turn :
        for i in range(len(game_array)):
            for j in range(len(game_array[i])):
                x, y, char,can_play = game_array[i][j]
                dis = math.sqrt((x - m2_x) ** 2 + (y - m2_y) ** 2)
                if dis < 20 and can_play:
                    if game_array[i][j][2] == 'white':
                        if (x,y,WHITE_IMAGE) in images:
                            images.remove((x,y,WHITE_IMAGE))
                        game_array[i][j] = (x,y,'',True)
    elif black_turn:
        for i in range(len(game_array)):
            for j in range(len(game_array[i])):
                x, y, char,can_play = game_array[i][j]
                dis = math.sqrt((x - m2_x) ** 2 + (y - m2_y) ** 2)
                if dis < 20 and can_play:
                    if game_array[i][j][2] == 'black':
                        if (x,y,BLACK_IMAGE) in images:
                            images.remove((x,y,BLACK_IMAGE))
                        game_array[i][j] = (x,y,'',True)


def click4(game_array):
    global black_turn, white_turn,images,count_white,count_black
    m_x,m_y = pygame.mouse.get_pos()
    for i in range(len(game_array)):
        for j in range(len(game_array[i])):
            x, y, char,can_play = game_array[i][j]
            dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
            if dis < 20 and can_play:
                if black_turn:  
                    images.append((x, y, BLACK_IMAGE))
                    black_turn = False
                    white_turn = True
                    game_array[i][j] = (x, y, 'black',False)

                elif white_turn: 
                    images.append((x, y, WHITE_IMAGE))
                    black_turn = True
                    white_turn = False
                    game_array[i][j] = (x, y, 'white',False)
            elif dis < 20 and not can_play:
                if black_turn:
                    if (x,y,BLACK_IMAGE) in images:
                        images.remove((x,y,BLACK_IMAGE))
                    game_array[i][j] = (x,y,'',True)
                elif white_turn:
                    if (x,y,WHITE_IMAGE) in images:
                        images.remove((x,y,WHITE_IMAGE))
                    game_array[i][j] = (x,y,'',True)



def mill(game_array):
    no_of_mills = 0
    check = False
    for sq in range(3):
        if (game_array[sq][0][2] == game_array[sq][1][2] == game_array[sq][2][2]) and game_array[sq][0][2] != "":
            pygame.draw.line(win, GREEN, (game_array[sq][0][0],game_array[sq][0][1]), (game_array[sq][2][0],game_array[sq][2][1]), 3)
            pygame.display.update()
            check = True
            no_of_mills += 1
            
        if (game_array[sq][0][2] == game_array[sq][3][2] == game_array[sq][5][2]) and game_array[sq][0][2] != "":
            pygame.draw.line(win, GREEN, (game_array[sq][0][0],game_array[sq][0][1]), (game_array[sq][5][0],game_array[sq][5][1]), 3)
            pygame.display.update()
            check = True
            no_of_mills += 1
    
        if (game_array[sq][5][2] == game_array[sq][6][2] == game_array[sq][7][2]) and game_array[sq][5][2] != "":
            pygame.draw.line(win, GREEN, (game_array[sq][5][0],game_array[sq][5][1]), (game_array[sq][7][0],game_array[sq][7][1]), 3)
            pygame.display.update()
            check = True
            no_of_mills += 1
        
        if (game_array[sq][2][2] == game_array[sq][4][2] == game_array[sq][7][2]) and game_array[sq][2][2] != "":
            pygame.draw.line(win, GREEN, (game_array[sq][2][0],game_array[sq][2][1]), (game_array[sq][7][0],game_array[sq][7][1]), 3)
            pygame.display.update()
            check = True
            no_of_mills += 1
    if (game_array[0][1][2] == game_array[1][1][2] == game_array[2][1][2]) and game_array[0][1][2] != "":
        pygame.draw.line(win, GREEN, (game_array[0][1][0],game_array[0][1][1]), (game_array[2][1][0],game_array[2][1][1]), 3)
        pygame.display.update()
        check = True
        no_of_mills += 1
    if (game_array[0][6][2] == game_array[1][6][2] == game_array[2][6][2]) and game_array[0][6][2] != "":
        pygame.draw.line(win, GREEN, (game_array[1][6][0],game_array[1][6][1]), (game_array[2][6][0],game_array[2][6][1]), 3)
        pygame.display.update()
        check = True
        no_of_mills += 1
    
    if (game_array[0][3][2] == game_array[1][3][2] == game_array[2][3][2]) and game_array[0][3][2] != "":
        pygame.draw.line(win, GREEN, (game_array[0][3][0],game_array[0][3][1]), (game_array[2][3][0],game_array[2][3][1]), 3)
        pygame.display.update()
        check = True
        no_of_mills += 1
    if (game_array[0][4][2] == game_array[1][4][2] == game_array[2][4][2]) and game_array[0][4][2] != "":
        pygame.draw.line(win, GREEN, (game_array[0][4][0],game_array[0][4][1]), (game_array[2][4][0],game_array[2][4][1]), 3)
        pygame.display.update()
        check = True
        no_of_mills += 1
    
    return no_of_mills
    
    
def phase_one(game_array):
    if count_white == 9 and count_black == 9:
        return True


def has_won(game_array):
    blacks = 0
    whites = 0
    for sq in range(3):
        for i in range(8):
            if game_array[sq][i][2] == "white":
                whites +=1
            if game_array[sq][i][2] == "black":
                blacks += 1
    if (whites > 3 and blacks == 2):
        display_message("White has won!")
        return True   
    elif (blacks > 3 and whites == 2):
        display_message("Black has won!")
        return True

def render():
    win.fill(SKY_BLUE)
    draw_grid()
    for image in images:
        x, y, IMAGE = image
        win.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))
    pygame.display.update()

def main():
    display_message("Welcome to the game")
    global black_turn, white_turn, images, draw
    global count_white,count_black
    count_white = 0
    count_black = 0
    images = []
    run = True
    black_turn = True
    white_turn = False
    game_array = initialize_grid()
    while run :
        old_mills = mill(game_array)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click(game_array)

        render()
        new_mills = mill(game_array) 
        if new_mills > old_mills:
            if black_turn == False and white_turn == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        click3(game_array)
            elif black_turn == True and white_turn == False:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        click3(game_array)
        if phase_one(game_array):
            display_message("Coins empty")
            run = False    
    run = True
    while run:
        old_mills = mill(game_array)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()                
            if event.type == pygame.MOUSEBUTTONDOWN:
                click2(game_array)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    click4(game_array)
        render()
        new_mills = mill(game_array)
        if new_mills > old_mills:
            if black_turn == False and white_turn == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        click3(game_array)
            elif black_turn == True and white_turn == False:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        click3(game_array)
        if has_won(game_array): 
            run = False

while True:
    if __name__ == '__main__':
        main()