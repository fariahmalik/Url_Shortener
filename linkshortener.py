from tkinter import *
import pyshorteners
#for btn copy
import clipboard

window=Tk()
window.title("url Shortener")
window.geometry("450x250")
window.configure(bg="pale turquoise")
window.resizable(False,False)# making window non-resizable
# create input field for url
url_input=Entry(window,font=("Helvetica","16"),width=30)
url_input.grid(row=1,column=2,pady=7)
# creating label
str_url=StringVar(window)
l1=Label(window,textvariable=str_url,font=("Helvetica","16"),bg="#1abc9c"
         ,fg="#fff")
l1.grid(row=3,column=2,pady=6)
# now create functions for buttons
# btn short
def url_short():
    try:
        s = pyshorteners.Shortener()
        url = url_input.get()
        final_result = s.tinyurl.short(url)
        str_url.set(final_result)
        url_input.delete(0, END)  # to clear the input field
    except:
        str_url.set("Plz enter url")

# btn copy function
def copy():
    try:
        clipboard.copy(str_url.get())
        print("url copied successfully!!")
    except:
        str_url.set("Something went wrong!!!")



# now create a button to short the url
btn_short=Button(window,text="Short Url",font=("Helvetica","16"),
                 bg="#2ecc71",fg="#fff",activebackground="#16a085",
                 command=url_short)
btn_short.grid(row=2,column=2,pady=6)
# Now create a button to copy url
btn_copy=Button(window,text="Copy",font=("Helvetica","12"),bg="#34495e",fg="#fff",
                command=copy)
btn_copy.grid(row=3,column=3,pady=6,padx=10)
window.mainloop()