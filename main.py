from data.provider.pg_provider import PGProvider
import glob
db = PGProvider()
'''
db.connect(host="rc1b-3t64ginmv5ottmzv.mdb.yandexcloud.net", port=6432, sslmode=None, dbname="dataset",
           user="lavrov",
           password="relibrebux")


db.commit()
'''

for f in glob.glob("raw_files\\datasets\\*.csv"):
    file = open(f, "r")
    nf = file.read().replace(";", ",")
    file.close()
    file = open(f, "w")
    file.write(nf)
    file.close()




'''
for i in range(1, 17):
    filename = "raw_files/datasets/circulaton_" + str(i) + ".csv"
    with open(filename, "r") as f:
        for row in f.readlines()[1::]:
            r = row.split(";")
            db.execute("INSERT INTO circulation VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                       (r[0], r[1], r[2], r[3], r[4], r[5], r[6], str(r[7])))
    db.commit()
'''
