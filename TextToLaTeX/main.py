import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x500")
x = " "

def logic():
    Text = entry1.get()
    for i in range(len(Text)):
        if Text[i] == "¬": 
            Text = Text.replace("¬",  ' \\neg ')
        elif Text[i] == "∧":
            Text = Text.replace("∧",  ' \\wedge ')
        elif Text[i] == '∨':
            Text = Text.replace("∨",  ' \\vee ')
        elif Text[i] == '↔':
            Text = Text.replace("↔",  ' \\rightleftarrow ')
        elif Text[i] == '→':
            Text = Text.replace("→",  ' \\to ')
    return Text

def filler():
    entryOut.insert(0, logic())


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Math Text")
entry1.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="format", command=filler)
button.pack(pady=12, padx=10)

entryOut = customtkinter.CTkEntry(master=frame)
entryOut.pack(pady=12, padx=10)

root.mainloop()