# CLI-Piano

Actually it is more than a piano now. At first I intended to make a CLI piano just for fun. But I finally
decided to record my own voice and made it into a beat-box machine.
<br>

## How to use it
1. clone the repo
2. Now you can run `./piano.py` and enjoy.
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

Now run `./player.py`. You should be able to play the music you just recorded by
doing so.

**Note:** Please do not exit the program by pressing `ctrl + C`. This might cause some
exceptions when running `./player.py`
