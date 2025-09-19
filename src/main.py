"""A Simple Todo list Application."""

from src.service.service import TodoListService


def main() -> None:
    todo_list_service = TodoListService()

    while True:
        command = input("Enter command (add/list/delete/modify/exit): ").strip().lower()
        if command == "add":
            title = input("Enter todo item title: ").strip()
            todo_list_service.add_item(title)
            print(f'Added todo item: "{title}"')

        elif command == "list":
            print("Todo List:")
            print(todo_list_service.list_all_items())

        elif command == "delete":
            try:
                item_id = int(input("Enter todo item ID to delete: ").strip())
                todo_list_service.delete_item(item_id)
                print(f"Deleted todo item with ID: {item_id}")
            except ValueError:
                print("Invalid ID. Please enter a number.")

        elif command == "modify":
            try:
                item_id = int(input("Enter todo item ID to modify: ").strip())
                new_title = input("Enter new title: ").strip()
                todo_list_service.modify_item(item_id, new_title)
            except ValueError:
                print("Invalid ID. Please enter a number.")

        elif command == "exit":
            print("Exiting the application.")
            break


if __name__ == "__main__":
    main()
