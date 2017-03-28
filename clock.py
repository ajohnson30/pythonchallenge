import time 


class Clock: 
     def __init__(self,root): 
         self.root = root 
         self.lb=Label(root,padx=5,pady=5, 
                       fg='blue',font=('Times',20)) 
         self.lb.pack() 
         self.root.after(1000, self.ck) 
         self.ck() 


     def ck(self): 
         self.lb.configure(text=time.asctime()[11:19]) 
         # set up the next callback 
         self.root.after(1000, self.ck) 


if __name__ == "__main__": 
     from Tkinter import * 
     root = Tk() 
     root.title('Clock') 
     Clock(root) 
     mainloop() 

