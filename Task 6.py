# Реализуйте функцию которая умеет работать с файлами
# (читать из заданного файла, записывать в заданный файл).
# Программа считает количество строк, слов и букв в заданном файле
# и дописывает эту информацию обратно в файл,
# так же выводит эту информацию на экран.

def funny_file_reader_writer(example_file):

    with open(example_file, "r") as file:
        lines, words, chars = 0, 0, 0
        for line in file.readlines():
            lines += 1
            words += len(line.split())
            chars += len(line)

    with open(example_file, "a") as file:
        file.write(f"\nSummary: "
                   f"\n"
                   f"{lines} lines, {words} words, {chars} letters")


print(funny_file_reader_writer("file_to_read.txt"))
