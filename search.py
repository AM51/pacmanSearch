# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util
from game import Directions


class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def dfsHelper(problem,state,nxt,path,vis):
    if (problem.isGoalState(state)):
        return 1

    for ( nextState, action, cost) in problem.getSuccessors(state):
        if(vis.has_key(nextState)):
            continue

        vis[nextState] = 1

        res = dfsHelper(problem,nextState,nxt,path,vis)
        if(res == 1):
            nxt[state] = nextState
            path[state] = action
            return 1

    return 0

def findPath(state,nxt,path,problem):
    if(problem.isGoalState(state)):
        return []

    action = path[state]
    lst = findPath(nxt[state],nxt,path,problem)
    lst.append(action)
    return lst

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  "*** YOUR CODE HERE ***"

  nxt = {}
  path = {}
  vis = {}

  vis[problem.getStartState()] = 1
  res = dfsHelper(problem,problem.getStartState(),nxt,path,vis)

  if(res == 0):
      util.raiseNotDefined()



  pt =  findPath(problem.getStartState(),nxt,path,problem)
  return list(reversed(pt))


def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """

  vis = {}
  nxt = {}
  path = {}

  startState = problem.getStartState()

  from util import Queue

  q = Queue()

  q.push(startState)

  goalState = (-1,-1)
  while( not q.isEmpty()):
      state = q.pop()

      for (nextState, action, cost) in problem.getSuccessors(state):
          if (vis.has_key(nextState)):
              continue

          vis[nextState] = 1
          nxt[nextState] = state
          path[nextState] = action

          if (problem.isGoalState(nextState)):
              goalState = nextState
              break

          q.push(nextState)

  return findPathAStar(goalState,path,nxt,problem)

def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def findPathAStar(state,path,nxt,problem):

    if(problem.getStartState() == state):
        return []

    action = path[state]
    lst = findPathAStar(nxt[state],path,nxt,problem)
    lst.append(action)
    return lst

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"

  from util import PriorityQueueCustom
  pq = PriorityQueueCustom()

  cst = {}
  vis = {}
  path = {}
  nxt = {}

  startState = problem.getStartState()
  cst[startState] = 0
  pq.push((problem.getStartState(),Directions.STOP,(-1,-1)),0)

  goalState = (-1,-1)
  while(not pq.isEmpty()):
      (priority,(state,action,prevState)) = pq.pop()
      cst [state] = priority
      path[state] = action
      nxt[state] = prevState
      vis[state] = 1

      if(problem.isGoalState(state)):
          goalState = state

      for (nextState, action, cost) in problem.getSuccessors(state):
          if (vis.has_key(nextState)):
              continue

          newCost = priority + cost + heuristic(nextState,problem)
          pq.push((nextState,action,state),newCost)


  lst =  findPathAStar(goalState,path,nxt,problem)
  print(lst)
  return lst

  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
