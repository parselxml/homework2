files = ['1.txt', '2.txt', '3.txt']

count_lines = []

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        stripped_lines = [line.lstrip() for line in lines]
        count_lines.append((file, len(stripped_lines), stripped_lines))

def sort_by_line_count(file_data):
    return file_data[1]

count_lines.sort(key=sort_by_line_count)

with open('result.txt', 'w', encoding='utf-8') as result_file:
    for file_name, line_count, lines in count_lines:
        result_file.write(f"{file_name}\n")
        result_file.write(f"{line_count}\n")
        result_file.writelines(lines)
        result_file.write('\n')

