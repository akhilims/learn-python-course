# Find What Broke the Website: datetime and collections
# Every cell of the notebook, in order, as one script (run: python Find_What_Broke_the_Website__datetime_and_collecti.py)

# Reading log times with datetime.strptime

from datetime import datetime
fmt = '%Y-%m-%d %H:%M:%S'
text = '2026-11-13 21:05:12'
t = datetime.strptime(text, fmt)
print(t.hour)
print(t.weekday())

# Subtracting and comparing times

text2 = '2026-11-13 21:45:30'
later = datetime.strptime(text2, fmt)
print(later - t)
print(later > t)

# timedelta and strftime: add time, format time

from datetime import timedelta
print(t + timedelta(minutes=30))
print(t.strftime('%H:%M'))

# Counter and most_common: count the log levels

from collections import Counter
levels = ['ERROR', 'INFO', 'WARN']
levels += ['ERROR', 'INFO', 'ERROR']
counts = Counter(levels)
print(counts)
print(counts.most_common(1))

# defaultdict: group log messages by level

from collections import defaultdict
bylevel = defaultdict(list)
rows = [('ERROR', 'payment timeout')]
rows += [('INFO', 'order saved')]
rows += [('ERROR', 'database locked')]
for lvl, msg in rows:
    bylevel[lvl].append(msg)
print(dict(bylevel))

# deque with maxlen: keep the last 3 log lines

from collections import deque
times = ['21:12:55', '21:35:12']
times += ['21:45:30']
last = deque(times, maxlen=3)
last.append('22:02:10')
print(list(last))

# namedtuple: name the places of a tuple

from collections import namedtuple
fields = ['time', 'level']
Entry = namedtuple('Entry', fields)
e = Entry('21:05:12', 'ERROR')
print(e.level)
print(e)
