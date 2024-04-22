def check_solution(filename: str, task_num: int):

    tests = {

        1: {"a": [1427, 0, 876652098643267843, 5276538], "out": [2297.0716, 936297014.1164, 0.0000, 37.7757]},
        2: {"a":5, "b": "5 8 13 27 14", "out": 3},
        3: {"a": 10, "out": 25},
        4: {"a": 1, "b": 5, "out": 6}
    }

    task = tests[task_num]

    with open(f'utils/{filename}', 'r') as f:

        a = f.read()

    with open('utils/solution_handler.py', 'w') as g:
        if task_num != 3:
            b = f'{task["a"]}, {task["b"]})'
        else:
            b = f'{task["a"]})'
        g.write(a + '\n\nres=solution(' + b)

    from solution_handler import solution

    if task_num != 3:
        res = solution(task["a"], task["b"])
    else:
        res = solution(task["a"])

    verdict = 'OK'

    if res != task["out"]:
        verdict = "WA"
    print(verdict)


check_solution('test.py', 4)
