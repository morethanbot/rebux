user_books = {}
book_users = {}


def read_user_books(filename):
    line_number = 0
    with open(filename, 'r') as fin:
        for line in fin.readlines()[1:]:
            if line_number % 1000000 == 0:
                print(f'\rLoading {filename} {line_number:07d}/4000000', end='')
            line_number += 1
            tokens = line.split(';')
            user_id = int(tokens[0])
            book_id = int(tokens[1])
            if user_id not in user_books:
                user_books[user_id] = []
            user_books[user_id].append(book_id)
            if book_id not in book_users:
                book_users[book_id] = []
            book_users[book_id].append(user_id)
    print()
            

def get_user_recommendations(user_from_id):
    limit = 15
    book_weights = {}
    for book_from_id in user_books[user_from_id]:
        if limit == 0:
            break
        limit -= 1
        for user_to_id in book_users[book_from_id]:
            if user_to_id != user_from_id:
                for book_to_id in user_books[user_to_id]:
                    if book_to_id not in book_weights:
                        book_weights[book_to_id] = 0
                    book_weights[book_to_id] += 1
    recommendations = [book_id for book_id in book_weights.keys()]
    return sorted(recommendations, key=lambda book_id: book_weights[book_id], reverse=True)         



for i in range(0, 3):
    read_user_books(f'dataset/user_books_{i+1}.csv')
print("Input format: <user_id>")
while True:
    user_id = int(input())
    limit = 5
    for book_id in get_user_recommendations(user_id):
        limit -= 1
        if limit == 0:
            print(book_id)
            break
        else:
            print(book_id, end=', ')
