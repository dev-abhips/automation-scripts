from abc import ABC, abstractmethod


class BaseTask(ABC):

    @abstractmethod
    def get_param_values(self):
        pass

    @abstractmethod
    def run(self):
        pass
