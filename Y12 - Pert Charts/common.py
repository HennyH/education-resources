from typing import List, NamedTuple

class Task():
    def __init__(self, name: str, duration: int, depends_on: List['Task']):
        self.name = name
        self.duration = duration
        self.depends_on = depends_on
    
    def __str__(self):
        return f"Task({self.name}, depends_on=({', '.join(t.name for t in self.depends_on)}))"
    
    def __repr__(self):
        return f"Task({self.name}, depends_on=({', '.join(t.name for t in self.depends_on)}))"
    
    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Task):
            return False
        return self.name == o.name and \
               self.duration == o.duration and \
               len(self.depends_on) == len(o.depends_on) and \
               all(xd == yd for xd, yd in zip(self.depends_on, o.depends_on))
    
    def __hash__(self) -> int:
        return hash((self.name, self.duration, tuple(self.depends_on)))

class Edge(NamedTuple):
    from_task: Task
    to_task: Task

class MissingTaskException(Exception):
    pass

class InvalidTaskFileException(Exception):
    pass
