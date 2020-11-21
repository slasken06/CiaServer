import qrcode
import tkinter as tk
from PIL import ImageTk
import http.server as server
import random
from threading import Thread
import sys
import os
import urllib.parse
import socket
from pyngrok import ngrok

ip = "localhost"
port = 4839

def GetUrl(obj):
    obj = str(obj)
    tmp = obj.find(r'"')
    obj = obj[tmp+1:-1]
    tmp = obj.find(r'"')
    obj = obj[0:tmp]
    obj = obj.lstrip("tcp://")


    return obj


# Moving to cia's location
cia = sys.argv[1]
cia_name = cia.split(os.sep)[-1]
cia_path = cia.rstrip(cia_name)
os.chdir(cia_path)


handler = server.SimpleHTTPRequestHandler
s = server.HTTPServer((ip ,port), handler)
thread = Thread(target=s.serve_forever)
thread.start()


url = GetUrl(ngrok.connect(port, "tcp"))
url = f"{url}/{cia_name}"
print(url)

root = tk.Tk()
root.title(f"Qr Code for {cia_name}")

# Creating QR Code image
img = ImageTk.PhotoImage(qrcode.make(url))

canvas = tk.Canvas(root, width=img.width(), height=img.height())
canvas.create_image(0, 0, anchor=tk.NW, image=img)

canvas.pack()
tk.mainloop()


s.shutdown()
