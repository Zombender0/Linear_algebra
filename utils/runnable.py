from PySide6.QtCore import QRunnable

class TaskRunnable(QRunnable):
    def __init__(self,function, *args, **kwargs):
        super().__init__()
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.function(*self.args,**self.kwargs)