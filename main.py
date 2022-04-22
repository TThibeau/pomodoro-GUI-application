from tkinter import *
import os
os.system('cls || clear')

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
session_nr = 1
start_pressed = 0   # Used to track if start button has already been pressed

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    global session_nr, start_pressed
    session_nr = 1
    start_pressed = 0
    sc_label.config(text="")
    timer_label.config(text="Timer",fg=GREEN)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def add_checkmark():
    global session_nr
    checkmarks= []
    checkmarks = ["✔" for i in range(session_nr) if i % 2 == 0]
    check_str = ''.join(str(e) for e in checkmarks)
    sc_label.config(text=check_str)

def start_timer():
    global session_nr, start_pressed
    if start_pressed < 1:
        start_pressed +=1
        if session_nr % 8 == 0:     # Long break session
            add_checkmark()
            timer_label.config(text="Long break",fg=PINK)
            timer_length = LONG_BREAK_MIN*60

        elif session_nr % 2 == 0:    # Short break session
            add_checkmark()
            timer_label.config(text="Short break",fg=GREEN)
            timer_length = SHORT_BREAK_MIN*60

        else:                        # Work session
            timer_label.config(text="Work",fg=RED)
            timer_length = WORK_MIN*60

        session_nr += 1

        count_down(timer_length)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes, seconds = divmod(count,60)
    minutes, seconds = round(minutes), round(seconds)
    if seconds < 10: seconds = f"0{seconds}"

    canvas.itemconfig(timer_text,text=f"{minutes}:{seconds}")
     
    if count > 0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50,pady=50, bg=YELLOW)

tomato_img = PhotoImage(file="tomato.png")

timer_label = Label(text="Timer",font=(FONT_NAME,35,"bold"),fg=GREEN,bg=YELLOW)
timer_label.grid(row=0,column=1)

canvas = Canvas(width=205,height=224,bg=YELLOW, highlightthickness=0)
canvas.create_image(103,112,image=tomato_img)
timer_text = canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)


start_button = Button(text="Start",command=start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2,column=2)

# Sessions completed Label
sc_label = Label(font=(FONT_NAME,25,"bold"),fg=GREEN,bg=YELLOW)
sc_label.grid(row=3,column=1)

window.mainloop()