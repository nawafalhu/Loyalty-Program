from abc import ABC, abstractmethod

class Reward(ABC):
    @abstractmethod
    def method1(self):
        pass
    
    @abstractmethod
    def method2(self):
        pass

class basic(Reward):
    def __init__(self):
        pass

class silver(Reward):
    def __init__(self):
        pass

class gold(Reward):
    def __init__(self):
        pass