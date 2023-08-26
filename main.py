from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#FFFFFF"
BLACK = "#000000"
SECONDS = 3*1000
words = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except:
    data = pandas.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")


# -------------------- CHECK BUTTON -------------------- #
def know_word():
    to_learn.remove(words)
    data = pandas.DataFrame(to_learn)

    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# -------------------- X BUTTON -------------------- #
def unknown_word():
    next_card()


# -------------------- NEXT CARD -------------------- #
def next_card():
    global words, timer

    window.after_cancel(timer)

    canvas.itemconfig(background, image=french_card)
    words = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill=BLACK)
    canvas.itemconfig(card_word, text=words["French"], fill=BLACK)

    timer = window.after(SECONDS, flip_card)


# -------------------- FLIP CARD -------------------- #
def flip_card():
    canvas.itemconfig(background, image=english_card)
    canvas.itemconfig(card_title, text="English", fill=WHITE)
    canvas.itemconfig(card_word, text=words["English"], fill=WHITE)


# -------------------- UI SETUP -------------------- #
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

timer = window.after(SECONDS, func=flip_card)

# Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

french_card = PhotoImage(file="images/card_front.png")
english_card = PhotoImage(file="images/card_back.png")
background = canvas.create_image(400, 263, image=french_card)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_img, highlightthickness=0, command=know_word)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=unknown_word)

right_button.grid(column=1, row=1)
wrong_button.grid(column=0, row=1)

next_card()

window.mainloop()
