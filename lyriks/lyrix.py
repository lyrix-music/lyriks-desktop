from typing import List

from .mpris.manage import get_current_song, get_players
from swaglyrics.cli import get_lyrics
from PySide2.QtCore import QObject, Slot, QTimer, Signal


class LyricsFetcher(QObject):

    lyricsUpdated = Signal(str, arguments=["lyrics"])

    def run(self, title: str, artist: str, _: str):
        """Long-running task."""
        if not title or not artist:
            return
        lyrics = get_lyrics(title, artist)
        self.lyricsUpdated.emit(lyrics)


class LyrixEngine(QObject):

    songUpdated = Signal(str, str, str, arguments=["track", "artist", "albumArt"])
    playersUpdated = Signal(list, arguments=['players'])

    def __init__(self):
        super().__init__()

        self.timer = QTimer()
        self.timer.setInterval(1000)  # msecs 100 = 1/10th sec
        self.timer.timeout.connect(self.update_lyrics)
        self.timer.timeout.connect(self.update_players)
        self.timer.start()

        self.last_played_song = ("", "")
        self.players = []
        self.user_selected_player = ""

    def update_lyrics(self):
        title, artist, album_art = get_current_song(self.user_selected_player)
        if (title, artist) == self.last_played_song:
            return
        self.songUpdated.emit(title, artist, album_art)
        self.last_played_song = title, artist
        print(title, artist)

    @Slot(str)
    def playerChanged(self, player: str) -> None:
        self.user_selected_player = player


    def update_players(self):
        players = get_players()
        if self.players != players:
            self.playersUpdated.emit(players)
        return
        

