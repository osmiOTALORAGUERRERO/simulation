import tkinter
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from board import Board
from needle import Needle

"""
Author: Osmi Santiago Otálora Guerrero
last_modification: 17/08/2020
"""

def pi_probability(n_needles, n_intersection, needle_size, distance_between_lines):
    return (2*needle_size*n_needles)/(distance_between_lines*n_intersection)

def initSimulation():
    # print(type(n_needles.get()), n_needles.get())
    # print(type(b_width.get()), b_width.get())
    # print(type(b_height.get()), b_height.get())
    # print(b_lines.get())
    # print(size_needle.get())

    if int(n_needles.get()) <= 0:
        return

    plt.cla()
    plt.clf()
    plt.close()



    my_board = None

    try:
        if (int(b_width.get())>0 and int(b_height.get())>0):
            my_board = Board(int(b_height.get()), int(b_width.get()))
        else:
            my_board = Board()
    except Exception as e:
        print(e)
        my_board = Board()


    print(my_board.width)

    if int(b_lines.get()) > 0 and int(b_lines.get()) < my_board.height:
        my_board.generate_lines(int(b_lines.get()))

    needle_size = None

    if float(size_needle.get()) <= my_board.distance_between_lines:
        needle_size = float(size_needle.get()) if (float(size_needle.get()) > 0) else my_board.distance_between_lines
    else:
        print('Line so large')
        return

    # print(needle_size)
    for throws in range(int(n_needles.get())):
        my_board.throw_needle(Needle(needle_size))

    n_needles_board = my_board.n_needles
    n_intersection = my_board.n_needles_intersection
    distance_between_lines = my_board.distance_between_lines

    pi = pi_probability(n_needles_board, n_intersection, needle_size, distance_between_lines)
    print('pi: ',pi)

    #Print lines
    for line in my_board.lines:
        x, y = [line.start.x, line.end.x], [line.start.y, line.end.y]
        plt.plot(x, y)
    #Print needles
    for needle in my_board.needles:
        x, y = [needle.head.x, needle.point.x], [needle.head.y, needle.point.y]
        plt.plot(x, y)

    textstr = '\n'.join((
    r'$\pi=%.2f$' % (pi, ),
    r'needles=%.2f' % (n_needles_board, ),
    r'intersections=%.2f' % (n_intersection, ),
    r'needle size=%.2f' % (needle_size, ),
    r'space lines=%.2f' % (distance_between_lines, )))
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

    plt.text(10, 10, textstr, fontsize=12, verticalalignment='top', bbox=props)

    plt.show()

    return

"""
  |------------------------------------
 |  Graphical
|------------------------------------
"""
class Placeholder_State(object):
     __slots__ = 'normal_color', 'normal_font', 'placeholder_text', 'placeholder_color', 'placeholder_font', 'with_placeholder'

def add_placeholder_to(entry, placeholder, color="grey", font=None):
    normal_color = entry.cget("fg")
    normal_font = entry.cget("font")

    if font is None:
        font = normal_font

    state = Placeholder_State()
    state.normal_color=normal_color
    state.normal_font=normal_font
    state.placeholder_color=color
    state.placeholder_font=font
    state.placeholder_text = placeholder
    state.with_placeholder=True

    def on_focusin(event, entry=entry, state=state):
        if state.with_placeholder:
            entry.delete(0, "end")
            entry.config(fg = state.normal_color, font=state.normal_font)

            state.with_placeholder = False

    def on_focusout(event, entry=entry, state=state):
        if entry.get() == '':
            entry.insert(0, state.placeholder_text)
            entry.config(fg = state.placeholder_color, font=state.placeholder_font)

            state.with_placeholder = True

    entry.insert(0, placeholder)
    entry.config(fg = color, font=font)

    entry.bind('<FocusIn>', on_focusin, add="+")
    entry.bind('<FocusOut>', on_focusout, add="+")

    entry.placeholder_state = state

    return state

window = Tk()
window.wm_title("Buffon's Needle")

ln = Label(window,text="n Needles:")
ln.grid(row=0,column=0)
n_needles = tkinter.IntVar()
e1 = Entry(window, textvariable=n_needles)
e1.grid(row=0,column=1)
add_placeholder_to(e1, '0')

ttk.Separator(window, orient='horizontal')
lo = Label(window, text="*Opcional*")
lo.config(fg="red", font=("Verdana",12))
lo.grid(row=1, column=0)

lb = Label(window,text="Board:")
lb.grid(row=2,column=0)
b_width = tkinter.StringVar()
e2 = Entry(window, textvariable=b_width)
e2.grid(row=2,column=1)
add_placeholder_to(e2, 'width')

b_height = tkinter.StringVar()
e3 = Entry(window, textvariable=b_height)
e3.grid(row=2,column=2)
add_placeholder_to(e3, 'height')

lb = Label(window,text="n Parallel lines:")
lb.grid(row=3,column=0)

b_lines = tkinter.IntVar()
e4 = Entry(window, textvariable=b_lines)
e4.grid(row=3,column=1)
add_placeholder_to(e4, '0')

lb = Label(window,text="size needle:")
lb.grid(row=4,column=0)

size_needle = tkinter.DoubleVar()
e5 = Entry(window, textvariable=size_needle)
e5.grid(row=4,column=1)
add_placeholder_to(e5, '0')


solver = ttk.Button(window,text="Simulate",width=8,command=initSimulation)
solver.grid(row=0,column=2)

window.mainloop()
