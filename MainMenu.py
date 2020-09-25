from tkinter import *
from tkinter.ttk import *
from InternetPicture import internetPic


class MainMenu:
    def __init__(self):
        # Setting Up These Variables (Instance)
        self.window = Tk()
        self.window.title("Screensaver Simulator")
        self.window.configure(padx=7, pady=7)
        self.bg = None
        self.icon = None

    def draw_Window(self):
        # Title Label
        title = Label(self.window, text='Screensaver Simulator')
        title.grid(column=0, row=0, columnspan=3)
        # That Guide Thing The Computer Tells You.
        Tutorial = Label(self.window,
                         text="Select 'Upload Image' on The Icon Seletcions and Type in your link in the Text Box.")
        Tutorial.grid(column=0, row=1, columnspan=3)
        # Background Combobox/Label.
        bg_choice = Combobox(self.window, )
        bg_choice["values"] = ('Forest', 'Sky', 'Beach', 'Mountian')
        bg_choice.grid(column=1, row=2)
        bg_choice.current(0)
        bg_label = Label(self.window, text="Choose Your Background")
        bg_label.grid(column=0, row=2)
        # Icon ComboBox/Label
        icon_choice = Combobox(self.window)
        icon_choice["values"] = ('Squarey', 'DVD Video', 'Minecraft Grass Block', 'Python Logo', 'Upload Image')
        icon_choice.grid(column=1, row=3)
        icon_choice.current(0)
        icon_label = Label(self.window, text="Choose Your Icon")
        icon_label.grid(column=0, row=3)
        # If User wants to upload there own image.
        url_entry = Entry(self.window)
        url_entry.config(state="normal")
        url_entry.grid(column=0, row=4, columnspan=3)

        # The Submit Button
        def submit():
            self.bg = bg_choice.get()
            self.icon = icon_choice.get()
            if self.icon == "Upload Image":
                # Grab The Picture from the internet
                url = url_entry.get()
                try:
                    img=internetPic(url)
                    img.getpic()
                    self.window.destroy()
                except:
                    # Let User Know That The URL IS WRONG.
                    error = Label(self.window,
                                  text="The Url Is Invalid, Make sure its A PNG or JPG and the link .(╯ ͠° ͟ʖ ͡°)╯┻━┻")
                    error.grid(column=0, row=6, columnspan=3)
            else:
                self.window.destroy()

        submit = Button(self.window, text="Submit", command=submit)
        submit.grid(column=0, row=5, columnspan=3)
        # MUST DO
        self.window.mainloop()