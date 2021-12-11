from pytube import YouTube
try:
    link=input("enter the youtube video link")
    video=YouTube(link)
    stream=video.streams.get_highest_resolution()
    stream.download()
except:
    print("threre is something wrong")