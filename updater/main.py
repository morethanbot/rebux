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
    for books in user_books.values():
        books.reverse()


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
                    if book_to_id in user_books[user_from_id]:
                        continue
                    if book_to_id not in book_weights:
                        book_weights[book_to_id] = 0
                    book_weights[book_to_id] += 1
    book_by_titles = {}
    for book_id in book_weights.keys():
        book = book_info[book_id]
        if book['title'] in book_by_titles:
            continue
        book_by_titles[book['title']] = book
    response = {
        'history': [book_info[book_id] for book_id in user_books[user_from_id]],
        'recommendations': sorted(book_by_titles.values(), key=lambda book: book_weights[book['book_id']], reverse=True)[:5],
    }
    return json.dumps(response, indent=4, ensure_ascii=False)


for i in range(0, 2):
    read_book_info(f'dataset/book_info_{i+1}.csv')
for i in range(0, 3):
    read_user_books(f'dataset/user_books_{i+1}.csv')
print("Input format: <user_id>")
while True:
    user_id = int(input())
    print(get_user_recommendations(user_id))
