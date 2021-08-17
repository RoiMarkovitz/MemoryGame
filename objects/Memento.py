class Memento(object):
    """
    Memento class contains state of an object to be restored.
    """
    def __init__(self, state):
        self.state = state

    def get_state(self):
        return self.state


class Originator(object):
    """
    Originator creates and stores states in Memento objects.
    """
    state = None

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def save_state_to_memento(self):
        return Memento(self.state)

    def get_state_from_memento(self, memento):
        self.state = memento.get_state()


class Caretaker(object):
    """
    Caretaker object is responsible to restore object state from Memento.
    """
    memento_list = []

    def add_memento(self, memento):
        self.memento_list.append(memento)

    def get_memento(self):
        return self.memento_list.pop()
