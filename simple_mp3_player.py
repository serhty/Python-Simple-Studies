# select a song with a simple mp3 player, increase the volume, decrease the volume, choose a random song, add a song, delete a song, turn it off.

from random import choice

class MP3Player():
    def __init__(self, musicList=[]):
        self.playingMusic = ""
        self.volume = 100
        self.musicList = musicList
        self.status = True
        
    def selectSong(self):
        counter = 1
        for song in self.musicList:
            print("{}){}".format(counter,song))
            counter += 1
            
        selectedSong = int(input("Enter the song number you want to select: "))
        self.playingMusic = self.musicList[selectedSong - 1]
    
    def volumeUp(self):
        if self.volume == 100:
            pass
        else:
            self.volume += 10
    
    def volumeDown(self):
        if self.volume == 0:
            pass
        else:
            self.volume -= 10
    
    def randomMusic(self):
        randomChoice = choice(self.musicList)
        self.playingMusic = randomChoice
    
    def addMusic(self):
        singer = input("Enter Singer: ")
        song = input("Enter Song: ")
        self.musicList.append(singer + "-" + song)
    
    def deleteMusic(self):
        counter = 1
        for song in self.musicList:
            print("{}){}".format(counter,song))
            counter += 1
        songDeleted = int(input("Enter the song number you want to delete: "))
        self.musicList.pop(songDeleted-1)
    
    def close(self):
        self.status = False
    
    def showMenu(self):
        print("""
              --- MP3 Player Menu ---
              Song list: {}
              Now Playing Song: {}
              Volume: {}
              
              1-Select Song
              2-Volume Up
              3-Volume Down
              4-Choose Random Song
              5-Add Song
              6-Delete Song
              7-Close
              """.format(self.musicList,self.playingMusic, self.volume))
        
    def choice(self):
        choice = int(input("Enter Your Choice: "))
        return choice
    
    def run(self):
        self.showMenu()
        choice = self.choice()
        if choice == 1:
            self.selectSong()
        if choice == 2:
            self.volumeUp()
        if choice == 3:
            self.volumeDown()
        if choice == 4:
            self.randomMusic()
        if choice == 5:
            self.addMusic()
        if choice == 6:
            self.deleteMusic()
        if choice == 7:
            self.close()
    
mp3player = MP3Player()
while mp3player.status:
    mp3player.run()
    
    
    
    
    
    
    
    