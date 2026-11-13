# Text analyser project
# Every cell of the notebook, in order, as one script (run: python Text_analyser_project.py)

# Text analyser project: the longest word helper

text = "the quick brown fox"
def word_count(text):
    return len(text.split())
def longest_word(text):
    """Return the longest word."""
    return max(text.split(), key=len)

# Python recursion on text: reverse a string

def reverse(s):
    if s == "":
        return ""
    return reverse(s[1:]) + s[0]
print(reverse("abc"))

# Text analyser project: run all three helpers

print("Words:", word_count(text))
print("Longest:", longest_word(text))
print("Reversed:", reverse(text))
