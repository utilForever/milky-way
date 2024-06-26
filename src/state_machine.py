class StateMachine:
    def __init__(self, states=None):
        self.states = states or {}
        self.current = None

    def change(self, state_name, enter_params=None):
        assert self.states[state_name]

        if self.current:
            self.current.exit()

        self.current = self.states[state_name]
        self.current.enter(enter_params)

    def handle_input(self, inputs):
        self.current.handle_input(inputs)

    def update(self):
        self.current.update()

    def draw(self):
        self.current.draw()
