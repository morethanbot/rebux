for i in range(0, 2):
    filename = f'dataset/cat_{i+1}.csv'
    print(filename)
    with open(filename + '.tmp', 'r') as fin:
        with open(filename, 'w') as fout:
            for line in fin.readlines():
                tokens = line.split(';')[:3]
                for token in tokens:
                    fout.write(token + ';')
                fout.write('\n')
    