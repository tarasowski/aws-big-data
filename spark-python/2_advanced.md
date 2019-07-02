# Advanced

### Most popular movie

```csv
user_id, movie_id, rating, timestamp
196 242 3 881250949
186 302 3 81717742
``` 

```py
from pyspark import SparkContext, SparkConf

conf = SparkConf().setMaster('local').setAppName('MostPopularMovie')
sc.stop()
sc = SparkContext(conf = conf)

def parseLines(line):
    fields = line.split(',')
    return (int(fields[1]))

lines = sc.textFile('u.data')
movies = lines.map(lambda x: (int(x.split()[1]), 1))
moviesCount = movies.reduceByKey(lambda x, y: x + y)
flipped = moviesCount.map(lambda x: (x[1], x[0]))
sortedMovies = flipped.sortByKey()
results = sortedMovies.collect()

for result in results:
    print(result)
sc.stop()
# (count, movieID)
# (320, 42)
# (340, 53)
# (583, 50)
``` 

### Broadcast Variables
* Display movie names, not ID's (from the u.item file)
* We could jus tkeep a talbe loaded in the driver program
  * Or we cloud even let Spark automatically forward it to each executor when
    needed
  * But what if the table were massive? We'd only want to transfer it once to
    each executor, and keep it there. That's the most efficient way (if you need
    a lookup object)
* Broadcast object to the execturos, such that they're always there whenever
  needed
* Just use cs.broadcast() to ship off whatever you want 
  * Spark will do all the work of serializing it, sending to each node in the
    cluster
* Then use .value() to get the object back
* Broadcast will transit table movie names object to the nodes

```py
from pyspark import SparkConf, SparkContext

def loadMovieNames():
    movieNames = {}
    with open("u.item", encoding='ISO-8859-1') as f:
        for line in f:
            fields = line.split('|')
            movieNames[int(fields[0])] = fields[1]
    return movieNames

conf = SparkConf().setMaster("local").setAppName("PopularMovies")
sc.stop()
sc = SparkContext(conf = conf)

nameDict = sc.broadcast(loadMovieNames())

lines = sc.textFile("u.data")
movies = lines.map(lambda x: (int(x.split()[1]), 1))
movieCounts = movies.reduceByKey(lambda x, y: x + y)

flipped = movieCounts.map( lambda x : (x[1], x[0]))
sortedMovies = flipped.sortByKey()

sortedMoviesWithNames = sortedMovies.map(lambda countMovie : (nameDict.value[countMovie[1]], countMovie[0]))

results = sortedMoviesWithNames.collect()

for result in results:
    print (result)
sc.stop()
```

### Most Popular Superhero
* In what superhero comic books appear in the same comic book are friends
* Input data:
  * marvel-graph.txt `4395 2237 1767 472 4997...` 
    * the first is the hero_id followed by all other heros they are apread with
    * a hero may span multiple lines!!!
  * marvel-names.txt
    ``` 
    5300 "Spencer, Tracy"
    5301 "Sprenzel, Anton"
    5302 "Spetsburo, Gen. Yuri"
    5303 "SPHINX"
    ```
* Strategy for find the most popular superhero:
  * Map input data to (heroId, number of co-occurrences) per line
  * Add up co-occurrences by heroId useing reduceByKey()
  * Flip (map) RDD to (number, heroId) so we can use max() on the RDD to find
    the hero with the most co-occurrences
  * Look up the name of the winner and display the result

```py
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
``` 

### Degrees of Separation between Superheroes 
* How is to whom connected
* To find the answer we need to use the algorithm Breadth-First-Search in Spark
* The first thing is we need to convert our file to nodes with connections, a
  a distance and a color. For example `5983 1165 3836 4361 1282` becomes `(5983,
  (1165, 3836, 4361, 1282), 9999,'WHITE')` 
* Our initial condition is that a node is infinitely distant (9999) and white

```py
def converToBFS(line):
  fields = line.split()
  heroID = int(fields[0])
  connections = []
  for connection if fields[1:]:
    connections.append(int(connection)
  color = 'WHITE'
  distance = 9999

  if (heroID == startCharacterID):
      color = 'GRAY'
  distance = 0

  return (heroID, (connections, distance, color))
```
* Just like each step of our BFS example
* Go through, looking for gray nodes to expand
* Color nodes we're done with black
* Update the distance as we go

* The mapper:
  * Creates new nodes for each connection of gray nodes, with a distance
    incremented by one, color gray, and no connections
  * Colors the gray node we just processed black
  * Copies the node itself into the result
* The reducer
  * Combines together all nodes for the same heroID
  * Preserves the shortest distance, and the darkest color found
  * Preserves the list of connections from the original node

* How do we know when we're done?
  * An accumulator allows many executors to increment a shared variable
  * For example:
    hitCounter = sc.accumulator(0) set up a shared accumulator with an initial
    value of 0
  * For each iteration, if the character we're interested in is hit, we
    increment the hitCounter accumulator
  * After each iteration, we check if hitCounter is greater than one - if so,
    we're done

### Callaborative filtering in Spark cache() persist()

#### Item-based collaborative filtering (finding similar movies)
* Finding similar movies using Spark and the Movielens data set
* Introducing caching RDD's
* Find every pair of movies that were watched by the same person
* Measure the similarity of their ratings across all users who watched both
* Sort by movie, then by similarity strength

![item-based](https://cdn-images-1.medium.com/max/1200/1*skK2fqWiBF7weHU8SjuCzw.png)

* Making it a spark problem:
  * Map input ratings to (userID, (movieID, rating))
  * Find every movie pair rated by the same user
    * This can be done with a "self-join" opeeration
    * At this point whe have (userID, ((movieID1, rating1), (movieID2, rating2))
  * Filter out duplicate pairs
  * Make the movie pairs the key
    * here we remove the userID because this is not relevant, we just want to
      combine the watched movies and ratings for 1 person
    * map to ((movieID1, movieID2), (rating1, raing2))
  * groupByKey() to get every rating pair found for each movie pair
  * Compute similarity between ratings for each movie in the pair
  * Sort, save and display results

* To spread the work across all cores we can use `local[*]` go and take
  advantage of all cores on the computer, it will create as many executors as
  you have cores on the machine

```py
conf = SparkConf().setMaster('local[*]').setAppName('MovieSimilarities')
sc = SparkContext(conf = conf)

```
* In this example, we'll query the final RDD of movie similarities as couple of
  times
* Any time you will perform more than one action on an RDD, you must cache it!
  * Otehrwise, Spark might re-evaluate the entire RDD all over again!
* Use .cache() or .persist() to do this
  * What's the difference?
  * Persist() optionally lets you cache it to disk instead of just memory just
    in case a node fails or something
