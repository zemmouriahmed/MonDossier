import tkinter as tk
from tkinter import messagebox

def convertir():
    try:
        fahrenheit = float(ent_temperature.get())
        celsius = (fahrenheit - 32) * 5/9
        lbl_result.config(text=f"{celsius:.2f} °C", fg="green")
        messagebox.showinfo("Conversion réussie", f"{fahrenheit} °F équivaut à {celsius:.2f} °C.")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer une température valide.")
        lbl_result.config(text="", fg="black")

def reset():
    ent_temperature.delete(0, tk.END)
    lbl_result.config(text="", fg="black")

window = tk.Tk()
window.title("Convertisseur de Température")
window.resizable(width=False, height=False)
window.configure(bg="lightgrey")

frm_entry = tk.Frame(master=window, bg="lightgrey")
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="°F", bg="lightgrey")
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(master=window, text="Convertir", command=convertir, bg="lightblue")
btn_reset = tk.Button(master=window, text="Réinitialiser", command=reset, bg="lightcoral")
lbl_result = tk.Label(master=window, text="", bg="lightgrey")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
btn_reset.grid(row=0, column=2, padx=10)
lbl_result.grid(row=1, column=0, columnspan=3)

window.mainloop()