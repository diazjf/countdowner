#!/usr/bin/env python3

import gui, timer
import threading, time

def countdown(view):
    while True:
        time_remaining = timer.getTimeRemaining()
        view.changeLabel(time_remaining)
        time.sleep(1)

def main():
    g = gui.GUI()

    # Update the UI in the background
    thread1 = threading.Thread(target=countdown, args = [g])
    thread1.setDaemon(True)
    thread1.start()

    g.mainloop()
    
if __name__ == '__main__':
    main()