from tasks.base_task import BaseTask


class DuplicateDetectorTask(BaseTask):

    def get_param_values(self):
        print("Inside DuplicateDetectorTask.get_param_values()")

    def run(self):
        print("Inside DuplicateDetectorTask.run()")
