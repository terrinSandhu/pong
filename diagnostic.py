import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')

length_plot = sns.barplot(x='sepal_length', y='species', data=iris)
plt.savefig('ex1.pdf')
plt.clf()
width_plot = sns.barplot(x='sepal_width', y='species', data=iris)
plt.savefig('ex2.pdf')