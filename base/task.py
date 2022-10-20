class BaseTask:
    def get_params(self):
        raise NotImplementedError("`get_params` function should be implemented by the subclass!")

    def run(self):
        raise NotImplementedError("`get_params` function should be implemented by the subclass!")
