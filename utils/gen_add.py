with open('generate.txt', 'w') as f:
    for i in range(10):
        f.write(f'{i}#\n')
    for i in range(100):
        f.write(f'{i}m2\n')
    for i in range(20):
        for j in range(65, 91):
            f.write(f'{i}{chr(j)}-\n')
    for i in range(100):
        f.write(f'({i}m2)\n')

    for i in range(10):
        for j in range(65, 91):
            for m in range(65, 91):
                for n in range(10):
                    f.write(f'{i}{chr(j)}{chr(m)}{n}\n')

    for i in range(50, 800, 50):
        for j in range(50, 1000, 50):
            f.write(f'{i}×{j}\n')