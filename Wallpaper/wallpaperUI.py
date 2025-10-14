import customtkinter
from wallpaperAPI import *

app = customtkinter.CTk()
app.title("Wallpaper Haven Grabber")
app.geometry("1000X10z00")

button = customtkinter.CTkButton(app, text="Get Wallpaper", command=wallpaper_get)
button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

app.mainloop()
