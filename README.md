# CLI-Piano

Actually it is more than a piano now. At first I intended to make a CLI piano just for fun. But I finally
decided to record my own voice and made it into a beat-box machine.
<br>

## How to use it

In mac terminal, clone the repo and use your favorite editor to open the piano.py file. Modify line 95 and 
line 104 to your current path of SOURCE folder. And do the same thing to line 41 in player.py

Now you can run `python3 piano.py` and enjoy.
<br>

## Keys
+ Number 1 - 7: Piano sound C3 to B3
+ QWERTYU: Human voice C3 to B3
+ ASDFGHJ: Human voice C4 to B4
+ ZXCVBNM<> and space: Bbox
+ tab: recording mode
+ esc: quit

### Recording mode
You can enter the recording mode by simply pressing the tab once.

From this point, every key you press will be recorded into the record.txt file.
Press `<esc>` to exit the program.

Now run `player.py`. You should be able to play the music you just recorded by
doing so.
