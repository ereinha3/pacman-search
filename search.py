# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    # Create a stack from the utils-declared Class
    myStack = util.Stack()

    # Get the start state of the problem
    startState = problem.getStartState()

    # Add the start state and the list of actions to get there to the stack
    myStack.push((startState, []))

    # Declare an array to hold all visited states so that each state is only explored once
    visited = []

    # Continue searching for a solution until all paths have been explored (if a solution exists it will be found and loop will end with return)
    while not myStack.isEmpty():

        # Unpack state and action sequence from stored element in stack
        state, actionSequence = myStack.pop()

        # If the current state is already at the goal, we have finished and can return the action sequence to get there
        if problem.isGoalState(state):
            return actionSequence
        
        # Each successor should return a list of triples, (successor, action, stepCost)
        if state not in visited:

            # Add this state to the array of visited states so that it won't appear later
            visited.append(state)

            # Iteratively unpack the attributes of each stored successor (we don't need stepCost for DFS so we can ignore it with _)
            for successor, action, _ in problem.getSuccessors(state):

                # Add the successor and the action sequence to get there from start to the stack
                myStack.push((successor, actionSequence + [action]))

    return []

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Create a queue from the utils-declared Class
    myQueue = util.Queue()

    # Get the start state of the problem
    startState = problem.getStartState()

    # Add the start state and the list of actions to get there to the stack
    myQueue.push((startState, []))

    # Declare an array to hold all visited states so that each state is only explored once
    visited = []

    # Continue searching for a solution until all paths have been explored (if a solution exists it will be found and loop will end with return)
    while not myQueue.isEmpty():

        # Unpack state and action sequence from stored element in stack
        state, actionSequence = myQueue.pop()

        # If the current state is already at the goal, we have finished and can return the action sequence to get there
        if problem.isGoalState(state):
            return actionSequence
        
        # Each successor should return a list of triples, (successor, action, stepCost)
        if state not in visited:

            # Add this state to the array of visited states so that it won't appear later
            visited.append(state)

            # Iteratively unpack the attributes of each stored successor (we don't need stepCost for DFS so we can ignore it with _)
            for successor, action, _ in problem.getSuccessors(state):

                # Add the successor and the action sequence to get there from start to the stack
                myQueue.push((successor, actionSequence + [action]))

    return []

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    myPriorityQueue = util.PriorityQueue()

    # Get the start state of the problem
    startState = problem.getStartState()

    # Add the start state and the list of actions to get there to the stack
    myPriorityQueue.push((startState, [], 0), 0)

    # Declare an array to hold all visited states so that each state is only explored once
    visited = []

    # Continue searching for a solution until all paths have been explored (if a solution exists it will be found and loop will end with return)
    while not myPriorityQueue.isEmpty():

        # Unpack state and action sequence from stored element in stack
        state, actionSequence, backCost = myPriorityQueue.pop()

        # If the current state is already at the goal, we have finished and can return the action sequence to get there
        if problem.isGoalState(state):
            return actionSequence
        
        # Each successor should return a list of triples, (successor, action, stepCost)
        if state not in visited:

            # Add this state to the array of visited states so that it won't appear later
            visited.append(state)

            # Iteratively unpack the attributes of each stored successor (we don't need stepCost for DFS so we can ignore it with _)
            for successor, action, pathCost in problem.getSuccessors(state):

                # Add the successor and the action sequence to get there from start to the stack
                myPriorityQueue.push((successor, actionSequence + [action], backCost + pathCost), backCost + pathCost)

    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    myPriorityQueue = util.PriorityQueue()

    # Get the start state of the problem
    startState = problem.getStartState()

    # Add the start state and the list of actions to get there to the stack
    myPriorityQueue.push((startState, [], 0), heuristic(startState, problem))

    # Declare an array to hold all visited states so that each state is only explored once
    visited = []

    # Continue searching for a solution until all paths have been explored (if a solution exists it will be found and loop will end with return)
    while not myPriorityQueue.isEmpty():

        # Unpack state and action sequence from stored element in stack
        state, actionSequence, backCost = myPriorityQueue.pop()

        # If the current state is already at the goal, we have finished and can return the action sequence to get there
        if problem.isGoalState(state):
            return actionSequence
        
        # Each successor should return a list of triples, (successor, action, stepCost)
        if state not in visited:

            # Add this state to the array of visited states so that it won't appear later
            visited.append(state)

            # Iteratively unpack the attributes of each stored successor (we don't need stepCost for DFS so we can ignore it with _)
            for successor, action, pathCost in problem.getSuccessors(state):

                # Add the successor and the action sequence to get there from start to the stack
                myPriorityQueue.push((successor, actionSequence + [action], backCost + pathCost), backCost + pathCost + heuristic(successor, problem))

    return []




# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
