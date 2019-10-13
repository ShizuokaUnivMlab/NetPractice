#作成者：田村　和広
#完全〇分木の作成練習
#nx.balanced_tree(分化数,深さ)

import networkx as nx
import matplotlib.pyplot as plt

def main():
    G= nx.Graph()
    G=nx.balanced_tree(2,5)
    figure_out(G)

def figure_out(G):
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True)
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()