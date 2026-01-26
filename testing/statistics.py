class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    RESET = '\033[0m'
print(Colors.RED + "This text is red." + Colors.RESET)
print(f"{Colors.GREEN}This text is green.{Colors.RESET}")