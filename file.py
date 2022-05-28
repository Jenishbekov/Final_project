from tkinter import *
from tkinter import filedialog


  

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    
    label_file_explorer.configure(text="File Opened: "+filename)     
                                                                                                  

window = Tk()
  

window.title('File Explorer')
  

window.geometry("500x500")
  

window.config(background = "#838B8B")
  

label_file_explorer = Label(window,
                            text = "FILE OPEN AND SHOWS ADRESS",
                            width = 100, height = 5,font=5,
                            fg = "red", bg="#838B8B")
  
      
button_explore = Button(window,
                        text = "OPEN FILES",
                        command = browseFiles, bg="red", width= 20)
  
button_exit = Button(window,
                     text = "Exit",
                     command = exit, bg="red", width= 10 )
  

label_file_explorer.grid(column = 1, row = 1)
  
button_explore.grid(column = 1, row = 2)
  
button_exit.grid(column = 1,row = 3)
  

window.mainloop()
