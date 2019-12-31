import pygame
import pyaudio
import wave
import threading
import time
import sys

tone = {49:   "piano_C3",
        50:   "piano_D3",
        51:   "piano_E3",
        52:   "piano_F3",
        53:   "piano_G3",
        54:   "piano_A3",
        55:   "piano_B3",
        97:   "human_C3",
        115:  "human_D3",
        100:  "human_E3",
        102:  "human_F3",
        103:  "human_G3",
        104:  "human_A3",
        106:  "human_B3",
        113:  "human_C2",
        119:  "human_D2",
        101:  "human_E2",
        114:  "human_F2",
        116:  "human_G2",
        121:  "human_A2",
        117:  "human_B2"}

# This function is important
# It plays a wav file
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


pygame.init()
while True:
   time.sleep(0.05)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
      elif event.type == pygame.KEYDOWN:
         if event.key == 27:
            print("Exiting the program, please wait...")
            pygame.quit()
            sys.exit()
         try:
            print(tone[event.key])
            path = "/Users/liguangyao/CLI-Piano/SOUND_SOURCE/" + tone[event.key] + ".wav"

            # Use multi-threading so that users can play several sounds simultaneously
            threading.Thread(target=play, args=(path,)).start()
         except:
            print("Invalid key pressed! (Error #: " + str(event.key) + " )")
            continue
