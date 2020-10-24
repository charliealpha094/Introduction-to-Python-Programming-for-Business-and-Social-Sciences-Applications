# Done by Carlos Amaral (2020/10/03)

# SCU 5.4 - Write Text to a File

sample_file = open("samplefile.txt", mode="r")

line_count = 0
for line in sample_file:
    line_count = line_count + 1

sample_file_info = open("samplefileinfo.txt", mode = "w")

sample_file_info.write(f"There are {line_count} lines of text in the file.")

sample_file_info.close()