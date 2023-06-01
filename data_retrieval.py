from SPARQLWrapper import SPARQLWrapper, JSON


class DataRetrieval:
    def __init__(self, endpoint_url):
        self.endpoint_url = endpoint_url
        self.sparql = SPARQLWrapper(self.endpoint_url)

    def query_dbpedia(self, query):
        self.sparql.setQuery(query)
        self.sparql.setReturnFormat(JSON)
        results = self.sparql.query().convert()
        return results

    def preprocess_data(self, results):
        data = []
        for result in results["results"]["bindings"]:
            label = result.get("label", {}).get("value")
            description = result.get("description", {}).get("value")

            if label and description:
                item = {"subject": label, "predicate": "description", "object": description}
                data.append(item)

        return data
