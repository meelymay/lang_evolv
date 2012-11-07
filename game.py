concepts = set(range(10))
symbols = 'abcde'

class Strategy:
    score_inc = 0.1

    def __init__():
        self.score = 1
    
    def hear(self, word):
        return concept

    def say(self, concept):
        return word
    
    def update_score(self, success):
        inc = score_inc if success else -1*score_inc
        self.score += inc

    def produce_offspring(self):
        return self.copy()

# returns True if the listener understood the speaker
def communicate(speaker, listener, concept):
    return listener.hear(speaker.say(concept))

class Game:
    players = {}

    def select_listeners(players):
        # returns a listener randomly based on distribution of players
        return listener

    def interact(speaker, listener):
        # only try to communicate a random subset of concepts
        for concept in concepts:
            if random.random() < concept_subset:
                success = communicate(speaker, listener, concept)

                speaker.update_score(success)
                listener.update_score(success)

    def generation_interact():
        # interact randomly
        for speaker in players:
            listener = select_listener(players)
            interact(speaker, listener)

        # offspring are generated, similar to parents
