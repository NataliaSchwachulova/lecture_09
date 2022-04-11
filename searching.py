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


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    print(linear_search(sequential_data, 9))


if __name__ == '__main__':
    main()
