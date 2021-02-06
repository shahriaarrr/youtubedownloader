from pytube import YouTube
from tkinter import *



class Main():
    def __init__(self):
        self.win = Tk()
        #config
        self.config_title = 'youtube downloader'
        self.config_width = 450
        self.confing_heigt = 350
        self.config_resizable = [False, False]
        self.config_background = '#F36A05'

        #load functions
        self.Load_Configs()
        self.Load_objects()

        #mainloop
        mainloop()

    def Load_Configs(self):
        self.win.title(self.config_title)
        self.win.geometry(str(self.config_width) + 'x' + str(self.confing_heigt))
        self.win.resizable(self.config_resizable[0], self.config_resizable[1])
        self.win.config(bg = self.config_background)

    def Load_objects(self):
        #space bitween head and text label
        Label(
            self.win,
            text = '  ',
            background = self.config_background,
            font = ('Arial', 30)
        ).pack()

        Label(
            self.win,
            text = "Give me your youtube link: ",
            foreground = 'black',
            background = self.config_background,
            font = ('Arial', 20, 'bold') ,
        ).pack()

        link_input = Entry(
            self.win,
            background = '#FFFFFF',
            foreground = 'black',
            width = 64,
        ).pack()

        #space bitween download button and text label
        Label(
            self.win,
            text = '  ',
            background = self.config_background,
            font = ('Arial', 30)
        ).pack()

        download_button = Button(
            self.win,
            text = 'download',
            background = '#0DF55E',
            foreground = 'black',
            border = 5,
        ).pack()



app = Main()