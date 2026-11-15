import argparse

parser = argparse.ArgumentParser()
parser.add_argument("level")
args = parser.parse_args()

text = open("server.log").read()
print(args.level, text.count(args.level))
