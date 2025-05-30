class Task:

    def __init__(self,name=None):
        self.name=name if name else " "
        self.status = 'pending'
        self.id = 0