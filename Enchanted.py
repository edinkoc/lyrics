import threading
import time

lock = threading.Lock()

def animate_text(text, delay):
    with lock:
        for c in text:
            print(c, end='', flush=True)
            time.sleep(delay)
        print()  

def enchanted():
    lines = [
        "This was the very first page",
        "Not where the storyline ends",
        "My thoughts will echo your name",
        "Until I see you again",
        "These are the words I held back",
        "As I was leaving too soon",
        "I was enchanted to meet you",
        "Please don't be in love with someone else",
        "Please don't have somebody waiting on you..."
    ]

    char_delays = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2]
    line_delays = [0.2, 0.3, 0.3, 0.3, 0.2, 0.2, 0.1, 0.3, 0.2]

    for i, line in enumerate(lines):
        animate_text(line, char_delays[i])
        time.sleep(line_delays[i])
