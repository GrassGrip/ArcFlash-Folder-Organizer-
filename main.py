import os
import shutil
import customtkinter

#System Settings
customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

#App Frame
app = customtkinter.CTk()
app.geometry('500x300')
app.title('Desktop Cleaner')

#Adding UI Elements
title = customtkinter.CTkLabel(app, text='Desktop Clean', font=('Roboto', 24))
title.pack(padx=10, pady=10)

#link input
path = customtkinter.CTkEntry(app, width=350, height=40, border_width=2, placeholder_text='Enter Path')
path.pack()

def cleanfolder():
    folder_path = path.get().replace('\\', '/')  # Replace double backslashes with single backslashes

    if folder_path:  # Check if the folder path is not empty
        try:
            files = os.listdir(folder_path)
            for file in files:
                filename, extension = os.path.splitext(file)
                extension = extension[1:]

                if os.path.exists(os.path.join(folder_path, extension)):
                    shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, extension, file))
                else:
                    os.makedirs(os.path.join(folder_path, extension))
                    shutil.move(os.path.join(folder_path, file), os.path.join(folder_path, extension, file))
        except FileNotFoundError as e:
            print(f"Error: {e}")
    else:
        print("Please enter a valid directory path.")

#Clean button
clean = customtkinter.CTkButton(app, text='Clean', command=lambda: cleanfolder())
clean.pack(padx=10, pady=10)

# Function to paste text into the search bar
# Function to paste text into the search bar
def paste_text(event=None):
    path.event_generate('<<Paste>>')

path.bind("<Control-v>", paste_text)  # Bind Ctrl+V to allow pasting


#Run app
app.mainloop()


#C:\Users\Goober\Desktop\Documents

