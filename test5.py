def summarize_values(values: list[int]) -> str:
    total = sum(values)
    average = total / len(values)
    return f"values={values} total={total} average={average:.2f}"


if __name__ == "__main__":
    sample_values = [5, 10, 15]
    print("Running test5.py")
    print(summarize_values(sample_values))
