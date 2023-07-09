## Objectives

This project involves performing basic analytics on a large-scale dataset using Python on a single machine. The dataset is a subset of Yelp's businesses, reviews, and user data. The dataset consists of five JSON files, which contain information about businesses across 8 metropolitan areas in the USA and Canada.
The dataset can be found and downloaded [here](https://www.kaggle.com/yelp-dataset/yelp-dataset/version/3) (registration to Kaggle is required).

This project contains four Python scripts/programs. The first program (*dstats.py*) performs descriptive analytics of the dataset. The second (*dist.py*) computes useful frequency distributions. The third (*network.py*) constructs a social network of Yelp friends. The fourth (*graph.py*) performs basic network analytics.

## Awareness
* Clone this repository to your local. 
* Use the [`pip freeze`](https://pip.pypa.io/en/stable/cli/pip_freeze/) command to get the requirements format from *requirements.txt*.
* Make sure your version Python >= 3.7.0.
* Change to CRLF line terminators for Windows.

## dstats.py
Original file provided by Kaggle ([*yelp_academic_dataset_business.json*](https://www.kaggle.com/yelp-dataset/yelp-dataset/version/3?select=yelp_academic_dataset_business.json)) for evaluation.

The variables `/path-to-file/filename.json` and a two-letter state/province abbreviation `ST` need to be passed to the script as command line arguments. The [*argparse*](https://docs.python.org/3/library/argparse.html) module makes it easy to write user-friendly command-line interfaces.

Run the script as follows:
```
$ python3 dstats.py /path-to-file/filename.json city ST (Linux)
or
$ python dstats.py /path-to-file/filename.json city ST (Windows)
```
For example:
```
$ python3 dstats.py yelp_academic_dataset_business.json Vancouver BC
```
The file *Q1.out* consists of six line-separated numbers as follows:
* The number of businesses in the `city`, `ST`
* The average number of stars of businesses in the `city`, `ST`
* The number of restaurants in the `city`, `ST`
* The average number of stars of restaurants in the `city`, `ST`
* The average number of reviews for all businesses in the `city`, `ST`
* The average number of reviews for restaurants in the `city`, `ST`
 
## dist.py
Original file provided by Kaggle ([*yelp_academic_dataset_business.json*](https://www.kaggle.com/yelp-dataset/yelp-dataset/version/3?select=yelp_academic_dataset_business.json)) for evaluation.

Given a collection of businesses in a file `/path-to-file/filename.json`, a two-letter state/province abbreviation `ST` (case-sensitive), and a name of a city `city` (case-sensitive) need to be passed to the script as command line arguments

dist.py contains **3** parts

Part 1. The frequency distribution of the number of restaurants in each category of restaurants (e.g., Japanese, Chinese, Canadian, Italian, etc.) The **top-10** categories are displayed in descending order with one line per pair of values as follows:

```
category:#restaurants
```
    
Part 2.The frequency distribution of the number of reviews submitted for each category of restaurants (e.g., Japanese, Chinese, Canadian, Italian, etc.). The **top-10** reviews are displayed in descending order with one line per triplet as follows:

```
category:#reviews:average_review_count
```

Part 3. A bar chart that shows the **top-5** restaurant categories identified in part (1), where the x-axis represents the restaurant category, and the y-axis represents its frequency (#restaurants).

Run the script as follows:

```
$ python3 dist.py /path-to-file/filename.json city ST (Linux)
or
$ python dist.py /path-to-file/filename.json city ST (Window)
```

For example:
```
$ python3 dist.py yelp_academic_dataset_business.json Vancouver BC
```

## network.py
Original file provided by Kaggle ([*yelp_academic_dataset_user.json*](https://www.kaggle.com/yelp-dataset/yelp-dataset/version/3?select=yelp_academic_dataset_user.json)) for evaluation.

Given a collection of users in a file `/path-to-file/filename.json` and an integer `n` (n >= 100) which indicates the social network of Yelp friends among Yelp users who sent **no less than `n` useful votes**.

The social network is represented as a graph G(V,E), where V is a set of vertices representing the Yelp users and E is a set of edges representing friendships between Yelp users. The graph/network is represented in a file using the edge list format. An edge list is a list that represents all the edges in a graph. For example, a small fully connected triangle-like graph between vertices *a1, a2, a3* is represented in the edge list as:
```
a1 a2
a2 a3
a3 a1
```

Run the script as follows:
```
$ python3 network.py /path-to-file/filename.json n
```
For example, the following command creates the social network of Yelp friends among Yelp users who sent no less than 100 useful votes.
```
$ python3 network.py yelp_academic_dataset_user.json 100
```

## graph.py
Yelp social network with format same as the output of network.py (You can directly use the result from network.py as input file)

Your script should be run as follows:
```
$ python3 graph.py /path-to-file/filename.txt (Linux)
or
$ python graph.py /path-to-file/filename.txt (Windows)
```
For example:
```
$ python3 graph.py graph.txt (change graph.txt to the name of your input text file)
```

The output (Q4.out) as follows:
* the number of vertices (*|V|*) and the number of edges (*|E|*) of the network.
* The average node degree of the graph (*avgNodeDegree*).
* The number of connected components in the network (*#components*).
* The number of triangles in the network (*#triangles*). 
