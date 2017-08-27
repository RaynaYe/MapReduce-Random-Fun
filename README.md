# MapReduce-Random-Fun
Task1: Inverted index with MapReduce
Use the files in the folder /data/assignments/ex2/task1/large/ as input and produce an inverted
index using MapReduce. For instance, given the following documents: (4 marks)    
d1.txt: cat dog cat fox  
d2.txt: cat bear cat cat fox＜/br＞

d3.txt: fox wolf dog＜/br＞
you should build the following full inverted index.＜/br＞
bear: 1 : {(d2.txt,1)}＜/br＞
cat : 2 : {(d1.txt, 2), (d2.txt, 3)}＜/br＞
dog : 2 : {(d1.txt, 1), (d3.txt, 1)}＜/br＞
fox : 3 : {(d1.txt, 1), (d2.txt, 1), (d3.txt, 1)}＜/br＞
wolf: 1 : {(d3.txt,1)}＜/br＞

Task2: Parsing StackOverflow＜/br＞
Which are the 10 most popular questions according to their view counts (attribute ViewCount in a question
post)?</br>

Task3: Who was the user that answered the most questions and what were the Ids of these questions?＜/br＞

Task4: Who was the user that had the most accepted answers and what were these answers? </br>

Task5: For large data, running reservoir sampling on a single machine would take too long. Implement
a MapReduce version of reservoir sampling which uniformly samples only a single line and uses
MapReduce to do so. Use your implementation to sample a single line from the file webLarge.txt.
Your output should contain only a single line.</br>

Task6: Extend the basic version of reservoir sampling such that it can sample multiple lines uniformly without
replacement and run on a single machine (i.e. no MapReduce). This means that if we want to sample
k lines from a file with n lines in total, then each of the (
n
k
) possible outcomes has equal probability.
Implement a program that will sample 100 lines from the file webLarge.txt. Run your program locally
(not as a MapReduce job).</br>

Task7: Make your own implementation of a Bloom filter. We leave the choice of a hashing function up to you.
Write a program that uses your implementation of Bloom filter to approximately de-duplicate the lines
in the file webLarge.txt. The output of an approximate de-duplication contains no duplicate lines, but
some lines from the input might not appear at all in the output. You should think carefully about the
number of hashing functions and the size of the Bloom filter you use. The probability that a line (and its
duplicates) from the input does not appear at all in the output should be less than 1%. You can assume
that your hashing functions produce every value equally likely. When choosing the size of your Bloom
filter and number of hashing functions, you should assume the worst case in which all lines are unique.
The number of lines should be a command-line parameter to your program. </br>

Task8: Imagine you are Google and you want to know which search queries (if any) form at least 1% of all
queries in total. In the file queriesLarge.txt each line is a hash of a query and queries occurred in the
order as listed in the file. Implement the lossy counting algorithm and run it on the file queriesLarge.txt.
Your output should contain all queries that form at least 1% of all queries and no query that formed less
than 0.9% of all queries. </br>

