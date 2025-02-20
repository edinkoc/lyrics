import threading
import time

lock = threading.Lock()

def animate_text(text, delay):
    with lock:
        for c in text:
            print(c, end='', flush=True)
            time.sleep(delay / 1000)
        print()

def sing_song(lyric, delay, speed):
    time.sleep(delay / 1000)
    animate_text(lyric, speed)

def sing_song_main():
    lyrics = [
        ("And I don't know what I'm crying for", 90),
        ("I don't think I could love you more", 90),
        ("It might not be long, but baby, I...", 90),
        ("I'll love you `till the day that I die", 90),
        ("`Till the day that I die..", 90),
        ("Till the lights leaves my eyes", 90),
        ("`Till the day that I die..", 90)
    ]
    
    delays = [300, 3900, 7000, 10500, 15000, 18500, 21500, 24900]
    
    threads = []
    for i, (lyric, speed) in enumerate(lyrics):
        thread = threading.Thread(target=sing_song, args=(lyric, delays[i], speed))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
