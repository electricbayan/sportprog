import time

def test_task(filename, task_num, time_limit=5):

    tests = {
        1: [[1, 4], [5]],
        2: [[5, [5, 18, 13, 27, 14]], [3]],
        3:[[1427,  0, 876652098643267843, 5276538], [2297.0716,936297014.1164,0.0000, 37.7757]],
        4: [[1, 5], [6]],
        5: [[4], [2]],
        6: [[-3], [-5]],
        7: [[5, 10, 0], [3, 4]],
        8: [[2, 10], [90]],
        9: [[3, [3, 7, 5]], [6]],
    }


    with open('test_handler.py', 'w') as f, open(filename) as g:
        f.write(g.read())

    from test_handler import solution

    task_data = tests[task_num]

    time_now = time.time()

    user_solution = solution(*task_data[0])
    right_solution = task_data[1]
    if len(right_solution) == 1:
        right_solution = right_solution[0]

    delta_time = time.time() - time_now
    if user_solution != right_solution:
        return 'WA'
    elif delta_time > time_limit:
        return 'TL'
    return 'OK'
