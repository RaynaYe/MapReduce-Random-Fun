# MapReduce-Random-Fun
Task1: Inverted index with MapReduce
Use the files in the folder /data/assignments/ex2/task1/large/ as input and produce an inverted
index using MapReduce. For instance, given the following documents: (4 marks)
d1.txt: cat dog cat fox \n
d2.txt: cat bear cat cat fox
d3.txt: fox wolf dog
you should build the following full inverted index.
bear: 1 : {(d2.txt,1)}
cat : 2 : {(d1.txt, 2), (d2.txt, 3)}
dog : 2 : {(d1.txt, 1), (d3.txt, 1)}
fox : 3 : {(d1.txt, 1), (d2.txt, 1), (d3.txt, 1)}
wolf: 1 : {(d3.txt,1)}
