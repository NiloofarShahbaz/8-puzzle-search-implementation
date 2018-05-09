from queue import PriorityQueue
from puzzle import Puzzle


def Astar_search(initial_state):
    count=0
    solution=[]
    explored=[]
    start_node=Puzzle(initial_state,None,None,0,True)
    q = PriorityQueue()
    q.put((start_node.evaluation_function,count,start_node))

    while (not q.empty()):
        node=q.get()
        node=node[2]
        explored.append(node.state)

        if node.goal_test():
            solution.append(node.action)
            path=node
            while path != start_node:
                path = path.parent
                solution.append(path.action)
            return solution

        children=node.generate_child()
        for child in children:
            if child.state not in explored:
                count += 1
                q.put((child.evaluation_function,count,child))
    return solution


easy_initial_state = [1, 3, 4, 8, 6, 2, 7, 0, 5]
solution=Astar_search(easy_initial_state)
solution=solution[:-1]
solution.reverse()
print('A* EASY SOLUTION:',solution)

medium_initial_state=[2,8,1,0,4,3,7,6,5]
solution=Astar_search(medium_initial_state)
solution=solution[:-1]
solution.reverse()
print('A* MEDIUM SOLUTION:',solution)

hard_initial_state=[2,8,1,4,6,3,0,7,5]
solution=Astar_search(hard_initial_state)
solution=solution[:-1]
solution.reverse()
print('A* HARD SOLUTION:',solution)