from tkinter import *



class Main():
    def __init__(self):
        self.win = Tk()
        # --- [config] ---- #
        self.config_title = 'youtube downloader'
        self.config_width = 350
        self.confing_heigt = 250
        self.config_resizable = [False, False]

        # --- [load functions] --- #
        self.Load_Configs()

        mainloop()

    def Load_Configs(self):
        self.win.title(self.config_title)
        self.win.geometry(str(self.config_width) + 'x' + str(self.confing_heigt))
        self.win.resizable(self.config_resizable[0], self.config_resizable[1])


application = Main()