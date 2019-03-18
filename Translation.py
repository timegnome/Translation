
# *****************************************************
# Marcel Maxwell
# Translation
# This file implements a window for an application that
# will process and record text in a different language 
# and translate it to the desired form for display. 
# Window will be the front end of the application as 
# the tools for translation will be processed in a
# seperate file.
# *****************************************************

import tkinter as tk
from tkinter import ttk
import socket
import os
import sys
#from Translator import *
import win32api
from tkinter import filedialog
from win32api import GetSystemMetrics

class Translator(tk.Tk):
	def __init__(self, *args, **kwargs):
		
		global systemType 
		systemType = root.tk.call('tk', 'windowingsystem')
		screenWidth = GetSystemMetrics(0)
		screenHeight = GetSystemMetrics(1)
		tk.Tk.__init__(self, *args, **kwargs)
		container = tk.Frame(self, borderwidth = 2, relief = "solid", width = screenWidth * .75, height = screenHeight * .75)
		container.option_add('*tearOff', FALSE)
		window.title('Wuxai Translator')
		win = Toplevel(self)
		toolBar = Menu(win)
		quickTools = Menu(win)
		window.minsize(screenHeight*.20,screenWidth*.15)
		if(systemType == 'aqua'):
			appmenu = Menu(toolBar, name='apple')
			windowmenu = Menu(toolBar, name='window')
			menubar.add_cascade(menu=appmenu)
			appmenu.add_command(label='About My Application')
			appmenu.add_separator()
			helpmenu = Menu(toolBar, name='help')
			menubar.add_cascade(menu=helpmenu, label='Help')
			root.createcommand('tk::mac::ShowHelp', ...)
	
			menubar.add_cascade(menu=windowmenu, label='Window')
			root.createcommand('tk::mac::ShowPreferences', showMyPreferencesDialog)
		elif(systemType == 'windows'):
				sysmenu = Menu(menubar, name='system')
				menubar.add_cascade(menu=sysmenu)
		else:
			menu_help = Menu(menubar, name='help')
			menubar.add_cascade(menu=menu_help, label='Help')
		win['menu'] = toolBar
		translation = tk.Frame(container)
		text = Text(translation, state = 'disabled', wrap = 'WORD')
		original = tk.Frame(container)
		statistics = tk.Frame(container)
		
		container.grid(column = 0, row = 0, columnspan = 3, rowspan = 3, sticky =(N,S, E, W))
		toolBar.grid(column = 0, row = 0, columnspan = 3, sticky =(N, E, W))
		statistics.grid(column = 0, row = 2, rowspan = 3, sticky =(S, W))
		translation.grid(column = 1, row = 2, columnspan = 3, rowspan = 3, sticky =(S, E, W))
		original.grid(column = 2, row = 2, columnspan = 3, rowspan = 3, sticky =(S, E))
		
		container.grid_columnconfigure(0, weight = 1)
		container.grid_rowconfigure(0, weight = 1)
		statisticsgrid_columnconfigure(0, weight = 0)
		statistics.grid_rowconfigure(0, weight = 1)
		toolBar.grid_columnconfigure(0, weight = 1)
		toolBar.grid_rowconfigure(0, weight = 1)
		translation.grid_columnconfigure(0, weight = 3)
		translation.grid_rowconfigure(0, weight = 1)
		original.grid_columnconfigure(0, weight = 2)
		original.grid_rowconfigure(0, weight = 1)
		
		menu_file = Menu(toolBar)
		menu_edit = Menu(toolBar)
		toolBar.add_cascade(menu= menu_file, label= 'File')
		toolBar.add_cascade(menu= menu_edit, label= 'Edit')
		
		menu_file.add_command(label= 'New', command=newFile)
		menu_file.add_command(label= 'Open...', command=openFile)
		menu_file.add_command(label= 'Save', command=saveFile)
		menu_file.add_command(label= 'Export', command=exportTranslation)
		menu_file.add_separator()
		
		menu_edit.add_command(label= Font)
		
		
		text.tag_bind('translated', '<1>', highlight)
	
	def insertText(self, text, translated):
		text['state'] = 'normal'
		text.insert('end', ' '+translated,(translated, 'translated') )
		text.tag_bind(translated, '<3>',  popupMeno)
		text['state'] = 'disabled'
	#def popUpMenu(self):
	
	#def showMyPreferencesDialog():
	
	#def newFile(self, frame)):
		#frame.
	def openFile(self, menu):
	#	menu.
		filename =  filedialog.askopenfilenames(initialdir="folderName", title="Select file",  filetypes=(("MIDI files", "*.mid *.midi"), ("all files", "*.*")))
	def saveFile(self, menu):
		filename = filedialog.asksaveasfilename()
	def directory(self, menu):
		dirname = filedialog.askdirectory()
	#def fontChange(self,frame):
		
	#def export(self, frame):
		
	#def	changeText(self, frame, ):
	
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

	def chooseFile(self, fileNameBox):
		global fileName
		#makes list from user selection
		fileName = filedialog.askopenfilenames(initialdir="folderName", title="Select file",  filetypes=(("MIDI files", "*.mid *.midi"), ("all files", "*.*")))
		getFiles = list(fileName)
		listlength = len(getFiles)

		global filePath, fileList
		
		filePath = []
		fileList = []
		
		#separate lists to split path and filename
		for i in range(0, listlength):
			(tempPath, tempList) = os.path.split((getFiles[i]))
			filePath.append(tempPath), fileList.append(tempList)

		#prints filename to make label less messy
		for i in range(0, listlength):
			fileNameBox.insert(tk.END, str(i) + ". " + fileList[i] + '\n')

		for i in range(0, len(fileList)):
			print (str(i) + ". " + fileList[i] + '\n')
	
	'''fdlg = FileDialog.LoadFileDialog(root, title="Choose A File")
	fname = fdlg.go() # opt args: dir_or_file=os.curdir, pattern="*", default="", key=None)
	if file == None: # user cancelled
	#sets the button information, location, and command
	ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
	
	#adds padding to the sides of the widgets
	#sets cursor to the variable space
	#sets the keybinding for the button and function of what to use 
	for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
	feet_entry.focus() 
	root.bind('<Return>', calculate)
	'''
	text = Translator()