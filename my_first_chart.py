import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Malgun Gothic"	

prices = [85, 86, 87, 88.5, 89, 87.5]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(prices)
for i, p in enumerate(prices):
	ax.annotate(f"{p:,}", (i, p), textcoords="offset points",
		xytext=(0, 8), ha="center")
ax.set_title("대학교 성적 그래프")
fig.savefig("my_first_chart.png")
