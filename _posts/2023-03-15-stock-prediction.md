---
layout: post
title: "Stock Prediction with Neural Networks"
author_github: Palgun7
date: 2023-03-15 00:00:00
description: "Stock market prediction is the act of trying to determine the future value of company stock or other financial assets that are traded. This can be achieved through deep learning models."
tags:
  - IEEE NITK
  - Blog
  - Neural Networks
  - Deep Learning
  - Stocks
categories:
  - Diode
github_username: "Palgun7"
---

# Stock Prediction with Neural Networks

## Introduction

A stock market is a public market where you can buy and sell shares for publicly listed companies. The stocks, also known as equities, represent ownership in the company. The stock exchange is the mediator that allows the buying and selling of shares. Trading in the stock market means that we are buying one or more shares of the stock. These represent a segment of the whole stock market exchanges that happen in a day.

## Stock Price Prediction

Stock Price Prediction using machine learning helps you discover the future value of company stock and other financial assets traded on an exchange. The idea of predicting stocks is such that we should be able to predict how and which stocks will perform well based on the previous trends. Predicting how the stock market will perform is a hard task to do. There are several factors involved in this prediction, such as physical and psychological factors, rational and irrational behavior. All these factors combine to make share prices dynamic and volatile. This makes it very difficult to predict stock prices with high accuracy.

There are multiple variables in the dataset – date, open, high, low, last, close, total_trade_quantity, and turnover.

- The columns Open and Close represent the starting and final price at which the stock is traded on a particular day.
- High, Low, and Last represent the maximum, minimum, and last price of the share for the day.
- Total Trade Quantity is the number of shares bought or sold in the day and Turnover (Lacs) is the turnover of the particular company on a given date.
  The profit or loss calculation is usually determined by the closing price of a stock for the day; hence we will consider the closing price as the target variable. Let’s plot the target variable to understand how it’s shaping up in our data.

## Linear Regression

The most basic machine learning algorithm that can be implemented on this data is linear regression. The linear regression model returns an equation that determines the relationship between the independent variables and the dependent variable.
The equation for linear regression can be written as:

Y= ⍵1x1 + ⍵2x2 + …+ ⍵nxn

Here x1,x2,...,xn represents the independent variables, and the coefficients ⍵1,⍵2,...,⍵n represent the weights.

For the case of stock prediction, we do not have a set of independent variables. We have only the dates instead. Let us use the date column to extract features like – day, month, year, Mon/Fri, etc., and then fit a linear regression model.

Linear regression is a simple technique and quite easy to interpret, but there are a few obvious disadvantages. One problem in using regression algorithms is that the model overfits the date and month column. Instead of taking into account the previous values from the point of prediction, the model will consider the value from the same date a month ago, or the same date/month a year ago.

## Understanding Long Short-Term Memory Network

LTSMs are a type of Recurrent Neural Network for learning long-term dependencies. It is commonly used for processing and predicting time-series data. The reason they work so well is that LSTM can store past important information and forget the information that is not. LSTM has three gates:

- The input gate: The input gate adds information to the cell state
- The forget gate: It removes the information that is no longer required by the model
- The output gate: Output Gate at LSTM selects the information to be shown as output

From the image on the top, you can see LSTMs have a chain-like structure. General RNNs have a single neural network layer. LSTMs, on the other hand, have four interacting layers communicating extraordinarily.

## Working of LSTMs

LSTMs work in a three-step process.

- The first step in LSTM is to decide which information to be omitted from the cell in that particular time step. The sigmoid function looks at the previous state and the current input, it then interprets which data is important and keeps that.
- There are two functions in the second layer. The first is the sigmoid function, and the second is the tanh function. The sigmoid function decides which values to let through (0 or 1). The tanh function gives the weightage to the values passed, deciding their level of importance from -1 to 1.
- The third step is to decide what will be the final output. First, you need to run a sigmoid layer which determines what parts of the cell state make it to the output. Then, you must put the cell state through the tanh function to push the values between -1 and 1 and multiply it by the output of the sigmoid gate.

# Google Stock Price Prediction Using LSTM

## 1. Import the Libraries.

## 2. Load the Training Dataset.

The Google training data has information from 3 Jan 2012 to 30 Dec 2016. There are five columns. The Open column tells the price at which a stock started trading when the market opened on a particular day. The Close column refers to the price of an individual stock when the stock exchange closed the market for the day. The High column depicts the highest price at which a stock is traded during a period. The Low column tells the lowest price of the period. Volume is the total amount of trading activity during a period.

## 3. Use the Open Stock Price Column to Train Your Model.

## 4. Normalizing the Dataset.

## 5. Creating X_train and y_train Data Structures.

## 6. Reshape the Data.

## 7. Building the Model

## 8. Fitting the Model.

## 9. Extracting the Actual Stock Prices of Jan-2017.

## 10. Preparing the Input for the Model.

## 11. Predicting the Values

## 12. Plotting the Actual and Predicted Prices

## Conclusion

As you can see above, the model can predict the trend of the actual stock prices very closely. The accuracy of the model can be enhanced by training with more data and increasing the LSTM layers.

The LSTM model can be tuned for various parameters such as changing the number of LSTM layers, adding dropout value, or increasing the number of epochs.
The stock market plays a remarkable role in our daily lives. It is a significant factor in a country's GDP growth.
Time series forecasting is a very intriguing field to work with and can help in predicting more about such fields closely.

## Bibliography

- [Stock market](https://www.wikiwand.com/en/Stock_market)
- [Stock Price Prediction Using Machine Learning: An Easy Guide!](https://www.simplilearn.com/tutorials/machine-learning-tutorial/stock-price-prediction-using-machine-learning)
- [Stock Prices Prediction Using Machine Learning and Deep Learning Techniques (with Python codes)](https://www.analyticsvidhya.com/blog/2018/10/predicting-stock-price-machine-learningnd-deep-learning-techniques-python/#h2_12)