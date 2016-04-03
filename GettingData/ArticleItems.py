article_names_set = set()

f = open('forGrisha.txt')

filestring = f.readline()

i = 0

while True:

    if filestring is None:
        break

    article_names_set.add(filestring)

    filestring = f.readline()


    i+=1

    if (i % 100 == 0):
        print i

print len(article_names_set)
