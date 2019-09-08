'''K-Fold CV comparison

Cross validation is essential but do not forget that the more folds you use, the more computationally expensive cross-validation becomes. In this exercise, you will explore this for yourself. Your job is to perform 3-fold cross-validation and then 10-fold cross-validation on the Gapminder dataset.

In the IPython Shell, you can use %timeit to see how long each 3-fold CV takes compared to 10-fold CV by executing the following cv=3 and cv=10:

%timeit cross_val_score(reg, X, y, cv = ____)
'''

# Import necessary modules
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn import linear_model

# Create a linear regression object: reg
reg = linear_model.LinearRegression()

# Perform 3-fold CV
cvscores_3 = 3
print(np.mean(cvscores_3))

# Perform 10-fold CV
cvscores_10 = 10
print(np.mean(cvscores_10))
