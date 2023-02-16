import signal

def handler(signum, frame):
    print 'Ctrl+Z pressed, but ignored'

signal.signal(signal.SIGTSTP, handler)

while True:
   pass 
