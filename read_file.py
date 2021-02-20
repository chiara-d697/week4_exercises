# create handle on file
handle = open("pelican.txt", "r")
pelican = handle.read()
print(type(pelican))
print(pelican)

# use context manager to open file and save individual lines into a list
with open("pelican.txt", "r") as handle:
    lines = handle.readlines()

print(lines)
print(len(lines))

# print each line in the file
for line in open("pelican.txt"):
    print(line, end="")