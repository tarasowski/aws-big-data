from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster('local').setAppName('PopularHero')
sc.stop()
sc = SparkContext(conf = conf)

def countCoOccurences(line):
    elements = line.split()
    return (int(elements[0]), len(elements) - 1)

def parseNames(line):
    fields = line.split('\"')
    return (int(fields[0]), fields[1].encode('utf-8'))

# instead of broadcasting we create an RDD that will be used across the nodes
# another way to solve the problem
names = sc.textFile('Marvel-Names.txt')
namesRdd = names.map(parseNames)

lines = sc.textFile('Marvel-Graph.txt')

pairings = lines.map(countCoOccurences)
# we can reduceByKey() because the heroID can be across multiple lines we need to add them
totalFriendsByCharacter = pairings.reduceByKey(lambda x, y: x + y)
flipped = totalFriendsByCharacter.map(lambda x: (x[1], x[0]))

# we'll get back the heroID with the most co-occurences
mostPopular = flipped.max()

mostPopularName = namesRdd.lookup(mostPopular[1])[0]

print(str(mostPopularName) + " is the most popular superher with " + str(mostPopular[0]) + " co-appearances.")
