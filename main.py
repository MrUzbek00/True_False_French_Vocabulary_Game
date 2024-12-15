from tkinter import * 
import pandas
from random import *

BACKGROUND_COLOR = "#B1DDC6"
CROSS_BUTTON ="D:/Python/100 days Python Challenge/Intermediate/day 31/images/wrong.png"
TICK_BUTTON = "D:/Python/100 days Python Challenge/Intermediate/day 31/images/right.png"
CARD_FRONT = "D:/Python/100 days Python Challenge/Intermediate/day 31/images/card_front.png"
CARD_BACK = "D:/Python/100 days Python Challenge/Intermediate/day 31/images/card_back.png"
WORD_LIST ="D:/Python/100 days Python Challenge/Intermediate/day 31/data/french_words.csv"
WORDS_TO_LEARN = "D:/Python/100 days Python Challenge/Intermediate/day 31/data/words_to_learn.csv"
current_word = {}
#--------------------------------Logic ------------------------------------#
try:
    data = pandas.read_csv(WORDS_TO_LEARN)
except FileNotFoundError:
    original_data = pandas.read_csv(WORD_LIST)
    data_dictionary = original_data.to_dict(orient="records")
else:
    data_dictionary = data.to_dict(orient="records")

def next_card():
    word_list =pandas.read_csv(WORD_LIST)
    random_word =word_list["French"][randint(1,len(word_list["French"])-1)]
    canvas.itemconfig(word, text=random_word)

def updated_next_card():
    global current_card, flipper_timer
    window.after_cancel(flipper_timer)
    current_card = choice(data_dictionary)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_background, image= card_front_img)
    flipper_timer = window.after(3000, func=flip_card)

def is_known():
    data_dictionary.remove(current_card)
    data = pandas.DataFrame(data_dictionary)
    data.to_csv(WORDS_TO_LEARN)
    updated_next_card()

def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_background, image= card_back_img)
    

#---------------------------UI-----------------------------------------------#
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(height=500, width=500, )
flipper_timer = window.after(3000, func=flip_card)
canvas = Canvas(height=526, width=800,bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img=PhotoImage(file=CARD_FRONT)
card_back_img = PhotoImage(file=CARD_BACK)
canvas_background = canvas.create_image(400, 263, image= card_front_img)
canvas.grid(column=0, row=0, columnspan=3)
title=canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Ariel", 50, "bold"))


#Buttons 
cross_img=PhotoImage(file=CROSS_BUTTON)
cross_button = Button(image=cross_img, highlightthickness=0, height=75, width=75, command=updated_next_card)
cross_button.grid(column=0, row=2)

tick_img = PhotoImage(file=TICK_BUTTON)
tick_button = Button(image=tick_img, highlightthickness=0, height=75, width=75, command=is_known)
tick_button.grid(column=2, row=2)

updated_next_card()
window.mainloop()



