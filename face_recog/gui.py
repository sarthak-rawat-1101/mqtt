import tkinter as tk
import cv2
import os
import threading
import PIL.Image, PIL.ImageTk
import time
import imutils




window = tk.Tk()
window.title("Driver Detection")
window.geometry("500x500")

# Create a canvas that can fit the above video source size
canvas = tk.Canvas(window, width = 500, height = 500)
canvas.pack()

# Button that lets the user take a snapshot
btn_snapshot=tk.Button(window, text="Snapshot", width=50, command=window.destroy)
btn_snapshot.pack(anchor=tk.CENTER, expand=True)








window.mainloop()

