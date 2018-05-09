class Puzzle:
    goal_state=[1,2,3,8,0,4,7,6,5]

    def __init__(self,state,parent,action,path_cost):
        self.parent=parent
        self.state=state
        self.path_cost=path_cost
        self.action=action

    def __str__(self):
        return str(self.state[0:3])+'\n'+str(self.state[3:6])+'\n'+str(self.state[6:9])

    def goal_test(self):
        if self.state == self.goal_state:
            return True
        return False

    @staticmethod
    def find_legal_actions(i,j):
        legal_action = ['U', 'D', 'L', 'R']
        if i == 0:  # up is disable
            legal_action.remove('U')
        elif i == 2:  # down is disable
            legal_action.remove('D')
        if j == 0:
            legal_action.remove('L')
        elif j == 2:
            legal_action.remove('R')
        return legal_action

    def generate_child(self):
        children=[]
        x = self.state.index(0)
        i = int(x / 3)
        j = int(x % 3)
        legal_actions=self.find_legal_actions(i,j)

        for action in legal_actions:
            new_state = self.state.copy()
            if action is 'U':
                new_state[x], new_state[x-3] = new_state[x-3], new_state[x]
            elif action is 'D':
                new_state[x], new_state[x+3] = new_state[x+3], new_state[x]
            elif action is 'L':
                new_state[x], new_state[x-1] = new_state[x-1], new_state[x]
            elif action is 'R':
                new_state[x], new_state[x+1] = new_state[x+1], new_state[x]
            children.append(Puzzle(new_state,self,action,1))
        return children



