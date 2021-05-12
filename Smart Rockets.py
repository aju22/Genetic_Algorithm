from p5 import *
import random

lifetime = 400 # Lifetime of Rockets
red = Color(255, 0, 0, 255)
target = Vector(400, 50)
mut_rate = 0.01 # Mutation Rate
rx, ry, rw, rh = [200, 350, 400, 10]
maxForce = 0.3

class Rockets:
    def __init__(self, dna):
        self.pos = Vector(400, 700)
        self.vel = Vector(0, 0)
        self.acc = Vector(0, 0)
        if dna is None:
            self.dna = DNA()
        else:
            self.dna = dna
        self.count = 0
        self.fitness = 0
        self.col = Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 150)
        self.completed = False
        self.crashed = False

    def show(self):
        fill(self.col)
        no_stroke()
        translate(self.pos.x, self.pos.y)
        theta = self.vel.angle + PI / 2
        rotate(theta)
        triangle((0, 0), (-10 * cos(PI / 6), 40 * cos(PI / 6)), (10 * cos(PI / 6), 40 * cos(PI / 6)))

        rotate(-(self.vel.angle + PI / 2))
        translate(-self.pos.x, -self.pos.y)

    def update(self):
        global target, rx, ry, rw, rh
        dis = dist(self.pos, target)
        if dis < 10:
            self.completed = True
        if rx < self.pos.x < rx + rw and ry < self.pos.y < ry + rh:
            self.crashed = True
        if self.pos.x > 800 or self.pos.x < 0:
            self.crashed = True
        if self.pos.y > 800 or self.pos.y < 0:
            self.crashed = True

        self.applyForce(self.dna.genes[self.count])
        self.count += 1

        if not self.completed and not self.crashed:
            self.pos += self.vel
            self.vel += self.acc
            self.acc *= 0

    def applyForce(self, force):
        self.acc += force

    def calcFitness(self):
        global target
        d = dist(self.pos, target)
        self.fitness = 1/(d+1)
        if self.completed:
            self.fitness = 1
        if self.crashed:
            self.fitness = 0
class Population:

    def __init__(self, size):
        self.rockets = []
        self.popsize = size
        self.fitness = [0]*size
        for i in range(self.popsize):
            r = Rockets(dna=None)
            self.rockets.append(r)

    def evaluate(self):
        for i in range(self.popsize):
            self.rockets[i].calcFitness()
        fitness = [0]*self.popsize
        for i in range(self.popsize):
            self.fitness[i] = self.rockets[i].fitness

    def selection(self):
        newRockets = []
        for i in range(len(self.rockets)):
            parentA = random.choices(self.rockets, weights=self.fitness, k=1)[0].dna
            parentB = random.choices(self.rockets, weights=self.fitness, k=1)[0].dna
            child = parentA.crossover(parentB)
            child.mutate()
            self.rockets[i] = Rockets(child)



    def run(self):

        for i in range(self.popsize):
            self.rockets[i].update()
            self.rockets[i].show()


class DNA:
    def __init__(self):
        global lifetime, maxForce
        self.genes = []
        for i in range(lifetime):
            force_dir = Vector.random_2D()
            force_dir *= maxForce
            self.genes.append(force_dir)

    def crossover(self, other):
        newdna = DNA()
        mid = random.randint(1, len(self.genes))
        newdna.genes = self.genes[:mid] + other.genes[mid:]

        return newdna

    def mutate(self):
        global mut_rate, maxForce
        for i in range(len(self.genes)):
            if random.random() < mut_rate:
                rnd_force = Vector.random_2D()
                rnd_force *= maxForce
                self.genes[i] = rnd_force


popsize = 25
pop = Population(popsize)
count = 0


def setup():
    size(800, 800)


def draw():
    global pop, target, red, count, popsize, rx, ry, rh, rw
    background(0)
    pop.run()
    fill(red)
    circle(target.x, target.y, 15)
    no_fill()

    count += 1
    if count == lifetime:
        count = 0
        pop.evaluate()
        pop.selection()

    fill(255, 255)
    rect(rx, ry, rw, rh)

run()
