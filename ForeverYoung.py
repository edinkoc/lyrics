import threading
import time

lock = threading.Lock()

def animate_text(text, delay):
    with lock:
        for c in text:
            print(c, end='', flush=True)
            time.sleep(delay)
        print()

def forever_young():
    lines = [
        "\nForever young",
        "I want to be forever young",
        "Do you really want to live forever?",
        "Forever, and ever",
        "Forever young",
        "I want to be forever young",
        "Do you really want to live forever?",
        "Forever, and ever"
    ]

    char_delays = [0.09, 0.09, 0.08, 0.14, 0.09, 0.1, 0.08, 0.14]
    line_delays = [0.3, 2.8, 7.5, 10.9, 14.5, 16.9, 21.6, 23.0]

    threads = []
    for i, line in enumerate(lines):
        thread = threading.Thread(target=lambda: (time.sleep(line_delays[i]), animate_text(line, char_delays[i])))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
