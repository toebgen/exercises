import random

file_name = "easy_problems.txt"


def get_problem_ids(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()
    ids = []
    for line in lines:
        try:
            i = int(line.strip())
        except ValueError:
            continue
        ids.append(i)
    return ids

if __name__ == "__main__":
    ids = get_problem_ids(file_name)
    random_problem_id = ids[random.randint(0, len(ids))]
    # print("Picked ID {} out of {} problem IDs.".format(random_problem_id, len(ids)))
    print(random_problem_id)
    