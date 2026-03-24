import tkinter
import clientS

root = tkinter.Tk()
root.title = "mail"
root.geometry("800x600")

def send():
    clientS.Send(inputYouOratio.get(), inputToOratio.get(), inputMessage.get("1.0", tkinter.END).strip())
    inputYouOratio.delete(0, tkinter.END) 
    inputToOratio.delete(0, tkinter.END) 
    inputMessage.delete("1.0", tkinter.END)

labelYouOratio =tkinter.Label(root, text="Your Oratio:", font=("Arial",16))
labelYouOratio.pack(pady=10)
inputYouOratio = tkinter.Entry(root, font=("Arial",16))
inputYouOratio.pack(pady=10)

labelToOratio =tkinter.Label(root, text="To Oratio:", font=("Arial",16))
labelToOratio.pack(pady=10)
inputToOratio = tkinter.Entry(root, font=("Arial",16))
inputToOratio.pack(pady=10)

labelMessage =tkinter.Label(root, text="Message:", font=("Arial",16))
labelMessage.pack(pady=10)
inputMessage = tkinter.Text(root, height=5, width=40, font=("Arial",16))
inputMessage.pack(pady=10)

bttn = tkinter.Button(root, text="send", command=send, font=("Arial",16, "bold"))
bttn.pack(pady=10)

root.mainloop()