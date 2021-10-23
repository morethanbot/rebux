import json


user_books = {}
book_users = {}
book_info = {}


def read_user_books(filename):
    print(f"Loading {filename}")
    with open(filename, 'r') as fin:
        for line in fin.readlines()[1:]:
            tokens = line.split(';')
            user_id = int(tokens[0])
            book_id = int(tokens[1])
            if book_id not in book_info:
                continue
            if user_id not in user_books:
                user_books[user_id] = []
            user_books[user_id].append(book_id)
            if book_id not in book_users:
                book_users[book_id] = []
            book_users[book_id].append(user_id)


def read_book_info(filename):
    print(f"Loading {filename}")
    with open(filename, 'r') as fin:
        for line in fin.readlines()[1:]:
            tokens = line.split(';')
            book_id = int(tokens[0])
            author = tokens[1]
            title = tokens[2]
            book_info[book_id] = {
                'book_id': book_id,
                'author': author,
                'title': title,
            }
            

def get_recommendations(book_ids):
    medium_popularity = 0
    for users in book_users.values():
        medium_popularity += len(users)
    medium_popularity /= len(book_users)
    print(medium_popularity)

    book_weights = {}
    for book_from_id in book_ids:
        if book_from_id in book_users:
            for user_id in book_users[book_from_id]:
                for book_to_id in user_books[user_id]:
                    if book_to_id not in book_ids:
                        if book_to_id not in book_weights:
                            book_weights[book_to_id] = 0
                        book_weights[book_to_id] += medium_popularity / len(book_users[book_to_id])
    book_by_titles = {}
    for book_id in book_weights.keys():
        book = book_info[book_id]
        if book['title'] not in book_by_titles:
            book_by_titles[book['title']] = book
    return {
        'history': [book_info[book_id] for book_id in book_ids],
        'recommendations': sorted(book_by_titles.values(), key=lambda book: book_weights[book['book_id']], reverse=True)[:5],
    }

for i in range(0, 2):
    read_book_info(f'dataset/book_info_{i+1}.csv')
for i in range(0, 3):
    read_user_books(f'dataset/user_books_{i+1}.csv')
print("Input format: <user_id>")
while True:
    import random
    id = input()
    try:
        user_books[int(id)]
    except:
        id = random.choice(list(user_books.keys()))
        print(id)
    book_ids = user_books[id][:15]
    print(json.dumps(get_recommendations(book_ids), indent=4, ensure_ascii=False))
