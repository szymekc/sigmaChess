from tkinter import *
from chatContents import *

class ChatWindow(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.sendCallback=None

        self.sendButton= Button(self,text="Send", command=self.sendBtnClick)
        self.sendButton.pack(side=BOTTOM)

        self.textEntry = Entry(self)
        self.textEntry.pack(side=BOTTOM)

        self.messageWindowScroll = Scrollbar(self)
        self.messageWindowScroll.pack(side=RIGHT,fill="y")

        self.messageWindow = Text(self,bd=5,relief=RIDGE,bg="gray90",state=DISABLED,width=20,font=("Comic Sans MS","10"),yscrollcommand=self.messageWindowScroll.set)
        self.messageWindow.pack(side=TOP,fill="both")
        self.messageWindowScroll.config(command=self.messageWindow.yview)
        self.chat = Chat()
        self.chat.content.trace("w", self.updateCallback)

    def sendBtnClick(self):
        self.chat.addContent(self.textEntry.get())

    def addSendBtnBind(self,callback):
        self.sendCallback=callback

    def updateCallback(self,*args):
        self.messageWindow["state"] = NORMAL
        self.messageWindow.delete(1.0, END)
        self.messageWindow.insert(END, self.chat.content.get())
        self.messageWindow["state"] = DISABLED
