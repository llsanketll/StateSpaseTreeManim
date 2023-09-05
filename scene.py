from queue import Queue
from manim import *
from Node import Node
import networkx as nx


class StateTree(Scene):
  def construct(self):
    initial_state = [3, 3, 1]
    goal_state = [0, 0, 0]

    root = Node(initial_state, None)
    g = nx.Graph()
    g.add_node(str(root), fill_color=GREEN)

    q = Queue()
    q.put(root)
    explored = []

    while (not q.empty()):
      cur_node = q.get()
      children = []
      if not cur_node.is_killed():
        children = cur_node.generate_child()
      current_color = GRAY
      for child in children:
        if child.is_goal_state():
          current_color = GOLD
          g.add_node(str(child), fill_color=current_color)
          g.add_edge(str(cur_node), str(child), label=child.action)
          goal_state = q.get()
        elif child.is_valid() and not g.has_node(str(child)):
          if child.is_killed():
            current_color = RED
          else:
            current_color = GREEN
            q.put(child)
          g.add_node(str(child), fill_color=current_color)
          g.add_edge(str(cur_node), str(child), label=child.action)

      explored.append(cur_node)

    vertex_colors = {}
    edge_labels = {}
    for i in range(len(g.nodes)):
      vertex_colors.update({str(list(g.nodes)[i]): list(g.nodes.data())[i][1]})
    for i in range(len(g.edges)):
      edge_labels.update({list(g.edges)[i]: list(g.edges.data())[i][2]})

    G = DiGraph(list(g.nodes), list(g.edges), layout="tree",
                root_vertex=list(g.nodes)[0], labels=True, layout_scale=12, vertex_config=vertex_colors)
    G.scale(0.3)
    self.play(Create(G), run_time=5)
    self.wait()
