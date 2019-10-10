#作成者：田村　和広
#barabshi-albertネットワークの作成練習
#nx.erdos_renyi_graph(ノード数,ノード追加時のリンク数)

import networkx as nx
import matplotlib.pyplot as plt

def main():
    G= nx.Graph()
    G=nx.barabasi_albert_graph(100,2)
    figure_out(G)

def figure_out(G):
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True)
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()