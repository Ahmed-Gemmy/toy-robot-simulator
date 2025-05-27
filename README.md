# Toy Robot Simulator

This is a command-line simulator for a toy robot moving on a 5x5 table. It is designed as a technical test with clean, production-grade Python code using TDD, modular architecture, and clear command parsing.

---

##  Features

- Supports `PLACE X,Y,F`, `MOVE`, `LEFT`, `RIGHT`, and `REPORT` commands
- Robot cannot fall off the table (safety enforced)
- Ignores invalid or malformed commands
- Modular and testable design using classes and the Command Pattern
- Fully tested with unit, and end-to-end tests

---

##  How to Run

### From a File

Prepare a text file with one command per line (e.g., `commands.txt`):

```
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT
```

Then run:

```bash
python main.py commands.txt
```

You should see:

```
3,3,NORTH
```

---

##  Project Structure

```
.
├── main.py                # CLI entry point
├── simulator.py           # Coordinates command execution and robot interaction
├── robot.py               # Core robot logic: placement, movement, turning, reporting
├── table.py               # Defines and validates the 5x5 table grid
├── direction.py           # Direction enum with left/right rotation logic
├── position.py            # Dataclass for representing positions (x, y)
├── .coveragerc            # Coverage configuration
├── .gitignore             # Git ignore rules
├── README.md              # Project documentation

├── command/               # Command Pattern implementation
│   ├── base.py            # Abstract Command interface
│   ├── factory.py         # Parses string input into Command objects
│   ├── left.py            # Turn robot left
│   ├── right.py           # Turn robot right
│   ├── move.py            # Move robot forward
│   ├── place.py           # Place robot at a position and direction
│   ├── report.py          # Output robot's position and direction
│   └── __init__.py

├── examples/              # Predefined command sequences for manual testing
│   ├── example_a.txt
│   ├── example_b.txt
│   ├── example_c.txt
│   ├── edge_block.txt
│   └── invalid_start.txt

├── tests/                 # Unit and integration test suite
│   ├── test_end_to_end.py       # Full scenario tests
│   ├── test_simulator.py
│   ├── test_robot.py
│   ├── test_position.py
│   ├── test_table.py
│   ├── test_direction.py
│   ├── test_command/
│   │   ├── __init__.py
│   │   ├── test_command_factory.py
│   │   ├── test_left_command.py
│   │   ├── test_move_command.py
│   │   ├── test_place_command.py
│   │   ├── test_report_command.py
│   │   └── test_right_command.py
│   └── __init__.py
```
---

##  Run Tests

To run the full test suite:

```bash
python -m unittest discover tests
```

---

##  Test Coverage

To check how much of the code is exercised by tests:

### 1. Install `coverage` (if not already installed)
```bash
pip install coverage
```

### 2. Run your tests with coverage tracking using the config file
```bash
coverage run --rcfile=.coveragerc -m unittest discover tests
```

### 3. Show coverage summary in terminal
```bash
coverage report
```

### 4. (Optional) Generate HTML report
```bash
coverage html
```

Then open `htmlcov/index.html` in your browser to view a detailed breakdown.

---

##  Notes

- The first valid command **must** be `PLACE`. All command before the first `PLACE` are ignored.
- `REPORT` prints the robot's current position and direction (e.g., `3,3,NORTH`)
- Direction is case-insensitive (`north`, `NORTH`, etc.)
- Any command that would result in falling off the table is ignored
- History of commands is not tracked or saved. This could be added later.
---

---

###  Design Patterns Used

This project applies several object-oriented design patterns to ensure maintainability, clarity, and extensibility:

- **Command Pattern**  
  Each robot command (`MOVE`, `LEFT`, `RIGHT`, `PLACE`, `REPORT`) is implemented as a separate class with a unified `execute(robot)` interface. This makes the system easy to extend with new commands.

- **Factory Pattern**  
  `CommandFactory` parses raw input strings and constructs the appropriate `Command` object. This centralizes parsing logic and cleanly separates concerns.

- **Strategy-like Encapsulation**  
  The robot’s behaviors (`move`, `turn`, `report`) are encapsulated as method calls, allowing different commands to invoke them independently. Direction rotation logic is also encapsulated for clarity.

- **Enum and Data Class Usage**  
  `Direction` is implemented as an `Enum` for safe, structured state. `Position` is a `dataclass`, used for clear and immutable coordinate representation.
