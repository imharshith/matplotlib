#BIT ME department placement analysis.

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
%matplotlib inline

style.use('ggplot')

YEAR=['2015','2016','2017','2018']
ME_OFFERS=[113,89,45,59] 
ME_ELIGIBLE=[105,124,104,104] 
ME_PLACED=[82,54,41,55]

xpos=np.arange(len(YEAR))
#print(xpos)

plt.xticks(xpos,YEAR)
plt.title("ME DEPARTMENT")
plt.xlabel("YEAR")
plt.ylabel("NO_OF_STUDENTS")

plt.bar(xpos-0.2,ME_OFFERS,color='teal',width=0.2,label="offers")
plt.bar(xpos,ME_ELIGIBLE,color='tan',width=0.2,label="eligible")
plt.bar(xpos+0.2,ME_PLACED,color='orange',width=0.2,label="placed")
plt.legend()
plt.show()
