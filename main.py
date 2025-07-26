from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn_dict = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn_dict = original_data.to_dict(orient="records")


else:
    to_learn_dict = data.to_dict(orient='records')
    print(to_learn_dict)

def is_known():
    to_learn_dict.remove(current_card)
    print(len(to_learn_dict))
    df=pandas.DataFrame(to_learn_dict)
    df.to_csv("data/words_to_learn.csv",index=False)
    next_card()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn_dict)
    random_french_word = current_card["French"]
    canvas.itemconfig(card_title, text="French",fill="black")
    canvas.itemconfig(card_word, text=random_french_word,fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    flip_timer=window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill= "white")
    canvas.itemconfig(card_word, text=current_card["English"], fill= "white")


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
flip_timer=window.after(3000, func=flip_card)


card_back_image=PhotoImage(file="images/card_back.png")
card_front_image=PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800,height=526)
card_background=canvas.create_image(400,263,image=card_front_image)
card_title=canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word=canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(highlightthickness=0,bg=BACKGROUND_COLOR)
canvas.grid(row=0,column=0,columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
right_button = Button(image=check_img, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)



next_card()




window.mainloop()
