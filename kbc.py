import pygame
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('KBC Console App')

# Set up fonts
font = pygame.font.SysFont(None, 55)
small_font = pygame.font.SysFont(None, 35)

# Load sounds
intro_sound = pygame.mixer.Sound('sounds/intro.mp3')
que_sound = pygame.mixer.Sound('sounds/que.mp3')
correct_sound = pygame.mixer.Sound('sounds/correct.mp3')
wrong_sound = pygame.mixer.Sound('sounds/wrong.mp3')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Questions and options
question = ['Q-1 Which one of the following river flows between Vindhyan and Satpura ranges?', 'Q-2 The Central Rice Research Station is situated in?',
            'Q-3 Who among the following wrote Sanskrit grammar?', 'Q-4 Which among the following headstreams meets the Ganges in last?', 'Q-5 The metal whose salts are sensitive to light is?', 'Q-6  Patanjali is well known for the compilation of –', 'Q-7 River Luni originates near Pushkar and drains into which one of the following?', 'Q-8 Which one of the following rivers originates in Brahmagiri range of Western Ghats?', 'Q-9 The country that has the highest in Barley Production?', 'Q-10 Tsunamis are not caused by', 'Q-11 Chambal river is a part of –', 'Q-12 D.D.T. was invented by?', 'Q-13 Volcanic eruption do not occur in the', 'Q-14 Indus river originates in –', 'Q-15 The hottest planet in the solar system?', 'Q-16 With which of the following rivers does Chambal river merge?']
options = [['(a) Narmada', '(b) Mahanadi', '(c) Son', '(d) Netravati'], ['(a) Chennai', '(b) Cuttack', '(c) Bangalore', '(d) Quilon'], ['(a) Kalidasa', '(b) Charak', '(c) Panini', '(d) Aryabhatt'], ['(a) Alaknanda', '(b) Pindar', '(c) Mandakini', '(d) Bhagirathi'], ['(a) Zinc', '(b) Silver', '(c) Copper', '(d) Aluminum'], ['(a) Yoga Sutra', '(b) Panchatantra', '(c) Brahma Sutra', '(d) Ayurveda'], ['(a) Rann of Kachchh', '(b) Arabian Sea', '(c) Gulf of Cambay', '(d) Lake Sambhar'], ['(a) Pennar', '(b) Cauvery', '(c) Krishna', '(d) Tapti'], ['(a) China', '(b) India', '(c) Russia', '(d) France'], ['(a) Hurricanes', '(b) Earthquakes', '(c) Undersea landslides', '(d) Volcanic eruptions'], ['(a) Sabarmati basin', '(b) Ganga basin', '(c) Narmada basin', '(d) Godavari basin'], ['(a) Mosley', '(b) Rudolf', '(c) Karl Benz', '(d) Dalton'], ['(a) Baltic sea', '(b) Black sea', '(c) Caribbean sea', '(d) Caspian sea'], ['(a) Kinnaur', '(b) Ladakh', '(c) Nepal', '(d) Tibet'], ['(a) Mercury', '(b) Venus', '(c) Mars', '(d) Jupiter'], ['(a) Banas', '(b) Ganga', '(c) Narmada', '(d) Yamuna']]
answers = ['(a) Narmada', '(b) Cuttack', '(c) Panini', '(d) Bhagirathi', '(b) Silver', '(a) Yoga Sutra', '(a) Rann of Kachchh', '(b) Cauvery', '(c) Russia', '(a) Hurricanes', '(c) Narmada basin', '(a) Mosley', '(a) Baltic sea', '(d) Tibet', '(b) Venus', '(d) Yamuna']

amount = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000, 70000000]
win = 0

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

# Play intro sound
pygame.mixer.Sound.play(intro_sound)
time.sleep(1)

running = True
question_index = 0

while running and question_index < len(question):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(black)
    
    draw_text("Wait your Question is Loading...", font, white, screen, 20, 20)
    pygame.display.update()
    pygame.mixer.Sound.play(que_sound)
    time.sleep(2)
    
    screen.fill(black)
    draw_text(question[question_index], font, white, screen, 20, 20)
    
    for i, option in enumerate(options[question_index]):
        draw_text(option, small_font, white, screen, 20, 100 + i * 40)
    
    pygame.display.update()
    
    answer_chosen = False
    while not answer_chosen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                answer_chosen = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    num = 0
                    answer_chosen = True
                elif event.key == pygame.K_b:
                    num = 1
                    answer_chosen = True
                elif event.key == pygame.K_c:
                    num = 2
                    answer_chosen = True
                elif event.key == pygame.K_d:
                    num = 3
                    answer_chosen = True
    
    if options[question_index][num] == answers[question_index]:
        win += amount[question_index]
        screen.fill(black)
        draw_text(f"Correct Answer! You won {win} RS", font, white, screen, 20, 20)
        pygame.mixer.Sound.play(correct_sound)
    else:
        screen.fill(black)
        draw_text("Sorry you Lost!", font, white, screen, 20, 20)
        pygame.mixer.Sound.play(wrong_sound)
        running = False
    
    pygame.display.update()
    time.sleep(2)
    question_index += 1

screen.fill(black)
draw_text(f"Your Final Winning Amount is {win} Rs", font, white, screen, 20, 20)
draw_text("Thanks ..", font, white, screen, 20, 80)
pygame.display.update()
time.sleep(5)

pygame.quit()
