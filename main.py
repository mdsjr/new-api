from tkinter import *
import requests
import json

class MovieData:

    def __init__(self):

        self.window = Tk()
        self.window.title("Movie Data")
        self.window.geometry("500x400+150+100")
        self.window.resizable(0,0)

        self.frame = Frame(self.window)
        self.frame.pack()

        self.text_entry = Entry(self.frame, font="arial 16", width=30)
        self.text_entry.grid()

        self.button_search = Button(self.frame, text="Search", font="arial 12", command=self.search)
        self.button_search.grid(row=0, column=1)

        self.list = Listbox(self.window)
        self.list.pack(fill=BOTH, expand=YES)

        self.window.mainloop()

    def search(self):
        try:
            request = requests.get("http://www.omdbapi.com/?t=" + self.text_entry.get() +"&apikey=f6389fed")
            dict = json.loads(request.text)

            self.list.delete(0, END)
            self.list.insert(END, "Title: " + dict["Title"])
            self.list.insert(END, "Year: " + dict["Year"])
            self.list.insert(END, "Released: " + dict["Released"])
            self.list.insert(END, "Runtime: " + dict["Runtime"])
            self.list.insert(END, "Genre: " + dict["Genre"])
            self.list.insert(END, "Director: " + dict["Director"])
        except:
            self.list.delete(0, END)
            self.list.insert(END, "Movie not found")



        print(dict)



MovieData()