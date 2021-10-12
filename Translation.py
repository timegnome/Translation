
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
from tkinter import *
import socket
import os
import sys
from Translator import Translator
#import win32api
from tkinter import filedialog
from win32api import GetSystemMetrics

class frameTranslate(tk.Tk):
	def __init__(self, *args, **kwargs):
		
		tk.Tk.__init__(self, *args, **kwargs)
		nightMode = False
		bgColor = ""
		fgColor = ""
		systemType = self.tk.call('tk', 'windowingsystem')
		screenWidth = GetSystemMetrics(0)
		screenHeight = GetSystemMetrics(1)
		
		#Set size of the application to be no smaller that 35% of the resolution and no bigger than the resolution
		self.minsize(int(screenWidth*.53), int(screenHeight*.53))
		self.maxsize(screenWidth, screenHeight)
		self.geometry(str(int(screenWidth * .85))+'x'+str(int(screenHeight * .85)))
		self.grid_rowconfigure(0, weight = 1)
		self.grid_columnconfigure(0, weight = 1)
		#Create the content frame for all widgets to operate in and have a size of 90% of the resolution
		#container = tk.Frame(self, borderwidth = 0, relief = 'solid',  bg = 'black', width = int(screenWidth) *.80)
		
		#Prevent the ability to tear off any widgets
		self.option_add('*tearOff', 0)
		self.title('Wuxai Translator')
		
		#Creates the menu bar and binds all the features for the program throughout
		self.__addMenubar(self)
		
		#Toplevel frame		
		maincontainer = tk.Frame(self)
		maincontainer.grid(column=0, row=0, sticky = (N, S, E, W))
		maincontainer.grid_rowconfigure(0, weight = 1)
		maincontainer.config(bg ='black')
	
		#First widgets
		statistics = tk.Frame(maincontainer, bg = 'white')
		translation = tk.Frame(maincontainer, width = int(screenWidth *.40),height= int(screenHeight *.40))
		original = tk.Frame(maincontainer, width = int(screenWidth *.40),height= int(screenHeight *.40))
		statistics.grid(column = 0, row = 0, sticky =(N, S, W))
		translation.grid(column = 1, row = 0, sticky =(N, S))
		original.grid(column = 2, row = 0, columnspan= 2, sticky =(N, S, E))
		#translation.grid_columnconfigure(0, weight = 1)
		'''
		statistics.grid_columnconfigure(0, weight = 1)
		statistics.grid_rowconfigure(0, weight = 1)
		translation.grid_columnconfigure(0, weight = 1)
		translation.grid_rowconfigure(0, weight = 1)
		original.grid_columnconfigure(0, weight = 1)
		original.grid_rowconfigure(0, weight = 1)
		'''
		#Secondary widgets
		sizeHolder = tk.Frame(translation, width = '27c' , height = '208c')
		lineNumberBar = TextLineNumbers(translation, width = 30, height = '208c')
		textTrans = Text(sizeHolder, state = 'disabled', wrap = 'word')
		textOrig = Text(original, state = 'disabled', wrap = 'word')
		stats = Listbox(statistics, height = 10)

		transScroll = ttk.Scrollbar(textTrans, orient="vertical", command= textTrans.yview)
		origScroll = ttk.Scrollbar(textOrig, orient="vertical", command= textOrig.yview)
		
		sizeHolder.grid(column = 2, row = 0, sticky = (N, S))
		lineNumberBar.grid(column = 0, row= 0, sticky = (N, S, W))
		translation.grid_rowconfigure(0, weight = 1)
		textTrans.pack(fill = 'both', expand = 1)
		textOrig.pack(fill = 'both', expand = 1)
		stats.pack(fill = 'both', expand =1)
		
		lineNumberBar.attach(textTrans)
		textTrans.tag_bind('translated', '<Double-1>', lambda: self.highlight([textTrans, textOrig]))
		textTrans.tag_bind('translated', '<1>', lambda: self.textTrans.tag_delete('highlight'))
		textOrig.tag_bind('translated', '<1>', lambda: self.textOrig.tag_delete('highlight'))
		
	# Creates the basic front end structure for the program. Will link all functions for backend here
	# Input: Base frame, User past settings if any
	# Output: Creates the frontend UI of the program 
	def __createFrameWork(self, frame):
		statistics = ttk.Frame(self)
		

	# Adds all the menu options and functions for the menubar
	# Inputs: frame 
	# Output: Creates menubar and attaches functions
	def __addMenubar(self, frame):
	
		toolBar = Menu(frame, tearoff=0)	
		menu_file = Menu(toolBar, tearoff=0)
		menu_edit = Menu(toolBar, tearoff=0)
		'''
		if(systemType == 'aqua'):
			appmenu = Menu(toolBar, name='apple', tearoff=0)
			windowmenu = Menu(toolBar, name='window', tearoff=0)
			helpmenu = Menu(toolBar, name='help', tearoff=0)
			toolBar.add_cascade(menu=appmenu)
			appmenu.add_command(label='About My Application')
			appmenu.add_separator()
			toolBar.add_cascade(menu=helpmenu, label='Help')
			self.createcommand('tk::mac::ShowHelp', Help)
			toolBar.add_cascade(menu=windowmenu, label='Window')
			self.createcommand('tk::mac::ShowPreferences', showMyPreferencesDialog)
		#elif(systemType == 'win32'):
			#sysmenu = Menu(toolBar, name='system', tearoff=0)
			#toolBar.add_cascade(menu=sysmenu)
		else:
			menu_help = Menu(toolBar, name='help', tearoff=0)
			toolBar.add_cascade(menu=menu_help, )
		'''
		menu_file.add_command(label= 'New', command = lambda : self.newFile(frame))
		menu_file.add_command(label= 'Open...', command = lambda : self.openFile(frame))
		menu_file.add_command(label= 'Save', command = lambda : self.saveFile(frame))
		menu_file.add_command(label= 'Export', command = lambda : self.exportTranslation(frame))
		menu_edit.add_command(label= 'Font')
		toolBar.add_cascade(menu= menu_file, label= 'File')
		toolBar.add_cascade(menu= menu_edit, label= 'Edit')
		toolBar.add_command(label = '|', state = 'disabled')
		frame.config(menu = toolBar)
	
	def Help(self):
		temp =1
	
	# Inserts the text for both the original and translated text into each widget and links them together
	# Inputs:text widgets Trans and Orig, text translated and original
	# Outputs: Adds text to the widgets and links them together
	def __insertText(self, Trans, Orig, info):
		Trans['state'] = 'normal'
		Orig['state'] = 'normal'
		Trans.insert('end', ' '+translated,(info(0), 'translated'))
		Orig.insert('end', ' '+original,(info(1), 'original'))
		Trans.tag_bind(info(0), '<3>',  lambda: self.__popupMenu(info))
		Orig.tag_bind(info(1), '<3>',  lambda: self.__popupMenu(info))
		Trans['state'] = 'disabled'
		Orig['state'] = 'disabled'
	
	# Sets the bg and fg colors of all widgets to night mode colors being darker and easier on the eyes.
	# No need to pass widgets as just the colors and bool will be enough
	# Inputs: bgColor and fgColor
	# Outputs: Sets the theme of the program to nightMode and changes color
	def __setNightMode(self, bgColor, fgColor):
		if nightMode:
			nightMode = False
			bgColor = ""
			fgColor = ""
		else:
			nightMode = True
			bgColor = ""
			fgColor = ""
	
	# Set the font of the selected text this 
	def __Font(self, Trans, Orig):
		Trans.tag_configure(tag_ranges('sel'), font = fontChoice + ' ' + str(size))
	
	# Popup menu when right clicked so the user can edit the text 
	# and other options to choose from on the specific text
	# 
	def __popUpMenu(self, event, info):
		popup = Menu(self, tearoff=0)
		popup.add_command(label="Edit", command = lambda: self.edit(info))
		popup.add_command(label="Highlight",command = lambda: self.highlight(info))
		#popup.add_separator()
		#popup.add_command(label="Home")
		try:
			popup.tk_popup(event.x_root, event.y_root, 0)
		finally:
		# make sure to release the grab (Tk 8.0a1 only)
			popup.grab_release()
		
	def __showMyPreferencesDialog(self):
		temp =1
		
	# Opens up the default language library setup along with asking the user to select a text and language to use
	# Input: Takes in a name ffrom user for the project/folder 
	# Output: Creates a Blank tab for the texts
	def __newFile(self, frame):
		#frame.
		temp=1
		
	# Opens the file of a translated text and its original. Use the information stored in a directory 
	# or multiple .csv files. 
	# Input: User selected file, the path name of the directory
	# Output: Opens up the translated text and original in a form of tab using Notepad widget
	def __openFile(self, menu):
		#menu.
		#filetypes=(("MIDI files", "*.mid *.midi"), ("all files", "*.*")))
		filename =  filedialog.askopenfilenames(initialdir="folderName", title="Select file")
	
	# Saves the file pf the translated text and its original in the form of a .csv or compressed into a 
	# encrypted file.
	# Input: The translated text and the original, the backend for the novel translated, name for the saved files.
	# Output: Multiple .csv files and an ok message.
	def __saveFile(self, menu):
		filename = filedialog.asksaveasfilename()
	
	# Selects the Directory folder of the current project or makes one if there isn't one made yet.
	# Will open all files if asked into the prompted into multiple tabs/notebook
	# Input: Directory path name from users choice
	# Output: The translated novels saved in the directory.
	def __directory(self, menu):
		dirname = filedialog.askdirectory()
	
	# Sets the font colors of both text widgets back to the default colors. 
	# Does not change the font, italized, bold or other features.
	def __default(self, Trans, Orig):
		Trans.tag_configure('translated', background = '', foreground = '')
		Orig.tag_configure('original', background = '', foreground = '')
		
	# Sets the selected text and corresponding original text to be highlighted
	# Does not change the font, italized, bold or other features.
	def __highlight(self, info):
		self.textTrans['state'] = 'normal'
		self.textOrig['state'] = 'normal'
		self.textTrans.tag_add(self.textTrans.tag_ranges(info(0), 'highlight'))
		self.textTrans.tag_add(self.textTrans.tag_ranges(info(1), 'highlight'))
		if not self.nightMode:
			Trans.tag_configure('highlight', background = 'yellow')
			Orig.tag_configure('highlight', background = 'yellow')
		else:
			Trans.tag_configure('highlight', background = 'gray', foreground = 'blue')
			Orig.tag_configure('highlight', background = 'gray', foreground = 'blue')
		Trans['state'] = 'disabled'
		Orig['state'] = 'disabled'
	
	# Export the file into a .text, .pdf, .doc, etc.
	# Input: The translated text from the 
	# Export: Create a file with the name of the 
	def changeText(self, frame ):
		temp=1
	
# Customer Canvas widget to attach line numbers for a text widget
# Author : Bryan Oakley
# Posted on https://stackoverflow.com/questions/16369470/tkinter-adding-line-number-to-text-widget
class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        index = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(index)
            if dline is None: break
            y = dline[1]
            linenum = str(index).split(".")[0]
            self.create_text(2,y,anchor="nw", text=linenum)
            index = self.textwidget.index("%s+1line" % index)


if __name__ == '__main__':
	Test = frameTranslate()
	Test.mainloop()