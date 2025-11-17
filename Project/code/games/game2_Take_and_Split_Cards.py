AUTHOR= 'Jiete Xue'
DATE= '2022/11/14'
VERSION= '1.0'



'''Whole file waiting to be debugged.'''



description='''There are initially n cards in one bunch on the table. \n
You can choose to take 1-k cards from one bunch, or split them into two bunches (each bunch can't be empty). \n
The player who get the last card on the table wins.'''







#------------------initial setting-------------------#
import random

def pre_words():
    print("We are going to start the game of taking and splitting cards.\n")
    n=input("Enter the number of initial cards (larger than 5, or enter directly for random setting): ")
    k=input("Enter the maximum number of cards you can take (larger than 1, or enter directly for random setting): ")
    if n.isdigit() and k.isdigit(): 
        if int(n)>5 and int(k)>1:
            return [int(k),int(n)]

def initial_list(list=None):

    '''We use a list to record the number of cards in each bunch.

    ATTENTION: the first element is the max number of cards you can take.'''

    if list is None:
        list=[random.randint(2,10),random.randint(6,20)]
    return list

def initial_setting():
    return(initial_list(pre_words()))






#------------------judge functions-------------------#

def SG(n,k):

    '''Given n(the number of initial cards) and 
    k(the maximum number of cards you can take), 
    return the value of SG.'''

    if n%(2**k) == 0:
        return n-1
    elif n%(2**k) == 2**k-1:
        return n+1
    else:
        return n

def judge_win(list):

    '''Check whether the given list is a winning list.'''
    sg=0
    for i in range(1,len(list)):
        sg^=SG(list[i],list[0])
    if sg==0:
        return False
    else:
        return True

def judge_move_local(list,i,num):

    '''Check whether the given point can be moved.'''
    '''m is exactly a list (for convenience of splitting part)'''

    if i==0:
        if list[num[1]]<=num[0] or num[0]<=0:
            return False
        else:
            return True
    else:
        if list[i]<num[0] or num[0]>list[0] or num[0]<1:
            return False
        else:
            return True

def judge_move_global(list):

    '''Check each point of the given list whether it can be moved,
    if it can be moved, return the index of the points. 
    If all the points cannot be moved, return [].'''

    moving=[]
    # Take
    for i in range(1,len(list)):
        for num in range(1,list[0]+1):
            if judge_move_local(list,i,[num]):
                moving.append([i,[num]])

    # Split
    for i in range(1,len(list)):
        if list[i]>1:
            for j in range(1,list[0]+1):
                if judge_move_local(list,i,[1,j]):
                    moving.append([i,[1,j]])
            moving.append([0,[list[i],i]])
    return moving




#------------------action functions-------------------#
def acted_list(list,i,m):

    '''Return the list after one move.
        Two mode: split or take
        (1) i==0: split, m=[rest number of cards at the place you choose, place you choose]
        (2) i!=0: take, m=[number of cards you choose]'''

    if i==0:
        list.append(list[m[1]]-m[0])
        list[m[1]]=m[0]
    else:
        list[i]-=m[0]
    

    









#------------------Test-------------------#

if __name__ == "__main__":
    #list setting part
    print(initial_setting())

    #judge win part
    list=[2,3,4,1,2,2,1]
    print(judge_win(list))

    #judge move part
    list=[2,3,4,1,2,2,1]
    print(judge_move_global(list))

    #acted list part
    list=[2,3,4,1,2,2,1]
    print(acted_list(list,judge_move_global(list)[0]))




