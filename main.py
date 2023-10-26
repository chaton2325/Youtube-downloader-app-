from pytube import YouTube
import tkinter
from tkinter import ttk

app=tkinter.Tk()
app.config(bg="black")
app.resizable(False,False)

frame=tkinter.Frame(app)
frame.grid(row=0,column=0,padx=12,pady=12)
frame.config(bg="red")

lab1=tkinter.Label(frame,text="REFLEX TUBE DOWNLOAD",font=("Calibri",15),fg="Black",bg="grey")
lab1.grid(row=1,column=0,padx=5,pady=5)

entry=tkinter.Entry(frame,bg="black",fg="red",width=40)
entry.insert(0,"Entrez le lien de la vidéo youtube")
entry.grid(row=2,column=0,padx=5,pady=5)

Liste=["Basse résolution","Haute résolution","Audio"]
combobox=ttk.Combobox(frame,values=Liste)
combobox.grid(row=1,column=1,padx=5,pady=5)

def click_button():
    from tkinter.messagebox import showinfo
    lien=str(entry.get())
    yt=YouTube(lien)
    res=combobox.get()
    if res==Liste[0]:
        stream=yt.streams.get_lowest_resolution()
        stream.download()
        showinfo(title="information",message="vidéo télécharger en basse résolution")
    elif res==Liste[1]:
        stream=yt.streams.get_highest_resolution()
        stream.download()
        showinfo(title="information",message="vidéo télécharger an haute résolution")
    elif res==Liste[2]:
        stream=yt.streams.get_audio_only()
        stream.download()
        showinfo(title="information",message="Audio télécharger avec succès")
    else:
        showinfo(title="erreur",message="une errueur s est produite")


button=tkinter.Button(frame,text="télécharger",command=click_button)
button.grid(row=3,column=0,padx=5,pady=5)



app.mainloop()
