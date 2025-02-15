from tkinter import *
import requests
import json

class MovieData:

    def __init__(self):

        self.window = Tk()
        self.window.title("Movie Data")
        self.window.geometry("1280x720+300+150")
        self.window.resizable(0,0)

        self.request = requests.get("http://www.omdbapi.com/?s=starwars&apikey=f6389fed")
        self.dict = json.loads(self.request.text)

        self.frame = Frame(self.window)
        self.frame.pack()

        self.text_entry = Entry(self.frame)
        self.text_entry.pack()

        self.button_search = Button(self.frame)
        self.button_search.grid(row=0, column=1)

        self.list = Listbox(self.window)
        self.list.pack()

        self.window.mainloop()


MovieData()