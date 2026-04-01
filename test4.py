def build_status_message(name: str, runs: int) -> str:
    return f"{name} test file executed successfully after {runs} run(s)."


if __name__ == "__main__":
    print("Running test4.py")
    print(build_status_message("Fourth", 1))
