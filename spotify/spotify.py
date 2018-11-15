# -*- coding: utf-8 -*-
"""
Display song currently playing in Spotify

Spotify is a digital music service that gives you access to millions of songs.

Requires:
    Spotify: https://www.spotify.com

@author di-wu
"""

import dbus

class Py3status:

    format = '{artist} - {song}'

    def _get_spotify_data(self):
        session_bus = dbus.SessionBus()
        spotify_bus = session_bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
        spotify_properties = dbus.Interface(spotify_bus, "org.freedesktop.DBus.Properties")
        metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")
        return (metadata['xesam:artist'][0], metadata['xesam:title'])

    def hello_world(self):
        artist, song = self._get_spotify_data()

        return {
            'full_text': self.py3.safe_format(self.format, {'artist': artist, 'song': song}),
            'cached_until': self.py3.time_in(1)
        }

if __name__ == "__main__":
    """
    Run module in test mode.
    """
    from py3status.module_test import module_test
    module_test(Py3status)
