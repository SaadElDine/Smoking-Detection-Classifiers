# Smoking-Detection-Classifiers
Apply Data analysis (3 techniques), Data Cleaning, Preprocessing, Feature Engineering And Implement 3 Ensemble Models From Scratch: Bagging, Boosting and Random Forest.

## Code Details:

### 1. Data Analysis:
  • Univariate Analysis: Understanding the distribution and characteristics of individual 
features provides crucial insights into their relevance and potential impact on model 
performance. This analysis aids in identifying which features might be significant for 
further manipulation in Feature Engineering.

  • Bivariate Analysis: Examining relationships between pairs of features helps identify 
dependencies or correlations. These identified patterns guide the selection of feature 
combinations that might contribute significantly to model performance during Feature 
Engineering.

  • Multivariate Analysis: Assessing complex interactions among multiple features offers a 
deeper understanding of their combined effects. This analysis assists in feature selection 
and dimensionality reduction techniques employed in Feature Engineering.

 ### 2. Feature Engineering and Preprocessing:
  • Techniques for Feature Engineering: Leveraging insights from Univariate, Bivariate, and 
Multivariate Analyses, techniques for extracting, creating, and selecting features are 
employed. This step involves transforming raw data into meaningful representations that 
positively impact model accuracy and performance.

  • Exploration of Feature Impacts: Hands-on exercises involving the manipulation of 
features based on data analysis findings provide a practical understanding of how 
feature modifications directly influence model outcomes.

  • - Remove Outliers
    - Adjust Skewed Features Using LOG
    - Check for Nans
    - Features Binning
    - Features Polynomial (automated)
    - Normalization

### 3. Ensemble Methods:
  • Bagging: Utilizes bootstrapping to train multiple models independently and combines 
their predictions through averaging or voting.
  • Boosting: Builds a sequence of models, each correcting errors made by the previous 
ones by assigning different weights to data instances.
  • Random Forests: Implement a Random Forest class or functions to combine multiple 
Decision trees using the DecisionTreeClassifier from scikit-learn.
>> These ensemble techniques leverage the enhanced features and models created through 
Feature Engineering. The refined features and diverse models contribute to improved predictive 
accuracy and robustness when combined using these ensemble methods.

### 4. Hyperparameter Tuning:
  • Grid Search: Exhaustively searches through a specified parameter grid to identify the 
best combination of hyperparameters.
  • Randomized Search: Randomly samples hyperparameters from specified distributions to 
efficiently find optimal settings.
  • Bayesian Method.
  
### 5. Final System:
  • After Finishing all of you analysis, trying different ensemble methods, and finetuning 
them, you will end up with a final Machine learning system with the best performance.


