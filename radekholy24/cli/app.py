from argparse import ArgumentParser


def main():
    """Run the application."""
    parse_arguments()


def parse_arguments():
    """Parse the command line arguments."""
    parser = ArgumentParser(add_help=False)
    parser.parse_args()
