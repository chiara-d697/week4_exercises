pelican = open("pelican.txt", "a")

pelican.write("A wonderful bird is the pelican,\n")

pelican.write("His bill holds more than his belican.\n")

lines = ["He can take in his beak,\n", "Enough food for a week,\n", "But I’m damned if I see how the helican.\n"]

pelican.writelines(lines)