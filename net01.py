#作成者：田村　和広
#ワッツとストロガッツのスモールワールドネットワークの作成練習
#nx.watts_strogatz_graph(ノード数,各ノードの最初の次数,繋ぎ変え確率)

import networkx as nx
import matplotlib.pyplot as plt

def main():
    G= nx.Graph()
    G=nx.watts_strogatz_graph(6,4,0.2)
    figure_out(G)

def figure_out(G):
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels=True)
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()