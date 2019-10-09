#作成者：田村　和広
#erdos_renyiのランダムグラフネットワークの作成練習
#nx.erdos_renyi_graph(ノード数,リンク確率)

import networkx as nx
import matplotlib.pyplot as plt

def main():
    G= nx.Graph()
    G=nx.erdos_renyi_graph(20,0.1)
    figure_out(G)

def figure_out(G):
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True)
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()