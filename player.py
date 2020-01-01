import pyaudio
import wave
import threading
import time
import os

def play(path):
   CHUNK    = 1024
   wf       = wave.open(path, 'rb')    # rb = read binary
   data     = wf.readframes(CHUNK)
   p        = pyaudio.PyAudio()
   FORMAT   = p.get_format_from_width(wf.getsampwidth())
   CHANNELS = wf.getnchannels()
   RATE     = wf.getframerate()

   stream = p.open(format            = FORMAT,
                   channels          = CHANNELS,
                   rate              = RATE,
                   frames_per_buffer = CHUNK,
                   output            = True)

   while len(data)>0:
      stream.write(data)
      data=wf.readframes(CHUNK)

# Read from the record.txt file. and store in the list.
COMMAND = list()

with open("record.txt", "r") as f:
   for line in f:
      COMMAND.append(line.split(" ")[0])
      COMMAND.append(line.split(" ")[1])

f.close()

# Play the music
T = "0"
while len(COMMAND)>0:
   time.sleep(float(T))
   sound = COMMAND.pop(0)
   T = COMMAND.pop(0)
   path = os.getcwd() + "/SOUND_SOURCE/" + sound + ".wav"
   threading.Thread(target=play, args=(path,)).start()

print("End of recording file. Exiting the program...")
