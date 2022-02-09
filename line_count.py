for i in range(3):
    path = f'assignment {i + 1}/assignment_{i + 1}.py'
    with open(path, 'r') as file:
        lines = file.readlines()
        print(f'assignment_{i + 1}.py contains: {len(lines)}')

    path = f'assignment {i + 1}/assignment_{i + 1}_sol.py'
    with open(path, 'r') as file:
        lines = file.readlines()
        print(f'assignment_{i + 1}_sol.py contains: {len(lines)}')

    