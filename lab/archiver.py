def archiver(*args):
    result_array = bytearray()
    if args:
        for filename in args:
            current_path = 'files/' + filename
            print(filename)
            with open(current_path, 'rb') as current_file:
                contents = current_file.read()

            result_array.extend(
                bytearray(
                    (converter(filename, 2) + filename + converter(
                        len(contents), 10)).encode() + contents))

    with open('archive.txt', 'wb') as output:
        output.write(result_array)
    return result_array


def converter(name_or_contents, digits: int):
    if type(name_or_contents) == str:
        result = hex(len(name_or_contents))
    elif type(name_or_contents) == int:
        result = hex(name_or_contents)
    else:
        raise TypeError('Input is of type ', type(name_or_contents))

    while len(result) != 2 + digits:
        result = result[:2] + '0' + result[2:]

    return result


def exploder(archive: str):
    def _to_int(num: str) -> int:
        return int(num, 16)

    with open(archive, 'rb') as arch_file:
        data = arch_file.read()
        data_length = len(data)
        working_point = 0

        while working_point < data_length:
            begin_point = working_point
            working_point += 4
            name_length = _to_int(data[begin_point:working_point].decode())

            begin_point = working_point
            working_point += name_length
            filename = data[begin_point:working_point].decode()

            with open(filename, 'wb') as current_file:
                begin_point = working_point
                working_point += 12
                file_length = _to_int(data[begin_point:working_point].decode())

                begin_point = working_point
                working_point += file_length
                file_data = data[begin_point:working_point]
                current_file.write(file_data)

    return 0


archiver("test1", "test2", "test3", )
exploder("archive.txt")

