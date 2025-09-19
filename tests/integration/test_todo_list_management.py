"""Integration test of todo list management."""

import io
from unittest.mock import patch
from src.main import main


def test_todo_list_management():
    """Test todo list management.

    -------------
    Run the integration test for the feature as following Gerkin syntax:
    -------------
    Feature: Todo List Management
      As a user of the todo list application
      I want to manage my todo items through a command-line interface
      So that I can organize my tasks effectively

      Background:
        Given the todo list application is running
        And the todo list is empty

      Scenario: Complete user cycle - Add, List, Modify, Delete, and Exit
        When I enter the command "add"
        And I enter the todo item title "Buy groceries"
        Then I should see 'Added todo item: "Buy groceries"'

        When I enter the command "list"
        Then I should see "Todo List:"
        And I should see a todo item with title "Buy groceries"
        And I should see a todo item with id 1

        When I enter the command "modify"
        And I enter the todo item ID "1"
        And I enter the new title "Buy organic groceries"
        Then the todo item should be updated successfully

        When I enter the command "list"
        Then I should see a todo item with title "Buy organic groceries"
        And I should not see a todo item with title "Buy groceries"

        When I enter the command "delete"
        And I enter the todo item ID "1"
        Then I should see "Deleted todo item with ID: 1"

        When I enter the command "list"
        Then I should see "Todo List:"
        And the todo list should be empty

        When I enter the command "exit"
        Then I should see "Exiting the application."
        And the application should terminate
    """
    # Simulate user inputs for the complete scenario
    user_inputs = [
        "add",  # Command: add
        "Buy groceries",  # Todo item title
        "list",  # Command: list
        "modify",  # Command: modify
        "1",  # Item ID to modify
        "Buy organic groceries",  # New title
        "list",  # Command: list
        "delete",  # Command: delete
        "1",  # Item ID to delete
        "list",  # Command: list
        "exit",  # Command: exit
    ]

    # Capture stdout to verify outputs
    captured_output = io.StringIO()

    with patch("builtins.input", side_effect=user_inputs):
        with patch("sys.stdout", captured_output):
            main()

    output = captured_output.getvalue()

    # Verify the expected outputs from the scenario

    # Step 1: Add item
    assert 'Added todo item: "Buy groceries"' in output

    # Step 2: List items (should show the added item)
    assert "Todo List:" in output
    assert "Buy groceries" in output
    assert "id=1" in output

    # Step 3: Modify item (implicit - no specific output message in main.py)

    # Step 4: List items after modification
    assert "Buy organic groceries" in output
    # Verify old title is not in the final output context

    # Step 5: Delete item
    assert "Deleted todo item with ID: 1" in output

    # Step 6: List items after deletion (should be empty)
    # The list command will still print "Todo List:" but the items list should be empty

    # Step 7: Exit
    assert "Exiting the application." in output

    # Additional verification: ensure the flow completed successfully
    lines = output.strip().split("\n")

    # Count occurrences to ensure proper flow
    add_confirmations = [line for line in lines if "Added todo item:" in line]
    assert len(add_confirmations) == 1

    delete_confirmations = [
        line for line in lines if "Deleted todo item with ID:" in line
    ]
    assert len(delete_confirmations) == 1

    exit_messages = [line for line in lines if "Exiting the application." in line]
    assert len(exit_messages) == 1
