"""Domain entities."""

from typing import TypedDict


class TodoItem(TypedDict):
    """A todo item entity."""

    id: int
    title: str
    completed: bool
