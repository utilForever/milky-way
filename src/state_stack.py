class StateStack:
    def __init__(self):
        self.states = []

    def push(self, state):
        self.states.append(state)
        state.enter()

    def pop(self):
        top = self.top()

        if top:
            self.states.remove(top)
            top.exit()

        return top

    def top(self):
        if self.states:
            return self.states[-1]
        else:
            return None

    def update(self, inputs):
        top = self.top()

        if top:
            top.handle_input(inputs)

        for state in reversed(self.states):
            carry_on = state.update()

            if not carry_on:
                break

    def draw(self):
        for state in self.states:
            state.draw()
