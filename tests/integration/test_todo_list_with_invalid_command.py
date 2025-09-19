"""Integration test for invalid command and ID scenarios."""

import io
from unittest.mock import patch
from src.main import main


def test_invalid_command_and_id_scenarios():
    """Test handling of invalid commands and IDs.

    -------------
    Run the integration test for the feature as following Gerkin syntax:
    -------------
    Feature: Invalid Input Handling
      As a user of the todo list application
      I want the application to handle invalid inputs gracefully
      So that I can recover from mistakes without the application crashing

      Scenario: Invalid command handling
        Given the todo list application is running
        When I enter an invalid command "invalid"
        Then the application should continue running
        And I should be prompted for the next command

      Scenario: Invalid ID handling for delete operation
        Given the todo list application is running
        And I have added a todo item
        When I enter the command "delete"
        And I enter an invalid ID "abc"
        Then I should see "Invalid ID. Please enter a number."
        And the application should continue running

      Scenario: Invalid ID handling for modify operation
        Given the todo list application is running
        And I have added a todo item
        When I enter the command "modify"
        And I enter an invalid ID "xyz"
        Then I should see "Invalid ID. Please enter a number."
        And the application should continue running

      Scenario: Non-existent ID for delete operation
        Given the todo list application is running
        When I enter the command "delete"
        And I enter a non-existent ID "999"
        Then I should see "Deleted todo item with ID: 999"
        And the application should continue running

      Scenario: Non-existent ID for modify operation
        Given the todo list application is running
        When I enter the command "modify"
        And I enter a non-existent ID "999"
        And I enter a new title "Updated title"
        Then the application should continue running
    """
    # Simulate user inputs for invalid scenarios
    user_inputs = [
        "invalid",  # Invalid command
        "add",  # Valid command to add an item
        "Test item",  # Todo item title
        "delete",  # Command: delete
        "abc",  # Invalid ID (not a number)
        "modify",  # Command: modify
        "xyz",  # Invalid ID (not a number)
        "delete",  # Command: delete
        "999",  # Non-existent ID
        "modify",  # Command: modify
        "999",  # Non-existent ID
        "Updated title",  # New title
        "exit",  # Command: exit
    ]

    # Capture stdout to verify outputs
    captured_output = io.StringIO()

    with patch("builtins.input", side_effect=user_inputs):
        with patch("sys.stdout", captured_output):
            main()

    output = captured_output.getvalue()

    # Verify the expected outputs from the scenario

    # Verify invalid command handling (application continues)
    # Note: The current implementation doesn't explicitly handle invalid commands
    # but the while loop continues, so it will prompt again

    # Verify item was added successfully
    assert 'Added todo item: "Test item"' in output

    # Verify invalid ID handling for delete
    assert "Invalid ID. Please enter a number." in output

    # Verify invalid ID handling for modify
    # The error message should appear twice (once for delete, once for modify)
    error_messages = [
        line
        for line in output.split("\n")
        if "Invalid ID. Please enter a number." in line
    ]
    assert len(error_messages) == 2

    # Verify non-existent ID handling for delete
    # Note: Current implementation doesn't check if ID exists before deletion
    assert "Deleted todo item with ID: 999" in output

    # Verify application exits properly
    assert "Exiting the application." in output

    # Verify the application didn't crash and completed all steps
    lines = output.strip().split("\n")
    exit_messages = [line for line in lines if "Exiting the application." in line]
    assert len(exit_messages) == 1


def test_invalid_command_recovery():
    """Test that the application recovers from invalid commands."""
    user_inputs = [
        "wrong",  # Invalid command
        "badcommand",  # Another invalid command
        "list",  # Valid command
        "exit",  # Exit
    ]

    captured_output = io.StringIO()

    with patch("builtins.input", side_effect=user_inputs):
        with patch("sys.stdout", captured_output):
            main()

    output = captured_output.getvalue()

    # Verify the application handled invalid commands gracefully
    assert "Todo List:" in output  # List command executed
    assert "Exiting the application." in output  # Application exited properly
