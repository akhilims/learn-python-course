def error_share(levels):
    errors = levels.count("ERROR")
    return errors / len(levels) * 100

if __name__ == "__main__":
    lvl = ["ERROR", "INFO", "ERROR", "WARN"]
    print(error_share(lvl))
