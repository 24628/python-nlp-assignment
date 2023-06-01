from fuzzywuzzy import fuzz


class QueryProcessing:
    def __init__(self, knowledge_graph):
        self.knowledge_graph = knowledge_graph

    def process_query(self, query, best_match):
        query = query.lower()

        information = self.get_information(best_match['subject'], query)
        return information

    def get_information(self, subject, query):
        nodes = self.knowledge_graph.get_nodes(subject)
        matching_nodes = [node for node in nodes if self.predicate_matches_query(node['predicate'], query)]
        information = [{'subject': node['subject'], 'predicate': node['predicate'], 'object': node['object']} for node
                       in matching_nodes]
        return information

    def predicate_matches_query(self, predicate, query):
        similarity = fuzz.token_set_ratio(predicate.lower(), query.lower())
        return similarity >= 35  # Ad

