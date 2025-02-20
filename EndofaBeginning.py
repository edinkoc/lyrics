import time
import sys
from threading import Thread

lyrics = [
    ("Just trust me, you'll be fine", 0.09),
    ("And when we're back in Chicago, I feel it", 0.09),
    ("Another version of me, I was in it", 0.09),
    ("I wave goodbye to the end of beginning", 0.08),
    ("Goodbye, goodbye, goodbye, goodbye", 0.01),
]

delays = [
    0.0,   
    5.0,   
    11.0,  
    17.0,  
    20.8, 
    
]

def print_line(line, char_delay):
    
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(char_delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def print_lyrics():
    
    start_time = time.time()
    for (line, char_delay), delay in zip(lyrics, delays):

        elapsed = time.time() - start_time
        if delay > elapsed:
            time.sleep(delay - elapsed)
        print_line(line, char_delay)

