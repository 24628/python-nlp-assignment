class ResponseGeneration:
    def generate_response(self, information):
        if not information:
            response = "Sorry, I couldn't find any relevant information."

        else:
            response = "Here is some information I found:\n"

            for i, properties in enumerate(information, 1):
                response += f"\n{i}."
                subject = properties.get('subject', '')
                predicate = self.convert_underscore_to_space(properties.get('predicate', ''))
                object_value = properties.get('object', '')

                response += f"{subject} {predicate} {object_value}"

        return response

    def convert_underscore_to_space(self, string):
        return string.replace('_', ' ')
