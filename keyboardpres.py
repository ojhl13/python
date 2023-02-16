def keyPressEvent(self, event):
    self.firstrelease = True
    astr = "pressed: " + str(event.key())
    self.keylist.append(astr)

def keyReleaseEvent(self, event):
    if self.firstrelease == True: 
        self.processmultikeys(self.keylist)

    self.firstrelease = False
    del self.keylist[-1]

def processmultikeys(self,keyspressed):
    # your logic here
    print ("hello")
    print (keyspressed)

def main():
 	print ("hello")
 	while True :
 		pass
    
    	
if __name__ == "__main__":
    main()


 		