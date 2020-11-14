import os
from tkinter import*
from tkinter import filedialog, messagebox, font, ttk
import cv2

folder = ""
vid = ""
def Video():
    global vid
    vid = filedialog.askopenfile(title="Select Video file")
    if(vid):
        print("Selected: "+vid.name)

    else:
        messagebox.showerror("Error", "Please Select Video File !")


def openLocation():
    global folder
    folder = filedialog.askdirectory(title="Select Folder to save image")
    if(len(folder) > 1):
        print("Selected folder is:"+folder)

    else:
        messagebox.showerror("Error", "Please Select Folder!")

def Exit_app():
        """
        This function will destroy Bill App and close the application
        """
        mess = messagebox.askyesno("Exit", "Do You Really Want to Exit ?")
        if mess > 0:
            root.destroy()


def convert():
    if vid==str("") and folder == str(""):
        messagebox.showerror("Error","Please Select Both Video file and Destination Folder")
    else:
        image_data = os.path.join(os.getcwd(), folder)
        cap = cv2.VideoCapture(vid.name)
        if (cap.isOpened() == False):
            print("Error Opening file")
        j = 0
        while(cap.isOpened()):
            ret, frame = cap.read()
            try:
                cv2.imwrite(os.path.join(image_data, str(j)+".png"), frame)
                cv2.imshow('Video to Image Converter Running...', frame)
                j+=1
        
            except:
                messagebox.showinfo("Message", "Video Conversion Process Completed!")
                cv2.destroyAllWindows()
                break
                
            k=cv2.waitKey(30) & 0xff
            if k==27:
                cv2.destroyAllWindows()
                break


        cap.release()
        cv2.destroyAllWindows()

root = Tk()
root.title("Video To Image Converter Application")

root.geometry("500x480") # sets the size of the app window
root.columnconfigure(0, weight=1) # sets all the content in center

#  Design of app
title = Label(root, text="Video to Images Converter",bg="SkyBlue",bd="7", fg="crimson" , relief=FLAT , font=("times new roman", 20, "bold"))
title.pack(fill=X)
 
dest = Label(root, font=("times new roman", 14, "bold"), fg="#C70039")
dest.place(y=100)

url_lbl = Label(dest, text="Select Video", font=("times new roman", 14, "bold"), fg="#17202A").grid()
path = Button(dest, width=10, bg="yellow", command=Video , fg="black", text="Click", font=("times new roman", 12), bd=5).grid()


dest_lbl = Label(dest, text="Select Destination folder", font=("times new roman", 14, "bold"), fg="#17202A").grid()

path = Button(dest, width=10, bg="yellow", fg="black", command=openLocation , text="Select", font=("times new roman", 12), bd=5).grid()

conv = Button(dest, text="Convert", width=12, command=convert , bg="red", fg="black", font=("times new roman", 15, "bold")).grid(pady=50)


# about section
abt = Label(dest, text="Developed By: Shivakant Vishwakarma", font=("times new roman", 14, "bold"), fg="#17202A").grid(padx=100, pady=10, sticky="w")
exit_btn = Button(dest, text="EXIT", command=Exit_app , font=("times new roman", 14, "bold") , bg="cadetblue", fg="yellow", bd=5).grid()


root.mainloop()