

#creating class in python
class Human: 
    def __init__(self,n,o):#creating properties of the class
        self.name = n
        self.occupation = o
    def do_work(self):
        if self.occupation == "AI/ML ":
            print("I am working on AI/ML")
        elif self.occupation == "Web Developer":
            print("I am working on Web Development")


tom = Human("Tom","AI/ML")
print(tom)