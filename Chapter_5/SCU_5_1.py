# Done by Carlos Amaral (2020/09/28)

sample_file = open("samplefile.txt", mode="r")

line_count = 0
for line in sample_file:
    line_count = line_count + 1


print(f"There are {line_count} lines of text in the file.")
