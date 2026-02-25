import customtkinter as ctk
import threading
from watcher import Observer, MiHandler
from tkinter import filedialog
from pathlib import Path
from pystray import MenuItem as item
from PIL import Image
import pystray
import json
import ctypes

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

downloads = Path.home() / "Downloads"

window_visible = True



def toggle_window(icon, item):
    global window_visible
    if window_visible:
        window.withdraw()
    else:
        window.deiconify()
    window_visible = not window_visible

def quit_app(icon, item):
    icon.stop()
    window.destroy()

def on_closing():
    global window_visible
    window.withdraw()
    window_visible = False



def iniciar_watcher(destino):
    event_handler = MiHandler(destino)
    observer = Observer()
    observer.schedule(event_handler, downloads, recursive=False)
    observer.start()
    observer.join()


def abrir_directorio():
    carpeta = filedialog.askdirectory()
    if carpeta:
        campo.delete(0, "end")
        campo.insert(0, carpeta)
        btn_iniciar.configure(state="normal")


def iniciar():
    carpeta = campo.get()
    btn_iniciar.configure(state="disabled")
    
    with open("config.json", "r") as f:
        config = json.load(f)

    config["Carpeta_Destino"] = carpeta

    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)

    hilo = threading.Thread(target=iniciar_watcher, args=(carpeta,))
    hilo.daemon = True
    hilo.start()



window = ctk.CTk()
window.geometry("600x300")
window.title("Beelc's Files Sorter")
window.iconbitmap("assets/logo.ico")
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("beelc.filesorter")

window.protocol("WM_DELETE_WINDOW", on_closing)


btn_iniciar = ctk.CTkButton(
    window,
    text="Start Sorting",
    state="disabled",
    command=iniciar
)
btn_iniciar.pack(pady=20)


campo = ctk.CTkEntry(
    window,
    width=400,
    placeholder_text="Write destination folder..."
)
campo.pack(pady=10)


buttondir = ctk.CTkButton(
    window,
    text="Select destination folder...",
    command=abrir_directorio
)
buttondir.pack(pady=10)

icon = pystray.Icon(name="Beelc Files Sorter", title="Beelc Files Sorter")
icon.icon = Image.open("assets/logo.png")
icon.menu = pystray.Menu(
    item(text='Toggle Window', action=toggle_window, default=True),
    item('Quit', quit_app)
)

icon_thread = threading.Thread(target=icon.run, daemon=True)
icon_thread.start()

with open("config.json") as f:
    config = json.load(f)

    carpeta_destino = config["Carpeta_Destino"]
    if carpeta_destino:
        campo.insert(0, carpeta_destino)
        btn_iniciar.configure(state="disabled")
        window_visible = False
        window.withdraw()
        hilo = threading.Thread(target=iniciar_watcher, args=(carpeta_destino,))
        hilo.daemon = True
        hilo.start()
    

window.mainloop()