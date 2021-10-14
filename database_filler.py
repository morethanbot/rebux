import api
import data

data.database_provider.execute("SELECT * FROM circulation")

index = 0
for row in data.database_provider.get_cursor():
    print(index)
    index += 1
    api.add_entry(user_id=row[5], book_id=row[0])

