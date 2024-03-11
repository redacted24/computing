state = input()

def solver():
    if int(state) > 0:
        return state
    else:
        if state[-2] > state[-1]:
            return int(state[:-2]+state[-1])
        else:
            return int(state[:-1])

print(solver())
