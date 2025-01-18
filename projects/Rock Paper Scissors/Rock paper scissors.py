from customtkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import pygame

pygame.init()
pygame.mixer.init()

def close_app():
    app.destroy()

app = CTk()
app.geometry('1000x800')
set_appearance_mode('dark')

pygame.mixer.music.load('music.wav')
pygame.mixer.music.play(-1)

frame1 = CTkFrame(app, border_width=2, fg_color="lightgray")
frame1.pack(padx=10, pady=10, fill="both", expand=True)
frame2 = CTkFrame(app, border_width=2, fg_color="lightblue")
frame2.pack(padx=10, pady=10, fill="both", expand=True)

choices = ['rock', 'paper', 'scissor']

rocki = Image.open("rock.png").resize((300, 200), Image.LANCZOS)
rocki = ImageTk.PhotoImage(rocki)

paperi = Image.open("paper.png").resize((300, 200), Image.LANCZOS)
paperi = ImageTk.PhotoImage(paperi)

scissori = Image.open("scissor.png").resize((300, 200), Image.LANCZOS)
scissori = ImageTk.PhotoImage(scissori)

image_label1 = CTkLabel(frame1, text='', text_color='Black', font=('Comic Sans MS', 30))
image_label1.pack(pady=20)

image_label2 = CTkLabel(frame2, text='', text_color='Black', font=('Comic Sans MS', 30))
image_label2.pack(pady=20)

playerq = CTkEntry(frame1, height=30, width=200, placeholder_text='Enter name', border_color='Orange', border_width=2)
playerq.pack()

score = 0

labi = CTkLabel(frame1, text=f'Score: {score}', font=('Comic Sans MS', 18), text_color='black')
labi.pack(pady=20)

name_lbl = CTkLabel(frame1, text='Player ', text_color='Black', font=('Comic Sans MS', 30))
name_lbl.pack(pady=20)

ai_lbl = CTkLabel(frame2, text='AI', text_color='Black', font=('Comic Sans MS', 30))
ai_lbl.pack(pady=20)

player_choice = None  

def check_input():
    global player_name
    input_value = playerq.get().strip()
    if not input_value:
        messagebox.showinfo('Input Required', 'Enter something')
    else:
        player_name = input_value
        name_lbl.configure(text=f'Player {name_get()}')
        playerq.destroy()
        btnq.destroy()

def name_get():
    return player_name

btnq = CTkButton(frame1, text='Submit', command=check_input, corner_radius=20, fg_color='lightgrey', text_color='black', font=('Comic Sans MS', 16), hover_color='yellow')
btnq.pack()

def choose_rock():
    global player_choice
    player_choice = 'rock'
    comb()

def choose_paper():
    global player_choice
    player_choice = 'paper'
    comb()

def choose_scissor():
    global player_choice
    player_choice = 'scissor'
    comb()

btn1 = CTkButton(app, text='Rock', command=choose_rock, corner_radius=20, fg_color='lightgrey', text_color='black', font=('Comic Sans MS', 20), hover_color='yellow')
btn1.pack(padx=20)

btn2 = CTkButton(app, text='Paper', command=choose_paper, corner_radius=20, fg_color='lightgrey', text_color='black', font=('Comic Sans MS', 20), hover_color='yellow')
btn2.pack(padx=20)

btn3 = CTkButton(app, text='Scissor', command=choose_scissor, corner_radius=20, fg_color='lightgrey', text_color='black', font=('Comic Sans MS', 20), hover_color='yellow')
btn3.pack(padx=20)

def prob():
    global player_choice
    choice2 = random.choice(choices)
    return player_choice, choice2

def imgchose(choice1, choice2):
    if choice1 == 'rock':
        image_label1.configure(image=rocki)
        image_label1.image = rocki
    elif choice1 == 'scissor':
        image_label1.configure(image=scissori)
        image_label1.image = scissori
    elif choice1 == 'paper':
        image_label1.configure(image=paperi)
        image_label1.image = paperi

    if choice2 == 'rock':
        image_label2.configure(image=rocki)
        image_label2.image = rocki
    elif choice2 == 'scissor':
        image_label2.configure(image=scissori)
        image_label2.image = scissori
    elif choice2 == 'paper':
        image_label2.configure(image=paperi)
        image_label2.image = paperi

def comb():
    choice1, choice2 = prob()
    imgchose(choice1, choice2)
    decise(choice1, choice2)

def decise(choice1, choice2):
    global score
    if (choice1 == 'rock' and choice2 == 'scissor') or (choice1 == 'paper' and choice2 == 'rock') or (choice1 == 'scissor' and choice2 == 'paper'):
        score += 1
        labi.configure(text=f'Score: {score}')
        messagebox.showinfo('Result', '+1 Point')
    elif (choice2 == 'rock' and choice1 == 'scissor') or (choice2 == 'paper' and choice1 == 'rock') or (choice2 == 'scissor' and choice1 == 'paper'):
        score -= 1
        labi.configure(text=f'Score: {score}')
        messagebox.showinfo('Result', '-1 Point')
    elif choice1 == choice2:
        messagebox.showinfo('Result', "Draw")
    elif score > 10:
        messagebox.showinfo('WIN', f'{name_get()} wins!')
        close_app()

app.mainloop()
