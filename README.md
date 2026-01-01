# password_generator
A secure, command-line tool for generating strong passwords and managing them locally. Built with Python, it supports customizable password options and logs actions for accountability. Perfect for developers and security-conscious users
# Secure Password Generator & Manager CLI

A simple, secure command-line interface (CLI) tool for generating strong, customizable passwords and managing them locally. Built with Python, it uses cryptographically secure random generation and stores passwords in a JSON file for easy retrieval. Ideal for developers, sysadmins, or anyone needing quick, secure password creation without relying on online tools.

## Features

- **Password Generation**: Create passwords with customizable length, uppercase letters, digits, and symbols.
- **Secure Randomness**: Uses Python's `secrets` module for cryptographically strong randomness.
- **Local Storage**: Saves passwords to a JSON file (`passwords.json`) with timestamps.
- **Logging**: Logs all actions (e.g., generation, display) to a text file (`logs.txt`) for auditing.
- **CLI Interface**: Easy-to-use command-line arguments for all operations.
- **Modular Code**: Organized into separate files for maintainability (e.g., config, logging, storage, generation).

## Installation

### Prerequisites
- Python 3.6 or higher (required for the `secrets` module).
- No external dependencies—uses only Python's standard library.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/password-manager-cli.git
   cd password-manager-cli

