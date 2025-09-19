from src.service.service import TodoListService

"""Unit tests for TodoListService methods."""


def test__when_no_items__returns_empty_string():
    """Test that list_all_items returns an empty string when there are no items."""
    service = TodoListService()
    result = service.list_all_items()
    print(result)
    assert result == ""


def test__when_one_item_added__returns_item_string():
    """Test that list_all_items returns the string of the single added item."""
    service = TodoListService()
    service.add_item("Test item")
    result = service.list_all_items()
    assert "Test item" in result
    assert isinstance(result, str)
    assert len(result.splitlines()) == 1


def test__when_multiple_items_added__returns_all_items():
    """Test that list_all_items returns all items, each on a new line."""
    service = TodoListService()
    service.add_item("First item")
    service.add_item("Second item")
    result = service.list_all_items()
    assert "First item" in result
    assert "Second item" in result
    lines = result.splitlines()
    assert len(lines) == 2
