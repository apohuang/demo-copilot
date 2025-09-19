from src.service.service import TodoListService

"""Unit tests for TodoListService.delete_item method."""


def test__when_delete_existing_item__returns_none():
    """Test that delete_item returns None when deleting an existing item."""
    service = TodoListService()
    service.add_item("Test item")
    result = service.delete_item(1)
    assert result is None


def test__when_delete_existing_item__item_removed():
    """Test that the item is actually removed from the todo list."""
    service = TodoListService()
    service.add_item("Test item")
    service.delete_item(1)
    result = service.list_all_items()
    assert "Test item" not in result
    assert result == ""


def test__when_delete_nonexistent_item__returns_none():
    """Test that delete_item returns None when trying to delete a non-existent item."""
    service = TodoListService()
    result = service.delete_item(999)
    assert result is None


def test__when_delete_from_multiple_items__only_specified_item_removed():
    """Test that only the specified item is removed when multiple items exist."""
    service = TodoListService()
    service.add_item("First item")
    service.add_item("Second item")
    service.add_item("Third item")
    service.delete_item(2)
    result = service.list_all_items()
    assert "First item" in result
    assert "Second item" not in result
    assert "Third item" in result
    lines = result.splitlines()
    assert len(lines) == 2


def test__when_delete_all_items__list_becomes_empty():
    """Test that deleting all items results in an empty list."""
    service = TodoListService()
    service.add_item("First item")
    service.add_item("Second item")
    service.delete_item(1)
    service.delete_item(2)
    result = service.list_all_items()
    assert result == ""
