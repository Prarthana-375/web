"""
Simple Stack-based Undo/Redo example in Python

This script demonstrates a minimal Stack class and using two stacks (undo/redo)
for state management. It isn't tied to the web UI but mirrors the same concept
we implemented in JavaScript for `homepage.html`.

Run: python stack_example.py
"""

from copy import deepcopy

class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self): 
        if not self._data:
            raise IndexError('pop from empty stack')
        return self._data.pop()

    def peek(self):
        return self._data[-1] if self._data else None

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)


def demo():
    # Simplified "state" representation
    initial = {'text': 'YOUR NAME', 'bg': 'blue', 'size': 48}

    undo = Stack()
    redo = Stack()

    # helper to capture/restore
    def save_state(s):
        undo.push(deepcopy(s))

    def restore_state(stack_from, stack_to):
        if stack_from.is_empty():
            print('nothing to restore')
            return None
        state = stack_from.pop()
        stack_to.push(deepcopy(current_state))
        return state

    current_state = deepcopy(initial)
    print('Initial:', current_state)

    # user makes change 1
    save_state(current_state)
    current_state['text'] = 'Alice'
    print('Change 1:', current_state)

    # user makes change 2
    save_state(current_state)
    current_state['bg'] = 'gradient(blue, purple)'
    print('Change 2:', current_state)

    # undo -> should revert to state before change 2
    print('\nPerforming undo...')
    prev = restore_state(undo, redo)
    if prev is not None:
        current_state = prev
    print('After undo:', current_state)

    # redo -> reapply the undone change
    print('\nPerforming redo...')
    next_state = restore_state(redo, undo)
    if next_state is not None:
        current_state = next_state
    print('After redo:', current_state)


if __name__ == '__main__':
    demo()
