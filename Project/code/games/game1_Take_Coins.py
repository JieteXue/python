AUTHOR= 'Jiete Xue'
DATE= '2025/11/11'
VERSION= '1.0'







description='''n positions on a line. \n
There are initially several coins at each position on the line. \n
You can choose a position to add a coin, and remove a coin from each side of its neighboring position, if it is possible. \n
The player who can not move loses.'''






#------------------initial setting-------------------#
import random

def pre_words():
    print("We are going to start the game of taking coins.")
    print("")
    n=input("Enter the number of positions to put coins (larger than 2, or enter directly for random setting): ")
    if n.isdigit(): 
        return int(n)

def random_list(n=-1):
    '''Generate a random list of coins.'''
    if n is None or type(n)!=int or n<=2:
        list=[random.randint(0,10) for i in range(random.randint(5,10))]
    else:
        list=[random.randint(0,10) for i in range(n)]
    return list

def initial_setting():
    return(random_list(pre_words()))




#------------------judge functions-------------------#
def judge_win(list):

    '''Check whether the given list is a winning list.'''

    a=[1,0,1,1,0,1]
    b=[1,1,0,1,1,0]
    A=B=0
    for i in range(len(list)):
        j=i%6
        A+=a[j]*list[i]
        B+=b[j]*list[i]
    if (A%2)^2+(B%2)^2==0:
        return False
    else:
        return True

def judge_move_local(list,i):

    '''Check whether the given point can be moved.'''

    if i==0 or i==len(list)-1:
        return False
    else:
        if list[i-1]*list[i+1]==0:
            return False
        else:
            return True

def judge_move_global(list):

    '''Check each point of the given list whether it can be moved,
    if it can be moved, return the index of the points. 
    If all the points cannot be moved, return [].'''

    moving=[]
    for i in range(len(list)):
        if judge_move_local(list,i):
            moving.append(i)
    return moving
    

#------------------action functions-------------------#
def acted_list(list,i):
    list[i]+=1
    list[i-1]-=1
    list[i+1]-=1
    return list



#------------------Test-------------------#
if __name__ == "__main__":
    list=[2,3,4,1,2,2,1]
    print(judge_win(list))
    print(judge_move_global(list))
    print(acted_list(list,judge_move_global(list)[0]))