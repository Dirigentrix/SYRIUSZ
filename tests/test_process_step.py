import pytest
from dartrix.vsm.process_step import ProcessStep

def test_process_step_creation():
    step = ProcessStep("Test", "processing", 5.0, True)
    assert step.name == "Test"
    assert step.value_added is True

def test_add_next():
    step1 = ProcessStep("A", "proc", 1, True)
    step2 = ProcessStep("B", "wait", 2, False)
    step1.add_next(step2)
    assert len(step1.next_steps) == 1
    assert step1.next_steps[0] == step2