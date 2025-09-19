"""Unit test for TodoService.add_item method."""

from src.service.service import TodoListService


def test__when_add_item__return_none():
    """Test adding an item to the todo list."""
    service = TodoListService()
    result = service.add_item("Test item")
    assert result is None


def test__when_add_item__item_exists():
    """Test that the item is actually added to the todo list."""
    service = TodoListService()
    service.add_item("Test item")
    assert "Test item" in service.list_all_items()
