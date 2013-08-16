#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import shuffle

def solveIt(n):
    # Modify this code to run your puzzle solving algorithm

    # define the domains of all the variables (0..n-1)
    domains = [range(0, n)] * n
    vis = [0] *n

    # start a trivial depth first search for a solution
    sol = tryall([], 0, n, vis)

    # prepare the solution in the specified output format
    # if no solution is found, put 0s
    outputData = str(n) + '\n'
    if sol is None:
        print 'no solution found.'
        outputData += ' '.join(map(str, [0] * n)) + '\n'
    else:
        outputData += ' '.join(map(str, sol)) + '\n'

    return outputData


# this is a depth first search of all assignments
def tryall(assignment, completed, n, vis):
    # base-case: if the domains list is empty, all values are assigned
    # check if it is a solution, return None if it is not

    if not checkIt(assignment):
        return

    if completed == n:
        if checkIt(assignment):
            return assignment
        else:
            return None

    # recursive-case: try each value in the next domain
    # if we find a solution return it. otherwise, try the next value
    else:
        trylst = range(n)
        shuffle(trylst)
        for v in trylst:
            if not vis[v]:
                vis[v] = 1
                sol = tryall(assignment[:] + [v], completed+1, n, vis)
                vis[v] = 0
                if sol is not None:
                    return sol



# checks if an assignment is feasible
def checkIt(sol):
    n = len(sol)
    for i in range(0, n):
        for j in range(i + 1, n):
            if sol[i] == sol[j] or \
                            sol[i] == sol[j] + (j - i) or \
                            sol[i] == sol[j] - (j - i):
                return False
    return True


import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1].strip())
        except:
            print sys.argv[1].strip(), 'is not an integer'
        print 'Solving Size:', n
        print(solveIt(n))

    else:
        print(
        'This test requires an instance size.  Please select the size of problem to solve. (i.e. python queensSolver.py 8)')

