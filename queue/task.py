from typing import List, Union

class Task:
    def __init__(self, _name: str) -> None:
        self.name = _name

class TaskQueue:
    def __init__(self) -> None:
        self.data: List[Task] = []
    
    def size(self) -> int:
        return len(self.data)

    def is_empty(self) -> bool:
        return self.size() == 0
    
    def add_task(self, task: Task) -> None:
        self.data.append(task)
    
    def get_next_task(self) -> Union[Task, None]:
        if self.is_empty():
            return None
        response = self.data[0]
        del self.data[0]
        return response

