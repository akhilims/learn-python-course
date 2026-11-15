def error_share(levels):
    errors = levels.count("ERROR")
    return errors / len(levels) * 100

print(error_share([]))
