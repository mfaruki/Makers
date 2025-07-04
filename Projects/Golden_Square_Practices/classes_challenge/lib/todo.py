class TODO():
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        if task.strip() == "":
            raise Exception("Please add a string")
        
        if "#TODO" not in task:
            return self.task_list
        else:
            self.task_list.append(task)
            return self.task_list
    
    def completed_task(self, task):
        if task.strip() == "":
            raise Exception("Please give a correct task to remove")
        
        if task not in self.task_list:
            raise Exception("That task does not exist")
        elif task in self.task_list:
            self.task_list.remove(task)
        
        return self.task_list