
from typing import List, Tuple, Dict, Optional, Union, Callable

def greet(name: str, age: int) -> str:
    return f"Hello, {name}! You are {age} years old."

print(greet.__annotations__)

class Person:
    name: str
    age: int

print(Person.__annotations__)

def process_data(items: List[int], mapping: Dict[str, int]) -> Tuple[int, int]:
    return sum(items), len(mapping)

def get_user_name(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Alice"
    return None

def add(x: Union[int, float], y: Union[int, float]) -> float:
    return x + y

def execute(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)
