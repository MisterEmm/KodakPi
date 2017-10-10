import imaplib
import email
import time
import atexit
import os
import unicornhat as uh
import time
import colorsys

uh.set_layout(uh.PHAT)
uh.brightness(0.9)
 
def redon():

    for x in range(8):
    	for y in range(4):
    		uh.set_pixel(x, y, 255,0,0)
    uh.show()

def yeon():

    for x in range(8):
    	for y in range(4):
    		uh.set_pixel(x, y, 255,255,0)
    uh.show()

def blon():

    for x in range(8):
    	for y in range(4):
    		uh.set_pixel(x, y, 0,0,255)
    uh.show()

def gron():

    for x in range(8):
    	for y in range(4):
    		uh.set_pixel(x, y, 0,128,0)
    uh.show()

def puon():

    for x in range(8):
    	for y in range(4):
    		uh.set_pixel(x, y, 128,0,128)
    uh.show()      

def whon():

    for x in range(8):
    	for y in range(4):
    		uh.set_pixel(x, y, 255,255,255)
    uh.show()

def pion():

    for x in range(8):
    	for y in range(4):
    		uh.set_pixel(x, y, 255,0,255)
    uh.show()

def lbon():

    for x in range(8):
    	for y in range(4):
    		uh.set_pixel(x, y, 0,128,128)
    uh.show()

def redalert():

	count=0
	while (count < 16):
	    for x in range(8):
	        for y in range(4):
	            uh.set_pixel(x, y, 255, 0, 0)
	    uh.show()
	    time.sleep(0.85)
	    uh.clear()
	    uh.show()
	    time.sleep(0.5)
	    count = count + 1

def snowalert():

	count=0
	while (count < 11):
	    for x in range(8):
	        for y in range(4):
	            uh.set_pixel(x, y, 255,255,255)
	    uh.show()
	    time.sleep(0.5)
	    uh.clear()
	    uh.show()
	    time.sleep(0.5)
	    count = count + 1

def rainbow():

	    spacing = 360.0 / 16.0
	    hue = 0

	    count=0
	    while (count<300):
	        hue = int(time.time() * 100) % 360
	        for x in range(8):
	            offset = x * spacing
	            h = ((hue + offset) % 360) / 360.0
	            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
 	            for y in range(4):
	                uh.set_pixel(x, y, r, g, b)
	        uh.show()
	        time.sleep(0.05)
	        count = count + 1

      
def alloff():

    uh.clear()
    uh.show()

def checkEmail():
        
    mail = imaplib.IMAP4_SSL('imap.gmail.com');
    mail.login('your_gmail_address','your_gmail_password');
    mail.list();  # Gives list of folders or labels in gmail.
    count = 0
    
    while count < 600:
        try:
            # Connect to inbox
            mail.select("inbox"); 
    
            # Search for an unread email from user's email address
            result, data = mail.search(None,'(UNSEEN FROM "your_sending_email_address")');
    
            ids = data[0]   # data is a list
            id_list = ids.split() # ids is a space separated string

            latest_email_id = id_list[-1] # get the latest
            result, data = mail.fetch(latest_email_id, "(RFC822)");

            raw_email = data[0][1];

            recv_msg = email.message_from_string(raw_email)

            ye ="yellow"
            bl ="blue"
            re ="red"
            pu ="purple"
            gr ="green"
            wh ="white"
            pi ="pink"
            lb ="lightblue"
	    ra ="alert"
	    sn ="snow"
	    bo ="rainbow"

            if ye in recv_msg['Subject']:

                print("Yellow Message")     
                print(recv_msg['Subject'])
                yeon()
                time.sleep(30)
                print "Release"
                time.sleep(1)
                alloff()
                
            elif bl in recv_msg['Subject']:

                print("Blue Message")     
                print(recv_msg['Subject'])
                blon()
                time.sleep(30)
                print "Release"
                time.sleep(1)
                alloff()
                

            elif re in recv_msg['Subject']:

                print("Red Message")     
                print(recv_msg['Subject'])
                redon()
                time.sleep(30)
                print "Release"
                time.sleep(1)
                alloff()

            elif pu in recv_msg['Subject']:

                print("Purple Message")     
                print(recv_msg['Subject'])
                puon()
                time.sleep(30)
                print "Release"
                time.sleep(1)
                alloff()

            elif gr in recv_msg['Subject']:

                print("Green Message")     
                print(recv_msg['Subject'])
                gron()
                time.sleep(30)
                print "Release"
                time.sleep(1)
                alloff()

            elif wh in recv_msg['Subject']:

                print("White Message")     
                print(recv_msg['Subject'])
                whon()
                time.sleep(30)
                print "Release"
                time.sleep(1)
                alloff()
                
            elif pi in recv_msg['Subject']:

                print("Pink Message")     
                print(recv_msg['Subject'])
                pion()
                time.sleep(30)
                print "Release"
                time.sleep(1)
                alloff()

                
            elif lb in recv_msg['Subject']:

                print("Light Blue Message")     
                print(recv_msg['Subject'])
                lbon()
                time.sleep(30)
                print "Release"
                time.sleep(1)
                alloff()

            elif ra in recv_msg['Subject']:

                print("Red Alert. Shields Up")     
                print(recv_msg['Subject'])
                redalert()
                print "Release"
                time.sleep(1)
                alloff()

            elif sn in recv_msg['Subject']:

                print("Snow Snow Snow")     
                print(recv_msg['Subject'])
                snowalert()
                print "Release"
                time.sleep(1)
                alloff()

            elif bo in recv_msg['Subject']:

                print("Paint the Whole World")     
                print(recv_msg['Subject'])
                rainbow()
                print "Release"
                time.sleep(1)
                alloff()
                
            else:

                print("Generic Message")     
                print(recv_msg['Subject'])
                time.sleep(2)
                print "Release"
                time.sleep(1)
                
                count = 6

        except IndexError:
            time.sleep(30*1)
            if count < 5:
                count = count + 1
                continue
            else:
                print("Nothing to read here")
                count = 6             
checkEmail()
