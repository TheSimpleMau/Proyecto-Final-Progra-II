import matplotlib.pyplot as plt

class Plots:

    def __init__(self,text) -> None:
        self.text = text
        try:
            self.graph()
        except Exception as e:
            print(e)
        # self.fig = plt.figure()
        # self.ax = self.fig.add_subplot(111)

    def graph(self):
        to_show = '$'+self.text+'$'
        plt.title("LaTeX plot")
        plt.text(0.5, 0.5, to_show, fontsize=40, ha="center")
        plt.xticks([])
        plt.yticks([])