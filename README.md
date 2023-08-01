# Banking System Simulation

This project is a simple banking system simulation that allows users to create accounts, perform deposits and withdrawals, and view transaction logs and account statements.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Banking System Simulation is built in Python and uses object-oriented programming principles to model the behavior of bank accounts, customers, and a simple banking system. The project uses classes to represent different entities and their interactions, such as `Account`, `Customer`, and `Bank`.

## Features

- Create and manage bank accounts for customers.
- Perform deposits and withdrawals on accounts.
- Generate transaction logs for each account.
- Generate monthly statements for accounts.
- Simple banking system that allows customers to interact with their accounts.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/VictorApaez/banking-system.git

```

2. Navigate to the project folder:

```bash
cd bank-app-python

```

3. Set up a virtual environment (optional but recommended):

```bash
python -m venv env
```

4. Activate the virtual environment (optional but recommended):

**On Linux/macOS**:

```bash
source env/bin/activate
```

**On Windows**:

```bash
env\Scripts\activate
```

5. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the banking system simulation, execute the `main.py` script:

```bash
python main.py
```

The script will present a simple command-line interface (CLI) that allows you to interact with the banking system. Follow the on-screen instructions to create accounts, perform transactions, and view transaction logs and account statements.

## Testing

The project includes test cases to ensure the correctness of the implemented classes and functionalities. To run the tests, use the following command:

```bash
python -m pytest tests/
```

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License

---

Feel free to customize this README to include more details about your specific project, such as additional features, implementation details, or how to contribute to the project. Make sure to update the installation and usage instructions if your project requires any specific setup or configurations.
