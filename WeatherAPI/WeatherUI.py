import customtkinter
from WeatherAPI import get_weather

app = customtkinter.CTk()
app.title("Weather Checker")
app.geometry("500x200")


button = customtkinter.CTkButton(app, text="Check Local Weather", command=get_weather)

app.grid_columnconfigure(0, weight=1)
button.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

textbox = customtkinter.CTkTextbox(app)
textbox.insert("0.0", "new text")

app.mainloop()