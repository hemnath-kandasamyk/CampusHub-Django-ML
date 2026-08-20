from abc import ABC, abstractmethod


class PerformancePredictor(ABC):

    @abstractmethod
    def predict(self, attendance, marks):
        pass

    @abstractmethod
    def explain(self):
        pass