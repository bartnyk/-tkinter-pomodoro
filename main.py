
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
clock = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global rep
    rep = 0
    tomato.after_cancel(clock)
    tomato.itemconfig(timer, text="")
    big_text.config(text="Timer", fg=GREEN)
    checkmark.config(text="")
    return rep

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global rep
    rep += 1
    if rep % 2 == 0:
        checkmark.config(text=f"{'✅' * (rep // 2)}")
    if rep in [1, 3, 5, 7]:
        big_text.config(text="Work", fg=GREEN)
        return count_down(WORK_MIN*60)
    elif rep in [2, 4, 6]:
        big_text.config(text="Short Brake", fg=PINK)
        return count_down(SHORT_BREAK_MIN*60)
    elif rep == 8:
        big_text.config(text="Long Brake", fg=RED)
        return count_down(LONG_BREAK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    minutes = count//60
    seconds = count%60
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    tomato.itemconfig(timer, text=f"{minutes}:{seconds}")
    if count > 0:
        global clock
        clock = window.after(1000, count_down, count-1)
    else:
        return start_timer()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=160, pady=100, bg=YELLOW)

big_text = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
big_text.grid(row=0, columnspan=3)

tomato = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
tomato.create_image(100, 112, image=tomato_img)
timer = tomato.create_text(100, 150, text="", fill="white", font=(FONT_NAME, 20, "bold"))
tomato.grid(row=1, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 16, "bold"), command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button( text="Reset", font=(FONT_NAME, 16, "bold"), command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark = Label(pady=10, text = "", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 16, "bold"))
checkmark.grid(row=4, column=1)


mainloop()