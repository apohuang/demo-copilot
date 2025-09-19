"""Todo list management service."""

from src.model.entity import TodoItem


class TodoListService:
    """Service for managing a todo list."""

    __todo_items: dict[int, TodoItem]
    __next_id: int

    def __init__(self) -> None:
        self.__todo_items = {}
        self.__next_id = 1

    def __get_id(self) -> int:
        current_id = self.__next_id
        self.__next_id += 1
        return current_id

    def add_item(self, title: str) -> None:
        """Add a new todo item."""
        item_id = self.__get_id()
        new_item = TodoItem(id=item_id, title=title, completed=False)
        self.__todo_items[item_id] = new_item

    def list_all_items(self) -> str:
        """Get all todo items."""
        return "\n".join(str(item) for item in self.__todo_items.values())

    def delete_item(self, item_id: int) -> None:
        """Delete a todo item by ID."""
        if item_id in self.__todo_items:
            del self.__todo_items[item_id]

    def modify_item(self, item_id: int, new_title: str) -> None:
        """Modify a todo item by ID."""
        if item_id in self.__todo_items:
            self.__todo_items[item_id].title = new_title
