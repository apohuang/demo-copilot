"""Domain entities."""

from pydantic import BaseModel


class TodoItem(BaseModel):
    """A todo item entity."""

    id: int
    title: str
    completed: bool
