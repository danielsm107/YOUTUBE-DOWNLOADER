import tkinter
import customtkinter
from pytube import YouTube
from tkinter import filedialog
from pytube import exceptions as exc

def startAudio():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        video = ytObject.streams.get_audio_only()
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download(output_path=downloadPath.get())
        finishLabel.configure(text="¡Descargado!")
    except:
        finishLabel.configure(text="Error en la descarga", text_color="red")
   

def startDownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink, on_progress_callback=on_progress)
        for stream in ytObject.streams.filter(progressive=True):
            print(f"Stream: {stream.resolution}, {stream.mime_type}, {stream.fps}")

        video = ytObject.streams.filter(file_extension='mp4', progressive=True).order_by('resolution').desc()

        highestQualityStream = video.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        highestQualityStream.download(output_path=downloadPath.get())
        finishLabel.configure(text="¡Descargado!")
    except:
        finishLabel.configure(text="Ha ocurrido un problema", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    # Actualizar la barra de progreso
    progressBar.set(float(percentage_of_completion) / 100)

def selectFolder():
    folderSelected = filedialog.askdirectory()
    if folderSelected:
        downloadPath.set(folderSelected)
        folderLabel.configure(text=folderSelected)

# Configuración del sistema
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame
app = customtkinter.CTk()
app.geometry("2560x1440") # Resolución del monitor
app.title("Youtube Downloader")

# Añadir elementos a la interfaz
title = customtkinter.CTkLabel(app, text="Introduzca la URL del vídeo de YouTube")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Descarga completada
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Porcentaje de progreso
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Boton de descarga
download = customtkinter.CTkButton(app, text="Descargar", command=startDownload)
download.pack(padx=10, pady=10)

# Botón de selección de carpeta
selectFolderButton = customtkinter.CTkButton(app, text="Seleccionar carpeta", command=selectFolder)
selectFolderButton.pack(padx=10, pady=10)

# Etiqueta para mostrar la carpeta seleccionada
downloadPath = tkinter.StringVar()
folderLabel = customtkinter.CTkLabel(app, text="No se ha seleccionado ninguna carpeta")
folderLabel.pack(padx=10, pady=10)

# Boton solo para descargar audio
audio = customtkinter.CTkButton(app, text="Descargar audio", command=startAudio)
audio.pack(padx=10, pady=10)

# Boton de salir
close = customtkinter.CTkButton(app, text="Salir", command=app.quit)
close.pack(padx=10, pady=10)


# Hacer que funcione la app
app.mainloop()