import os
import json
import time

class Scanner:

    def __init__(self):
        self.flags = []

    def add_flags(self):
        flags = input("Enter flags: split by '/': ").split("/")
        for flag in flags:
            self.findLink(flag)

    def findLink(self, flag):
        print(f"[FL] Finding flag {flag}...", end="")

        with open("links.json", "r") as json_link:
            data = json.load(json_link)

        if flag in data:
            print("flag found!")
            self.flags.append(data[flag]["link"])
        else:
            print("no flag :(")

class Counter:
    def __init__(self):
        Counter.count = 0

    def increment(self):
        Counter.count += 1

    def getCount(self):
        print("Count: ", Counter.count)

class Branch:
    def __init__(self, root_dir, branch_dir, indent, counter):
       self.root = root_dir
       self.branch_dir = branch_dir
       self.indent = indent
       self.counter = counter
       self.run()
        
    def run(self):
        new_path = os.path.join(self.root, self.branch_dir)
        try:
            contents = os.listdir(new_path)
            print((" " * self.indent) + "()", self.branch_dir)
            #self.counter.getCount()
            self.counter.increment()
             
            if len(contents) > 0:
                for i in contents:
                    time.sleep(0.005)
                    Branch(new_path, i, self.indent + 1, self.counter)

        except:
            print((" " * self.indent) + "+", self.branch_dir)
            #self.counter.getCount()
            self.counter.increment()


class Tree:
    def __init__(self, root_dir):
        self.root = root_dir
        self.indent = 0
        self.c = Counter()

        print("Running...\n")
        self.run()
        #self.c.getCount()
         
    def run(self):
        
        contents = os.listdir(self.root)
        if len(contents) > 0:
            for i in contents:
                Branch(self.root, i, self.indent, self.c)
        else:
            print("+", self.root)
            #self.counter.getCount()
            self.c.increment()
 
def run_application():
    print("\n", os.getcwd(), "\n")
    root_dir = input("Enter path:")
     
    if os.path.exists(root_dir):
        print("OK")
        tree = Tree(root_dir)
    else:
        print("FAILED")

def test_scanner():
    scanner = Scanner()
    scanner.add_flags()


if __name__ == '__main__':
    test_scanner()