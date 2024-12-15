import pytest
from project import add_task, del_task, completed, print_completed, print_all
def test_add_task():
    Task = {}
    result = add_task(Task, "Task 1", "1")
    assert result == {"1": "Task 1"}
    assert "1" in result

def test_del_task():
    Task = {"1": "Task 1"}
    result = del_task(Task, "1")
    assert result is True
    assert "1" not in Task

    # Test deleting a non-existing task
    result = del_task(Task, "2")
    assert result is False

def test_completed():
    Task = {"1": "Task 1"}
    complete = {}
    result = completed(Task, complete, "1")
    assert result is True
    assert "1" in complete
    assert "1" not in Task

    # Test completing a non-existing task
    result = completed(Task, complete, "2")
    assert result is False

def test_print_completed():
    complete = {"1": "Task 1"}
    result = print_completed(complete)
    assert result == ["Task 1 With ID: 1 Completed ✔️"]

def test_print_all():
    Task = {"1": "Task 1", "2": "Task 2"}
    result = print_all(Task)
    assert result == ["Task 1 With ID: 1 In Progress 🕜", "Task 2 With ID: 2 In Progress 🕜"]

if __name__ == "__main__":
    pytest.main()
