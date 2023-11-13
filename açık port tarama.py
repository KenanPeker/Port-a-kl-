from tkinter import*
import socket

pen = Tk()
pen.geometry("330x500")
pen.title("PEKER PORT ARAMA")
pen.resizable(FALSE,FALSE)
arkaplanresmi = PhotoImage(file="siyah-logo.png")
lblarkaplan = Label(pen, image=arkaplanresmi)
lblarkaplan.place(x=0, y=0)

def tarama():
    s1 = str(enturl.get())
    liste = [21,22,23,25,80,139,443,445,33890]
    try:
        for port in liste:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((s1, port))
            if result == 0:
                listsonuç.insert(1, "Port{} Açık.format(port)")
            else:
                listsonuç.insert(1, "Port{} Kapalı.format(port)")
            sock.close()
    except socket.error:
        print("Bilgisayara ulaşılmıyor")



lblurl = Label(pen, text="URL veya IP adresi", font="Verdana 12 bold", fg="white",
               bg="black")
lblurl.place(x=60, y=20)
listsonuç = Listbox(pen, font="Verdana 12 bold", width="25", height="17",
                   fg="white", bg="black")
listsonuç.place(x=27, y=140)
enturl = Entry(pen, font="Verdana 12 bold", fg="green")
enturl.place(x=50, y=50)
btntara = Button(pen, text="Portları Tara", font="Verdana 12 bold", fg="white",
                 bg="black", command=tarama)
btntara.place(x=80, y=90)


pen.mainloop()
