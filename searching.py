import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
    if field in set(data.keys()):
        return data[field]


def linear_search(sequence, number):
    num_of_apperances = 0
    idxes = []
    for idx in range(0, len(sequence)):
        if sequence[idx] == number:
            num_of_apperances += 1
            idxes.append(idx)
    output = {"idxes": idxes, "num_of_apperances": num_of_apperances}
    return output


def pattern_search(sequence, pattern):
    idxes = []
    for idx in range(0, (len(sequence) - (len(pattern) -1))):
        idx_sequence = idx
        counter = 0
        """for idx_pattern in range(0, len(pattern)):
            if sequence[idx_sequence] == pattern[idx_pattern]:
                counter += 1
                idx_sequence += 1"""
        for idx_pattern in range(0, len(pattern)):
            if sequence[idx_sequence] != pattern[idx_pattern]:
                break
            counter += 1
            idx_sequence += 1
        if counter == len(pattern):
            idxes.append(idx)
    output = set(idxes)
    return output


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    print(linear_search(sequential_data, 8))
    dna_data = read_data("sequential.json", "dna_sequence")
    print(dna_data)
    num_of_patterns = pattern_search(dna_data, "GCA")
    print(num_of_patterns)


if __name__ == '__main__':
    main()
