from abc import ABCMeta, abstractmethod

class GeometricFigures():

    __GeometricFigures__=ABCMeta

    def __init__(self):
        """Constructor"""
        pass

    @abstractmethod
    def space(self):
        """Вычисление площади"""
        pass