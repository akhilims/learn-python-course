# Log Tool with argparse - Part 2
# Every cell of the notebook, in order, as one script (run: python Log_Tool_with_argparse_-_Part_2.py)

# Create logcheck.py: choices, option, switch, exit code

# Run it: too many errors gives exit code 1

# The --max option changes the limit

# The --short switch: only the number

# Scripted arguments: call main from code

from logcheck import main
print(main(["ERROR"]))
print(main(["ERROR", "--max", "5"]))
