import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox

root = tk.Tk()
root.resizable(False, True)
root.configure(background = '#c97ee7')
root.title('Mad-Libs Generator')

n = StringVar()
adj = StringVar()
celeb = StringVar()
v = StringVar()
plu = StringVar()
adv = StringVar()
ing = StringVar()
ani = StringVar()

def mad():
    messagebox.showinfo(message = f"""'I love eating {n.get()}. Its my {adj.get()}. By the way, did you hear about {celeb.get()}? Apparently, they {v.get()} a bunch
                  of people, but {plu.get()} said nothing about it. Also, my sister is {adv.get()} {ing.get()} into a {ani.get()}. 
                  So that's good news!""")
def interface():
    canvas = tk.Canvas(root, bg = "#c97ee7",
            height = 600, width = 700)
    canvas.pack(side = 'left')

    scrollbar = tk.Scrollbar(root, command = canvas.yview)
    scrollbar.pack(side = 'left', fill = 'both')

    canvas.configure(yscrollcommand = scrollbar.set)

    canvas.bind('<Configure>', lambda E: canvas.configure(scrollregion = canvas.bbox('all')))

    frame = tk.Frame(canvas, bg = "#c97ee7")
    canvas.create_window((0,0), window = frame, anchor = 'nw')
                    
    title = tk.Label(frame, bg = "#c97ee7",
                text = "Mad-Libs Generator", font = ('Segoe Print', 24))
    title.pack(padx = 180, pady = 10)

    noun = tk.Label(frame, text = 'Noun:', bg = '#c97ee7',
            font = ('Segoe Print', 22))
    noun.pack(pady = 6)
    noun_entry = Entry(frame, width = 15,
                justify = 'center', 
                borderwidth = 2,
                font = ('Segoe Print', 14),
                textvariable = n)
    noun_entry.pack(pady = 5, ipady = 7)

    adjective = tk.Label(frame, text = 'Adjective:', bg = '#c97ee7',
            font = ('Segoe Print', 22))
    adjective.pack(pady = 6)
    adj_entry = Entry(frame, width = 15,
                justify = 'center', 
                borderwidth = 2,
                font = ('Segoe Print', 14),
                textvariable = adj)
    adj_entry.pack(pady = 5, ipady = 7)

    celebrity = tk.Label(frame, text = 'Celebrity:', bg = '#c97ee7',
            font = ('Segoe Print', 22))
    celebrity.pack(pady = 6)
    celebrity_entry = Entry(frame, width = 15,
                justify = 'center', 
                borderwidth = 2,
                font = ('Segoe Print', 14),
                textvariable = celeb)
    celebrity_entry.pack(pady = 5, ipady = 7)


    verb = tk.Label(frame, text = 'Verb ending w/ "ed":', bg = '#c97ee7',
            font = ('Segoe Print', 22))
    verb.pack(pady = 6)
    verb_entry = Entry(frame, width = 15,
                justify = 'center', 
                borderwidth = 2,
                font = ('Segoe Print', 14),
                textvariable = v)
    verb_entry.pack(pady = 5, ipady = 7)


    pluNoun = tk.Label(frame, text = 'Plural noun:', bg = '#c97ee7',
            font = ('Segoe Print', 22))
    pluNoun.pack(pady = 6)
    pluNoun_entry = Entry(frame, width = 15,
                justify = 'center', 
                borderwidth = 2,
                font = ('Segoe Print', 14),
                textvariable = plu)
    pluNoun_entry.pack(pady = 5, ipady = 7)

    adverb = tk.Label(frame, text = 'Adverb:', bg = '#c97ee7',
                font = ('Segoe Print', 22))
    adverb.pack(pady = 6)
    adverb_entry = Entry(frame, width = 15,
                justify = 'center', 
                borderwidth = 2,
                font = ('Segoe Print', 14),
                textvariable = adv)
    adverb_entry.pack(pady = 5, ipady = 7)

    ingVerb = tk.Label(frame, text = 'Verb ending w/ "ing":', bg = '#c97ee7',
                font = ('Segoe Print', 22))
    ingVerb.pack(pady = 6)
    ingVerb_entry = Entry(frame, width = 15,
                justify = 'center', 
                borderwidth = 2,
                font = ('Segoe Print', 14),
                textvariable = ing)
    ingVerb_entry.pack(pady = 5, ipady = 7)


    animal = tk.Label(frame, text = 'Animal:', bg = '#c97ee7',
                font = ('Segoe Print', 22))
    animal.pack(pady = 6)
    animal_entry = Entry(frame, width = 15,
                justify = 'center',
                borderwidth = 2,
                font = ('Segoe Print', 14),
                textvariable = ani)
    animal_entry.pack(pady = 5, ipady = 7)

    button = tk.Button(frame, bg = '#110416', command = mad,
                bd = 2,
                text = "Let's Go!", 
                fg = 'white', 
                relief = tk.SUNKEN, 
                activebackground = '#741c97',
                justify = 'center',
                font = ('Segoe Print', 16),
                width = 10)
    button.pack(pady = 18, ipady = 7)
    
interface()
  
root.mainloop()