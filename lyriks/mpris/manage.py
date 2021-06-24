from typing import Tuple

import dbus




def get_current_song() -> Tuple[str, str, str]:
    session_bus = dbus.SessionBus()
    spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.elisa",
                                        "/org/mpris/MediaPlayer2")
    spotify_properties = dbus.Interface(spotify_bus,
                                        "org.freedesktop.DBus.Properties")
    metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")

    artists = metadata["xesam:artist"]
    artist = ""
    if isinstance(artists, dbus.Array):
        # more than one artist, we should return only the first
        artist = str(artists[0])
    title = str(metadata["xesam:title"])
    album_art = str(metadata.get("mpris:artUrl", ""))
    return title, artist, album_art