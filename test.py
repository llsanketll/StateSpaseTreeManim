from manim import *

import networkx as nx


class Tree(Scene):
  def construct(self):
    G = nx.Graph()

    G.add_node("ROOT")

    G.add_node(1)
    G.add_node(2)
    G.add_node(3)

    G.add_edge("ROOT", 1)
    G.add_edge("ROOT", 2)
    G.add_edge("ROOT", 3)

    G.add_node(4)
    G.add_node(5)
    G.add_node(6)

    G.add_edge(1, 4)
    G.add_edge(1, 5)
    G.add_edge(1, 6)

    G.add_node(7)
    G.add_node(8)
    G.add_node(9)

    G.add_edge(2, 7)
    G.add_edge(2, 8)
    G.add_edge(2, 9)

    G.add_node(10)
    G.add_node(11)
    G.add_node(12)

    G.add_edge(3, 10)
    G.add_edge(3, 11)
    G.add_edge(3, 12)

    self.play(Create(Graph(list(G.nodes), list(G.edges), layout="tree",
              root_vertex="ROOT", labels=True, layout_scale=5)))
    self.wait()
