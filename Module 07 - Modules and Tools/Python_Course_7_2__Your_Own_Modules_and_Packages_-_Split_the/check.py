from count import count_levels

lines = [
"2026-11-13 21:05:12 ERROR payment timeout",
"2026-11-13 21:12:55 INFO checkout opened",
"2026-11-13 21:35:12 ERROR database locked",
]
print(count_levels(lines))
