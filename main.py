def unmutemusic():
    global currentvol
    root.MuteButton.grid()
    root.UnmuteButton.grid_remove()
    mixer.music.set_volume(currentvol)



def mutemusic():
    global currentvol
    root.MuteButton.grid_remove()
    root.UnmuteButton.grid()
    currentvol = mixer.music.get_volume()
    mixer.music.set_volume(0)
    Audiostatuslabel.configure(text='Muted....')


def resume():
    root.ResumeButton.grid_remove()
    root.PauseButton.grid()
    mixer.music.unpause()
    Audiostatuslabel.configure(text='Playing....')


def stop():
    mixer.music.stop()
    Audiostatuslabel.configure(text='Stopped!!!!')


def volumeup():
    vol = mixer.music.get_volume()
    if (vol >= vol*10):

        mixer.music.set_volume(vol + 0.1)
    else:
        mixer.music.set_volume(vol + 0.05)
    Progressbarvolumelabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    Progressbarvolume['value'] = mixer.music.get_volume()*100


def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol - 0.1)
    vol = mixer.music.get_volume()
    if (vol <= vol * 100):

        mixer.music.set_volume(vol - 0.1)
    else:
        mixer.music.set_volume(vol - 0.05)
    Progressbarvolumelabel.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
    Progressbarvolume['value'] = mixer.music.get_volume() * 100


def pause():
    mixer.music.pause()
    root.PauseButton.grid_remove()
    root.ResumeButton.grid()
    Audiostatuslabel.configure(text='Paused....')


def playmusic():
    ad = audiotrack.get()
    mixer.music.load(ad)
    ProgressbarLabel.grid()
    root.MuteButton.grid()
    ProgressbarMusicLabel.grid()
    mixer.music.set_volume(0.4)
    Progressbarvolume['value'] = 40
    Progressbarvolumelabel['text'] = '40%'
    mixer.music.play()
    Audiostatuslabel.configure(text='Playing....')

    Song = MP3(ad)
    totalsonglength = int(Song.info.length)
    ProgressbarMusic['maximum'] = totalsonglength
    ProgressbarMusicEndTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglength))))

    def Progressbarmusictick():
        Currentsonglength = mixer.music.get_pos()//1000
        ProgressbarMusic['value'] = Currentsonglength
        ProgressbarMusicStartTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=Currentsonglength))))
        ProgressbarMusic.after(2,Progressbarmusictick)
    Progressbarmusictick()



def musicurl():
    try:
        dd = filedialog.askopenfilename(initialdir='D:/music', title='Selct Audio file', filetype=(('.MP3', '*.mp3'), ('WAV','*wav')))
    except:
        dd=filedialog.askopenfilename(title='Selct Audio file',filetype=(('.MP3','*.mp3'),('WAV','*wav')))

    audiotrack.set(dd)


def createwidthes():
    global imbrowse, implay, impause, imvolumeup, imvolumedown, imresume,imstop,Audiostatuslabel,ProgressbarLabel,Progressbarvolume,Progressbarvolumelabel,ProgressbarMusicLabel,ProgressbarMusic,ProgressbarMusicEndTimeLabel,ProgressbarMusicStartTimeLabel
    ############Image Register############
    implay = PhotoImage(file='play-button-arrowhead.png')
    impause = PhotoImage(file='pause-button-made-up-of-two-vertical-lines.png')
    imbrowse = PhotoImage(file='browsing (1).png')
    imvolumeup = PhotoImage(file='volume-up (1).png')
    imvolumedown = PhotoImage(file='volume-down (1).png')
    imstop = PhotoImage(file='stop-button (1).png')
    imresume = PhotoImage(file='media-end.png')

    ##############Change size of images##########
    imbrowse = imbrowse.subsample(1, 1)
    implay = implay.subsample(1, 1)
    impause = impause.subsample(1, 1)
    imvolumeup = imvolumeup.subsample(1, 1)
    imvolumedown = imvolumedown.subsample(1, 1)
    imstop = imstop.subsample(14, 14)
    imresume = imresume.subsample(1, 1)

    #############################labels#############################################
    TrackLabel = Label(root, text='Select Audio Track:', bg='sky blue', font=('arial', 15, 'italic bold'))
    TrackLabel.grid(row=0, column=0, padx=20, pady=20)

    Audiostatuslabel = Label(root, text='', bg='sky blue', font=('arial', 15, 'italic bold'),width=20)
    Audiostatuslabel.grid(row=2,column=1)

    ############Progress bar Volume###############################################
    ProgressbarLabel = Label(root, text='', bg='red')
    ProgressbarLabel.grid(row=0,column=4,rowspan=3,padx=20,pady=30)
    ProgressbarLabel.grid_remove()


    Progressbarvolume = Progressbar(ProgressbarLabel, orient=VERTICAL, mode='determinate', value=0, length=190)

    Progressbarvolume.grid(row=0, column=0, ipadx=5)

    Progressbarvolumelabel=Label(ProgressbarLabel,text='0%',bg='lightgray',width=3)
    Progressbarvolumelabel.grid(row=0,column=0)



################# Progreess bar Music##########################
    ProgressbarMusicLabel= Label(root,text='',bg='red')
    ProgressbarMusicLabel.grid(row=3,column=0,columnspan=3,padx=20,pady=20)
    ProgressbarMusicLabel.grid_remove()


    ProgressbarMusicStartTimeLabel = Label(ProgressbarMusicLabel,text='0.00:0',bg='red',width=6)
    ProgressbarMusicStartTimeLabel.grid(row=0,column=0)


    ProgressbarMusic =  Progressbar(ProgressbarMusicLabel, orient=HORIZONTAL, mode='determinate', value=0)
    ProgressbarMusic.grid(row=0,column=1,ipadx=250,ipady=3)



    ProgressbarMusicEndTimeLabel = Label(ProgressbarMusicLabel, text='0.00:0', bg='red')
    ProgressbarMusicEndTimeLabel.grid(row=0, column=2)



    ##########Entry#########################################################
    TrackLabelEntry = Entry(root, font=('arial', 16, 'italic bold'), width=38, textvariable=audiotrack)
    TrackLabelEntry.grid(row=0, column=1, padx=20, pady=20)

    #########Buttons#################
    BrowseButton = Button(root, text='Search', bg='deeppink', font=('arial', 13, 'italic bold'), width=200, height=25,
                          bd=5, activebackground='purple4',
                          image=imbrowse, compound=RIGHT, command=musicurl)
    BrowseButton.grid(row=0, column=3, padx=20, pady=20)

    PlayButton = Button(root, text='Play', bg='green2', font=('arial', 14, 'italic bold'), width=200, bd=5,
                        activebackground='purple4', image=implay, compound=RIGHT, command=playmusic)
    PlayButton.grid(row=1, column=0, padx=20, pady=20)

    root.PauseButton = Button(root, text='Pause', bg='yellow2', font=('arial', 13, 'italic bold'), width=200, bd=5,
                         activebackground='purple4', image=impause, compound=RIGHT, command=pause)
    root.PauseButton.grid(row=1, column=1, padx=20, pady=20)

    root.ResumeButton = Button(root, text='Resume', bg='yellow2', font=('arial', 13, 'italic bold'), width=200, bd=5,
                          activebackground='purple4', image=impause, compound=RIGHT, command=resume)
    root.ResumeButton.grid(row=1, column=1, padx=20, pady=20)
    root.ResumeButton.grid_remove()

    StopButton = Button(root, text='Stop', bg='red2', font=('arial', 13, 'italic bold'), width=200, bd=5,
                        activebackground='purple4', image=imstop, compound=RIGHT, command=stop)
    StopButton.grid(row=2, column=0, padx=20, pady=20)

    VolumeUpButton = Button(root, text='Volume Up', bg='blue', font=('arial', 13, 'italic bold'), width=200, bd=5,
                            activebackground='purple4', image=imvolumeup, compound=RIGHT, command=volumeup)
    VolumeUpButton.grid(row=1, column=3, padx=20, pady=20)

    VolumeDownButton = Button(root, text='Volume Down', bg='blue', font=('arial', 13, 'italic bold'), width=200, bd=5,
                              activebackground='purple4', image=imvolumedown, compound=RIGHT, command=volumedown)
    VolumeDownButton.grid(row=2, column=3, padx=20, pady=20)

    root.MuteButton = Button(root, text='Mute', width=20,bg='yellow',font=('arial', 13, 'italic bold'), activebackground= 'purple4', bd=5, compound=RIGHT,command=mutemusic)

    root.MuteButton.grid(row=3, column=3)
    root.MuteButton.grid_remove()


    root.UnmuteButton = Button(root, text='Unmute', width=20, bg='yellow', font=('arial', 13, 'italic bold'),
                             activebackground='purple4', bd=5, compound=RIGHT,command=unmutemusic)
    root.UnmuteButton.grid(row=3, column=3)
    root.UnmuteButton.grid_remove()



########################################################################
from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3

root = Tk()
root.geometry('1100x500+200+50')
root.title('Gana Bajane ka yantra')
root.iconbitmap('music.ico')
root.resizable(False, False)
root.configure(bg='lightskyblue')
########################Gloabl variables#################
audiotrack = StringVar()
currentvol=0
totalsonglength=0
count = 0
text = ''

##########Create Slider##############################
ss = 'Developed By Sidhant'


SliderLabel = Label(root, text=ss, bg='lightskyblue', font=('arial', 40, 'italic bold'))
SliderLabel.grid(row=4, column=0, padx=20, pady=20, columnspan=3)


def IntroLabelTick():
    global count, text
    if (count >= len(ss)):
        count = -1
        text = ''
        SliderLabel.configure(text=text)
    else:
        text = text + ss[count]
        SliderLabel.configure(text=text)
    count += 1
    SliderLabel.after(200, IntroLabelTick)


IntroLabelTick()
mixer.init()
createwidthes()

root.mainloop()
