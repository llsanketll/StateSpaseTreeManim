from manim import *


class Node(Scene):

  def __init__(self, state, parent, action=[0, 0, 0]):
    self.parent = parent
    self.state = state
    self.action = action
    self.goal_state = [0, 0, 0]

  def __str__(self):
    return str(self.state)

  def is_valid(self):
    missionaries = self.state[0]
    cannibals = self.state[1]
    boat = self.state[2]
    if missionaries < 0 or missionaries > 3:
      return False
    if cannibals < 0 or cannibals > 3:
      return False
    if boat > 1 or boat < 0:
      return False
    return True

  def is_killed(self):
    missionaries = self.state[0]
    cannibals = self.state[1]
    if missionaries < cannibals and missionaries > 0:
      return True
    # Check for the other side
    if missionaries > cannibals and missionaries < 3:
      return True

  def generate_child(self):
    children = []
    op = -1  # Boat Moves from Left to Right
    if self.state[2] == 0:
      op = 1  # Boat Moves from Right to Left

    for mis in range(3):
      for can in range(3):
        new_state = self.state.copy()
        new_state[0] += op * mis
        new_state[1] = new_state[1] + op * can
        new_state[2] = new_state[2] + op * 1
        action = [mis, can, op]
        new_node = Node(new_state, self, action)
        if mis + can >= 1 and mis + can <= 2:
          children.append(new_node)
    return children

  def is_goal_state(self):
    if self.state == self.goal_state:
      return True
    return False
