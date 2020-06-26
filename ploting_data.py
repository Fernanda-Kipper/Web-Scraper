import matplotlib.pyplot as plt
import numpy as np


def ploting_results():
    file = open("preços.txt", "r")
    lines = file.readlines()

    prices_kayak = []
    prices_viajanet = []
    datas = []
    all_prices = []

    for line in lines:
        if "/" in line:
            data = line.split(" ")[0]
            if data not in datas:
                datas.append(data)
            if "kayak" in line:
                prices_kayak.append(line.split(" ")[1])
                all_prices.append(int(line.split(" ")[1]))
            else:
                prices_viajanet.append(line.split(" ")[1])
                all_prices.append(int(line.split(" ")[1]))

    mean = np.mean(all_prices)
    prices_dv = [mean - x for x in all_prices]
    std_dv = np.std(prices_dv)

    plt.title("Preços Voo FLNxLAX")
    plt.ylabel("Preços Tickets R$")
    plt.xlabel("Data")
    plt.annotate(f"Média: R${mean:.2f} \nDesvio Padrão: R${std_dv:.2f}", xy=(0, 1.5), size=8,
                 bbox=dict(boxstyle="round", alpha=0.2))

    plt.style.use("dark_background")
    plt.plot_date(datas, prices_kayak, linestyle="solid", linewidth=2, color="#ae7ac7", label="kayak")
    plt.plot_date(datas, prices_viajanet, linestyle="dotted", linewidth=2, color="#89d4be", label="viajanet")
    plt.legend()
    plt.grid(True)

    plt.show()
