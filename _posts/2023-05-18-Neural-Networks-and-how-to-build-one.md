---
layout: post  
title: "Neural Networks and how to build one"
date: 2023-05-18 00:00:00 
description: ‘A blog demonstrating the python implementation of a simple vanilla neural network with the MNIST hand-written digits dataset.’

tags:
- IEEE NITK
- Neural networks
- MNIST dataset

categories:
- CompSoc

github_username: bleasey
github_username_2: Vignaraj-pai

---

# Neural Networks and how to build one

## Abstract
Neural networks are powerful machine learning models inspired by the human brain. They are the building blocks for tasks such as image recognition, natural language processing, and prediction. In this blog post, we will explore the basics of neural networks and provide an implementation in Python.

### Understanding Neural Networks
Neural networks consist of interconnected nodes called neurons, organized in layers. These layers include an input layer, one or more hidden layers, and an output layer. Each neuron receives input, applies an activation function to it, and passes the output to the next layer.

![Header Image](/blog/assets/img/2023-05-18-Neural-Networks-and-how-to-build-one/2023-05-18-Neural-Networks-and-how-to-build-one-header_img.png) 



The connections between neurons are represented by weights, which determine the strength of the connection. Neural networks learn by adjusting these weights during the training process to minimize the difference between predicted and actual outputs.

#### Input Layer : 
The input layer is the starting point of the neural network. It represents the raw data that is fed into the network. In the case of recognizing handwritten digits, the input layer would receive pixel values of an image representing the digit.
IMAGE
#### Hidden Layer: 
Hidden layers are the intermediate layers between the input and output layers. They perform complex computations and extract features from the input data. Each neuron in a hidden layer receives inputs from the previous layer and applies an activation function to produce an output.

In the context of recognizing handwritten digits, hidden layers help the network learn patterns and representations that are relevant to distinguishing between different digits. These layers enable the network to recognize important features such as curves, edges, and shapes.

| ![Hidden Layers](/blog/assets/img/2023-05-18-Neural-Networks-and-how-to-build-one/2023-05-18-Neural-Networks-and-how-to-build-one-hidden_layers.png) |
| :--: |
|from - [3B1B, Neural Networks](https://www.3blue1brown.com/lessons/neural-networks)|

#### Output Layer: 
The output layer provides the final prediction or output of the neural network. The number of neurons in the output layer depends on the task at hand. In the case of recognizing handwritten digits, there are 10 neurons in the output layer, each representing a digit from 0 to 9.

The output layer applies an activation function that maps the inputs to a probability distribution. In other words, each neuron's output represents the probability that the input belongs to the corresponding digit class. The network's prediction is usually based on the neuron with the highest probability.
 
| ![Ouput Layer](/blog/assets/img/2023-05-18-Neural-Networks-and-how-to-build-one/2023-05-18-Neural-Networks-and-how-to-build-one-output_layer.png) |
| :--: |
|from - [3B1B, Neural Networks](https://www.3blue1brown.com/lessons/neural-networks)|

#### Connections and Weights
Neurons in adjacent layers are connected by weighted connections. These connections transmit information in the form of signals. Each connection is associated with a weight, which determines the strength of the connection. The weights are adjusted during the training process to optimize the network's performance.

During training, the network learns to adjust the weights in such a way that it can differentiate between different digits accurately. By assigning appropriate weights, the network learns to emphasize important features and suppress irrelevant ones.

#### Activation Functions

Activation functions introduce non-linearity to the neural network. They determine the output of a neuron based on its weighted sum of inputs. In the example of recognizing handwritten digits, the activation function helps the network model complex relationships between pixel values and the corresponding digit labels.

In our implementation, we use the sigmoid activation function, which maps the weighted sum to a value between 0 and 1. This value represents the neuron's output or activation level. Other popular activation functions include ReLU (Rectified Linear Unit) and softmax, depending on the specific requirements of the task.
#### Conclusion
Neural networks, with their layered structure and activation functions, enable us to model complex relationships and make accurate predictions. By understanding the role of each layer and the process of adjusting weights, we can build powerful models that excel at recognizing patterns, including handwritten digits.

| ![Conclusion](/blog/assets/img/2023-05-18-Neural-Networks-and-how-to-build-one/2023-05-18-Neural-Networks-and-how-to-build-one-conclusion.png) |
| :--: |
|from - [3B1B, Neural Networks](https://www.3blue1brown.com/lessons/neural-networks)|


In the next section, we will dive into the implementation details of a neural network for recognizing handwritten digits using Python.

### Prerequisites
In this implementation code, we will explore a simple neural network architecture for digit recognition. The code is written in Python and uses libraries such as NumPy, OpenCV, and Matplotlib for data manipulation, image processing, and visualization.

1. Python: Make sure you have Python installed on your system. You can download and install Python from the official Python website (python.org).
2. NumPy: NumPy is a fundamental package for scientific computing with Python. Install it using the package manager pip by running the command pip install numpy.
3. OpenCV: OpenCV is a popular library for image processing and computer vision tasks. Install it using pip install opencv-python.
4. Matplotlib: Matplotlib is a plotting library that helps visualize data and results. Install it using pip install matplotlib.

### Implementation

#### Intializing the neurral network class:

```python
class Network:
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]
```

This section defines the `Network` class, which represents a neural network. Let's break down the code:

- `class Network:`: This line starts the class definition for the `Network` class.

- `def __init__(self, sizes):`: This is the constructor method (initializer) for the `Network` class. It is executed when a new instance of the class is created.

- `self.num_layers = len(sizes)`: The `num_layers` attribute is set to the number of layers in the network, which is determined by the length of the `sizes` list.

- `self.sizes = sizes`: The `sizes` attribute is set to the `sizes` argument passed to the constructor. It represents the number of neurons in each layer of the network.

- `self.biases = [np.random.randn(y, 1) for y in sizes[1:]]`: The `biases` attribute is initialized as a list of bias vectors for each layer (excluding the input layer). Each bias vector is a numpy array of random values drawn from a standard normal distribution (`np.random.randn()`). The size of each bias vector is determined by the number of neurons in the corresponding layer.

- `self.weights = [np.random.randn(y, x) for x, y in zip(sizes[:-1], sizes[1:])]`: The `weights` attribute is initialized as a list of weight matrices for each layer. Each weight matrix is a numpy array of random values drawn from a standard normal distribution. The dimensions of each weight matrix are determined by the number of neurons in the current and next layers.

In summary, this section sets up the initial state of the `Network` class by initializing the number of layers, sizes of each layer, biases (randomly initialized), and weights (randomly initialized) for each layer of the neural network.


#### Forward prop:

```python
def feedforward(self, a):
        for b, w in zip(self.biases[:-1], self.weights[:-1]):
            a = sigmoid(np.matmul(w, a) + b)
        z = np.matmul(self.weights[-1], a) + self.biases[-1]
        se = self.sumofexp(z)
        a = np.multiply(np.exp(z), 1 / se)
        return a
```
Certainly! Let's go through the code snippets and explain what each part does:



1. Loop over the layers (except the output layer):
```python
for b, w in zip(self.biases[:-1], self.weights[:-1]):
    a = sigmoid(np.matmul(w, a) + b)
```
This loop iterates over the biases (`b`) and weights (`w`) of each layer, except the output layer. It performs the following steps for each layer:
   - It calculates the weighted sum of the input `a` by multiplying the weight matrix `w` with the input vector `a` using `np.matmul(w, a)`.
   - It adds the bias vector `b` to the weighted sum using `+ b`.
   - It applies the sigmoid function (`sigmoid()`) to the result. The sigmoid function "squashes" the value to a range between 0 and 1, representing the activation level of the neuron. The result is assigned back to `a`, overwriting the previous value.

2. Calculate the output layer activations:
```python
z = np.matmul(self.weights[-1], a) + self.biases[-1]
se = self.sumofexp(z)
a = np.multiply(np.exp(z), 1 / se)
```
   - It calculates the weighted sum of the output layer by multiplying the weights of the output layer (`self.weights[-1]`) with the activations `a` obtained from the previous loop. It then adds the bias vector of the output layer (`self.biases[-1]`) to the result. The result is assigned to `z`.
   - It calculates the sum of exponentials of `z` using the `sumofexp()` method and assigns it to `se`.
   - It applies the softmax function to the weighted sum `z` using `np.exp(z)`. This exponentiates each value in `z`.
   - It normalizes the exponentiated values by multiplying them by `1 / se`. This ensures that the values sum up to 1, representing probabilities of different classes.
   - The resulting array `a` contains the probabilities of each class.

3. Return the output layer activations:
```python
return a
```
The method returns the array `a`, which represents the output layer activations or the predicted probabilities for each class.

In summary, the code performs calculations on the input data using weights and biases. It applies the sigmoid function to calculate activations for each layer, except the output layer. Finally, it calculates the output layer activations using the softmax function and returns the predicted probabilities for each class.

#### Defining essential functions:

##### Sigmoid and its derivative:

```
def sigmoid(z):
    return (1.0/(1.0 + np.exp(-z)))

def sigmoid_prime(z):
    return sigmoid(z) * (1 - sigmoid(z))
```

1. Sigmoid function:
```python
def sigmoid(z):
    return (1.0 / (1.0 + np.exp(-z)))
```
The sigmoid function takes an input `z` and returns the output of the sigmoid activation function. The sigmoid function "squashes" the input value to a range between 0 and 1. It's defined as the reciprocal of 1 plus the exponential of the negative input value. In simpler terms, it transforms the input into a probability-like value, with values closer to 1 indicating a higher activation level.

2. Sigmoid derivative function:
```python
def sigmoid_prime(z):
    return sigmoid(z) * (1 - sigmoid(z))
```
The sigmoid_prime function calculates the derivative of the sigmoid function with respect to its input `z`. The derivative of the sigmoid function can be expressed in terms of the sigmoid function itself. It multiplies the sigmoid function of `z` by `1 - sigmoid(z)`. The derivative represents the rate of change of the sigmoid function at a particular input value `z`.

These functions are crucial for the neural network because the sigmoid activation function is commonly used to introduce non-linearity and model the activation levels of neurons. The sigmoid_prime function is used during the backpropagation process to calculate gradients and update the weights and biases of the network.

In summary, the `sigmoid` function applies the sigmoid activation function to an input, while the `sigmoid_prime` function calculates the derivative of the sigmoid function with respect to its input. These functions play a vital role in the activation and learning processes of the neural network.

##### Utility Functions:

```
def costDerivative(self, outActivation, y):
    return (np.add(outActivation, np.multiply(y, -1)))

def sumofexp(self, a):
    b = np.exp(a)
    return np.sum(b)

def vOneAt(j):
    vec = np.zeros((10, 1))
    vec[j] = 1.0
    return vec
```

1. Cost derivative function:
```python
def costDerivative(self, outActivation, y):
    return (np.add(outActivation, np.multiply(y, -1)))
```
The `costDerivative` function calculates the derivative of the cost with respect to the output activations. In other words, it determines how much the output activations need to change to minimize the difference between the predicted output and the expected output (`y`). It subtracts the expected output from the predicted output by multiplying `y` with `-1` and adding it to `outActivation`.

1. Sum of exponentials function:
```python
def sumofexp(self, a):
    b = np.exp(a)
    return np.sum(b)
```
The `sumofexp` function calculates the sum of exponentials of the input array `a`. It exponentiates each element of `a` using the exponential function (`np.exp`) and then computes the sum of all the exponentiated values. This function is used in the softmax activation function to normalize the output probabilities.

1. One-hot vector function:
```python
def vOneAt(j):
    vec = np.zeros((10, 1))
    vec[j] = 1.0
    return vec
```
The `vOneAt` function generates a one-hot encoded vector for a given index `j`. A one-hot vector is a binary representation where only one element is `1` (indicating the desired index) and all other elements are `0`. In this case, the vector has a length of 10, and the element at index `j` is set to `1`, while all other elements are `0`. This function is used to encode the expected output labels in a suitable format for training and evaluation.

These utility functions serve specific purposes within the neural network implementation. The `costDerivative` function is used during the backpropagation process to compute the gradients, the `sumofexp` function is employed in the softmax activation function to normalize probabilities, and the `vOneAt` function assists in creating one-hot encoded vectors for target labels.

In summary, these functions contribute to the functionality and calculations involved in training and evaluating the neural network.


#### Backprop:

```python
def backprop(self, x, pre_y):
        grad_b = [np.zeros(b.shape) for b in self.biases]
        grad_w = [np.zeros(w.shape) for w in self.weights]

        y = np.array(pre_y).reshape((10, 1))
        activation = np.array(x).reshape((784, 1))
        activations = [activation]
        zs = []
        for b, w in zip(self.biases, self.weights):
            z = np.matmul(np.array(w), np.array(activation)) + b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)

        se = self.sumofexp(zs[-1])
        finaloutput = np.multiply(np.exp(z), 1 / se)
        activations[-1] = finaloutput

        error = np.multiply(self.costDerivative(activations[-1], y), 1)

        grad_b[-1] = error
        grad_w[-1] = np.matmul(error, np.array(activations[-2]).transpose())

        for l in range(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            error = np.multiply(np.matmul(self.weights[-l+1].transpose(), error), sp)
            grad_b[-l] = error
            grad_w[-l] = np.matmul(error, np.array(activations[-l-1]).transpose())
        
        return grad_b, grad_w

```
1. Gradient initialization:
```python
grad_b = [np.zeros(b.shape) for b in self.biases]
grad_w = [np.zeros(w.shape) for w in self.weights]
```
These lines initialize `grad_b` and `grad_w` as lists of arrays with the same shapes as biases and weights, respectively. They will store the gradients for each layer of the network.

2. Data preparation:
```python
y = np.array(pre_y).reshape((10, 1))
activation = np.array(x).reshape((784, 1))
activations = [activation]
zs = []
```
These lines prepare the data by reshaping `pre_y` into a column vector `y` with shape (10, 1) and `x` into a column vector `activation` with shape (784, 1). `activations` is initialized as a list with the first element being the input activation. `zs` will store the weighted inputs for each layer.

3. Forward propagation:
```python
for b, w in zip(self.biases, self.weights):
    z = np.matmul(np.array(w), np.array(activation)) + b
    zs.append(z)
    activation = sigmoid(z)
    activations.append(activation)
```
This loop performs the forward propagation step. It iterates over the biases and weights, calculating the weighted inputs `z` for each layer by taking the dot product of weights and activations, and then adding the corresponding bias. These `z` values are stored in the `zs` list. The sigmoid activation function is applied to each `z` value, producing the activations for each layer, which are stored in the `activations` list.

4. Softmax activation:
```python
se = self.sumofexp(zs[-1])
finaloutput = np.multiply(np.exp(z), 1 / se)
activations[-1] = finaloutput
```
These lines modify the output activations of the last layer using the softmax function. The `sumofexp` method calculates the sum of the exponential values of the last layer's weighted inputs `zs[-1]`, and then the final output activations are obtained by multiplying the exponential of `z` with the reciprocal of the sum.

5. Error calculation:
```python
error = np.multiply(self.costDerivative(activations[-1], y), 1)
```
Here, the error is computed by multiplying the cost derivative with 1. The `costDerivative` method calculates the derivative of the cost function with respect to the output activations.

6. Gradient calculation:
```python
grad_b[-1] = error
grad_w[-1] = np.matmul(error, np.array(activations[-2]).transpose())
```
These lines assign the error to the last element of `grad_b`, representing the gradients of the output layer biases. The gradients of the output layer weights are calculated by multiplying the error with the transpose of the previous layer's activations.

7. Backpropagation:
```python
for l in range(2, self.num_layers):
    z = zs[-l]
    sp = sigmoid_prime(z)
    error = np.multiply(np.matmul(self.weights[-l+1].transpose(), error), sp)
    grad_b[-l] = error
    grad_w[-l] = np.matmul(error, np.array(activations[-l-1]).transpose())
```
This loop performs the backward propagation step. It iterates from the second-to-last layer (`self.num_layers - 1`) to the second layer (`2`). For each layer, it updates the error by multiplying the error from the next layer with the derivative of the sigmoid function applied to the weighted input `z`. The updated error is then assigned to the corresponding element in `grad_b`. The gradients of the weights for each layer are calculated by multiplying the updated error with the transpose of the previous layer's activations.

```python
return grad_b, grad_w
```
Finally, the gradients `grad_b` and `grad_w` are returned, representing the gradients of biases and weights, respectively, computed through backpropagation. These gradients will be used to update the weights and biases during the training process.

#### Training:

```python
def train(self, data, lrate, lmda):
        epochs = 10
        itr = epochs * len(data)
        eta = lrate
        for k in range (0, epochs):
            random.shuffle(data)
            for x, y in data:
                grad_b, grad_w = self.backprop(x, y)
                self.weights = [w * (1 - eta * lmda) - eta * gw for w, gw in zip(self.weights, grad_w)]
                self.biases = [b - eta * gb for b, gb in zip(self.biases, grad_b)]
                eta = np.max([eta - (lrate / (itr)), 0])
```

1. Setting up variables:
```python
epochs = 10
itr = epochs * len(data)
eta = lrate
```
Here, we define the number of training epochs as `10`. The `itr` variable represents the total number of iterations by multiplying the number of epochs with the size of the training data. The learning rate `eta` is initialized with the provided learning rate `lrate`.

2. Training loop:
```python
for k in range(0, epochs):
    random.shuffle(data)
    for x, y in data:
        grad_b, grad_w = self.backprop(x, y)
        self.weights = [w * (1 - eta * lmda) - eta * gw for w, gw in zip(self.weights, grad_w)]
        self.biases = [b - eta * gb for b, gb in zip(self.biases, grad_b)]
        eta = np.max([eta - (lrate / (itr)), 0])
```
This loop performs the training process. It iterates over the specified number of `epochs`.

a. Data shuffling:
```python
random.shuffle(data)
```
Before each epoch, we shuffle the training data to introduce randomness in the order of training examples. This helps the neural network generalize better.

b. Iterating over training examples:
```python
for x, y in data:
    grad_b, grad_w = self.backprop(x, y)
    self.weights = [w * (1 - eta * lmda) - eta * gw for w, gw in zip(self.weights, grad_w)]
    self.biases = [b - eta * gb for b, gb in zip(self.biases, grad_b)]
    eta = np.max([eta - (lrate / (itr)), 0])
```
For each training example `x` and its corresponding expected output `y`, we perform the following steps:

- Backpropagation: We calculate the gradients of the biases and weights using the `backprop` method. The `backprop` method takes an input `x` and its corresponding expected output `y` and computes the gradients using the backpropagation algorithm.

- Weight and bias updates: Using the gradients, we update the weights and biases of the neural network. The new values are calculated using the learning rate `eta`, the regularization parameter `lmda`, and the gradients. This step applies the gradient descent optimization algorithm to adjust the network's parameters.

- Learning rate decay: After each example, we update the learning rate `eta` to gradually decrease it over time. This helps in fine-tuning the training process. The learning rate is reduced by subtracting a fraction of the initial learning rate `lrate` divided by the total number of iterations `itr`. The learning rate is clipped to a minimum value of `0` to prevent negative values.

By repeating this process for the specified number of epochs, the neural

 network learns to make better predictions on the training data and improves its ability to generalize to unseen data.

Overall, the `train` method encapsulates the training process, including data shuffling, forward propagation, backpropagation, weight and bias updates, and learning rate decay.

#### Image preprocessing and loading:
```
def preprocessimage(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.resize(img, [28, 28])
    return img

def loadData(root):
    images = []
    y = []
    for i in range(0, 10):
        folder = root + "/" + str(i)
        for filename in os.listdir(folder):
            img = cv.imread(os.path.join(folder,filename))
            if img is not None:
                images.append(preprocessimage(img))
                y.append(vOneAt(i))
    return images, y
```

1. Image preprocessing:
```python
def preprocessimage(img):
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.resize(img, [28, 28])
    return img
```
The `preprocessimage` function takes an image `img` as input and performs the following steps to preprocess it:

- Convert to grayscale: The `cv.cvtColor` function is used to convert the image from BGR (Blue-Green-Red) color space to grayscale. This reduces the image's color channels from 3 to 1, which simplifies further processing.

- Resize the image: The `cv.resize` function is used to resize the image to a specific size of [28, 28]. This ensures that all input images have the same dimensions, which is typically required for neural network models.

The function then returns the preprocessed image.

2. Loading image data:
```python
def loadData(root):
    images = []
    y = []
    for i in range(0, 10):
        folder = root + "/" + str(i)
        for filename in os.listdir(folder):
            img = cv.imread(os.path.join(folder,filename))
            if img is not None:
                images.append(preprocessimage(img))
                y.append(vOneAt(i))
    return images, y
```
The `loadData` function loads and preprocesses the image data for training the neural network. It takes a `root` directory path as input, which is the root directory where the image data is stored.

- Iterating over class folders: The function iterates over each class label (from 0 to 9) using the outer `for` loop. It constructs the folder path for each class using the `root` directory and the class label.

- Iterating over image files: For each class folder, the function iterates over the image files using the inner `for` loop. It reads each image file using the `cv.imread` function, which reads the image in BGR format.

- Preprocessing and storing images: If the image is successfully loaded (`img is not None`), it is preprocessed using the `preprocessimage` function. The preprocessed image is then appended to the `images` list.

- Creating labels: The function uses the `vOneAt` function (explained earlier) to create a one-hot encoded label vector for each image. The label vector represents the class label of the image. The one-hot encoding ensures that the network can learn to predict the correct class.

Finally, the function returns two lists: `images` containing the preprocessed image data and `y` containing the corresponding labels.

These functions work together to preprocess and load the image data required for training the neural network. The `preprocessimage` function converts the images to grayscale and resizes them, while the `loadData` function iterates over the image files, preprocesses them, and creates the appropriate labels.

#### Shuffling:

```python
def shuffle(a, b):
    k = np.array(b).shape[0]
    p = np.random.permutation(k)
    return a[p], b[p]
```
The `shuffle` function is used to randomly shuffle two arrays `a` and `b` in the same order. It takes two arrays `a` and `b` as input and returns the shuffled arrays `a[p]` and `b[p]`.

- Determining the size: The function first determines the size of array `b` using `np.array(b).shape[0]`. This is done to ensure that both arrays `a` and `b` have the same number of elements. Here, `np.array(b)` is used to convert `b` into a NumPy array, and `shape[0]` retrieves the number of elements along the first axis (assuming `b` is a 2D array).

- Generating a random permutation: The function then uses `np.random.permutation(k)` to generate a random permutation of integers from 0 to `k-1`. The `k` value represents the number of elements in array `b`.

- Shuffling the arrays: The permutation generated in the previous step is used to shuffle the arrays `a` and `b`. By indexing `a[p]` and `b[p]`, the elements of both arrays are rearranged in the same order specified by the permutation.

- Returning shuffled arrays: Finally, the function returns the shuffled arrays `a[p]` and `b[p]`, where `a` and `b` are now in the same random order.

The `shuffle` function is commonly used in machine learning tasks to randomize the order of training data and corresponding labels. This randomness helps prevent any systematic biases that may arise from having a specific order in the data.

#### Data prep:

```python
def dataprep(images):
    finaldata = []
    for arr in images:
        arrimg = np.array(arr).flatten()
        arrimg = np.multiply(arrimg, 1.0/255.0)
        finaldata.append(arrimg)
    return finaldata
```
The `dataprep` function is used to prepare the image data for training or testing.

- Iterating over images: The function takes a list of images as input, which are typically preprocessed images.

- Flattening the image: For each image `arr` in the list, the function uses `np.array(arr).flatten()` to convert the image into a 1-dimensional array. This is done to create a flat representation of the image, where each pixel value is a separate element in the array.

- Normalizing pixel values: The function then normalizes the pixel values of the flattened image by dividing each element by 255.0. This step is performed using `np.multiply(arrimg, 1.0/255.0)`. The purpose of this normalization is to scale the pixel values between 0 and 1, which can help improve the training process of the neural network.

- Building the final data: The normalized flattened image, `arrimg`, is added to the `finaldata` list using `finaldata.append(arrimg)`.

- Returning the prepared data: Once all the images have been processed, the function returns the `finaldata` list, which contains the flattened and normalized images ready for further processing or training.

The `dataprep` function is commonly used to preprocess the image data before feeding it into a neural network. Flattening the images and normalizing the pixel values are common preprocessing steps to ensure the data is in a suitable format for training or inference.

#### Train:

```python
def test(network, root):
    correct = 0
    total = 0
    y = []
    for i in range(0, 10):
        folder = root + "/" + str(i)
        for filename in os.listdir(folder):
            img = cv.imread(os.path.join(folder,filename))
            if img is not None:
                img = preprocessimage(img)
                img = np.array(img).flatten()
                img = np.multiply(img, 1.0/255.0)
                img = np.array(img).reshape((784, 1))
                ans = network.feedforward(img)
                if(np.argmax(ans) == i):
                    correct = correct + 1
                total = total + 1
    return (correct / total , correct, total)
```

- Initializing counters: Two variables, `correct` and `total`, are set to 0. These will be used to keep track of the number of correctly classified images and the total number of images, respectively.

- Iterating over test images: The function iterates over the test dataset, which is organized in subfolders labeled with class names ranging from 0 to 9. The outer loop runs through each class using `range(0, 10)`. Within the class loop, it prepares the path to the current class's folder using `root + "/" + str(i)`.

- Reading and preprocessing images: For each class, the function iterates over the image files in the corresponding folder using `os.listdir()`. It reads each image using `cv.imread()` and stores it in the `img` variable. 

- Preprocessing the test image: The `img` is then passed to the `preprocessimage()` function, which converts the image to grayscale and resizes it to 28x28 pixels. The preprocessed image is stored back in `img`.

- Normalizing the image: The preprocessed image is flattened into a 1-dimensional array using `np.array(img).flatten()`. Then, each pixel value is normalized by multiplying it with `1.0/255.0`, ensuring that the pixel values range from 0 to 1.

- Reshaping the image: After normalization, the flattened image is reshaped into a column vector of size 784x1 using `np.array(img).reshape((784, 1))`. This reshaped vector matches the input shape expected by the neural network.

- Forward propagation and prediction: The preprocessed image is passed through the trained neural network using `network.feedforward(img)`. It computes the forward propagation of the image through the network and returns the output activation, `ans`, which represents the predicted probabilities for each class.

- Checking correctness: The function compares the index of the maximum probability in `ans` (predicted label) with the true label `i` to check if the prediction is correct. If the prediction matches the true label, the `correct` counter is incremented.

- Updating total count: Regardless of whether the prediction is correct or not, the `total` counter is incremented for each processed image.

- Returning evaluation metrics: After evaluating all the test images, the function returns a tuple `(accuracy, correct, total)`. The accuracy is calculated as the ratio of correctly classified images (`correct`) to the total number of images (`total`).

By running the `test` function on a trained neural network and a test dataset, you can assess the accuracy and performance of the network on unseen data.


#### Training the Neural Network with Preprocessed Data:

```python
images, y = loadData('train')
images = np.array(images, dtype = np.float32)
y = np.array(y)
images, y = shuffle(images, y)
train_data = dataprep(images)
train_data = np.array(train_data)
final_train_data = [(img, x) for img, x in zip(train_data, y)]

network = Network([784, 16, 16, 10])
network.train(final_train_data, 0.6, 0.0007)
```

```python
images, y = loadData('train')
images = np.array(images, dtype=np.float32)
y = np.array(y)
```

- `images, y = loadData('train')`: This line loads the training dataset using the `loadData` function. The images are stored in the `images` variable, and the corresponding labels are stored in the `y` variable.

- `images = np.array(images, dtype=np.float32)`: The `images` array is converted to a NumPy array with the data type set as `np.float32`. This step is often performed to ensure numerical compatibility and efficient computation.

- `y = np.array(y)`: The `y` array, which represents the labels, is also converted to a NumPy array.

```python
images, y = shuffle(images, y)
train_data = dataprep(images)
train_data = np.array(train_data)
final_train_data = [(img, x) for img, x in zip(train_data, y)]
```

- `images, y = shuffle(images, y)`: The `shuffle` function is called with the `images` and `y` arrays to randomly shuffle the order of the images and their corresponding labels. This is often done to introduce randomness during training.

- `train_data = dataprep(images)`: The `dataprep` function is applied to the shuffled `images` array to preprocess the images. This typically involves converting the images to grayscale, resizing them, and normalizing the pixel values.

- `train_data = np.array(train_data)`: The preprocessed `train_data` array is converted to a NumPy array.

- `final_train_data = [(img, x) for img, x in zip(train_data, y)]`: This line creates a list `final_train_data` by pairing each preprocessed image (`img`) with its corresponding label (`x`) using the `zip` function. Each element in `final_train_data` is a tuple containing an image and its label.

```python
network = Network([784, 16, 16, 10])
network.train(final_train_data, 0.6, 0.0007)
```

- `network = Network([784, 16, 16, 10])`: A new neural network is instantiated using the `Network` class, specifying the layer sizes as `[784, 16, 16, 10]`. This means the network has an input layer of size 784, two hidden layers of size 16 each, and an output layer of size 10.

- `network.train(final_train_data, 0.6, 0.0007)`: The `train` method of the `network` object is called to train the neural network using the `final_train_data` as the training dataset. The parameters passed are the learning rate (`0.6`) and the regularization parameter (`0.0007`). This function applies the backpropagation algorithm to update the weights and biases of the network based on the provided training data.

Overall, this final section of code loads the training dataset, shuffles the data, preprocesses the images, creates a training dataset with labels, instantiates a neural network, and trains it using the training data. It represents the process of training a neural network for a classification task.


#### Testing and Evaluation:
```python
test_images, test_y = loadData('test')
test_images = np.array(test_images, dtype=np.float32)
test_y = np.array(test_y)

accuracy, correct, total = test(network, 'test')

print(f"Accuracy: {accuracy * 100}%")
print(f"Correct predictions: {correct}")
print(f"Total images: {total}")
```
In this section, the loadData function is used to load the test images and their corresponding labels from the 'test' directory. The test images are then converted into a numpy array and preprocessed using the preprocessimage function.

Next, the test function is called to perform the testing. It takes the trained network and the path to the 'test' directory as input. The function iterates over the test images, preprocesses each image, feeds it to the network using network.feedforward, and compares the predicted class with the actual class to calculate the accuracy and the number of correct predictions.

Finally, the accuracy, number of correct predictions, and total number of images are printed to evaluate the performance of the network on the test dataset.

By running this section, you can obtain the accuracy of the network on the test dataset and analyze how well it performs in classifying the test images.

## Conclusion

In this tutorial, you learned how to build a neural network from scratch using Python. You implemented the backpropagation algorithm to train the network and used it to classify handwritten digits from the MNIST dataset. You also learned how to preprocess the images and evaluate the performance of the network on the test dataset.

Implementation on [Github]((https://github.com/Wolfram70/MNIST-Classifier)) by [Srinivasa R](https://www.linkedin.com/in/srinivasar-wolfram/)

You can use the same code to train a neural network on other datasets and perform classification tasks. You can also modify the code to build a neural network for regression tasks. You can experiment with different network architectures, hyperparameters, and optimization algorithms to improve the performance of the network.


## References

- [3B1B, Neural Networks](https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
- [Neural Network from scratch in Python, Omar Aflak](https://towardsdatascience.com/math-neural-network-from-scratch-in-python-d6da9f29ce65)


