# test_project.py
from project import add_task, view_tasks, remove_task, tasks

def test_add_task():
    tasks.clear()  # Start with an empty list
    add_task()
    assert len(tasks) == 1

def test_view_tasks():
    tasks.clear()
    add_task()
    assert view_tasks() is None  # view_tasks() only prints output

def test_remove_task():
    tasks.clear()
    add_task()
    remove_task()
    assert len(tasks) == 0
