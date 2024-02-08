# Bailey Carlton | Concepts of Programming Languages - Project 3 | 5/1/2023

# We are given a matrix of a variable size consisting of 'O's and '.'s. We must perform the first 100 steps of a modified cellular life
# simulator using multiprocessing following these rules:
#       1) Any position in the matrix with a period ‘.’ is considered “dead” during the current time step.
#       2) Any position in the matrix with a capital letter ‘O’ is considered “alive” during the current time step.
#       3) If an “alive” square has a prime number of living neighbors, then it will be “alive” in the next time step.
#       4) If a “dead” square has 1, 3, 5, or 7 living neighbors, then it will be “alive” in the next time step.
#       5) Every other square dies or remains dead, causing it to be “dead” in the next time step.

# This program takes the command line arguments to get the input file, output file, and the number of processes. It reads the array from the input file
# then divides it into equil parts according to the number of processes. It then processes each cell by counting the number of alive neighbors and
# determines if it will be alive or dead in the next step. The results of each process is combined into another array that represents the next step
# for processing. The next step array is processed, and the cycle continues until the 100th step, which is printed to the output file.



import argparse # for getting command line inputs
from multiprocessing import Process, Queue # for multiprocessing


def fun(arr, queue, upper, lower, lenC, lenR, inx):
    nextArr = [] # stores this process's portion of the next array 

    # Count the number of alive neighbors for each cell
    for i in range(lower, upper):
        list = [] # stores the next individual lines to add to nextArr
        for j in range(lenR):
            count = 0
            if(i == 0): # if at the top of the matrix
                if(j == 0): # if in the top left corner of the matrix
                    if(arr[lenC-1][lenR-1] == 'O'): #up left
                        count = count + 1
                    if(arr[lenC-1][j] == 'O'): #up
                        count = count + 1
                    if(arr[lenC-1][j+1] == 'O'): #up right
                        count = count + 1
                    if(arr[i][lenR-1] == 'O'): #left
                        count = count + 1
                    if(arr[i][j+1] == 'O'): #right
                        count = count + 1
                    if(arr[i+1][lenR-1] == 'O'): #down left
                       count = count + 1
                    if(arr[i+1][j] == 'O'): #down
                        count = count + 1
                    if(arr[i+1][j+1] == 'O'): #down right
                        count = count + 1
                
                elif(j==lenR-1): # If in the top right corner of the marix
                    if(arr[lenC-1][j-1] == 'O'):
                        count = count + 1
                    if(arr[lenC-1][j] == 'O'):
                        count = count + 1
                    if(arr[lenC-1][0] == 'O'):
                        count = count + 1
                    if(arr[i][j-1] == 'O'):
                        count = count + 1
                    if(arr[i][0] == 'O'):
                        count = count + 1
                    if(arr[i+1][j-1] == 'O'):
                        count = count + 1
                    if(arr[i+1][j] == 'O'):
                        count = count + 1
                    if(arr[i+1][0] == 'O'):
                        count = count + 1

                else: # if not in a corner but on the top edge
                    if(arr[lenC-1][j-1] == 'O'):
                        count = count + 1
                    if(arr[lenC-1][j] == 'O'):
                        count = count + 1
                    if(arr[lenC-1][j+1] == 'O'): 
                        count = count + 1
                    if(arr[i][j-1] == 'O'):
                        count = count + 1
                    if(arr[i][j+1] == 'O'):
                        count = count + 1
                    if(arr[i+1][j-1] == 'O'):
                        count = count + 1
                    if(arr[i+1][j] == 'O'):
                        count = count + 1
                    if(arr[i+1][j+1] == 'O'): 
                        count = count + 1
            
            elif(i == lenC-1): # if on the bottom of the matrix
                if(j == 0): # if in the bottom left corner of the matrix
                    if(arr[i-1][lenR-1] == 'O'):
                        count = count + 1
                    if(arr[i-1][j] == 'O'):
                        count = count + 1
                    if(arr[i-1][j+1] == 'O'):
                        count = count + 1
                    if(arr[i][lenR-1] == 'O'):
                        count = count + 1
                    if(arr[i][j+1] == 'O'):
                        count = count + 1
                    if(arr[0][lenR-1] == 'O'):
                        count = count + 1
                    if(arr[0][j] == 'O'):
                        count = count + 1
                    if(arr[0][j+1] == 'O'):
                        count = count + 1

                elif(j==lenR-1): # If in the bottom right corner of the marix
                    if(arr[i-1][j-1] == 'O'):
                        count = count + 1
                    if(arr[i-1][j] == 'O'):
                        count = count + 1
                    if(arr[i-1][0] == 'O'):
                        count = count + 1
                    if(arr[i][j-1] == 'O'):
                        count = count + 1
                    if(arr[i][0] == 'O'): 
                        count = count + 1
                    if(arr[0][j-1] == 'O'): 
                        count = count + 1
                    if(arr[0][j] == 'O'): 
                        count = count + 1
                    if(arr[0][0] == 'O'): 
                        count = count + 1

                else: # If on the bottom edge, but not in a corner
                    if(arr[i-1][j-1] == 'O'): 
                        count = count + 1
                    if(arr[i-1][j] == 'O'):
                        count = count + 1
                    if(arr[i-1][j+1] == 'O'): 
                        count = count + 1
                    if(arr[i][j-1] == 'O'): 
                        count = count + 1
                    if(arr[i][j+1] == 'O'): 
                        count = count + 1
                    if(arr[0][j-1] == 'O'): 
                        count = count + 1
                    if(arr[0][j] == 'O'): 
                        count = count + 1
                    if(arr[0][j+1] == 'O'): 
                        count = count + 1                   
            
            elif (j == 0): # if on the left edge
                if(arr[i-1][lenR-1] == 'O'): 
                    count = count + 1
                if(arr[i-1][j] == 'O'): 
                    count = count + 1
                if(arr[i-1][j+1] == 'O'): 
                    count = count + 1
                if(arr[i][lenR-1] == 'O'):
                    count = count + 1
                if(arr[i][j+1] == 'O'): 
                    count = count + 1
                if(arr[i+1][lenR-1] == 'O'): 
                    count = count + 1
                if(arr[i+1][j] == 'O'):
                    count = count + 1
                if(arr[i+1][j+1] == 'O'): 
                    count = count + 1
            
            elif (j == lenR-1): # if on the right edge
                if(arr[i-1][j-1] == 'O'): 
                    count = count + 1
                if(arr[i-1][j] == 'O'): 
                    count = count + 1
                if(arr[i-1][0] == 'O'): 
                    count = count + 1
                if(arr[i][j-1] == 'O'): 
                    count = count + 1
                if(arr[i][0] == 'O'): 
                    count = count + 1
                if(arr[i+1][j-1] == 'O'): 
                    count = count + 1
                if(arr[i+1][j] == 'O'): 
                    count = count + 1
                if(arr[i+1][0] == 'O'): 
                    count = count + 1                
            
            else: # if in the middle
                if(arr[i-1][j-1] == 'O'): 
                    count = count + 1
                if(arr[i-1][j] == 'O'): 
                    count = count + 1
                if(arr[i-1][j+1] == 'O'): 
                    count = count + 1
                if(arr[i][j-1] == 'O'): 
                    count = count + 1
                if(arr[i][j+1] == 'O'): 
                    count = count + 1
                if(arr[i+1][j-1] == 'O'): 
                    count = count + 1
                if(arr[i+1][j] == 'O'): 
                    count = count + 1
                if(arr[i+1][j+1] == 'O'): 
                    count = count + 1

            if arr[i][j] == 'O':# if current node is alive and its count of alive neighbors is prime
                if (count == 2 or count == 3 or count == 5 or count == 7):
                    list.append('O')
                else:
                    list.append('.')
            elif arr[i][j] == '.':# if current node is dead and its count of alive neighbors is 1, 3, 5, or 7
                if (count == 1 or count == 3 or count == 5 or count == 7):
                    list.append('O')
                else:
                    list.append('.')
        nextArr.append(list)

    queue.put((inx, nextArr), False) # puts this process's next arr into the queue with its index



def main():
    #------------------ File Managment ------------------
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=argparse.FileType('r'), dest='i')
    parser.add_argument('-o', type=argparse.FileType('w'), dest='o')
    parser.add_argument('-p', action='store', dest='p', type=int)
    args = parser.parse_args()
    if args.p:
        p = args.p
    else:
        p = 1

    in_ptr = args.i
    out_ptr = args.o

     #------------------ Get Array from File ------------------
    arr = []
    line = []
    lenC = 1
    lenR = 0
    temp = ''
    while True:
        c = in_ptr.read(1) 

        if(c == '\n'):
            lenR = len(line)
            arr.append(line)
            line = []
            temp = '\n'
        elif (c == 'O' or c == '.'):
            line.append(c)
            temp = ''
        elif (c == ''):
            if(temp == '\n'):
                break
            arr.append(line)
            break
        else:
            print("ERROR - INVALID CHARACTER")
            exit()
    
    
    lenC = len(arr)
    x = lenC/p # determines how many lines per process
    x = int(x)
    queue = Queue()

#------------------ Processing Steps ------------------
    for step in range(100):
        processes = []
        c = p # counts the index for later reordering
        upper = lenC # creates upper and lower bounds for each process

        for i in range(p):
            if(i == p-1): # if on the last process, create process with remaining lines
                processes.insert(0,(Process(target=fun, args=(arr, queue, upper, 0, lenC, lenR, c))))
            else: # create process with x lines
                processes.insert(0,(Process(target=fun, args=(arr, queue, upper, upper-x, lenC, lenR, c))))
                upper = upper - x
            c = c - 1

        for pro in processes:
            pro.start()

        # get the queue from processes and order them according to index
        arrCount = 0
        unsorted_result = [queue.get() for _ in processes]
        result = [val[1] for val in sorted(unsorted_result)]

        for pro in processes:
            pro.join()

        # set arr = nextArr for next step
        for i in range(len(result)):
            for j in result[i]:
                arr[arrCount] = j
                arrCount = arrCount + 1

#------------------ Write Final Array to File ------------------
    for k in range(lenC):
        for l in range (lenR):
            out_ptr.write(arr[k][l])
        out_ptr.write('\n')
        


if __name__ == '__main__':
    main()
