from graphviz import Digraph

dot = Digraph(comment="My Dad's Logic when it comes to gaming on MY pc")


dot.node("A", "Is Timo\nsleeping?")
dot.node("B", "Is Timo on\nthe computer?")
dot.node("C", "Does mom have\na work day?")
dot.node("D", "Is mom\nsleeping?")
dot.node("E", "FU** i can't,\nplay games :(")
dot.node("F", "I CAN PLAY\nGAMES! :D")

dot.edge("A", "B", label="No")
dot.edge("A", "E", label="Yes")
dot.edge("B", "C", label="No")
dot.edge("B", "E", label="Yes")
dot.edge("C", "D", label="No")
dot.edge("C", "E", label="Yes")
dot.edge("D", "F", label="No")
dot.edge("D", "E", label="Yes")


print(f"Saved to: {dot.source}")
dot.render("My Dads logic when it comes to gaming on MY pc", format='png', view=True)