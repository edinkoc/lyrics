import threading
import time

lock = threading.Lock()

def animate_text(text, delay):
    with lock:
        for c in text:
            print(c, end='', flush=True)
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def now_im_ready():
    lines = [
        ("i cannot vanish", 0.08, 0.3),
        ("you will not scare me", 0.06, 0.1),
        ("try to get through it", 0.08, 0.3),
        ("try to push through it", 0.06, 0.3),
        ("you were not thinking that i will not do it", 0.07, 0.6),
        ("they be lovin' someone", 0.06, 0.3),
        ("and i'm another story", 0.07, 0.4),
        ("take the next ticket", 0.05, 0.6),
        ("take the next train", 0.05, 0.5),
        ("why would i do it?", 0.08, 0.5),
        ("anyone'd think that", 0.06, 0.3),
        ("baby", 0.1, 0.8),
        ("now i'm ready", 0.06, 1),
        ("moving on", 0.08, 1),
        ("oh, but maybe", 0.08, 1),
        ("i was ready", 0.07, 1),
        ("all along", 0.05, 1),
        ("oh, i'm ready", 0.07, 1),
        ("for the moment", 0.08, 0.9),
        ("and the sound", 0.08, 0.9),
        ("oh, but maybe", 0.08, 0.9),
        ("i was ready", 0.06, 0.9),
        ("all along", 0.06, 0.9),
        ("oh, baby", 0.07, 0.9),
        ("now i'm ready", 0.06, 0.9),
        ("moving on", 0.07, 0.9),
        ("oh, but maybe", 0.07, 0.9),
        ("i was ready", 0.05, 0.9),
        ("all along", 0.05, 0.9)
    ]
    
    threads = []
    for lyric, char_delay, line_delay in lines:
        thread = threading.Thread(target=sing_lyric, args=(lyric, line_delay, char_delay))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
