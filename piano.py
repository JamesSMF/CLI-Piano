import pygame
import pyaudio
import wave
import threading
import time
import sys
import os

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
        117:  "human_B2",
        122:  "human_bass",
        120:  "human_kick_drum",
        99:   "human_kick_drum2",
        118:  "human_water_drop",
        98:   "human_rimshot",
        110:  "human_in",
        109:  "human_hi_hats",
        44:   "human_hi_hats2",
        32:   "human_scratch",
        46:   "human_echo"}

# This function is important
# It plays a wav file
def play(path):
   wf       = wave.open(path, 'rb')    # rb = read binary
   CHUNK    = 1024
   p        = pyaudio.PyAudio()
   data     = wf.readframes(CHUNK)
   RATE     = wf.getframerate()
   CHANNELS = wf.getnchannels()
   FORMAT   = p.get_format_from_width(wf.getsampwidth())

   stream = p.open(format            = FORMAT,
                   frames_per_buffer = CHUNK,
                   rate              = RATE,
                   channels          = CHANNELS,
                   output            = True)

   while len(data)>0:
      stream.write(data)
      data=wf.readframes(CHUNK)

pygame.init()
PATH = os.getcwd() + "/SOUND_SOURCE/"
while True:
   time.sleep(0.05)
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
      elif event.type == pygame.KEYDOWN:
         if event.key == 27:    # <esc>
            print("Exiting the program, please wait...")
            pygame.quit()
            sys.exit()
         elif event.key == 9:   # <tab>: recording mode
            f          = open("record.txt", "w")
            loop_count = 0
            start      = time.time()
            print("Now in recording mode")
            invalid_key = False
            while True:
               interval = 0
               for rec_key in pygame.event.get():   # get user input key
                  if rec_key.type == pygame.KEYDOWN:
                     if rec_key.key == 27:
                        f.write(" 0")
                        f.close()
                        print("Exiting the program, please wait...")
                        pygame.quit()
                        sys.exit()
                     else:
                        try:
                           tone[rec_key.key]       # check if the key pressed is valid
                           loop_count += 1
                           if loop_count > 1:         # not the first iteration
                              interval = time.time() - start if time.time() - start > 0.05 else 0.05
                              f.write(" " + str(interval) + "\n")

                           start = time.time()
                           print(tone[rec_key.key])
                           # Use multi-threading so that users can play several sounds simultaneously
                           curr_PATH = PATH + tone[rec_key.key] + ".wav"
                           threading.Thread(target=play, args=(curr_PATH,)).start()
                           f.write(tone[rec_key.key])   # write down the key
                        except:
                           print("invalid key pressed! (Error #: " + str(rec_key.key) + ")")
         else:
            try:
               print(tone[event.key])

               # Use multi-threading so that users can play several sounds simultaneously
               curr_PATH = PATH + tone[event.key] + ".wav"
               threading.Thread(target=play, args=(curr_PATH,)).start()
            except:
               print("Invalid key pressed! (Error #: " + str(event.key) + ")")
               continue
