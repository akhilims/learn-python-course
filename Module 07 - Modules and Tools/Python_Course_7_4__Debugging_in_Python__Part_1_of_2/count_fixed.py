import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(message)s",
)

def count_errors(lines):
    total = 0
    for line in lines:
        if "ERROR" in line:
            total = total + 1
            logging.info("error number %s", total)
    return total

sample = ["ERROR a", "INFO b", "ERROR c"]
print(count_errors(sample))
