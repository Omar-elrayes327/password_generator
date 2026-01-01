import argparse
from datetime import datetime
from logger import log_action
from password_store import load_passwords, save_passwords
from password_generator import generate_password

def main():
    parser = argparse.ArgumentParser(
        description="Secure Password Generator & Manager CLI"
    )

    parser.add_argument("--service", type=str, required=True,
                        help="Service name (e.g., Gmail, GitHub)")

    parser.add_argument("-l", "--length", type=int, default=12)
    parser.add_argument("--upper", action="store_true")
    parser.add_argument("--digits", action="store_true")
    parser.add_argument("--symbols", action="store_true")

    parser.add_argument("--show", action="store_true",
                        help="Show saved passwords")

    args = parser.parse_args()

    passwords = load_passwords()

    if args.show:
        for service, info in passwords.items():
            print(f"{service}: {info['password']}")
        log_action("Displayed stored passwords")
        return

    password = generate_password(
        args.length,
        args.upper,
        args.digits,
        args.symbols
    )

    passwords[args.service] = {
        "password": password,
        "created_at": str(datetime.now())
    }

    save_passwords(passwords)
    log_action(f"Generated password for {args.service}")

    print(f"Password for {args.service}: {password}")

if __name__ == "__main__":
    main()