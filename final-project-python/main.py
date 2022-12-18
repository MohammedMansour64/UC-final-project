











#
#
# BEFORE DOING ANYTHING, READ THE README FILE INSIDE 'final-project-python' FOLDER
#
#







from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import pygame
import sys
import random
import data
import os
import time
import threading
from tkinter import font as FontTk
pygame.mixer.init()

main_bg_color = '#0A0C1E'
questions_answers_easy = data.easy_questions
questions_answers_medium = data.medium_questions
questions_answers_hard = data.hard_questions

random.shuffle(questions_answers_easy)
random.shuffle(questions_answers_medium)
random.shuffle(questions_answers_hard)
questions_answers_easy = questions_answers_easy[0:4]
questions_answers_medium = questions_answers_medium[0:5]
questions_answers_hard = questions_answers_hard[0:5]

questions_answers = []
questions_answers.extend(questions_answers_easy)
questions_answers.extend(questions_answers_medium)
questions_answers.extend(questions_answers_hard)

final_question = {
    'question' : 'ما هو أفضل مسار في يوني كود؟',
    'answers' : ['بايثون' , 'سايبر سيكيوريتي' , 'الويب' , 'فلاتر'],
    'correct_answer' : 'بايثون'
}

questions_answers.append(final_question)

question_number = 0
root = Tk()
root.title("Who wants to be a Tkinter millionare?")
root.iconbitmap('images/center.png')
root.configure()
root.attributes('-fullscreen', True)


# Frames
main_page = Frame(root, background=main_bg_color)
main_page.pack(fill=BOTH , expand=True)
instructions_page = Frame(root , background=main_bg_color)
questions_page = Frame(root , background=main_bg_color)
final_page = Frame(root, background=main_bg_color)


# End of Frames
# Functions
def instruction_page_move():
    pygame.mixer.music.stop()
    main_page.pack_forget()
    welcoming_sound = pygame.mixer.Sound("sounds/يسعد مسائكم.wav")
    welcoming_sound.set_volume(1)
    welcoming_sound.play()
    intro_sound.set_volume(0.08)
    instructions_page.pack(fill=BOTH , expand=True)
def questions_page_move():
    intro_sound.set_volume(0.05)
    new_game_sound = pygame.mixer.Sound('sounds/فإذن معك متسابق.wav')
    new_game_sound.set_volume(0.45)
    new_game_sound.play() 
    instructions_page.after(3000)
    intro_sound.stop()
    global questions_heartbeat_sound
    tense_sound = pygame.mixer.Sound('sounds/tense.wav')
    tense_sound.set_volume(1)
    tense_sound.play()
    questions_heartbeat_sound = pygame.mixer.Sound('sounds/questions_heartbeat.wav')
    questions_heartbeat_sound.set_volume(0.5)
    questions_heartbeat_sound.play(-1)
    instructions_page.pack_forget()
    questions_page.pack(fill=BOTH , expand=True)

def final_page_move():

    ending_sound = pygame.mixer.Sound('sounds/intro.wav')
    ending_sound.set_volume(0.3)
    ending_sound.play(-1)
    if (question_number <= 4) :
            final_page_money_recieved.config(text='0$')
    elif(question_number > 4 and question_number <= 9) :
            final_page_money_recieved.config(text='1000$')
    elif(question_number > 9 and question_number <= 14) :
            final_page_money_recieved.config(text='25000$')
    elif(question_number > 14) :
            final_page_money_recieved.config(text='1000000$')

    questions_page.pack_forget()
    final_page.pack(fill=BOTH , expand=True)

def instruction_buttons(title, message):
    messagebox.showinfo(title=title, message=message)
def close_app():
    sys.exit()

def select_answer(clicked_button , disabled_button_1 , disabled_button_2 , disabled_button_3):
    correct_answer = questions_answers[question_number].get('correct_answer')


    if clicked_button.cget('text') == correct_answer:
        clicked_button['state'] = 'disabled'
        disabled_button_3['state'] = 'disabled'
        disabled_button_2['state'] = 'disabled'
        disabled_button_1['state'] = 'disabled'
        clicked_button_image = clicked_button['image']
        clicked_button.configure(image= answer_correct)

        if question_number < 4:
            questions_page.after(2000)
            correct_answer_sound = pygame.mixer.Sound('sounds/إجابة صحيحة.wav')
            correct_answer_sound.set_volume(1)
            correct_answer_sound.play()
        elif question_number == 4:
            question_tension_sound = pygame.mixer.Sound('sounds/big_question_tension.wav')
            question_tension_sound.set_volume(0.5)
            question_tension_sound.play()
            questions_page.after(7500)
            correct_answer_sound = pygame.mixer.Sound('sounds/إجابة صحيحة2.wav')
            correct_answer_sound.set_volume(1)
            correct_answer_sound.play()
            questions_page_continue_button.place(x=725 , y=980)
        elif question_number ==  9:
            question_tension_sound = pygame.mixer.Sound('sounds/big_question_tension.wav')
            question_tension_sound.set_volume(0.5)
            question_tension_sound.play()
            questions_page.after(7500)
            correct_answer_sound = pygame.mixer.Sound('sounds/إجابة صحيحة2.wav')
            correct_answer_sound.set_volume(0.5)
            correct_answer_sound.play()
            questions_page_continue_button.place(x=725 , y=980)
        elif question_number == 14:
            question_tension_sound = pygame.mixer.Sound('sounds/big_question_tension.wav')
            question_tension_sound.set_volume(1)
            question_tension_sound.play()
            questions_page.after(7500)
            correct_answer_sound = pygame.mixer.Sound('sounds/one_million_congrats.wav')
            correct_answer_sound.set_volume(1)
            correct_answer_sound.play()
            questions_page.after(6500)
            questions_page_money_label.place(x= 475 , y=400)
            questions_page_money_label['text'] = "1000000$"
            questions_page_continue_button.place(x=725 , y=980)
        else:
            questions_page.after(2000)
            correct_answer_sound = pygame.mixer.Sound('sounds/إجابة صحيحة.wav')
            correct_answer_sound.set_volume(1)
            correct_answer_sound.play()    

        if question_number == 4:
            questions_page_money_label.place(x= 475 , y=400)
            questions_page_money_label['text'] = "1000$"
        elif question_number == 5:
            questions_page_money_label.place(x= 475 , y=400)
            questions_page_money_label['text'] = "2000$"
        elif question_number == 6:
            questions_page_money_label.place(x= 475 , y=400)
            questions_page_money_label['text'] = "4000$"
        elif question_number == 7:
            questions_page_money_label.place(x= 475 , y=400)
            questions_page_money_label['text'] = "8000$"
        elif question_number == 8:
            questions_page_money_label.place(x= 475 , y=400)
            questions_page_money_label['text'] = "16000$"
        elif question_number == 9:
            questions_page_money_label.place(x= 475 , y=400)
            questions_page_money_label['text'] = "25000$"
        elif question_number == 10:
            questions_page_money_label.place(x= 475 , y=400)
            questions_page_money_label['text'] = "50000$"
        elif question_number == 11:
            questions_page_money_label.place(x= 475 , y=400)
            questions_page_money_label['text'] = "100000$"
        elif question_number == 12:
            questions_page_money_label.place(x= 475 , y=400)
            questions_page_money_label['text'] = "250000$"
        elif question_number == 13:
            questions_page_money_label.place(x= 475 , y=400)
            questions_page_money_label['text'] = "500000$"
            

        questions_page_continue_button.place(x=725 , y=980)   
        questions_page_continue_button['command'] = lambda : next_question_fun(clicked_button , disabled_button_1 , disabled_button_2 , disabled_button_3 , questions_page_answers , clicked_button_image)

    if disabled_button_1.cget('text') == correct_answer:
        clicked_button['state'] = 'disabled'
        disabled_button_3['state'] = 'disabled'
        disabled_button_2['state'] = 'disabled'
        disabled_button_1['state'] = 'disabled'

        if question_number < 4:
            questions_page.after(2000)
            wrong_answer_sound = pygame.mixer.Sound('sounds/lose2.wav')
            wrong_answer_sound.set_volume(1)
            wrong_answer_sound.play()
        elif question_number >= 4:
            question_tension_sound = pygame.mixer.Sound('sounds/big_question_tension.wav')
            question_tension_sound.set_volume(1)
            question_tension_sound.play()
            questions_page.after(7500)
            wrong_answer_sound = pygame.mixer.Sound('sounds/lose.wav')
            wrong_answer_sound.set_volume(1)
            wrong_answer_sound.play()


        clicked_button.configure(image= answer_wrong)
        disabled_button_1.configure(image= answer_correct)
        questions_page_next_button.place(x=725 , y=980)

    if disabled_button_2.cget('text') == correct_answer:
        clicked_button['state'] = 'disabled'
        disabled_button_3['state'] = 'disabled'
        disabled_button_2['state'] = 'disabled'
        disabled_button_1['state'] = 'disabled'
        if question_number < 4:
            questions_page.after(2000)
            wrong_answer_sound = pygame.mixer.Sound('sounds/lose2.wav')
            wrong_answer_sound.set_volume(1)
            wrong_answer_sound.play()
        elif question_number >= 4:
            question_tension_sound = pygame.mixer.Sound('sounds/big_question_tension.wav')
            question_tension_sound.set_volume(1)
            question_tension_sound.play()
            questions_page.after(7500)
            wrong_answer_sound = pygame.mixer.Sound('sounds/lose.wav')
            wrong_answer_sound.set_volume(1)
            wrong_answer_sound.play()


        clicked_button.configure(image= answer_wrong)
        disabled_button_2.configure(image= answer_correct)
        questions_page_next_button.place(x=725 , y=980)

    if disabled_button_3.cget('text') == correct_answer:
        clicked_button['state'] = 'disabled'
        disabled_button_3['state'] = 'disabled'
        disabled_button_2['state'] = 'disabled'
        disabled_button_1['state'] = 'disabled'
        if question_number < 4:
            questions_page.after(2000)
            wrong_answer_sound = pygame.mixer.Sound('sounds/lose2.wav')
            wrong_answer_sound.set_volume(1)
            wrong_answer_sound.play()
        elif question_number >= 4:
            question_tension_sound = pygame.mixer.Sound('sounds/big_question_tension.wav')
            question_tension_sound.set_volume(1)
            question_tension_sound.play()
            questions_page.after(7500)
            wrong_answer_sound = pygame.mixer.Sound('sounds/lose.wav')
            wrong_answer_sound.set_volume(1)
            wrong_answer_sound.play()


        clicked_button.configure(image= answer_wrong)
        disabled_button_3.configure(image= answer_correct)
        questions_page_next_button.place(x=725 , y=980)


def next_question_fun(clicked_button , disabled_button_1 , disabled_button_2 , disabled_button_3 , answers_images , clicked_button_image):
    clicked_button['state'] = 'normal'
    disabled_button_1['state'] = 'normal'
    disabled_button_2['state'] = 'normal'
    disabled_button_3['state'] = 'normal'
    questions_page_poll.pack_forget()
    questions_page_poll.place_forget()
    questions_page_continue_button.pack_forget()
    questions_page_continue_button.place_forget()
    clicked_button.configure(image= clicked_button_image)
    global question_number
    question_number += 1
    questions_page_money_label.place_forget()
    questions_page_money_label.pack_forget()

    if question_number > 14:
        final_page_move()

    if question_number == 1:
        answers_images.configure(image=answers_1_image)
    elif question_number == 2:
        answers_images.configure(image=answers_2_image)
    elif question_number == 3:
        answers_images.configure(image=answers_3_image)
    elif question_number == 4:
        answers_images.configure(image=answers_4_image)
    elif question_number == 5:
        answers_images.configure(image=answers_5_image)
    elif question_number == 6:
        answers_images.configure(image=answers_6_image)
    elif question_number == 7:
        answers_images.configure(image=answers_7_image)
    elif question_number == 8:
        answers_images.configure(image=answers_8_image)
    elif question_number == 9:
        answers_images.configure(image=answers_9_image)
    elif question_number == 10:
        answers_images.configure(image=answers_10_image)
    elif question_number == 11:
        answers_images.configure(image=answers_11_image)
    elif question_number == 12:
        answers_images.configure(image=answers_12_image)
    elif question_number == 13:
        answers_images.configure(image=answers_13_image)
    elif question_number == 14:
        answers_images.configure(image=answers_14_image)
    elif question_number == 15:
        answers_images.configure(image=answers_15_image)


    next_question = questions_answers[question_number].get('question')
    answers = questions_answers[question_number].get('answers')


    random.shuffle(answers)
    questions_page_question_bracket['text'] = next_question
    clicked_button['text'] = answers[0]
    disabled_button_1['text'] = answers[1]
    disabled_button_2['text'] = answers[2]
    disabled_button_3['text'] = answers[3]
    
    
   
  
def fifty_fifty_help(fifty_fifty_button , button_1 , button_2 , button_3 , button_4):
    wrong_buttons = []
    fifty_help_sound = pygame.mixer.Sound('sounds/remove_two_answers.wav')
    fifty_help_sound.set_volume(1)
    fifty_help_sound.play() 
    questions_heartbeat_sound.stop()
    questions_page.after(10000)
    questions_heartbeat_sound.play(-1)
    if button_1.cget('text') != questions_answers[question_number].get('correct_answer'):    
        wrong_buttons.append(button_1)
    if button_2.cget('text') != questions_answers[question_number].get('correct_answer'):
        wrong_buttons.append(button_2)
    if button_3.cget('text') != questions_answers[question_number].get('correct_answer'):
        wrong_buttons.append(button_3)
    if button_4.cget('text') != questions_answers[question_number].get('correct_answer'):
        wrong_buttons.append(button_4)
    if len(wrong_buttons) != 1:
        random.shuffle(wrong_buttons)
        wrong_buttons[0]['text'] = ''
        wrong_buttons[0]['state'] = 'disabled'
        wrong_buttons[1]['text'] = ''
        wrong_buttons[1]['state'] = 'disabled'
  
    fifty_fifty_button.configure(image = fifty_fifty_X_image)
    fifty_fifty_button['state'] = 'disabled'


def call_friend_help(call_friend_button , button_1 , button_2 , button_3 , button_4):
    call_friend_sound = pygame.mixer.Sound('sounds/إتصال بصديق.wav')
    call_friend_sound.set_volume(1)
    call_friend_sound.play()
    questions_heartbeat_sound.stop()
    questions_page.after(17000)
    if button_1.cget('text') == questions_answers[question_number].get('correct_answer'):    
        friend_answer_sound = pygame.mixer.Sound('sounds/الإجابة ب.wav')
        friend_answer_sound.set_volume(1)
        friend_answer_sound.play()
        questions_page.after(8000)
        questions_heartbeat_sound.play(-1)
    if button_2.cget('text') == questions_answers[question_number].get('correct_answer'):
        friend_answer_sound = pygame.mixer.Sound('sounds/الإجابة أ.wav')
        friend_answer_sound.set_volume(1)
        friend_answer_sound.play()
        questions_page.after(8000)
        questions_heartbeat_sound.play(-1)
    if button_3.cget('text') == questions_answers[question_number].get('correct_answer'):
        friend_answer_sound = pygame.mixer.Sound('sounds/الإجابة ج.wav')
        friend_answer_sound.set_volume(1)
        friend_answer_sound.play()
        questions_page.after(8000)
        questions_heartbeat_sound.play(-1)
    if button_4.cget('text') == questions_answers[question_number].get('correct_answer'):
        friend_answer_sound = pygame.mixer.Sound('sounds/الإجابة د.wav')
        friend_answer_sound.set_volume(1)
        friend_answer_sound.play()
        questions_page.after(8000)
        questions_heartbeat_sound.play(-1)
    call_friend_button.configure(image = ask_friend_X_image)
    call_friend_button['state'] = 'disabled'

def ask_audience_help(ask_audience_button , button_1 , button_2 , button_3 , button_4):
    call_friend_sound = pygame.mixer.Sound('sounds/جمهور جهزوا حالكم.wav')
    call_friend_sound.set_volume(1)
    call_friend_sound.play()
    questions_heartbeat_sound.stop()
    questions_page.after(15500)

    equal_poll = random.randint(0, 10)

    if equal_poll == 1:
        questions_page_poll.pack(side=LEFT , anchor="nw" , padx=50 , pady=100)
        questions_page_poll.config(image= poll_equal_image)
        questions_heartbeat_sound.play(-1)
    elif equal_poll != 1:
        if button_1.cget('text') == questions_answers[question_number].get('correct_answer'):  
            questions_page_poll.pack(side=LEFT , anchor="nw" , padx=50 , pady=100)  
            questions_page_poll.config(image= poll_B_image)
            questions_heartbeat_sound.play(-1)
        if button_2.cget('text') == questions_answers[question_number].get('correct_answer'):
            questions_page_poll.pack(side=LEFT , anchor="nw" , padx=50 , pady=100)
            questions_page_poll.config(image= poll_A_image)
            questions_heartbeat_sound.play(-1)
        if button_3.cget('text') == questions_answers[question_number].get('correct_answer'):
            questions_page_poll.pack(side=LEFT , anchor="nw" , padx=50 , pady=100)
            questions_page_poll.config(image= poll_C_image)
            questions_heartbeat_sound.play(-1)
        if button_4.cget('text') == questions_answers[question_number].get('correct_answer'):
            questions_page_poll.pack(side=LEFT , anchor="nw" , padx=50 , pady=100)
            questions_page_poll.config(image= poll_D_image)
            questions_heartbeat_sound.play(-1)
    
    


    ask_audience_button.configure(image = ask_image_X)
    ask_audience_button['state'] = 'disabled'



  
# End of Functions
# Images

ask_image = ImageTk.PhotoImage((Image.open("images/audience.png")).resize((150 , 105) , Image.ANTIALIAS))
ask_image_X = ImageTk.PhotoImage((Image.open("images/audience_X.png")).resize((150 , 105) , Image.ANTIALIAS))
fifty_fifty_image = ImageTk.PhotoImage((Image.open("images/50_50.png")).resize((150 , 105) , Image.ANTIALIAS))
fifty_fifty_X_image = ImageTk.PhotoImage((Image.open("images/50_50_X.png")).resize((150 , 105) , Image.ANTIALIAS))
logo_tkinter_image = ImageTk.PhotoImage((Image.open("images/center.png")).resize((650 , 600) , Image.ANTIALIAS ))
logo_image = ImageTk.PhotoImage((Image.open("images/logo.png")).resize((600 , 600) , Image.ANTIALIAS ))
logo_image_small = ImageTk.PhotoImage((Image.open("images/logo.png")).resize((400 , 400) , Image.ANTIALIAS ))
proceed_image = ImageTk.PhotoImage((Image.open("images/Picture3.png") ).resize((600 , 100) , Image.ANTIALIAS))
ask_friend_image = ImageTk.PhotoImage((Image.open("images/phone.png")).resize((150 , 105) , Image.ANTIALIAS))
ask_friend_X_image = ImageTk.PhotoImage((Image.open("images/phone_X.png")).resize((150 , 105) , Image.ANTIALIAS))
question_bracket_image = ImageTk.PhotoImage((Image.open("images/question.png")).resize((850 , 150) , Image.ANTIALIAS))
answer_A_image = ImageTk.PhotoImage((Image.open("images/answer_A.png")).resize((425 , 75) , Image.ANTIALIAS))
answer_B_image = ImageTk.PhotoImage((Image.open("images/answer_B.png")).resize((425 , 75) , Image.ANTIALIAS))
answer_C_image = ImageTk.PhotoImage((Image.open("images/answer_C.png")).resize((425 , 75) , Image.ANTIALIAS))
answer_D_image = ImageTk.PhotoImage((Image.open("images/answer_D.png")).resize((425 , 75) , Image.ANTIALIAS))
empty_bracket_image = ImageTk.PhotoImage((Image.open("images/Picture6.png")).resize((425 , 75) , Image.ANTIALIAS))
answer_wrong = ImageTk.PhotoImage((Image.open("images/wrong_answer.png")).resize((425 , 75) , Image.ANTIALIAS))
answer_correct = ImageTk.PhotoImage((Image.open("images/correct_answer.png")).resize((425 , 75) , Image.ANTIALIAS))
answer_correct_large = ImageTk.PhotoImage((Image.open("images/correct_answer.png")).resize((850 , 150) , Image.ANTIALIAS))
exit_image = ImageTk.PhotoImage((Image.open("images/Picture5.png")).resize((250 , 75) , Image.ANTIALIAS))
exit_image_large = ImageTk.PhotoImage((Image.open("images/Picture5.png")).resize((350 , 100) , Image.ANTIALIAS))
exit_image_xlarge = ImageTk.PhotoImage((Image.open("images/Picture5.png")).resize((425 , 135) , Image.ANTIALIAS))

continue_image = ImageTk.PhotoImage((Image.open("images/Picture4.png")).resize((350 , 100) , Image.ANTIALIAS))
continue_image_large = ImageTk.PhotoImage((Image.open("images/Picture4.png")).resize((450 , 150) , Image.ANTIALIAS))
answers_0_image = ImageTk.PhotoImage((Image.open("images/answers_0.png")).resize((300 , 900) , Image.ANTIALIAS))
answers_1_image = ImageTk.PhotoImage((Image.open("images/answers_1.png")).resize((300 , 900) , Image.ANTIALIAS))
answers_2_image = ImageTk.PhotoImage((Image.open("images/answers_2.png")).resize((300 , 900) , Image.ANTIALIAS))
answers_3_image = ImageTk.PhotoImage((Image.open("images/answers_3.png")).resize((300 , 900) , Image.ANTIALIAS))
answers_4_image = ImageTk.PhotoImage((Image.open("images/answers_4.png")).resize((300 , 900) , Image.ANTIALIAS))
answers_5_image = ImageTk.PhotoImage((Image.open("images/answers_5.png")).resize((300 , 900) , Image.ANTIALIAS))
answers_6_image = ImageTk.PhotoImage((Image.open("images/answers_6.png")).resize((300 , 900) , Image.ANTIALIAS))
answers_7_image = ImageTk.PhotoImage((Image.open("images/answers_7.png")).resize((300 , 900) , Image.ANTIALIAS))
answers_8_image = ImageTk.PhotoImage((Image.open("images/answers_8.png")).resize((300 , 900) , Image.ANTIALIAS))
answers_9_image = ImageTk.PhotoImage((Image.open("images/answers_9.png")).resize((300 , 900) , Image.ANTIALIAS))
answers_10_image = ImageTk.PhotoImage((Image.open("images/answers_10.png")).resize((300 , 900) , Image.ANTIALIAS))
answers_11_image = ImageTk.PhotoImage((Image.open("images/answers_11.png")).resize((300 , 900) , Image.ANTIALIAS))
answers_12_image = ImageTk.PhotoImage((Image.open("images/answers_12.png")).resize((300 , 900) , Image.ANTIALIAS))
answers_13_image = ImageTk.PhotoImage((Image.open("images/answers_13.png")).resize((300 , 900) , Image.ANTIALIAS))
answers_14_image = ImageTk.PhotoImage((Image.open("images/answers_14.png")).resize((300 , 900) , Image.ANTIALIAS))
answers_15_image = ImageTk.PhotoImage((Image.open("images/answers_15.png")).resize((300 , 900) , Image.ANTIALIAS))

poll_A_image = ImageTk.PhotoImage((Image.open("images/poll_A.png")).resize((370 , 592) , Image.ANTIALIAS))
poll_B_image = ImageTk.PhotoImage((Image.open("images/poll_B.png")).resize((370 , 592) , Image.ANTIALIAS))
poll_C_image = ImageTk.PhotoImage((Image.open("images/poll_C.png")).resize((370 , 592) , Image.ANTIALIAS))
poll_D_image = ImageTk.PhotoImage((Image.open("images/poll_D.png")).resize((370 , 592) , Image.ANTIALIAS))
poll_equal_image = ImageTk.PhotoImage((Image.open("images/poll_equal.png")).resize((370 , 592) , Image.ANTIALIAS))

# End of Images
# Main page


intro_sound = pygame.mixer.Sound('sounds/intro.wav')
intro_sound.set_volume(0.2)
intro_sound.play(-1)  
main_page_logo = Label(main_page , image=logo_tkinter_image , bg=main_bg_color)
main_proceed_image_button = Button(main_page, image=continue_image_large, text="Play" , bg=main_bg_color , borderwidth=0 , highlightthickness=0 , fg=main_bg_color, activebackground=main_bg_color, activeforeground=main_bg_color, command=instruction_page_move)
main_proceed_image_button.pack(side= BOTTOM , pady=50)
main_page_logo.place(x=685 , y =100)
# End of Main Page
# Instructions Page
instructions_page_bg_label = Label(instructions_page , image=logo_image , bg=main_bg_color)
instructions_page_bg_label.pack(side=TOP , pady=50)
instructions_page_proceed_image_button = Button(instructions_page, command=questions_page_move , image=proceed_image, text="Play" , bg=main_bg_color , borderwidth=0 , highlightthickness=0 , fg=main_bg_color, activebackground=main_bg_color, activeforeground=main_bg_color)
instructions_page_proceed_image_button.pack(side= BOTTOM , pady=50)
instructions_page_ask_image_button = Button(instructions_page  , compound=TOP ,  command=lambda : instruction_buttons("اسأل الجمهور" , "تستطيع إستعمال هذه المساعدة لسؤال الجمهور والحصول على نسبة الإجابات") , image= ask_image , text="اسأل الجمهور" , fg='white', bg=main_bg_color , borderwidth=0 , highlightthickness=0 , activebackground=main_bg_color, activeforeground="white" , font=("Arial" , 25 , 'bold'))
instructions_page_ask_image_button.place(x=670 , y=700)
instructions_page_50_50_image_button = Button(instructions_page , compound=TOP , command=lambda : instruction_buttons("50/50" , "تستطيع إستعمال هذه المساعدة لتحذف إجابتين خاطئتين"), image= fifty_fifty_image , text="حذف إجابتين" , fg='white', bg=main_bg_color , borderwidth=0 , highlightthickness=0 , activebackground=main_bg_color, activeforeground="white" , font=("Arial" , 25 , 'bold'))
instructions_page_50_50_image_button.place(x=870 , y=700)
instructions_page_ask_friend_image_button = Button(instructions_page , compound=TOP, command=lambda : instruction_buttons("إتصل بصديق" , "تستطيع إستعمال هذه المساعدة بالإتصال بصديق لمساعدتك في سؤال معين") , image= ask_friend_image , text="إتصل بصديق" , fg='white', bg=main_bg_color , borderwidth=0 , highlightthickness=0 , activebackground=main_bg_color, activeforeground="white" , font=("Arial" , 25 , 'bold'))
instructions_page_ask_friend_image_button.place(x=1070 , y=700)
# End of Instructions Page
# Questions Page




first_question = questions_answers[0].get('question')
answers = questions_answers[0].get('answers')
random.shuffle(answers)
answer1 = answers[0]
answer2 = answers[1]
answer3 = answers[2]
answer4 = answers[3]
    

questions_page_ask_image_button = Button(questions_page  , image= ask_image , text="اسأل الجمهور" , bg=main_bg_color , borderwidth=0 , highlightthickness=0 , fg=main_bg_color, activebackground=main_bg_color, activeforeground=main_bg_color)
questions_page_ask_image_button['command'] = lambda : ask_audience_help(questions_page_ask_image_button , questions_page_answer_bracket_one , questions_page_answer_bracket_two , questions_page_answer_bracket_three , questions_page_answer_bracket_four)
questions_page_ask_image_button.place(x=550 , y=50)
questions_page_50_50_image_button = Button(questions_page , image= fifty_fifty_image , text="اسأل الجمهور" , bg=main_bg_color , borderwidth=0 , highlightthickness=0 , fg=main_bg_color, activebackground=main_bg_color, activeforeground=main_bg_color)
questions_page_50_50_image_button['command'] = lambda : fifty_fifty_help(questions_page_50_50_image_button , questions_page_answer_bracket_one , questions_page_answer_bracket_two , questions_page_answer_bracket_three , questions_page_answer_bracket_four)
questions_page_50_50_image_button.place(x=850 , y=50)
questions_page_ask_friend_image_button = Button(questions_page , image= ask_friend_image , text="اسأل الجمهور" , bg=main_bg_color , borderwidth=0 , highlightthickness=0 , fg=main_bg_color, activebackground=main_bg_color, activeforeground=main_bg_color)
questions_page_ask_friend_image_button['command'] = lambda : call_friend_help(questions_page_ask_friend_image_button , questions_page_answer_bracket_one , questions_page_answer_bracket_two , questions_page_answer_bracket_three , questions_page_answer_bracket_four)
questions_page_ask_friend_image_button.place(x=1150 , y=50)
questions_page_logo = Label(questions_page , image=logo_image_small , bg=main_bg_color)
questions_page_logo.place(x= 725 , y=170)
questions_page_answers = Label(questions_page , image= answers_0_image, bg=main_bg_color)
questions_page_answers.pack(side=RIGHT , padx=50 )

questions_page_poll = Label(questions_page , image=poll_A_image , bg=main_bg_color)
# questions_page_poll.pack(side=LEFT , anchor="nw" , padx=50 , pady=100)
questions_page_poll.pack_forget()

questions_page_question_bracket = Label(questions_page , image= question_bracket_image , text=first_question  , compound=CENTER , borderwidth=0 , highlightthickness=0 , fg='white', bg=main_bg_color, activebackground=main_bg_color, activeforeground=main_bg_color , font=("Arial" , 25 , 'bold') , wraplength=800)
questions_page_question_bracket.place(x= 475 , y=600)

questions_page_answer_bracket_one = Button(questions_page , image= answer_B_image , text=answer1 , compound=CENTER , fg='white', bg=main_bg_color , borderwidth=0 , highlightthickness=0 , activebackground=main_bg_color, activeforeground="white" , font=("Arial" , 25 , 'bold'))
questions_page_answer_bracket_one.place(x= 475 , y=800)
questions_page_answer_bracket_one['command'] = lambda : select_answer(questions_page_answer_bracket_one , questions_page_answer_bracket_two , questions_page_answer_bracket_three , questions_page_answer_bracket_four)

questions_page_answer_bracket_two = Button(questions_page , image= answer_A_image , text=answer2 , compound=CENTER , fg='white', bg=main_bg_color , borderwidth=0 , highlightthickness=0 , activebackground=main_bg_color, activeforeground="white" , font=("Arial" , 25 , 'bold'))
questions_page_answer_bracket_two.place(x= 905 , y=800)
questions_page_answer_bracket_two['command'] = lambda : select_answer( questions_page_answer_bracket_two, questions_page_answer_bracket_one , questions_page_answer_bracket_three , questions_page_answer_bracket_four)

questions_page_answer_bracket_three = Button(questions_page , image= answer_C_image , text=answer3 , compound=CENTER , fg='white', bg=main_bg_color , borderwidth=0 , highlightthickness=0 , activebackground=main_bg_color, activeforeground="white" , font=("Arial" , 25 , 'bold'))
questions_page_answer_bracket_three.place(x= 905 , y=900)
questions_page_answer_bracket_three['command'] = lambda : select_answer( questions_page_answer_bracket_three, questions_page_answer_bracket_two , questions_page_answer_bracket_one , questions_page_answer_bracket_four)

questions_page_answer_bracket_four = Button(questions_page , image= answer_D_image , text=answer4 , compound=CENTER , fg='white', bg=main_bg_color , borderwidth=0 , highlightthickness=0 , activebackground=main_bg_color, activeforeground="white" , font=("Arial" , 25 , 'bold'))
questions_page_answer_bracket_four.place(x= 475 , y=900)
questions_page_answer_bracket_four['command'] = lambda : select_answer( questions_page_answer_bracket_four, questions_page_answer_bracket_two , questions_page_answer_bracket_three , questions_page_answer_bracket_one)

questions_page_continue_button = Button(questions_page , image= continue_image , compound=CENTER , fg='white', bg=main_bg_color , borderwidth=0 , highlightthickness=0 , activebackground=main_bg_color, activeforeground="white" , font=("Arial" , 25 , 'bold'))
# questions_page_continue_button.place(x=725 , y=980)
questions_page_continue_button.pack_forget()
questions_page_continue_button['command'] = lambda : next_question_fun(questions_page_answer_bracket_one , questions_page_answer_bracket_two , questions_page_answer_bracket_three , questions_page_answer_bracket_four)

questions_page_next_button = Button(questions_page , image= exit_image_large , compound=CENTER , fg='white', bg=main_bg_color , borderwidth=0 , highlightthickness=0 , activebackground=main_bg_color, activeforeground="white" , font=("Arial" , 25 , 'bold'))
# questions_page_next_button.place(x=725 , y=980)
questions_page_next_button.pack_forget()
questions_page_next_button['command'] = lambda : final_page_move()

questions_page_money_label = Label(questions_page , image= answer_correct_large , text="1000000$"  , compound=CENTER , borderwidth=0 , highlightthickness=0 , fg='gold', bg=main_bg_color, activebackground=main_bg_color, activeforeground=main_bg_color , font=("Modern No. 20" , 55 , 'bold') , wraplength=800)
# questions_page_money_label.place(x= 475 , y=400)
questions_page_money_label.pack_forget()

questions_page_exit = Button(questions_page , image= exit_image , command=close_app , bg=main_bg_color , borderwidth=0 , highlightthickness=0 , fg=main_bg_color, activebackground=main_bg_color, activeforeground=main_bg_color , )
questions_page_exit.place(x=25, y=950)

# End of Questions Page

# Start of Final Page

final_page_logo = Label(final_page , image=logo_image , bg=main_bg_color)
final_page_logo.pack(side= TOP , pady=100)

final_page_money_recieved = Label(final_page , image=question_bracket_image  , compound=CENTER , borderwidth=0 , highlightthickness=0 , fg='white', bg=main_bg_color, activebackground=main_bg_color, activeforeground=main_bg_color , font=("Arial" , 55 , 'bold') , wraplength=800)
final_page_money_recieved.place(x=525 , y=700)

questions_page_exit = Button(final_page , image= exit_image_xlarge , command=close_app , bg=main_bg_color , borderwidth=0 , highlightthickness=0 , fg=main_bg_color, activebackground=main_bg_color, activeforeground=main_bg_color , )
questions_page_exit.place(x=750, y=877)

root.mainloop()