from faulthandler import disable
import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import filedialog as fd

from DES_Vf import *
# from DDES import *


customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  


class App(customtkinter.CTk):

    WIDTH = 680
    HEIGHT = 370
    
    def __init__(self):
        super().__init__()
        

        self.filetypes = (
                ('text files', '*.txt'),
                ('All files', '*.*')
            )
        self.title("DES ALgorithm")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  

        # ============ Creation des frames ============

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=7)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

        #======== information frams

        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="DES Algorithm" ,
                                                   height=30,
                                                     # <- custom tuple-color
                                                   justify=tkinter.CENTER)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)
        #radio
        self.radio_var = tkinter.IntVar(value=0)
        self.radio_button_1 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=0,
                                                           text="Use Input",
                                                           command=self.mode
                                                           )
        self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")

        self.radio_button_2 = customtkinter.CTkRadioButton(master=self.frame_right,
                                                           variable=self.radio_var,
                                                           value=1,
                                                           text="Use Files",
                                                           command=self.mode
                                                            
                                                           )
        self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")

        self.slider_button_1 = customtkinter.CTkButton(master=self.frame_right,
                                                       height=37,
                                                       text="Ciffrer",
                                                       command=self.chiffre
                                                       )
        self.slider_button_1.grid(row=4, column=2, columnspan=1, pady=3, padx=20, sticky="we")

        self.slider_button_2 = customtkinter.CTkButton(master=self.frame_right,
                                                       height=37,
                                                       text="Dechiffre",
                                                       command=self.dechiffre
                                                       )
        self.slider_button_2.grid(row=5, column=2, columnspan=1, pady=3, padx=20, sticky="we")
        #Entry

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            height=37,
                                            placeholder_text="Text")
        self.entry.grid(row=3, column=0, columnspan=2, pady=3, padx=20, sticky="we")
        self.entry2 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            height=37,
                                            placeholder_text="Key")
        self.entry2.grid(row=4, column=0, columnspan=2, pady=3, padx=20, sticky="we")

        #button

        self.selectfile_button = customtkinter.CTkButton(master=self.frame_right,
                                            height=37,
                                            text="Select File",
                                            
                                            state = disable,
                                            command=self.selectFil,)

        self.selectfile_button.grid(row=5, column=0, columnspan=2, pady=3, padx=20, sticky="we")

        self.entry3 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            height=67,
                                            placeholder_text="Resultat")
        self.entry3.grid(row=8, column=0, columnspan=2, pady=3, padx=20, sticky="we")

        self.data=""

        
        self.selectfile_button.configure(state=tkinter.DISABLED)

    def on_closing(self, event=0):
        self.destroy()
    def chiffre(self):
        if(self.radio_var.get()==0):
            chiffre=chiffrerText(self.entry.get(),self.entry2.get())
        else:
            chiffre=chiffrerText(self.data,self.entry2.get())
        self.entry3.delete(0,"end")
        self.entry3.insert(0, chiffre )

    def dechiffre(self):
        if(self.radio_var.get()==0):
            dechiffre=DechiffrerText(self.entry.get(),self.entry2.get())
        else:
            dechiffre=DechiffrerText(self.data,self.entry2.get())
        self.entry3.delete(0,"end")
        self.entry3.insert(0, dechiffre)

    def mode(self):
        if(self.radio_var.get()==0):
            self.selectfile_button.configure(state=tkinter.DISABLED)
            self.entry.configure(state=tkinter.NORMAL)


        else:
            self.selectfile_button.config(state=tkinter.NORMAL)

            self.entry.configure(state=tkinter.DISABLED)



    def selectFil(self):
        filename = fd.askopenfilename(title='Open a file',initialdir="/",filetypes=self.filetypes)
        f = open(filename, "r")
        self.data = f.read()
        print(self.data)
        
        


if __name__ == "__main__":
    app = App()
    app.mainloop()