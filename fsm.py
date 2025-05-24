

def_st = 0
text_st = 1
img_st = 2

class FSM:
    def __init__(self):
        self.states = {}
    def get_state(self, uid):
        if uid not in self.states:
            self.states[uid] = def_st
        return self.states[uid]
    
    def set_state(self, uid, state):
        self.states[uid] = state