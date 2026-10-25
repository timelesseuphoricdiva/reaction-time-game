
from tkinter import *
from random import *
from time import *

window = Tk()
window.title("Reaction Time")
window.geometry("500x350")

is_green = False
start_time = None

screen1 = Frame(window)
screen2 = Frame(window)
screen3 = Frame(window)

Label(screen3, text="Game Results", font=("Arial", 22)).pack()

results_label = Label(screen3, text="", font=("Arial", 18))
results_label.pack()


def switch_screen(current, next_screen):
    current.pack_forget()
    next_screen.pack(fill="both", expand=True)


def turn_green():
    global is_green, start_time

    is_green = True
    start_time = perf_counter()

    main_button.config(
        bg="green",
        highlightbackground="green",
        text="CLICK!!!"
    )


def button_clicked():
    if is_green:
        end_time = perf_counter()
        reaction_time = (end_time - start_time) * 1000

        print(reaction_time)
        results_label.config(
            text=f"Reaction time: {reaction_time:.0f} ms"
        )
    else:
        print("You clicked too early!!!")
        results_label.config(text="Too early!")

        # Cancel the scheduled green transition
        main_button.after_cancel(green_timer)

    switch_screen(screen2, screen3)


# Screen 2 Widgets
main_button = Button(
    screen2,
    width=33,
    height=10,
    text="Wait for green...",
    font=("Arial", 22),
    highlightbackground="red",
    command=button_clicked
)

main_button.place(x=20, y=40)

green_timer = main_button.after(
    randint(2000, 5100),
    turn_green
)

screen2.pack(fill="both", expand=True)

window.mainloop()

