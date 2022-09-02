```
 ---
 layout: post
 title: "Semi Supervised Learning"
 author_github: Vaish-922
 date: 2017-05-14 23:32:44
 image: '/assets/img/'
 description: 'Semi Supervised Learning'
 tags:
 - IEEE NITK
 - Blog
 categories:
 - CompSoc
 github_username: 'Vaish-922'
 ---
```

Machine Learning is broadly classified into three main categories - 
1. Supervised Learning - used when all the available data is annotated
2. Unsupervised Learning - no annotated data is available
3. Semi Supervised Learning. 

Supervised Learning includes models like linear regression, whereas unsupervised has logistic regression. Semi-supervised Learning falls between unsupervised Learning (with no labelled training data) and supervised Learning (with only labelled training data). It is a remarkable instance of weak supervision. 

  
  

Semi Supervised Learning (SSL) is an upcoming field that is gaining popularity day by day. It is an approach to machine learning that combines a small amount of labelled data with a large amount of unlabeled data during training. When labelled data isn’t available due to various reasons, unlabeled data when used in conjunction with a small amount of labelled data can produce considerable improvement in training accuracy. The collection of labelled data for a learning problem often requires a skilled human agent or a physical experiment. Since the cost of acquiring labelled data is very high, it renders these training sets infeasible, whereas the collection of unlabeled data is relatively inexpensive. The best example of this is medical images such as X-Rays. Getting labelled X-ray images involves a lot of time to be spent by the doctors which isn’t feasible. In such situations, semi-supervised Learning can be of great practical value. Semi-supervised Learning is also of theoretical interest in machine learning and as a human learning model.

  

A Semi-Supervised algorithm assumes the following about the data:

  

1.  **Continuity Assumption:** The algorithm assumes that the points which are closer to each other are more likely to have the same output label.
    
2.  **Cluster Assumption:** The data can be divided into discrete clusters and points in the same group are more likely to share an output label.
    
3.  **Manifold Assumption:** The data lie approximately on a manifold of a much lower dimension than the input space. This assumption allows the use of distances and densities which are defined on a manifold.
    

  

The basic working of an SSL model is as given:

-   Train the model with the small amount of labelled training data just like you would in supervised Learning until it gives you good results.
    
-   Then use it with the unlabeled training dataset to predict the outputs, which are pseudo labels since they may not be entirely accurate.
    
-   Link the labels from the labelled training data with the pseudo labels created in the previous step.
    
-   Link the data inputs in the labelled training data with the inputs in the unlabeled data.
    
-   Then, train the model the same way you did with the labelled set in the beginning in order to decrease the error and improve the model’s accuracy.

The above method is commonly known as the self training method or psuedo label method. However, this method becomes heavily dataset dependent and in some cases might reduce accuracy by a great extent. 

The algorithm for psuedo label is as follows:

Pseudo-Label are target classes for unlabeled data as if they were true labels. The class, which has maximum predicted probability predicted using a network for each unlabeled sample, is picked up:


    

SSL is used in various aspects of our lives nowadays. Its most common practical uses include Speech Analysis, Web Content Classification, Protein Sequence Classification, Text Document Classifier, etc.

References:
[1] https://en.wikipedia.org/wiki/Semi-supervised_learning#:~:text=Semi%2Dsupervised%20learning%20is%20an,with%20only%20labeled%20training%20data)
[2] https://www.geeksforgeeks.org/ml-semi-supervised-learning/
