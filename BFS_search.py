from queue import Queue
from puzzle import Puzzle

def breadth_first_search(initial_state):
    solution=[]
    start_node = Puzzle(initial_state, None, None, 0)
    if start_node.goal_test():
        return solution
    q = Queue()
    q.put(start_node)
    explored=[]
    while not(q.empty()):
        node=q.get()
        explored.append(node.state)
        children=node.generate_child()
        for child in children:
            if child.state not in explored:
                if child.goal_test():
                    solution.append(child.action)
                    path=child
                    while path!=start_node:
                        path=path.parent
                        solution.append(path.action)
                    return solution
                q.put(child)
    return solution


easy_initial_state = [1, 3, 4, 8, 6, 2, 7, 0, 5]
solution=breadth_first_search(easy_initial_state)
solution=solution[:-1]
solution.reverse()
print('BFS EASY SOLUTION:',solution)

medium_initial_state=[2,8,1,0,4,3,7,6,5]
solution=breadth_first_search(medium_initial_state)
solution=solution[:-1]
solution.reverse()
print('BFS MEDIUM SOLUTION:',solution)

hard_initial_state=[2,8,1,4,6,3,0,7,5]
solution=breadth_first_search(hard_initial_state)
solution=solution[:-1]
solution.reverse()
print('BFS MEDIUM SOLUTION:',solution)