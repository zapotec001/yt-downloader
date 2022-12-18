import tkinter as tk
from tkinter import ttk
import youtube_dl

# Tkinter penceresini oluşturalım
window = tk.Tk()
window.title("YouTube Video/MP3 İndirici")
window.geometry("500x300")

# Arayüzümüz için etiketleri oluşturalım
label1 = ttk.Label(window, text="YouTube URL:")
label1.grid(column=0, row=0, padx=10, pady=10)

label2 = ttk.Label(window, text="İndirilecek Dosya Türü:")
label2.grid(column=0, row=1, padx=10, pady=10)

# Girdi alanlarımızı oluşturalım
url_input = tk.StringVar()
url_entry = ttk.Entry(window, width=50, textvariable=url_input)
url_entry.grid(column=1, row=0, padx=10, pady=10)

# İndirilecek dosya türünü seçme için seçeneklerimizi oluşturalım
file_type = tk.StringVar()
file_type.set("video") # varsayılan seçenek olarak "video" seçilecek
radio_video = ttk.Radiobutton(window, text="Video", variable=file_type, value="video")
radio_video.grid(column=1, row=1, padx=10, pady=10)
radio_audio = ttk.Radiobutton(window, text="MP3", variable=file_type, value="audio")
radio_audio.grid(column=2, row=1, padx=10, pady=10)

# İndirme işlemini gerçekleştirecek düğmeyi oluşturalım
download_button = ttk.Button(window, text="İndir", command=download)
download_button.grid(column=1, row=2, padx=10, pady=10)

# İndirme işlemini gerçekleştirecek fonksiyonu yazalım
def download():
  # Kullanıcıdan aldığımız URL'yi ve indirilecek dosya türünü alalım
  url = url_input.get()
  file_type = file_type.get()

  ydl_opts = {
      'format': file_type, # İndirilecek dosya türü
      'outtmpl': '%(title)s.%(ext)s' # İndirilen dosyanın adını YouTube videonun adı olarak ayarlayalım
  }


# YouTube üzerinden indirme işlemini gerçekleştirelim
  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
      ydl.download([url])
