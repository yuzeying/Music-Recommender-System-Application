#This is the final project of music recommender system application
#by Kaiqi Du, Cheng You and Zeying Yu as a Group in DSC 478 Course

class User:
    def __init__(self,username="",password="",playlist=[]):
        self.username = username
        self.password = password
        self.playlist = playlist
    def addSong(self, song):
        if(song in self.playlist):
            print("Song already exists")
        else:
            self.playlist.append(song)
            print("song added")
    def songInPlaylist(self, song):
        if(song in self.playlist):
            return True
        else:
            return False
    def getUsername(self):
        return self.username
    def getPlaylist(self):
        return self.playlist
    def validatePassword(self, password):
        return self.password == password
    def __str__(self):
        playstr = ""
        for i in self.playlist:
            playstr  = playstr + i + "|"
        return self.username + "," + self.password + "," + playstr

