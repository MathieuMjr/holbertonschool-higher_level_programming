#!/usr/bin/env python3

from task_04_flyingfish import Fish, FlyingFish, Bird

flying_fish = FlyingFish()
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()

fish_1 = Fish()
fish_1.habitat()
fish_1.swim()

bird_1 = Bird()
bird_1.fly()
bird_1.habitat()

print(FlyingFish.mro())
