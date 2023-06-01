from fuzzywuzzy import fuzz


class FuzzyMatching:

    def fuzzy_match(self, query, options, threshold=30):
        best_match = None
        max_similarity = 0

        for option in options:
            similarity = fuzz.token_set_ratio(query, option)
            if similarity >= max_similarity and similarity >= threshold:
                max_similarity = similarity
                best_match = option

        return best_match
