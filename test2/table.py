import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# %matplotlib inline

df = pd.DataFrame(np.random.randn(10,4),columns=['a','b','c','d'])
sty = df.style
print(sty,type(sty))
# 查看样式类型6
print(df)
sty