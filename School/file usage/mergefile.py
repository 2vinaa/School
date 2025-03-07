def mergefile(file1, file2, newfilename, interleaved=False):
    with open(file1) as file_1:
        with open(file2) as file_2:
            with open(newfilename, "w+") as newfile_name:
                if not interleaved:
                    file_merge(file_1,file_2, newfile_name)
                    return newfile_name
                else:
                    alt_merge(file_1, file_2, newfile_name)
                    return newfile_name

def file_merge(file_1, file_2, newfile_name):
    for line in file_1:
        newfile_name.write(line)

    for line in file_2:
        newfile_name.write(line)

def alt_merge(file_1, file_2, newfile_name):
    line_1 = 0
    line_2 = 0
    while line_1 != "" or line_2 != "":
        line_1 = file_1.readline()
        newfile_name.write(line_1)
        line_2 = file_2.readline()
        newfile_name.write(line_2)


if __name__ == "__main__":

    x = mergefile("text_file_merge_file1.txt", "text_file_merge_file2.txt", "merged_file.txt", True)

    
