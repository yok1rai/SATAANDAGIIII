from tkinter import *
from PIL import Image, ImageTk     # modern image support
import os
import platform
from win10toast import ToastNotifier

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# === Toast notification function ===
def send_notify():
    """Send a Windows toast notification."""
    if platform.system() == "Windows":
        toaster = ToastNotifier()
        toaster.show_toast(
            "U MEAN YES?",
            "SATA ANDAGIII!!!!!!!!",
            duration=5,
            icon_path=None,
            threaded=True
        )

# === New squished window ===
def open_new_page():
    """Open a new window with a squished SATA ANDAGI image."""
    new_window = Toplevel(root)
    new_window.title("UNYA")
    new_window.geometry("350x350")

    # Load and squish SATA ANDAGI image
    img = Image.open("sata_andagi.png")
    width, height = img.size
    squished = img.resize((int(width * 1.2), int(height * 0.5)))  # ✅ squished look
    new_window.sata_andagi_icon = ImageTk.PhotoImage(squished)

    # Apply window icon and display image
    new_window.iconphoto(True, new_window.sata_andagi_icon)
    Label(new_window, image=new_window.sata_andagi_icon).pack(pady=10)
    Label(
        new_window,
        text="Saattaa andaagii~ 🍩",
        font=("Arial", 14, "bold")
    ).pack(pady=10)

# === Combined "No" action ===
def no_button_action():
    """Open squished window + show toast notification."""
    open_new_page()
    send_notify()

# === Main window ===
root = Tk()
root.title("SATA ANDAGI APP 🍩")
root.geometry("420x450")

# ✅ Set main window icon
icon_img = Image.open("sata_andagi1.png")
icon_img = icon_img.resize((64, 64))
root.icon = ImageTk.PhotoImage(icon_img)
root.iconphoto(True, root.icon)

# === Main label ===
Label(
    root,
    text="Do you want a SATA ANDAGI??!",
    font=("Arial", 16, "bold")
).pack(pady=25)

# === Buttons ===
Button(
    root,
    text="YES 😋",
    font=("Arial", 12, "bold"),
    bg="#90EE90",
    activebackground="#77DD77",
    command=open_new_page,
    width=12
).pack(pady=5)

Button(
    root,
    text="NO 😤",
    font=("Arial", 12, "bold"),
    bg="#FF7F7F",
    activebackground="#FF6B6B",
    command=no_button_action,
    width=12
).pack(pady=5)

# === Main image (normal version) ===
main_img = Image.open("sata_andagi1.png")
main_img = main_img.resize((256, 256))
main_photo = ImageTk.PhotoImage(main_img)

main_label = Label(root, image=main_photo)
main_label.image = main_photo  # keep reference alive
main_label.pack(pady=15)

# === Run app ===
root.mainloop()
