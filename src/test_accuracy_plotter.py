# %%
import pandas as pd
import numpy as np
import seaborn as sns

sns.set_theme()


# %%

df = pd.DataFrame({"Test Accuracy": [52.56, 52.44, 52.88, 51.42, 47.41, 44.16], "Time Skip": [50, 25, 75, 100, 10, 0], "CIFAR Test Accuracy": [69., 68.63, 69.06, 69.1, 64.44, 61.55]})

fig = sns.lineplot(data=df, x="Time Skip", y="Test Accuracy", markers=True)
sns.scatterplot(data=df, x="Time Skip", y="Test Accuracy", markers=True, ax=fig)

fig.set_title("Stream51 Test Accuracy")
# %%

fig = sns.lineplot(data=df, x="Time Skip", y="CIFAR Test Accuracy", markers=True)
sns.scatterplot(data=df, x="Time Skip", y="CIFAR Test Accuracy", markers=True, ax=fig)

fig.set_title("CIFAR Test Accuracy")
# %%
