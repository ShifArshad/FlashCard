import random
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
new_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/new_words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def new_random_card():
    global new_card, flip_timer
    window.after_cancel(flip_timer)
    new_card = random.choice(to_learn)
    canvas.itemconfig(new_title, text="French", fill="black")
    canvas.itemconfig(new_word, text=new_card["French"], fill="black")
    canvas.itemconfig(front_image, image=image_png_front)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(front_image, image=image_png_back)
    canvas.itemconfig(new_title, text="English", fill="white")
    canvas.itemconfig(new_word, text=new_card["English"], fill="white")


def new_file():
    to_learn.remove(new_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/new_words_to_learn.csv", index=False)
    new_random_card()


window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526)
image_png_back = PhotoImage(file="images/card_back.png")
image_png_front = PhotoImage(file="images/card_front.png")
front_image = canvas.create_image(400, 263, image=image_png_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
new_title = canvas.create_text(400, 150,text="Title", font=("Arial", 40, "italic"))
new_word = canvas.create_text(400, 263,text="Word", font=("Arial", 40, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=new_random_card)
cross_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=new_file)
check_button.grid(row=1, column=1)


new_random_card()

window.mainloop()
