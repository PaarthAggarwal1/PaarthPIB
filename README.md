# PaarthPIB

This is an AI generated markdown file for better understanding of the content. For original content, kindly refer OriginalReadme.md

This project contains my solutions for the given Python, FastAPI, React, data processing, and machine learning tasks.

## Project Structure

The project contains separate files/folders for the different questions:

* `main.py` – FastAPI API implementation
* `Duplicate.py` – Duplicate value handling
* `dataprocessing.py` – Data processing solution
* `UserSearch/` – React search application
* Machine Learning files – Customer churn classification
* `customer.csv` – Customer data used for the machine learning task

---

## How to Run the Project

### 1. FastAPI Project

First install the required packages:

```bash
pip install fastapi uvicorn
```

Run the FastAPI application:

```bash
uvicorn main:app --reload
```

After starting the server, the API documentation can be accessed at:

```text
http://127.0.0.1:8000/docs
```

The Swagger documentation can be used to test the API endpoints directly.

---

### 2. React User Search Application

Go to the React project folder:

```bash
cd UserSearch
```

Install the required dependencies:

```bash
npm i
```

Start the development server:

```bash
npm run dev
```

The application can then be opened using the local URL shown by Vite.

---

### 3. Machine Learning

Install the required Python packages:

```bash
pip install pandas scikit-learn
```

The machine learning code uses the customer CSV file as the input dataset and performs binary classification to predict customer churn.

---

# Design Decisions

## FastAPI

I used FastAPI because it is simple to set up and provides automatic API documentation through Swagger. It also makes it easy to define request schemas and validate incoming data.

## Duplicate Handling

For the duplicate problem, I changed the logic so that duplicate values are checked again before adding them to the result. This prevents the same duplicate value from being returned multiple times.

The solution can be found in:

```text
Duplicate.py
```

## Data Processing

The data processing logic has been kept separate from the API and other questions so that each solution can be tested independently.

The implementation is available in:

```text
dataprocessing.py
```

## React Search

For the search component, I considered the number of API calls made while the user is typing.

For example, if a user types:

```text
Paarth
```

without any delay, the search can potentially run once for each character typed.

Instead of making a backend request after every key press, a small delay/debounce can be used so that the request is made after the user stops typing for a short period.

## Machine Learning

I selected **Logistic Regression** because the task is a binary classification problem. The target is to predict whether a customer will churn or not.

The model was trained using the customer CSV data and evaluated using accuracy, precision, and recall.

---

# Assumptions

* The customer CSV contains the required columns for the churn prediction task.
* Customer churn is treated as a binary classification problem.
* The dataset is suitable for demonstrating the classification model.
* The React application is expected to run using the standard Node.js/npm environment.
* The FastAPI application is expected to run locally.
* The API is primarily intended for testing and demonstration rather than production deployment.
* The reported machine learning metrics are based on the train/test split used in the implementation.

---

# Problems Encountered

### 1. Duplicate Values

The initial duplicate logic could return the same duplicate value multiple times. I changed the logic to recheck the duplicate collection before adding a value to the final result.

### 2. React Search Requests

The search component could make a backend request every time the search value changed. This can create unnecessary API calls, especially when the user types quickly.

A debounce/delay after typing can reduce unnecessary requests.

### 3. React `useEffect`

The provided `useEffect` did not have a dependency array:

```jsx
useEffect(() => {
    console.log("Selected:", selectedUser);
});
```

Because of this, the effect can run after every render.

The updated version should use the appropriate dependency:

```jsx
useEffect(() => {
    console.log("Selected:", selectedUser);
}, [selectedUser]);
```

### 4. React List Keys

The original `users.map()` did not provide a `key` for each element.

The updated code uses:

```jsx
{users.map((user) => (
    <div key={user.id} onClick={() => setSelectedUser(user)}>
        {user.name}
    </div>
))}
```

### 5. Machine Learning

One of the main considerations was selecting an algorithm that matches the problem type. Since the target has two possible outcomes, Logistic Regression was selected as a simple starting point for binary classification.

---

# Testing

I tested the different parts separately.

## FastAPI Testing

I started the application using:

```bash
uvicorn main:app --reload
```

Then I used the Swagger UI at:

```text
http://127.0.0.1:8000/docs
```

to send requests and check the API responses.

## Duplicate Solution

I tested the duplicate logic with values containing repeated elements and checked that the final output contains the expected distinct duplicate values.

## Data Processing

I ran the data processing Python file and checked the generated output against the expected result.

## React Application

I started the React application using:

```bash
npm run dev
```

and tested the search functionality by entering different names and checking the displayed results.

I also checked the `useEffect`, list keys, and clear button behaviour.

## Machine Learning

The machine learning model was tested using a train/test split. I evaluated the model using:

* Accuracy: **0.95**
* Precision: **0.875**
* Recall: **1.0**

These metrics were used to understand how the model performed on the test data.

---

# Machine Learning Details

### Algorithm

**Logistic Regression**

I selected Logistic Regression because the problem is a binary classification problem where the expected result is whether a customer will churn or not.

### Results

| Metric    | Result |
| --------- | -----: |
| Accuracy  |   0.95 |
| Precision |  0.875 |
| Recall    |    1.0 |

### Overfitting

Overfitting happens when a model learns the training data too closely, including its noise, and therefore does not perform as well on new data.

For example:

```text
Training accuracy = 95%
Testing accuracy  = 80%
```

A large difference between training and testing performance can be an indication of overfitting.

### Possible Improvements

The model could be improved by:

1. **Collecting more data**
   More customer records can help the model learn general patterns.

2. **Trying other algorithms**
   For example:

   * Random Forest
   * Decision Tree
   * Gradient Boosting
   * XGBoost

3. **Hyperparameter tuning**
   Cross-validation and hyperparameter tuning can be used to find better model settings.

4. **Reducing overfitting**
   Regularization, cross-validation, and controlling model complexity can help improve performance on unseen data.

---

# AI Assistance

AI assistance was used in a limited way during the preparation of this project.

* AI assistance was used for creating/customizing the **customer CSV data** required for the machine learning task.
* AI assistance was also used to help structure and prepare this **README.md file** for better documentation and understanding of the project requirements.
* The Original REAME.md file can be accessed at **OriginalReadme.md**.

The actual solutions and code were reviewed and tested locally as part of the project.
