import tkinter as tk
from tkinter import ttk
from googletrans import Translator

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Translator App")

        self.create_widgets()

    def create_widgets(self):
        # Frame utama
        main_frame = ttk.Frame(self.root, padding=(20, 20))
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Label dan Entry untuk input
        ttk.Label(main_frame, text="Enter Text:", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        self.input_entry = ttk.Entry(main_frame, font=("Arial", 14), width=40)
        self.input_entry.grid(row=1, column=0, columnspan=2, pady=10, padx=(0, 10))

        # Tombol untuk menerjemahkan
        translate_button = ttk.Button(main_frame, text="Translate", command=self.translate_text, style="TButton")
        translate_button.grid(row=1, column=2, pady=10)

        # Label untuk menampilkan hasil terjemahan
        ttk.Label(main_frame, text="Translation:", font=("Arial", 16, "bold")).grid(row=2, column=0, columnspan=3, pady=10)
        self.output_label = ttk.Label(main_frame, text="", font=("Arial", 14), wraplength=400, justify="left")
        self.output_label.grid(row=3, column=0, columnspan=3, pady=10)

        # Konfigurasi gaya tombol
        self.root.option_add('*TButton*padding', 8)
        self.root.option_add('*TButton*background', '#4CAF50')  # Warna hijau untuk tombol
        self.root.option_add('*TButton*foreground', 'white')
        self.root.option_add('*TButton*font', ('Arial', 12, 'bold'))

    def translate_text(self):
        # Mengambil teks dari input
        input_text = self.input_entry.get()

        # Menerjemahkan teks menggunakan Google Translate API
        translator = Translator()
        translation = translator.translate(input_text, dest='en')  # Ganti 'en' dengan kode bahasa target yang diinginkan

        # Menampilkan hasil terjemahan
        self.show_translation(translation.text)

    def show_translation(self, translation_text):
        # Tampilkan hasil terjemahan dalam jendela baru
        result_window = tk.Toplevel(self.root)
        result_window.title("Translation Result")

        result_label = ttk.Label(result_window, text=translation_text, font=("Arial", 14), wraplength=400, justify="left")
        result_label.pack(padx=20, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()
