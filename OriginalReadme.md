# PaarthPIB


Question 1 :
Step 1 - pip install fastapi uvicorn
Step 2 - uvicorn main:app --reload

API documentation will be available at:

http://127.0.0.1:8000/docs


Question 2 :
The previous code was returning each occurence of the duplicate value and the new code requires the rechecking of the duplicates list making the values distinct

Correct Code is in Duplicate.py 

Question 3 :
Kindly check dataprocessing.py for the code

Question 4 :
To Start the search react app, follow the below steps
 Step 1. cd UserSearch
 Step 2. npm i
 Step 3. npm run dev

 The given useeffect is problematic as the search will runs each time search is changed.
 For Example - for Paarth it will run 6 times. Instead of search, a delay after key press release is adviced so that there can be minimum backend calls with fastest output.

Question 5 :
There are several problems in the code : 
1. 
```
useEffect(() => {
 console.log("Selected:", selectedUser);
 });
```
dependency on selectedUser is missing here making it run recursively instead of initially or onchange

2. 
```
 {users.map((user) => (
 <div onClick={() => setSelectedUser(user)}>
 {user.name}
 </div>
 ))}
```
key is missing in the map the updated code should be
```
 {users.map((user) => (
 <div key={user.id} onClick={() => setSelectedUser(user)}>
 {user.name}
 </div>
 ))}
 ```

3. React Hooks are not imported and function is not exported

Question 6 :
pip install pandas scikit-learn

Q1. Why you selected the algorithm
    I selected Logistic Regression because this is a binary classification problem. I am trying to predict whether a customer will churn or not.

Q2. Accuracy
    0.95

Q3. Precision
    0.875

Q4. Recall
    1.0

Q5. Explanation of overfitting
    Overfitting happens when a model learns the training data too closely with its noise.

    For example:

    Training accuracy = 95%
    Testing accuracy  = 80%

Q6. How you would improve the model
 1. Collect more data
    More customer records can help the model learn general patterns.
 2. Try other algorithms
    Random Forest
    Decision Tree
    Gradient Boosting
    XGBoost
 3. Tune the model
    I could use cross-validation and hyperparameter tuning to find better model settings.
 4. Prevent overfitting
    Regularization, cross-validation and limiting model complexity can help the model perform better on unseen data.