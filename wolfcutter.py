import numpy as np
from tkinter import Tk,ttk,filedialog,StringVar,Spinbox,PhotoImage
from PIL import Image,ImageDraw,ImageTk
import os
tate=8
yoko=8
class griddraw:
  imgpass=""
  width=0
  height=0
  putpass=""
  def readimg(self, imgpass):
    self.imgpass=imgpass
    self.img = Image.open(imgpass)
    self.width,self.height = self.img.size
    self.updatelabel1()
  def imgtrim(self):
    img = Image.open(self.imgpass)
    if self.putpass=="":
      print("保存先パスが指定されていません")
    else:
      imgname=os.path.basename(img.filename)[:-4]
      dirname=self.putpass+"/"+imgname
      tate=int(sptxt1.get())
      yoko=int(sptxt2.get())
      if not os.path.exists(dirname):
        os.mkdir(dirname)
      trimwidth=self.width//yoko
      trimheight=self.height//tate
      for i in range(tate):
        for j in range(yoko):
          trimimg=img.crop((trimwidth*j,trimheight*i,trimwidth*(j+1),trimheight*(i+1)))
          #上書き確認入れたい
          trimimg.save(dirname+"/"+imgname+str(i*yoko+j+1)+".png")
      #完了時になんかメッセージ出したい
  def setputpass(self,n):
    self.putpass=n
  def updatelabel1(self):
    img = Image.open(self.imgpass)
    drawimg = ImageDraw.Draw(img)
    draw_vertical(int(sptxt1.get()),drawimg)
    draw_horizonal(int(sptxt2.get()),drawimg)
    img.save('original_grided.png','PNG')
    photoim=PhotoImage(file='original_grided.png')
    label1.configure(image=photoim)
    label1.image=photoim
  def getwidth(self):
    return self.width
  def getheight(self):
    return self.height
image=griddraw()
def draw_vertical(n:int,draw):
  if n>1:
    width=image.getwidth()
    height=image.getheight()
    for i in range(1,n):
      a=int(width/n)
      draw.line([(a*i,0),(a*i,height)],fill=(255,0,0),width=1)
def draw_horizonal(n:int,draw):
  if n>1:
    width=image.getwidth()
    height=image.getheight()
    for i in range(1,n):
      a=int(height/n)
      draw.line([(0,a*i),(width,a*i)],fill=(255,0,0),width=1)
root = Tk()
root.title('補助線描画')

frame1 = ttk.Frame(root)
frame1['height'] = 200
frame1['width'] = 400
frame1.grid()

label1=ttk.Label(frame1)
label1.grid(row=4,column=0,columnspan=4)

label2=ttk.Label(frame1,text="縦")
label2.grid(row=0,column=0)

label3=ttk.Label(frame1,text="横")
label3.grid(row=0,column=1)

txt4=StringVar()
txt4.set("")
label4=ttk.Label(frame1,textvariable=txt4,background="white")
label4.grid(row=2,column=0,columnspan=2)

def redrawline():
  image.updatelabel1()
sptxt1=StringVar()
sptxt1.set(tate)
spinbox1=Spinbox(frame1,from_=0,to=1000,textvariable=sptxt1,command=redrawline)
spinbox1.grid(row=1,column=0)

sptxt2=StringVar()
sptxt2.set(yoko)
spinbox2=Spinbox(frame1,from_=0,to=1000,textvariable=sptxt2,command=redrawline)
spinbox2.grid(row=1,column=1)

def inputimage():
  fTyp = [("Image Files",('.jpg','.png'))]
  iDir = os.path.abspath(os.path.dirname(__file__))
  imgpath = filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)
  image.readimg(imgpath)
button1=ttk.Button(frame1,text="画像を読み込み",command=inputimage)
button1.grid(row=1,column=2)

def gridreset():#線の設定を上書きするための関数。tateとyokoを変えると好きな本数線を引けてすごい
  tate=0
  yoko=0
  sptxt1.set(tate)
  sptxt2.set(yoko)
  redrawline()
button3=ttk.Button(frame1,text="リセット",command=gridreset)
button3.grid(row=3,column=2)

def choosefolder():
  ini_dir = 'C:\\Program Files\\Python37'
  ret = filedialog.askdirectory(initialdir=ini_dir, title='フォルダを選択してください', mustexist = True)
  txt4.set(str(ret))
  image.setputpass(str(ret))
button4=ttk.Button(frame1,text="保存先フォルダ選択",command=choosefolder)
button4.grid(row=2,column=2)

def triming():
  image.imgtrim()
button5=ttk.Button(frame1,text="連番出力",command=triming)
button5.grid(row=3,column=0)

root.mainloop()
