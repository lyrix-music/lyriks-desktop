import QtQuick 2.6

import QtQuick.Controls 2.0
import org.kde.kirigami 2.13 as Kirigami

Kirigami.ApplicationWindow
{
    title: "Lyriks"
    width: 480
    height: 720

    property string lyrixLyrics: ""
    property string lyrixTrack: ""
    property string lyrixArtist: ""
    property string lyrixAlbumArt: ""
    property var availablePlayers: []
    property variant user
    
    
    property QtObject lx
    property QtObject lyricsFetcher

    Connections {
        target: lx

        function onSongUpdated(track, artist, albumArt) {
            lyrixTrack = track;
            lyrixArtist = artist;
            lyrixAlbumArt = albumArt;
            if (lyrixTrack == "" || lyrixArtist == "") {
                return
            }
            lyrixLyrics = `Loading lyrics for ${track} by ${artist}...`
        }

        function onPlayersUpdated(players) {
            availablePlayers = players
        }

    }

    Connections {
        target: lyricsFetcher

        function onLyricsUpdated(msg) {
            lyrixLyrics = msg;
        }

    }
    

    pageStack.initialPage: Qt.resolvedUrl("LyricsPage.qml")
    
}