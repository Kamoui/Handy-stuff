#!/usr/bin/python

import random
import fileinput
import os, sys
import tkinter as tk
import threading
import time


class myThread (threading.Thread):
		def __init__(self, threadID, name):
			threading.Thread.__init__(self)
			self.threadID = threadID
			self.name = name
			self.status = True
		def run(self):
			print ("Starting " + self.name)
			# Get lock to synchronize threads
			threadLock.acquire()
			limiter = 0
			while (self.status == True and limiter<10000) :
							if (self.status == False):
									break
							else:
									FindFile()
									time.sleep(1)
							limiter += 1
								
							
		

		def receivekey(self):
					self.status = False
					print ("%s: %s" % (self.name, time.ctime(time.time()))+" Got Killed")
					threadLock.release()# Free lock to release next thread
					for t in threads:
									t.join()
					
def log(entry):
		L = open(".\log","a")
		L.write(entry + "")
		L.close()

def FindFile():
	dirs = os.listdir(".\IN")
	for file in dirs:
		ChangeFile= str(".\IN\\"+file)
		FileDefinite= str(".\TMP\\"+file)
		try:
					#Contens of file to procces
					F = open(ChangeFile,"r")
					Filelines = str(F.read())
					F.close()
					#Get header
					H = open(".\Header.txt","r")
					Headerlines = str(H.read())
					H.close()
					#remove old File
					os.remove(ChangeFile)
					#Create new file stream
					Z = open(FileDefinite,"w+")
					outlines = (Headerlines + "\n"	+ Filelines)
					Z.write(outlines)
					Z.close()
					#Entru Log
					log(str("File Processed" + FileDefinite + "\n"))

		except:
				log(str("Failed" + ChangeFile + "\n"))
	print("Running")
		

class Operate():
	def __init__(self):
		# Create new threads
		self.thread1 = myThread(1, "Thread")
		# Start new Threads
		self.thread1.start()
		# Add threads to thread list
		threads.append(self.thread1)
		#lol

	def sendkey(self):
		self.thread1.receivekey()


class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.press = False
		self.pack()
		self.create_widgets()


	def create_widgets(self):
		self.Run = tk.Button(self)
		self.Run["text"] = "Start"
		self.Run["command"] = self.scalp
		self.Run.pack(side="top")
		self.Once = 0
		self.quit = tk.Button(self, text="QUIT", fg="red",command= lambda:[self.Off(),self.master.destroy])
		self.quit.pack(side="bottom")

	def scalp(self):
			if(self.press):
				self.Off()
				self.press = False
			else:
				self.On()
				self.press = True


	def On(self):
		self.Run["text"] = "Stop"
		self.NewOperation = Operate()
		self.Once = 1

	def Off(self):
		if(self.Once == 1):
			print("Not Running")
			self.NewOperation.sendkey()
			self.Run["text"] = "Start"
			self.Once += 1
		else:
			sys.exit()
	
threadLock = threading.Lock()
threads = []
root = tk.Tk()
app = Application(master=root)
app.master.protocol("WM_DELETE_WINDOW", app.Off)
app.master.title("This App adds Header")
app.master.minsize(300, 200)
app.master.maxsize(300, 200)
app.mainloop()
sys.exit()