#include <cstdio>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <mutex>
#include <unordered_map>


#define BOOKS_PER_USER_LIMIT 15


void read_user_books(const char *);
void update_heavy_users();
void update_user_recommendations(int);


std::unordered_map<int, std::set<int> > user_books;
std::unordered_map<int, std::set<int> > book_users;
std::unordered_map<int, std::vector<int> > user_recommendations;

int main() {
    for (int i = 1; i <= 3; i++) {
        std::string filename = "dataset/user_books_" + std::to_string(i) + ".csv";
        read_user_books(filename.c_str());
    }

    std::vector<int> users_sorted;
    for (auto user : user_books) {
        users_sorted.push_back(user.first);
    }
    std::sort(users_sorted.begin(), users_sorted.end(), [&](const int &a, const int &b) {
        return user_books[a].size() > user_books[b].size();
    });
    for (int user_id : users_sorted) {
        update_user_recommendations(user_id);
        printf("\r%06d:%04d", user_id, (int) user_books[user_id].size());
        fflush(stdout);
    }
    printf("\n");
    
    printf("Input format: <user_id> <index>\n");
    while (true) {
        int user_id, index;
        scanf("%d %d", &user_id, &index);
        update_user_recommendations(user_id);
        if (user_recommendations[user_id].size() > (size_t) index) {
            printf("%d\n", user_recommendations[user_id][index]);
        } else {
            printf("-1\n");
        }
    }
    return 0;
}

void read_user_books(const char *dataset_path) {
    if (FILE *fin = fopen(dataset_path, "r")) {
        char header[256];
        fscanf(fin, "%s", header);
        int user_id, book_id;
        int line = 0;
        while (fscanf(fin, "%d;%d;", &user_id, &book_id) == 2) {
            if (line % 1000000 == 0) {
                printf("\rLoading %s %07d/4000000", dataset_path, line);
                fflush(stdout);
            }
            line++;
            user_books[user_id].insert(book_id);
            book_users[book_id].insert(user_id);
        }
        printf("\n");
    } else {
        printf("Can't read file!\n");
    }
}

void update_user_recommendations(int user_from_id) {
    if (user_recommendations.find(user_from_id) == user_recommendations.end()) {
        std::unordered_map<int, float> book_weights;
        int limit = BOOKS_PER_USER_LIMIT;
        for (int book_from_id : user_books[user_from_id]) {
            if (--limit == 0) {
                break;
            }
            for (int user_to_id : book_users[book_from_id]) {
                if (user_to_id != user_from_id) {
                    for (int book_to_id : user_books[user_to_id]) {
                        book_weights[book_to_id] += 1;
                    }
                }
            }
        }
        std::vector<int> recommendations;
        for (auto book : book_weights) {
            recommendations.push_back(book.first);
        }
        std::sort(recommendations.begin(), recommendations.end(), [&](const int &a, const int &b) {
            return book_weights[a] > book_weights[b];
        });
        user_recommendations[user_from_id] = recommendations;
    }
}
