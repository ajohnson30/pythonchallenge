
U = ord("W")      # keycodes 
L = ord("A") 
R = ord("D")
D = ord("S")


class myApp: 
    id = 0 
    def __init__(self, root): 
        self.root = root 


        self.draw = Canvas(self.root, width=400, height=400) 
        self.draw.create_oval(200, 200, 210, 210, tags="it", fill="blue") 
        self.draw.pack() 


        # What's better: this, or binding <KeyPress> and ignoring everything 
        # that's not a keycode of one of these? 
        self.root.bind("<KeyPress>", self.move_it)


    def move_it(self, *args): 
        # Because bind gives an argument, which I will always need, but 
        # after doesn't give the argument. 
        if len(args): 
            self.dir = args[0] 


        if self.dir.keycode == U and self.draw.coords("it")[1] > 2: 
            self.draw.move("it", 0, -1) 
        elif self.dir.keycode == D and self.draw.coords("it")[1] < 390: 
            self.draw.move("it", 0, 1) 
        elif self.dir.keycode == R and self.draw.coords("it")[0] < 390: 
            self.draw.move("it", 1, 0) 
        elif self.dir.keycode == L and self.draw.coords("it")[0] > 2: 
            self.draw.move("it", -1, 0) 


        # Because otherwise, it gets called twice as many times. 
        if self.id: 
            self.root.after_cancel(self.id) 


        self.id = self.root.after(10, self.move_it) 


if __name__ == "__main__": 
     from Tkinter import * 
     root = Tk() 
     root.title('tkDemo') 
     myApp(root)
     mainloop()
