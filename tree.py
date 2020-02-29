import os
import json
import sys

class Counter:

    def __init__(self):
        Counter.count = 0

    def increment(self):
        Counter.count += 1

    def getCount(self):
        print("Count: ", Counter.count)

class Tree:

    def __init__(self, root_dir, hidden_allowed, output_data):
        self.root = root_dir
        self.indent = 0
        self.c = Counter()
        self.hidden_allowed = hidden_allowed
        self.output_data = output_data

        print("Running...\n")
        self.run()
        self.c.getCount()
         

    def run(self):
        
        contents = os.listdir(self.root)
        if not self.hidden_allowed:
            contents = self.remove_hidden(contents)

        if len(contents) > 0:
            for i in contents:
                Branch(self.root, i, self.indent, self.c, self.hidden_allowed, self.output_data)
        else:
            data = f"+ {self.root}"
            self.output(data)
            #self.counter.getCount()
            self.c.increment()

    def remove_hidden(self, l):
        return [i for i in l if not i.startswith(".")]
    
    def output(self, data):
        if self.output_data:
            print(data)

    

class Branch:

    def __init__(self, root_dir, branch_dir, indent, counter, hidden_allowed, output_data):
       self.root = root_dir
       self.branch_dir = branch_dir
       self.indent = indent
       self.counter = counter
       self.hidden_allowed = hidden_allowed
       self.output_data = output_data
       self.run()
        
    def run(self):
        new_path = os.path.join(self.root, self.branch_dir)
        try:
            contents = os.listdir(new_path)
            if not self.hidden_allowed:
                contents = self.remove_hidden(contents)

            data = " " * self.indent + f"() {self.branch_dir}"
            self.output(data)
            #self.counter.getCount()
            self.counter.increment()
             
            if len(contents) > 0:
                for i in contents:
                    Branch(new_path, i, self.indent + 1, self.counter, self.hidden_allowed, self.output_data)

        except:
            data = " " * self.indent + f"+ {self.branch_dir}"
            self.output(data)
            #self.counter.getCount()
            self.counter.increment()

    def remove_hidden(self, l):
        return [i for i in l if not i.startswith(".")]

    def output(self, data):
        if self.output_data:
            print(data)

def confirmed_input(prompt, acceptable_values):
	user_answer = input(prompt)
	acceptable_values = [av.lower() for av in acceptable_values]

	while user_answer.lower() not in acceptable_values:
		print(f"Answer is not in {acceptable_values}")
		user_answer = input(prompt)
	return user_answer

def main():
    print("\nCurrent:", os.getcwd(), "\n")
    output_data = True

    args = sys.argv
    if len(args) > 1:
        if args[1] == "-np":
            output_data = False

    root_dir = input("Enter path:")
    root_dir = root_dir if root_dir != "" else os.getcwd()
     
    if os.path.exists(root_dir):
        print(f"OK, using path: {root_dir}")
        
        hidden_allowed = confirmed_input("Search hidden files/dirs? (y/n): ", ["y", "n"])
        hidden_allowed = True if hidden_allowed == "y" else False
        
        Tree(root_dir, hidden_allowed, output_data)
        
    else:
        print("FAILED")


if __name__ == '__main__':
	main()
