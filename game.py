import random

concepts = set(range(10))
symbols = 'abcde'

class Genes:

    def __init__(self, strength):
        self.strength = strength

    def play(self, opponent):
        return self.strength > opponent.strength

    def hear(self, word):
        return concept

    def say(self, concept):
        return word

class Player:
    fitness_inc = .1
    offspring_variance = 1
    fitness_variance = .1

    def __init__(self, fitness, genes):
        self.genes = Genes(fitness)
        self.fitness = fitness
    
    def show(self):
        return 'fit'+str(self.fitness)

    def play(self, opponent):
        self.update_fitness(self.genes.play(opponent.genes))

    def update_fitness(self, success):
        inc = Player.fitness_inc if success else -1*Player.fitness_inc
        self.fitness += inc

    def child(self):
        return Player(random.normalvariate(self.fitness,
                                           Player.fitness_variance), 
                      self.genes)

    def reproduce(self):
        return [self.child() for i in range(max(0, 
                                                int(random.normalvariate(self.genes.strength,
                                                                         Player.offspring_variance))))]
                

# returns True if the listener understood the speaker
def communicate(speaker, listener, concept):
    return listener.hear(speaker.say(concept))

class Game:
    opponents_per_gen = 10

    def __init__(self, num_players):
        self.players = [Player(random.normalvariate(1.3,.1), None) for x in range(num_players)]

    def select_players(self):
        # returns a listener randomly based on distribution of players
        return [random.choice(self.players) for i in range(Game.opponents_per_gen)]
                
    def show_players(self):
        print "generation:"
        for player in self.players:
            print '\t',player.show()

    def play_generation(self):
        new_generation = []

        # for each player, play, reproduce
        for player in self.players:
            opponents = self.select_players()
            # play some opponents
            for opponent in opponents:
                player.play(opponent)
            
            # reproduce, die
            new_generation += player.reproduce()
        
        # welcome the new generation
        self.players = new_generation
        
    def play(self, iterations):
        for i in range(iterations):
            self.show_players()
            self.play_generation()
            
if __name__ == '__main__':
    g = Game(15)
    g.play(5)
                            
