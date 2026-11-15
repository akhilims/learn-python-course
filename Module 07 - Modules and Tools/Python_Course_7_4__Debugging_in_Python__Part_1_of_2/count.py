def count_errors(lines):
    total = 0
    for line in lines:
        if "ERROR" in line:
            total = 1
    return total

print(count_errors(["ERROR a", "INFO b", "ERROR c"]))
