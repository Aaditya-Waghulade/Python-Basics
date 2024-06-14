#creating class in python
class Human: 
    def __init__(self,n,o,a):#creating properties of the class
        self.name = n
        self.occupation = o
        self.age = a
        int(a)
    
    def do_work(self):
        if self.occupation == "AI/ML ":
            print("I am working on AI/ML")
        elif self.occupation == "Web Developer":
            print("I am working on Web Development")


tom = Human("Tom","AI/ML",21)
tom.do_work
