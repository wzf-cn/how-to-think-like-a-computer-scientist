# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 19:30:37 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
"""
    Every week a computer scientist buys four lotto tickets. She always
    chooses the same prime numbers, with the hope that if she ever hits the 
    jackpot, she will be able to go onto TV and Facebook and tell everyone 
    her secret. This will suddenly create widespread public interest in prime 
    numbers, and will be the trigger event that ushers in a new age of 
    enlightenment. She represents her weekly tickets in Python as a list 
    of lists:
    my_tickets = [[ 7, 17, 37, 19, 23, 43],
                  [ 7,  2, 13, 41, 31, 43],
                  [ 2,  5,  7, 11, 13, 17],
                  [13, 17, 37, 19, 23, 43] ]
"""
my_tickets = [[ 7, 17, 37, 19, 23, 43],
              [ 7,  2, 13, 41, 31, 43],
              [ 2,  5,  7, 11, 13, 17],
              [13, 17, 37, 19, 23, 43] ]
"""
q_a:
    Each lotto draw takes six random balls, numbered from 1 to 49. Write a 
    function to return a lotto draw.
"""
def q_a():
    import random
    rng = random.Random()
    
    balls = list(range(1,49))
    rng.shuffle(balls)
    lotto_draw = balls[:6]
    return lotto_draw

"""
q_b:
    Write a function that compares a single ticket and a draw, and returns 
    the number of correct picks on that ticket:
    test(lotto_match([42,4,7,11,1,13], [2,5,7,11,13,17]), 3)
"""
def lotto_match(draw, tkt):
    right_picks = 0
    for num in tkt:
        if num in draw:
            right_picks += 1
    return right_picks



"""
q_c:
    Write a function that takes a list of tickets and a draw, and returns a 
    list telling how many picks were correct on each ticket:
    test(lotto_matches([42,4,7,11,1,13], my_tickets), [1,2,3,1])
"""
def lotto_matches(draw, tkts):
    eatch_right_picks = []
    
    for tkt in tkts:
        eatch_right_picks.append(lotto_match(draw, tkt))
    return eatch_right_picks
        
"""
q_d:
    Write a function that takes a list of integers, and returns the number 
    of primes in the list:
    test(primes_in([42, 4, 7, 11, 1, 13]), 3)
"""
def is_prime(num):
    flag = True
    if num == 1:
        return False
    for i in range(2,num):
        if num % i != 0:
            continue
        flag = False
        break
    return flag

def primes_in(lst):
    nums_in_list = 0
    for value in lst:
        if is_prime(value) == True:
            nums_in_list += 1
    return nums_in_list

"""
q_e:
    Write a function to discover whether the computer scientist has missed
    any prime numbers in her selection of the four tickets. Return a list 
    of all primes that she has missed:
    test(prime_misses(my_tickets), [3, 29, 47])
"""
def prime_list(num):
    plist = []
    for i in range(2,num + 1):
        if is_prime(i):
            plist.append(i)
    return plist

def remove_adjacent_dups(xs):
    """ Return a new list in which all adjacent
        duplicates from xs have been removed.
    """
    result = []
    most_recent_elem = None
    for e in xs:
        if e != most_recent_elem:
            result.append(e)
            most_recent_elem = e

    return result
     
def prime_misses(my_tickets):
    new_list = []
    for each_ticket in my_tickets:
        new_list.extend(each_ticket[:])
    new_list.sort()
    num_in_tkts = remove_adjacent_dups(new_list)
    plist = prime_list(49)
    
    miss_prime = []
    for prime in plist:
        if prime in num_in_tkts:
            continue
        miss_prime.append(prime)
    
    return miss_prime
    
"""
q_f:
    Write a function that repeatedly makes a new draw, and compares the draw 
    to the four tickets.
    
    1.Count how many draws are needed until one of the computer scientist’s 
    tickets has at least 3 correct picks. Try the experiment twenty times, 
    and average out the number of draws needed.
    
    2.How many draws are needed, on average, before she gets at least 4 picks
    correct?
    
    3.How many draws are needed, on average, before she gets at least 5 
    correct? (Hint: this might take a while. It would be nice if you could 
    print some dots, like a progress bar, to show when each of the 20 
    experiments has completed.)

"""
def cnt(n):  #when get n correct picks, return counts
    count = 0   # count the times of draw
    counter = 0 # count dots
    get_3_correct = False
    while get_3_correct == False:
        count += 1
        lotto_draw = q_a()
        for ticket in my_tickets:
            if lotto_match(lotto_draw, ticket) >= n:
                print('\nin {0} counts, there are at least {1} correct picks\n'.
                      format(count, n))
                get_3_correct = True
                break
        if count % 200 == 0:
            print('.', end = '')
            counter += 1
            if counter == 55:
                counter = 0
                print('\n')
    return count    

def average_counts_num(total_experiments): #return average counts
    sum_counts = 0
    for i in range(total_experiments):
        sum_counts += cnt(5)
    average_count = sum_counts / total_experiments
    return average_count
        
print('the average counts num is {0}'.format(average_counts_num(20)))











