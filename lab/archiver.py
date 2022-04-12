def archiver(*args):
    result_array = bytearray()
    if args:
        for filename in args:
            current_path = 'files/' + filename
            print(filename)
            with open(current_path, 'rb') as current_file:
                contents = current_file.read()

            result_array.extend(
                bytearray((converter(filename, 2) + filename + converter(
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


def exploder(archive):
    with open(archive, 'rb') as archived_file:
        contents = archived_file.read()
        finish_line = len(contents)
        progress = 0

        while progress < finish_line:
            begin_point = progress
            progress += 4
            name_length = int((contents[begin_point:progress].decode()), 16)

            begin_point = progress
            progress += name_length
            filename = contents[begin_point:progress].decode()

            with open(filename, 'wb') as current_file:
                begin_point = progress
                progress += 12
                file_length = int((contents[begin_point:progress].decode()), 16)

                begin_point = progress
                progress += file_length
                file_data = contents[begin_point:progress]
                current_file.write(file_data)

    return 0


archiver("QOTD", "Oz", "flirt", )
exploder("archive.txt")
