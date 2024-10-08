import time,threading
from pynput.mouse import Controller,Button
from pynput.keyboard import Listener,KeyCode

delay=0.001
button=Button.right
startKey=KeyCode(char="x")
endKey=KeyCode(char="s")

class ClickMouse(threading.Thread):
   def __init__(self,delay,button):
    super(ClickMouse,self).__init__()
    self.delay=delay
    self.button=button
    self.running=False
    self.program_running=True

    def start_clicking(self):
        self.running=True
    def stop_clicking(self):
        self.running=False
    def exit(self):
        self.stop_clicking()
        self.program_running=False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
                time.sleep(.001)
mouse=Controller
click_thread=ClickMouse(delay,button)
click_thread.start()