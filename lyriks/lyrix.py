
from .mpris.manage import get_current_song
from swaglyrics.cli import get_lyrics
from PySide2.QtCore import QObject, Slot, QTimer, Signal, 



class LyricsFetcher(QObject):
    
    lyricsUpdated = Signal(str, arguments=['lyrics'])

    def run(self, title: str, artist: str, _: str):
        """Long-running task."""
        lyrics = get_lyrics(title, artist)
        self.lyricsUpdated.emit(lyrics)
        



class LyrixEngine(QObject):

    
    songUpdated = Signal(str, str, str, arguments=['track', 'artist', 'albumArt'])


    def __init__(self):
        super().__init__()

        self.timer = QTimer()
        self.timer.setInterval(1000)  # msecs 100 = 1/10th sec
        self.timer.timeout.connect(self.update_lyrics)
        self.timer.start()

        self.last_played_song = ("", "")
    

    def update_lyrics(self):
        title, artist, album_art = get_current_song()
        if (title, artist) == self.last_played_song:
            return
        self.songUpdated.emit(title, artist, album_art)
        self.last_played_song = title, artist
        print(title, artist)
        


    def start(self):
        self.timer.start()


    @Slot(str)
    def outputStr(self, s):
        print(s)
