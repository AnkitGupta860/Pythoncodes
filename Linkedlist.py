class node:
    def __init__(self,value):
        self.info = value
        self.link = None

class Singlelinkedlist:
    def __init__(self):
        self.start = None
    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        else:
            print("List is     ")
            p = self.start
            while p is not None:
                print(p.info," ",end="")
                p = p.link
            print()

    def count_nodes(self):
        p = self.start
        n=0
        while p is not None:
            n += 1
            p = p.link
        print("Number of nodes of the list = ",n)

    def