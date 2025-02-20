import threading
import time
import sys

def apply_gradient(text):
    colors = [
        "\033[38;5;88m",  # Dark red
        "\033[38;5;130m", # Orange-red
        "\033[38;5;94m",  # Deep orange
        "\033[38;5;136m", # Orange
        "\033[38;5;166m", # Dark orange
        "\033[38;5;202m", # Red-orange
        "\033[38;5;208m", # Orange-red
        "\033[38;5;124m", # Red
        "\033[38;5;88m"   # Dark red
    ]
    gradient_text = ''
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        gradient_text += color + char
    gradient_text += "\033[0m" 
    return gradient_text

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

def apocalypse():
    lines = [
        ("Got the music in you, baby", 0.08, 0.1),
        ("Tell me why", 0.08, 2),
        ("Got the music in you, baby", 0.08, 0.3),
        ("Tell me why", 0.08, 2),
        ("You've been locked in here forever", 0.05, 0.2),
        ("And you just can't say goodbye", 0.09, 6.6),
        ("Your lips, my lips", 0.09, 1.2),
        ("Apocalypse", 0.009, 6.4),
        ("Your lips, my lips", 0.09, 1.2),
        ("Apocalypse", 0.009, 5)
    ]
    
    threads = []
    for lyric, char_delay, line_delay in lines:
        if "Apocalypse" in lyric:
            lyric = lyric.replace("Apocalypse", apply_gradient("Apocalypse"))
        thread = threading.Thread(target=sing_lyric, args=(lyric, line_delay, char_delay))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()