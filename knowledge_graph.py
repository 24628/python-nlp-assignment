class KnowledgeGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        subject = node['subject']
        if subject not in self.nodes:
            self.nodes[subject] = []
        self.nodes[subject].append(node)

    def get_nodes(self, subject):
        return self.nodes.get(subject, [])

    def get_all_nodes(self):
        return [node for nodes in self.nodes.values() for node in nodes]

