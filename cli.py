# cli.py
import argparse
from angkor import run

def main():
    parser = argparse.ArgumentParser(description="AngkorCMS Server CLI")
    parser.add_argument('command', help='Command to execute (e.g., run)')

    args = parser.parse_args()

    if args.command == 'run':
        run()
    else:
        print(f"Unknown command: {args.command}")

if __name__ == '__main__':
    main()
