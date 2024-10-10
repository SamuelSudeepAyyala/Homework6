# Homework5

This repository demonstrates different functionalities split across multiple branches. The project includes a plugin-based command handling system and individual command implementations in separate branches.

## Branches

### 1. **master**
   The main branch of this repository, which contains the base code without the plugin system or command implementations. If you're looking for the core project structure, check out this branch.

### 2. **development**
   This branch contains work-in-progress code and features that are under active development. New functionalities or fixes are tested here before merging into the `master`.

### 3. **plugins**
   This branch contains the implementation of a **plugin system**. The plugin system allows commands to be loaded dynamically, making the project extensible and modular. If you're interested in the plugin architecture, switch to this branch.

   To check out this branch:

   ```bash
   git checkout plugins
   ```

### 4. **commands**
   This branch focuses on the **command classes** implementation, such as the `AddCommand`, which performs the addition of two numbers. If you are interested in how individual commands are structured and implemented, explore this branch.

   To check out this branch:

   ```bash
   git checkout commands
   ```

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/SamuelSudeepAyyala/Homework5.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Homework5
    ```

3. Checkout the desired branch (e.g., `plugins` or `commands`) based on your area of interest.

    ```bash
    git checkout commands
    ```

4. **Run the main Python file:**
    ```bash
    python main.py
    ```

5. **Execute a command:**
    The program will prompt for user input. For example, to add two numbers:
    ```
    Type 'menu' to show menu
    Type 'exit' to exit 
    >>> menu
    Welcome to the Basic Calcualator.
    Select the operation to be performed
    Add
    Subtract
    Multiply
    Divide
    >>> add
    Enter two space-seperated numbers: 23 2
    Addition result: 25
    ```


## Usage

To run the project (based on the branch you're on):

```bash
python main.py
```

To run tests:

```bash
pytest
pytest --pylint
pytest --pylint --cov
```
