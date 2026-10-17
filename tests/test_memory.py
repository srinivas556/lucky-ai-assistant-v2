from src.memory.memory import Memory

def test_memory():
    memory = Memory()
    memory.add("test")
    assert memory.recent() == ["test"]
