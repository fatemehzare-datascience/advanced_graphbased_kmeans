"""AGKmeans code."""
import pandas as pd
import networkx as nx
__author__ = 'Fatemeh Zare<faz361@mail.usask.ca>'
"""
 Advanced graph-based k-means is an appropriate algorithm for the datasets
which have lots of dynamic objects.
 Instead of passing through space, Advanced graph-based k-means can only
  pass through certain points. Thus, it can be applied to datasets
which can be modeled as graphs.
In Advanced graph-based k-means, initial centroids would be selected based on
Global Unique Interaction instead of random selection.
 Wisely selection of initial
centroids would decrease the probability of falling
into the local optimal clustering.
"""


def agkmeans(G, k):
    """Initialize selection of centrids."""
    index_list1 = []
    for i in G.node:
        index_list1.append(i)
    df_initial = pd.DataFrame(columns=['node', 'degree', 'centroid'],
                              index=index_list1)
    df_initial = df_initial.reset_index(drop=True)
    p = 0
    for i in G.node:
        df_initial["node"][p] = i
        df_initial["degree"][p] = G.degree(i)
        p = p + 1

    df_initial.sort_values("degree", inplace=True, ascending=False)
    df_initial = df_initial.reset_index(drop=True)

    k_list1 = df_initial['node'].tolist()
    k_list = k_list1[:k]

    df2 = pd.DataFrame(columns=['node', 'shoretest_path_centroid', 'centroid'])
    df2['node'] = df_initial['node']

    def assignment1(G, df, randomlist):
        df['shoretest_path_centroid'] = float('inf')
        df['centroid'] = None
        for j in randomlist:
            for i in G.node:
                b = df.loc[df['node'] == i, 'shoretest_path_centroid'].iloc[0]

                try:
                    n = nx.shortest_path_length(G, i, j)
                except nx.NetworkXNoPath:
                    n = 1000000000000000000000
                if n < b:
                    df.loc[df['node'] == i, 'shoretest_path_centroid'] = n
                    df.loc[df['node'] == i, 'centroid'] = j

        randomlist.sort()
        return (randomlist)

    def update(G, df2, k_list):
        df2_sum = df2.groupby(['centroid'])['shoretest_path_centroid'].sum()

        for i in k_list:
            for j in G.neighbors(i):
                p = 0
                sump = 0
                for b in G.node:
                    if (df2.loc[df2['node'] == b, 'centroid'].iloc[0] == i):
                        try:
                            p = nx.shortest_path_length(G, j, b)
                        except nx.NetworkXNoPath:
                            p = float('inf')

                        sump += p
                if sump < df2_sum[i]:
                    df2.loc[df2['centroid'] == i, 'centroid'] = j

        for i in df2['node']:
            b = df2.loc[df2['node'] == i, 'centroid'].iloc[0]
            try:
                v = nx.shortest_path_length(G, i, b)
            except nx.NetworkXNoPath:
                v = float('inf')
            df2.loc[df2['node'] == i, 'shoretest_path_centroid'] = v
#
        lista = df2['centroid'].unique().tolist()
        return (lista)

    a = assignment1(G, df2, k_list)

    b = update(G, df2, k_list)

    while (a.sort() != b.sort()):
        k_list = b
        a = assignment1(G, df2, k_list)
        b = update(G, df2, k_list)
    dict1 = df2.set_index('node')['centroid'].to_dict()
    return (dict1)
