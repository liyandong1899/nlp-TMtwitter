### Analysis of Twitter data

The data are the tweets about an American novelist. The data was collected immediately after her passing.

## Warning

Don't construct a graph with more than 20000 tweets at one time. This amount of data may exceed the capability of the RAM.

## DONE

1. draw the network graph and label different clusters (communities) with different colors. The communities are found through a modularity-based greedy algorithm.

2. embed the words and plot them w.r.t. their PCs.

### results

![network graph (isolated islands not shown)](./results/network_community.png)

![word PCs](./results/words_PCA.png)
