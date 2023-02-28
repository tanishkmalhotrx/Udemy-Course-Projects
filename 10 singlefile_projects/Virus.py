import webbrowser
import time
import random

while True:
    sites = random.choice(['tanishkmalhotrx.wixsite.com/tancryptedx', 'geekprank.com/hacker/', 'geekprank.com/', 'hackthissite.org/', 'geekprank.com/fake-virus/', 'mrdoob.com/projects/chromeexperiments/google-gravity/', 'hackertyper.net/'])
    visit = 'http://{}' .format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(5, 100)
    time.sleep(seconds)
    
    #this code will randomly open these links so that it looks like a virus attack!
