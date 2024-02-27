import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd ='C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
def open_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        original_image = Image.open(file_path)
        detected_text = pytesseract.image_to_string(original_image, lang='fas')
        show_detected_text(detected_text)
def show_detected_text(detected_text):
    text_window = tk.Toplevel(app)
    text_window.title("Detected Text")
    text_widget = ScrolledText(text_window, wrap=tk.WORD)
    text_widget.pack(expand=True, fill="both")
    text_widget.insert(tk.END, detected_text)
    save_frame = ttk.Frame(text_window)
    save_frame.pack()
app = tk.Tk()
app.title("text detector")
app.geometry("500x300")
style = ttk.Style()
open_button = ttk.Button(app, text="انتخاب عکس", command=open_image)
open_button.pack(pady=10,padx=10,side="right")
app.mainloop()