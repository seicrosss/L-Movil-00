import datetime
import os
import webbrowser

# Importar clases
from Clases.SpeechModule import SpeechModule
from Clases.VoiceRecognitionModule import VoiceRecognitionModule

# Variables
usu="seicros"
usu1="SeicroS"
no="Funcion en desarrollo"
name="Erika"


# Crear acceso a funciones
speech = SpeechModule()
recognition = VoiceRecognitionModule()

# Función para hacer que el asistente hable


# Función para escuchar al usuario
def listen():
    text = recognition.recognize()
    if text:

        if name in text :
            speech.talk("Si, " + usu)
            print("*" + name + " escuchando")
            text = recognition.recognize()
            comand(text)
        comand(text)
    print("*" + name + " en reposo")

# Función para ejecutar acciones según la entrada de voz del usuario
def comand(text):
    text=text.lower()
    if "reproduce" in text:
        song = text.split("reproduce ")[1]
        speech.talk(f"Reproduciendo {song}")
        os.system(f"am start -a android.intent.action.VIEW -d \"https://www.youtube.com/results?search_query={song}\"")
    elif "pausa" in text:
        speech.talk("Pausando la canción")
        os.system("input keyevent 85")
    elif "siguiente" in text:
        speech.talk("Reproduciendo la siguiente canción")
        os.system("input keyevent 87")
    elif "anterior" in text:
        speech.talk("Reproduciendo la canción anterior")
        os.system("input keyevent 88")
    elif "busca" in text:
        search = text.split("busca ")[1]
        speech.talk(f"Buscando {search}")
        webbrowser.open(f"https://www.google.com/search?q={search}")
    elif "hora" in text:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        speech.talk("Son las " + hora + ", " + usu)
        print("*Reloj: " + hora)

    elif "cierra" in text or "apagado" in text:
        speech.talk("Hasta luego")
        exit()
    else:
        speech.talk("Lo siento, no existe el comando.")

# Inicio
print("*Iniciada")
speech.talk("Iniciada, " + usu)
print("*" + name + " escuchando")

# Loop principal del asistente virtual

while True:
    text = listen()
