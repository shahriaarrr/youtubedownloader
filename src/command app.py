#pip install pytube
from pytube import YouTube


url= input("Give me your youtube link: ")
x= YouTube(url)
print(x)

for i in x.streams.first().download():
    print(i)