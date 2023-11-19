# KeyManager

KeyManager is a password manager tool built in Python that uses the SHA-256 algorithm to securely store passwords. It allows you to generate strong passwords, customize their attributes, and manage your stored passwords with ease.

## Build and Execution Steps

### Prerequisites

- Python 3.x installed
- [PyInstaller](https://www.pyinstaller.org/) installed (`pip install pyinstaller`)

### Build Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/manishjoshieng/KeyManager.git
   cd KeyManager
   ```

2. Run the following command to build the executable:

   ```bash
   pyinstaller --onefile KeyManager.py
   ```

   This command will create a `dist` directory containing the executable file.

### Execution

1. Navigate to the `dist` directory:

   ```bash
   cd dist
   ```

2. Run the KeyManager executable:

   ```bash
   ./KeyManager
   ```

## Functionality

### Storing Passwords

The `KeyManager` main file, `KeyManager.py`, provides a function to securely store passwords using the SHA-256 algorithm and a master password.

### Password Generation

The password generator allows you to generate passwords with the following options:

- Length: Between 8 to 32 characters
- Customization: Include or exclude numbers, uppercase letters, lowercase letters, and special characters.

### Managing Stored Passwords

- View a list of stored passwords.
- Copy a password to the clipboard for easy use.
- Delete passwords when no longer needed.

## Usage

1. Run the executable as per the execution steps mentioned above.
2. Follow the on-screen instructions to store, generate, and manage passwords.

Feel free to explore the features and customize the settings to suit your needs!

## License

This project is licensed under the [MIT License](LICENSE).

---

Make sure to replace placeholders like `your-username` with your actual GitHub username and update the content as needed. Additionally, include the license file (e.g., `LICENSE`) in your project repository.
