# -*- coding: utf-8 -*-

import Tkinter

import os
import sys
import mp3play

class Core():

    def __init__(self):

        self.Music = os.listdir(os.path.join(os.path.expanduser('~'), 'Desktop', 'NarutoLibMin'))
        self.MusicPath = os.path.join(os.path.expanduser('~'),'Desktop', 'NarutoLibMin')
        print self.Music

        self.count = ''
        self.mp3 = ''
        self.VolumeSlider = ''
        self.count = 1

        self.createRoot()
        self.createButtons()

        #self.LoadSong(False)

    #---------------------------------------------

    def createRoot(self, w = 729, h = 170):

        self.root = Tkinter.Tk()
        self.root.option_add('*Font', 'courier 12')
        self.root.option_add('*Background', 'light blue')
        self.root.configure(bg='light blue')

        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws/2) - (w/2)    
        y = (hs/2) - (h/2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #---------------------------------------------

    def createButtons(self):

        Tkinter.Button(self.root, height=2, width=10, text='◄◄', borderwidth=10,command=self.BackwardSong, fg = 'black', bg='light blue').grid(row=0,column=0)
        Tkinter.Button(self.root, height=2, width=10, text='►', borderwidth=10,command=self.PlayButton, fg = 'black', bg='light blue').grid(row=0,column=1)

        self.buttonPause = Tkinter.Button(self.root, height=2, width=10, text='║║', borderwidth=10,command=self.PauseButton, fg = 'black', bg='light blue')
        self.buttonPause.grid(row=0,column=2)

        Tkinter.Button(self.root, height=2, width=10, text='■', borderwidth=10,command=self.StopButton, fg = 'black', bg='light blue').grid(row=0,column=3)
        Tkinter.Button(self.root, height=2, width=10, text='►►', borderwidth=10,command=self.ForwardSong, fg = 'black', bg='light blue').grid(row=0,column=4)
        Tkinter.Button(self.root, height=2, width=10, text='Quit', borderwidth=10,command=self.Quit, fg = 'black', bg='light blue').grid(row=1,column=1)
        self.VolumeSlider = Tkinter.Scale(self.root, length = 140, label='  Volume ', orient = 'horizontal', fg = 'black', bg='light blue', command = self.VolAdj).grid(row=1, column=2)    

    #---------------------------------------------

    def LoadSong(self, play=True):
        self.mp3 = self.mp3play.load(os.path.join(self.MusicPath, self.Music[self.count]))
        print play
        if play:
            self.mp3.play()  

    #---------------------------------------------

    def PlayNextSongAuto(self):

        track = 0
        while track < self.mp3.seconds():
            self.root.after(3600)
            track += 1
        self.count = 0
        self.LoadSong()  

    #---------------------------------------------

    def ForwardSong(self):
        Stop = len(self.Music) - 2
        print Stop
        if self.count > Stop:
            print 'End of Play List'
            self.count = 0
            raw_input('')
            self.Quit()    
        self.StopButton()        
        self.count += 1
        self.LoadSong()  

    #---------------------------------------------

    def BackwardSong(self):
#        if self.count > -3:            
#            print 'End of Play List'
#            self.Quit()        
        self.StopButton()
        self.count -= 1
        self.LoadSong()  

    #---------------------------------------------

    def PlayButton(self):
        self.buttonPause.configure(text = '║║', command=self.PauseButton)
        self.mp3.play()

    #---------------------------------------------

    def PauseButton(self):
        self.buttonPause.configure(text = 'Unpause', command=self.UnPauseButton)
        if self.mp3.isplaying():
            self.mp3.pause()

    #---------------------------------------------

    def UnPauseButton(self):
        self.buttonPause.configure(text = '║║', command=self.PauseButton)
        if self.mp3.ispaused():
            self.mp3.unpause() 
    #---------------------------------------------

    def StopButton(self):
        self.buttonPause.configure(text = '║║', command=self.PauseButton)
        self.mp3.stop()

    #---------------------------------------------

    def Quit(self):
        self.StopButton()
        sys.exit('')

    #---------------------------------------------

    def VolAdj(self, val):
        self.mp3.volume(val)

    #---------------------------------------------

    def Run(self):
        self.root.mainloop()

#---------------------------------------------------------------------

Core().Run()