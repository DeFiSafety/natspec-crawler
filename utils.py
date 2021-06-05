
def count_occurences(filename: str, string_to_find: str) -> int:
    occurences = 0
    try:
        
        with open(filename, 'r') as myfile:
            for line in myfile:
                filetext = ''.join(line.split())
                # TODO: add handling for multiple occurences
                # of a string in one line

                if string_to_find in filetext:
                    occurences += 1

        return occurences

    except:
        raise Exception(f'Cannot read file {filename} as .sol file.')
