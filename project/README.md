### Task Manager
## Video Demo: <URL https://www.youtube.com/watch?feature=shared&v=yhM6n0UrNYk>
## Description:
The Task Manager is a command-line application developed in Python to assist users in managing their daily tasks effectively. This program is designed to provide a simple yet powerful interface for users to add, complete, delete, and view tasks. The core idea behind this project is to help users stay organized and productive by allowing them to track their tasks and prioritize their workload.

## Key Features:
# Add Tasks: Users can easily add new tasks along with a unique task ID. This feature allows for efficient identification of tasks, making it easier to manage a growing list.

# Mark Tasks as Completed: When a task is finished, users can mark it as completed with a confirmation prompt. This feature not only keeps track of completed tasks but also provides a sense of accomplishment.

# Delete Tasks: The application allows users to delete tasks they no longer need. Before deletion, the user is prompted to confirm their choice, preventing accidental removal.

# View Completed Tasks: Users can view a list of all tasks marked as completed. This feature helps in keeping track of what has been accomplished and allows users to reflect on their productivity.

# View All In-Progress Tasks: The Task Manager provides a straightforward method for users to view all ongoing tasks. This functionality assists users in prioritizing tasks that require immediate attention.

## File Structure:
# project.py: This is the main file of the project where all the functionality resides. It contains the main function, which drives the program and calls other core functions. The user interface is defined here, guiding the user through the available actions.

# test_project.py: This file includes unit tests for the core functions of the Task Manager. Each function in the main program has a corresponding test function that verifies its correctness. The tests are designed to be run using pytest, ensuring the reliability of the application's functionality.

# requirements.txt: This file lists any third-party libraries required by the project. As the Task Manager is implemented using standard Python libraries, this file may remain empty or include specific versions of Python used for compatibility.

## Design Choices:
During the development of the Task Manager, several design choices were made to enhance usability and functionality. One key decision was to implement a command-line interface instead of a graphical user interface (GUI). This choice was made to simplify the application and make it accessible for users who may prefer working in terminal environments. Additionally, the use of a dictionary to manage tasks allows for efficient retrieval and manipulation of task data, making the program both fast and responsive.

# Another important aspect of the design was the incorporation of user prompts and confirmations. This design choice ensures that users are aware of their actions and prevents accidental deletions or incorrect task modifications, enhancing the overall user experience.

## Conclusion:
The Task Manager is a practical and user-friendly application that aims to improve task organization and management. By offering essential features and a simple interface, this project provides a valuable tool for anyone looking to enhance their productivity. The development of this project has not only solidified my understanding of Python programming but also improved my ability to design and implement user-centered applications.

### Feel free to explore the code, run the application, and start managing your tasks efficiently!
