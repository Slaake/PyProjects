import customtkinter

def get_wallpaper():
    print("Getting Wallpaper")

app = customtkinter.CTk()
app.title("Wallpaper Haven Grabber")
app.geometry("1000X10z00")

button = customtkinter.CTkButton(app, text="Get Wallpaper", command=get_wallpaper)
button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

app.mainloop()
