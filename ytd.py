from tkinter import *
from pytube import *

def Streams():
    try:    
        vid = YouTube(link.get())
        ar = (vid.streams.filter(type = 'video',progressive = True))
        stream_root = Tk()
        stream_root.title('Streams Available')
        Label(stream_root, text = 'Available Streams for Download are listed below').pack(pady = 5)
        lb = Listbox(stream_root,width = 80 )
        for i in range(len(ar)):
            lb.insert(i,str(ar[i]))
        lb.pack(fill = BOTH)
        stream_root.mainloop()
    except:
        Label(root, text = 'No streams available to download',bg = 'red')    

def DownloadVideo():
    try:
        vid = YouTube(link.get()).streams.get_by_itag(itag.get()).download()
        Label(root, text = 'Dowload Successful...!',bg = 'green').pack(pady = 5)
    except:
        Label(root, text = 'Some error ocurred...!',bg = 'red').pack(pady = 5)

root = Tk()
root.geometry('600x500')
root.title('YouTube Video Downloader')

C = Canvas(root,bg = 'white',height = '20',width = '20')
C.pack()
imagename = PhotoImage(file = 'D:\\Studies\\YouTube Downloader\\2.png')   #give your own path
background_label = Label(root, image = imagename)
background_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

Label(root, text = 'YOUTUBE VIDEO DOWNLOADER', font = 'Consolas 15 bold').pack()
Label(root, text = 'by Prajjwal').pack()

Label(root, text = 'Enter the link', font = 10).pack(pady = 5)
link = StringVar()
Entry(root,textvariable = link, width = 80).pack(pady = 5)

Button(root, width = 30, text = 'Check Streams', command = Streams).pack(pady = 5)

itag = StringVar()
Label(root, text = 'Enter the itag: (e.g. 160, 22 ...)').pack()
Entry(root,textvariable = itag).pack(pady = 10)

Button(root, text = 'Download', command = DownloadVideo).pack()

root.mainloop() 


