import sys
try:
    import dbus
except ImportError:
    print "Please install the python interface to dbus (on Ubuntu, apt-get install python-dbus)"
    sys.exit(0)
from opster import command

@command(usage='%name COMMAND [ARGS]')
def send_command(command, *args):
    '''Send a command to spotify.
    Available commands:
        Raise() 
        Quit() 
        Next() 
        Previous() 
        Pause() 
        PlayPause() 
        Stop() 
        Play() 
        Seek( Offset )
        SetPosition( TrackId, Position )
        OpenUri( Uri )
        Seeked( Position )
    '''
    with open("/tmp/shit", "w") as f:
        f.write("hello\n")
    session = dbus.SessionBus.get_session()
    spotify = session.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")
    getattr(spotify, command)(*args)

if __name__ == '__main__':

    send_command.command()
