import os
import re
from pathlib import Path

def get_readme_data():
    """
    Reads a README file and formats it according to specified rules.

    Parameters:
    filepath (str): Path to the README file.

    Returns:
    str: The formatted content of the README file.
    """
    with open('problem_description.txt', 'r') as file:
        lines = file.readlines()

    # Process the main content
    cleaned_lines = []
    for line in lines:
        if line.strip():
            cleaned_lines.append(line.strip())
        elif cleaned_lines and cleaned_lines[-1]:
            cleaned_lines.append(line.strip())

    add_new_lines = []
    add_code_tags = False
    # Add a newline before each 'Example #' except 'Example 1:'
    for line in cleaned_lines:
        if line == 'Example 1:':
            add_new_lines.append('### ' + line)
            add_code_tags = True
        elif re.match(r'^Example \d+:', line):
            add_new_lines.append('```')
            add_new_lines.append('')
            add_new_lines.append('### ' + line)
            add_code_tags = True
        elif re.match(r'Constraints:', line):
            add_new_lines.pop()
            add_new_lines.append('```')
            add_new_lines.append('')
            add_new_lines.append('### ' + line)
            add_code_tags = True
        else:
            add_new_lines.append(line)
            if add_code_tags:
                add_new_lines.append('```')
                add_code_tags = False

    add_new_lines.append('```')
    text = '\n'.join(add_new_lines)
    text += '\n\n## Code\n\n```python\n\n```'
    return text

def list_directories(path):
    """Return a list of directories in the given path."""
    return [entry for entry in path.iterdir() if entry.is_dir()]

def choose_directory(path):
    """Display directories in the current path and let user choose one."""
    while True:
        directories = list_directories(path)
        if not directories:
            print(f"No directories to display")
        else:
            # Display directories with numbers
            print(f"\nCurrent Directory: {path}")
            for i, dir in enumerate(directories, 1):
                print(f"{i}. {dir.name}")
        print("b. Go back to the parent directory")
        print("Press Enter to create a new directory")

        # Get user choice
        choice = input("Choose a directory (number), b to go back, or press Enter to create a new directory: ")

        if choice == 'b':
            return None  # Return None to go back to the parent directory
        elif choice.isdigit() and 1 <= int(choice) <= len(directories):
            chosen_directory = directories[int(choice) - 1]
            return chosen_directory  # Return the chosen directory to navigate into
        elif choice == '':
            create_directory(path)  # Call the function to create a new directory
            break  # Exit the loop after creating a directory
        else:
            print("Invalid choice. Please choose a valid number or 'b' to go back.")

def create_directory(path):
    """Prompt the user to create a new directory in the given path."""
    dir_name = input(f"Enter the name of the new directory to create in {path}: ")
    new_dir = path / dir_name
    if not new_dir.exists():
        new_dir.mkdir()
        print(f"Directory '{dir_name}' created at {new_dir}.")
        create_readme(new_dir)
    else:
        print(f"Directory '{dir_name}' already exists.")

def create_readme(path):
    """Prompt the user for the readme contents."""    
    # Now create the README.md file inside the new directory
    title = input('Title: ')
    link = input('Link: ')
    
    readme_header = f"# {title}\n{link}\n\n"
    readme_path = path / 'README.md'
    readme_data = get_readme_data()
    
    with open(readme_path, 'w') as readme_file:
        readme_file.write(readme_header)
        readme_file.write(readme_data)
        
    print(f"README.md file created in {path}.")

def main():
    current_path = Path('..')  # Start in the current working directory
    while True:
        chosen_directory = choose_directory(current_path)
        
        if chosen_directory is None:
            current_path = current_path.parent  # Go back to the parent directory
            if current_path == Path('..'):  # If we reach the root directory, stop
                print("Outside leetcode directory. Exiting.")
                break
        else:
            current_path = chosen_directory  # Change to the selected directory
    
if __name__ == "__main__":
    main()