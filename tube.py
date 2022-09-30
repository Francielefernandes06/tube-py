import re
from pytube import YouTube
import moviepy.editor as mp
import os
import re

link = input("Digite o link que deseja fazer o donwload:  ")
path = input("Digite o caminho que deseja salvar o arquivo:  ")
yt = YouTube(link)

print("Título: ", yt.title)
print("Número de views: ", yt.views)
print("Tamanho do vídeo: ", yt.length)

print ("Baixando...")
ys = yt.streams.filter(only_audio=True).first().download(path)
print ("Download completo")

print("Realizando a cnversão...")
for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0] + '.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
print("Só sucesso!")