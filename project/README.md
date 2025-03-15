# Task Manager

## Video Demo: 
[Watch the Demo](https://www.youtube.com/watch?feature=shared&v=yhM6n0UrNYk)

## Description:
The Task Manager is a command-line application developed in Python to help users manage their daily tasks effectively. This program provides a simple yet powerful interface that allows users to add, complete, delete, and view tasks. The core idea behind this project is to enhance productivity by providing an organized way to track tasks and prioritize workloads.

## Key Features:
- **Add Tasks**: Easily add new tasks, each with a unique task ID. This feature enables efficient task management and helps users keep track of their growing list of tasks.
- **Mark Tasks as Completed**: When a task is finished, users can mark it as completed with a confirmation prompt. This provides a sense of accomplishment while keeping track of completed tasks.
- **Delete Tasks**: Users can delete tasks they no longer need. Before deletion, a confirmation prompt ensures tasks are not accidentally removed.
- **View Completed Tasks**: View a list of all completed tasks to reflect on accomplishments and track productivity.
- **View All In-Progress Tasks**: Quickly view all ongoing tasks to prioritize items that need immediate attention.

## File Structure:
- `project.py`: This is the main file where all functionality resides. It contains the main function, which drives the program and invokes core functions. The user interface is defined here, guiding users through the available actions.
- `test_project.py`: This file includes unit tests for the core functions of the Task Manager. Each function in the main program has a corresponding test function that ensures its correctness. The tests can be run using `pytest`, ensuring the reliability of the application's functionality.
- `requirements.txt`: This file lists any third-party libraries required by the project. Since the Task Manager is implemented using standard Python libraries, this file may remain empty or specify the version of Python used for compatibility.

## Design Choices:
During the development of the Task Manager, several design choices were made to enhance usability and functionality. One key decision was to implement a command-line interface (CLI) instead of a graphical user interface (GUI). This choice was made to simplify the application and make it accessible for users who prefer working in terminal environments. Additionally, a dictionary was used to manage tasks, allowing for efficient retrieval and manipulation of task data, making the program both fast and responsive.

Another important design aspect was the use of user prompts and confirmations. This ensures that users are aware of their actions, preventing accidental deletions or incorrect task modifications, and improving the overall user experience.

## Conclusion:
The Task Manager is a practical and user-friendly application that aims to improve task organization and management. By offering essential features and a simple interface, this project provides a valuable tool for anyone looking to enhance their productivity. The development of this project has not only solidified my understanding of Python programming but also enhanced my ability to design and implement user-centered applications.

### Feel free to explore the code, run the application, and start managing your tasks efficiently!
