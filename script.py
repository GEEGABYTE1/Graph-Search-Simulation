from test_values import dictionary
from vertex import Vertex 
from graph import Graph 
from bfs import bfs
from dfs import dfs
import time


class Script:

    def __init__(self, dictionary):
        self.dictionary = dictionary 


    def script(self):
        time.sleep(0.1)
        print()
        print('***GRAPH SEARCH SIMULATION***')
        print('1: View the Graph Dictionary')
        print('2: Simulate the Breadth-First Graph Search')
        print('3: Simulate the Depth-First Graph Search')


        prompt = int(input(':'))
        print('\n')

        if prompt == 1:
            for key, value in self.dictionary.items():
                print(str(key) + ' ---> ' + str(value))
        elif prompt == 2:
            self.bfs_implementation()

        elif prompt == 3:
            print('Please enter a number that is between 1 and 6')
            player = True
            while player:
                start = int(input('Enter a number you want to start the path with: '))
                if start > 6:
                    print("That does not seem like a valid number")
                else:
                    break 
            while player:
                end = int(input('Enter a number you would like to find a path to: '))
                if end > 6:
                    print('That does not seem like a valid number ')
                else:
                    break
            
            print(dfs(self.dictionary, start, end))

    def bfs_implementation(self):
        print('Please enter a number that is between 1 and 6')
        player = True
        while player:
            start = int(input('Enter a number you want to start the path with: '))
            if start > 6:
                print("That does not seem like a valid number")
            else:
                break 
        while player:
            end = int(input('Enter a number you would like to find a path to: '))
            if end > 6:
                print('That does not seem like a valid number ')
            else:
                break 
        
        print(bfs(self.dictionary, start, end))
        print()
        time.sleep(0.1)
        
        running = True
        while running:
            prompt2 = input("Would you like to see another path? Enter y/n: ")

            if prompt2 == 'y':
                current_edge = self.dictionary[start]
                self.dictionary[start].pop(0)
                output = bfs(self.dictionary, start, end)
                if output == None:
                    break 
                else:
                    print(output)
            else:
                break

            
            

            

        




test = Script(dictionary)

print(test.script())