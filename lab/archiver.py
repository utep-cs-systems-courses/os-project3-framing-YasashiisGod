def archiver(*args):
    result_array = bytearray()
    if args:
        for filename in args:
            current_path = 'files/' + filename
            print(filename)
            with open(current_path, 'rb') as current_file:
                contents = current_file.read()

            result_array.extend(
                bytearray((converter(filename, 2) + filename + converter(len(contents), 10)).encode() + contents))

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


archiver("test1", "test2", "test3", )
