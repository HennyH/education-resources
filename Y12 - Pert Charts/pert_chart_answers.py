import itertools
import unittest
from typing import List, MutableSet, Iterable, Optional
from common import Task, Edge, MissingTaskException, InvalidTaskFileException

def get_all_edges(tasks: Iterable[Task]) -> Iterable[Edge]:
    for to_task in tasks:
        for from_task in to_task.depends_on:
            yield Edge(from_task, to_task)

def toposort(tasks: MutableSet[Task]) -> List[Task]:
    """Topologically sort an unordered set of tasks.

    L ← Empty list that will contain the sorted elements
    S ← Set of all nodes with no incoming edge

    while S is not empty do
        remove a node n from S
        add n to L
        for each node m with an edge e from n to m do
            remove edge e from the graph
            if m has no other incoming edges then
                insert m into S

    if graph has edges then
        return error   (graph has at least one cycle)
    else 
        return L   (a topologically sorted order)
    
    See: https://en.wikipedia.org/wiki/Topological_sorting
    """
    sorted_tasks = []
    tasks_with_no_dependencies = \
        [task for task in tasks if not task.depends_on]
    edges = set(get_all_edges(tasks))
    while tasks_with_no_dependencies:
        from_task = tasks_with_no_dependencies.pop()
        sorted_tasks.append(from_task)
        for to_task in tasks:
            edge = Edge(from_task, to_task)
            if edge not in edges:
                continue
            edges.remove(edge)
            to_task_has_dependencies = \
                any(e for e in edges if e.to_task == to_task)
            if not to_task_has_dependencies:
                tasks_with_no_dependencies.append(to_task)
    if edges:
        raise Exception("Task list has cycles")
    return sorted_tasks


def parse_task_file(filename: str) -> List[Task]:
    task_infos = []
    with open(filename, "r") as fileobj:
        name: Optional[str] = None
        duration: Optional[int] = None
        depends_on: Optional[List[str]] = None

        def maybe_build_task_info():
            nonlocal name, duration, depends_on
            if name:
                task_infos.append((name, duration or 0, depends_on or []))
            name = None
            duration = None
            depends_on = None

        for lineno, line in enumerate(fileobj):
            line = line.strip()
            if line.startswith("task:"):
                maybe_build_task_info()
                name = line.removeprefix("task:").strip()
            elif line.startswith("duration:") and duration is None:
                duration = int(line.removeprefix("duration:").strip())
            elif line.startswith("depends_on:") and depends_on is None:
                depends_on = []
            elif line.startswith("-") and depends_on is not None:
                depends_on.append(line.removeprefix("-").strip())
            elif len(line) > 1:
                raise InvalidTaskFileException(f"{lineno}: {line}")
        maybe_build_task_info()

    name_to_task = {n: Task(n, d, []) for n, d, _ in task_infos}
    for name, _, depends_on in task_infos:
        task = name_to_task[name]
        for dependency_name in depends_on:
            if not dependency_name in name_to_task:
                raise MissingTaskException(dependency_name)
            name_to_task[name].depends_on.append(name_to_task[dependency_name])
    return list(name_to_task.values())
