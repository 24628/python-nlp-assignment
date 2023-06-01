from data_retrieval import DataRetrieval
from knowledge_graph import KnowledgeGraph
from nlp_processing import NLPProcessing
from fuzzy_matching import FuzzyMatching
from query_processing import QueryProcessing
from response_generation import ResponseGeneration

data_retrieval = DataRetrieval(endpoint_url="https://dbpedia.org/sparql")
knowledge_graph = KnowledgeGraph()
nlp_processing = NLPProcessing()
fuzzy_matching = FuzzyMatching()
query_processing = QueryProcessing(knowledge_graph)
response_generation = ResponseGeneration()

query = """
        SELECT ?label ?description WHERE {
            ?s rdf:type dbo:Person .
            ?s rdfs:label ?label .
            ?s dbo:abstract ?description .
            FILTER (LANG(?label) = 'en' && LANG(?description) = 'en')
        }
        LIMIT 10000
        """

results = data_retrieval.query_dbpedia(query)
datas = data_retrieval.preprocess_data(results)

for data in datas:
    knowledge_graph.add_node(data)


while True:
    user_input = input("User Query: ")
    preprocessed_query = nlp_processing.preprocess_query(user_input)

    best_match = fuzzy_matching.fuzzy_match(preprocessed_query, knowledge_graph.get_all_nodes())

    if best_match:
        information = query_processing.process_query(user_input, best_match)
        response = response_generation.generate_response(information)
    else:
        response = "Sorry, I couldn't understand your query."

    print("Chatbot Response:", response)

