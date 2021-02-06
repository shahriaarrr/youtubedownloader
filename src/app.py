#pip install pytube
from pytube import YouTube

def main_programm(url):
    x = YouTube(url)
    print(x)

    for i in x.streams.first().download():
        print(i)

a = input("Give me your youtube link: ")

main_programm(a)
