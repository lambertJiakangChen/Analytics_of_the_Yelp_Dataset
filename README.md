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

Part 1. Compute the frequency distribution of the number of restaurants in each category of restaurants (e.g., Japanese, Chinese, Canadian, Italian, etc.) Display the **top-10** categories in descending order with one line per pair of values as follows:
    ```
    category:#restaurants
    ```
Part 2. Compute the frequency distribution of the number of reviews submitted for each category of restaurants (e.g., Japanese, Chinese, Canadian, Italian, etc.). Display the **top-10** reviews in descending order with one line per triplet as follows:
    ```
    category:#reviews:average_review_count
    ```

Part 3. Create a bar chart that shows the **top-5** restaurant categories identified in part (1), where the x-axis represents the restaurant category, and the y-axis represents its frequency (#restaurants).

Run the script as follows:
    ```
    $ python3 dist.py /path-to-file/filename.json city ST (Linux)
    or
    $ python dist.py /path-to-file/filename.json city ST (Windows)
    ```
    For example:
    ```
    $ python3 dist.py yelp_academic_dataset_business.json Vancouver BC
    ```

## Q3. Creating the Yelp Social Network (20%)
The social network will be represented as a graph G(V,E), where V is a set of vertices representing the Yelp users and E is a set of edges representing friendships between Yelp users.
The graph/network should be represented in a file using the edge list format. An edge list is a list that represents all the edges in a graph. Each edge is represented as a space-separated pair of vertices. For example, a small fully connected triangle-like graph between vertices *a1, a2, a3* would be represented in the edge list as:
```
a1 a2
a2 a3
a3 a1
```
Note that the order of the lines does not matter, and edges are bidirectional (so either *"a1 a2"* or *"a2 a1"* should be listed but NOT both).


Given a collection of users in a file `/path-to-file/filename.json` and an integer `n` (n >= 100), write a Python script (*network.py*) that creates the social network of Yelp friends among Yelp users who sent **no less than `n` useful votes**, and writes the edge list of the created graph to a text file named **Q3.out** in the **current working directory**. Your script should only consider Yelp users who sent no less than `n` useful votes. For example, users *a1* and *a2* are friends, who sent *n+1* and *n-1* useful votes, respectively. In this case, neither *"a1 a2"* nor *"a2 a1"* should be listed.

We use the original file provided by Kaggle ([*yelp_academic_dataset_user.json*](https://www.kaggle.com/yelp-dataset/yelp-dataset/version/3?select=yelp_academic_dataset_user.json)) for evaluation.

Your script should be run as follows:
```
$ python3 network.py /path-to-file/filename.json n
```
For example, the following command should create the social network of Yelp friends among Yelp users who sent no less than 100 useful votes.
```
$ python3 network.py yelp_academic_dataset_user.json 100
```

## Q4. Compute Network Statistics (20%, 5% each)
Given a Yelp social network as an edge list in a text file `/path-to-file/filename.txt` (the format is the same as the Q3 output), write a Python script (*graph.py*) that computes the following network statistics and writes the answer to a text file named ***Q4.out*** in the **current working directory**.

* the number of vertices (*|V|*) and the number of edges (*|E|*) of the network. The output should be two space-separated integers.
* The average node degree of the graph (*avgNodeDegree*). The degree of a node is the number of edges that are incident to the node (i.e., #neighbors).
* The number of connected components in the network (*#components*). A connected component is a connected subgraph that is not part of any larger connected subgraph. The connected components of any graph partition its vertices into disjoint sets, and are the induced subgraphs of those sets. A graph that is itself connected has exactly one component, consisting of the whole graph.
* The number of triangles in the network (*#triangles*). For example, vertices *a1, a2, a3* (the order doesn't matter) form a triangle in the social network if *a1* and *a2* are friends, *a1* and *a3* are friends, and *a2* and *a3* are friends.

The output (Q4.out) should be one line per answer to the question as follows:
```
|V| |E|
avgNodeDegree
#components
#triangles
```
For example:
```
4415 402945
182.53
3
10116817
```

Your script should be run as follows:
```
$ python3 graph.py /path-to-file/filename.txt
```
For example:
```
$ python3 graph.py graph.txt
```

## FAQ
### Restaurant categories in Q2
Please note you only need to find the top-10 categories. Therefore, you don't need to name all legit categories. Also, your code will be evaluated using one of the following parameters based on the original Kaggle dataset:
```
Austin, TX
Portland, OR
Atlanta, GA
Orlando, FL
Vancouver, BC
Boston, MA
```
For the sake of clarity, please assume that the following categories are NOT legit restaurant categories based on geographical origin:
```
Tex-Mex
Ethnic Food
Sushi Bars
Specialty Food
Tacos
```
You still need to filter out other invalid categories.

### Is there a good source for studying and learning of how to work with json files data using python scripts?
You could use the built-in json package to parse JSON files. You can refer to this website (https://docs.python.org/3/library/json.html) for the documentation and some code snippets.

### For Q3, are we using the user_id attribute to represent the vertices in the edge list for the output?
Yes. You should use the user_id attribute to represent users.

### The files I produced usually have a new line at the end. Is that okay?
That is okay. Ending files with a new line is a standard convention.

### For Q2, I read the categories from a text file. Is it okay if I submit the text file along with my other files?
You should strictly follow the directory structure specified in the project description, which means your submission should not include any additional files. I recommend you hard-code the list in your script.
