import random

class PhraseBank:
    def __init__(self, fname):
        self.phrases = {}
        self.load_phrases(fname)

    def load_phrases(self, fname):
        current_topic = None
        with open(fname, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith("**"):
                    current_topic = line[2:].strip()
                    self.phrases[current_topic] = []
                elif current_topic and line:
                    self.phrases[current_topic].append(line)

    def next_phrase(self, topic):
        if topic in self.phrases:
            return random.choice(self.phrases[topic])
        return None

    def get_all_topics(self):
        return list(self.phrases.keys())
