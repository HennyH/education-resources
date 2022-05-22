import os
import unittest
from textwrap import dedent
from typing import List, MutableSet
from tempfile import NamedTemporaryFile
from common import Task, Edge, MissingTaskException, InvalidTaskFileException

def toposort(tasks: MutableSet[Task]) -> List[Task]:
    """Topologically sort an unordered tuple of tasks.

    Psudeocode from wikipedia:

    ```
    L ← Empty list that will contain the sorted elements
    S ← tuple of all nodes with no incoming edge

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
    ```
    
    See: https://en.wikipedia.org/wiki/Topological_sorting
    """
    pass

def parse_task_file(filename: str) -> List[Task]:
    """Parses a task file into a list of tasks.

    A task is a series of entries with the following syntax:

    task: <name>
    duration: <int>
    depends_on:
        - <name>

    The duration and depends_on parts of an entry are OPTIONAL.
    If they are not specified the following defaults:

    duration = 0
    depends_on = []

    If any syntax is encountered other than the above throw an
    InvalidTaskFileException. If a task references a non-existent
    task in its depends_on section throw a MissingTaskException.

    There can be any number of BLANK lines between teach task entry!

    For example, the following file:

    task: a
    duration: 5



    task: b
    duration: 1
    depends_on:
        - a

    Should construct a list equivalent to the following python code:

    a = Task("a", duration=5, depends_on=[])
    b = Task("b", duration=1, depends_on=[a])
    return [a, b]

    Important: See how task b in the example referred to a? If you had two
    tasks b1 and b2 both depend on a then they should referr to the SAME
    object instance of task a.
    """
    pass




try:
    from pert_chart_answers import toposort, parse_task_file
except ImportError:
    pass

class TestToposort(unittest.TestCase):
    def __perform_toposort_test(self, tasks, allowed_answers):
        output = toposort(tasks)
        for allowed_answer in allowed_answers:
            try:
                self.assertListEqual(output, allowed_answer)
                return
            except AssertionError:
                pass
        self.fail(f"The result {output} did not match any of the allowed "
                  f"answers {','.join(map(str, allowed_answers))}.")
    
    def test_single_linear(self):
        a = Task("a", 1, [])
        tasks = [a]
        self.__perform_toposort_test(
            tasks=tasks,
            allowed_answers=[
                [a]
            ]
        )
    
    def test_two_linear(self):
        a = Task("a", 1, [])
        b = Task("b", 1, [a])
        tasks = [b, a]
        self.__perform_toposort_test(
            tasks=tasks,
            allowed_answers=[
                [a, b]
            ]
        )

    def test_simple_diamond(self):
        a = Task("a", 1, [])
        b1 = Task("b1", 1, [a])
        b2 = Task("b2", 1, [a])
        c = Task("c", 1, [b1, b2])
        tasks = [c, b2, a, b1]
        self.__perform_toposort_test(
            tasks=tasks,
            allowed_answers=[
                [a, b1, b2, c],
                [a, b2, b1, c]
            ]
        )
    
    def test_repeated_diamond(self):
        # diamond 1
        a = Task("a", 1, [])
        b1 = Task("b1", 1, [a])
        b2 = Task("b2", 1, [a])
        c = Task("c", 1, [b1, b2])
        # diamon 2
        d = Task("d", 1, [c])
        e1 = Task("e1", 1, [d])
        e2 = Task("e2", 1, [d])
        f = Task("f", 1, [e1, e2])
        tasks = [c, b2, a, b1, e2, f, e1, d]
        self.__perform_toposort_test(
            tasks=tasks,
            allowed_answers=[
                [a, b1, b2, c, d, e1, e2, f],
                [a, b1, b2, c, d, e2, e1, f],
                [a, b2, b1, c, d, e1, e2, f],
                [a, b2, b1, c, d, e2, e1, f],
            ]
        )

class PartupleaskFileTests(unittest.TestCase):
    def __perform_parse_file_test(self, contents, allowed_answers):
        with NamedTemporaryFile("w", delete=False) as tmp_file:
            try:
                tmp_file.write(dedent(contents))
                tmp_file.close()
                result = toposort(parse_task_file(tmp_file.name))
                for allowed_answer in allowed_answers:
                    try:
                        self.assertListEqual(result, allowed_answer)
                        return
                    except AssertionError:
                        pass
                self.fail(f"The result {result} did not match any of the allowed "
                        f"answers {','.join(map(str, allowed_answers))}.")
            finally:
                os.unlink(tmp_file.name)

    def test_single_linear_file(self):
        a = Task("a", 5, [])
        tasks = [a]
        self.__perform_parse_file_test(
            contents="""
            task: a
            duration: 5
            """,
            allowed_answers=[
                [a]
            ]
        )
    
    def test_multiple_linear_file(self):
        a = Task("a", 5, [])
        b = Task("b", 1, [a])
        tasks = [a, b]
        self.__perform_parse_file_test(
            contents="""
            task: a
            duration: 5

            task: b
            duration: 1
            depends_on:
                - a
            """,
            allowed_answers=[
                [a, b]
            ]
        )
    
    def test_diamond_file(self):
        a = Task("a", 5, [])
        b1 = Task("b1", 1, [a])
        b2 = Task("b2", 3, [a])
        c = Task("c", 5, [b1, b2])
        tasks = [a, b1, b2, c]
        self.__perform_parse_file_test(
            contents="""
            task: a
            duration: 5

            task: b1
            duration: 1
            depends_on:
                - a

            task: b2
            duration: 3
            depends_on:
                - a

            task: c
            duration: 5
            depends_on:
                - b1
                - b2
            """,
            allowed_answers=[
                [a, b1, b2, c],
                [a, b2, b1, c]
            ]
        )
    
    def test_invalid_task_file_repeated_duration(self):
        try:
            self.__perform_parse_file_test(
                contents="""
                task: foo
                duration: 5
                duration: 5
                """,
                allowed_answers=[]
            )
        except InvalidTaskFileException:
            return
        self.fail("Expected an invalid task file exception to be raised")

    def test_invalid_task_file_invalid_field(self):
        try:
            self.__perform_parse_file_test(
                contents="""
                task: foo
                duration: 5
                bar
                """,
                allowed_answers=[]
            )
        except InvalidTaskFileException:
            return
        self.fail("Expected an invalid task file exception to be raised")

    def test_invalid_task_file_missing_task(self):
        try:
            self.__perform_parse_file_test(
                contents="""
                task: foo
                duration: 5
                depends_on:
                    - bar
                """,
                allowed_answers=[]
            )
        except MissingTaskException:
            return
        self.fail("Expected an invalid task file exception to be raised")

if __name__ == "__main__":
    unittest.main()
