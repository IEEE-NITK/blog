---
layout: post
title: Text Generation using RNN
author_github: ChinmayaSharma-hue
date: 2022-07-15 00:00:00
description: 'A text generation model that trains over a book and generates text in the style of writing of the book.'
tags:
- IEE NITK
- Blog
- Deep Learning
- Sequential Models
- RNNs
- LSTMs

categories:
- Diode

github_username: 'ChinmayaSharma-hue'
---

# Text Generation using RNN
Long-short-term memory models, or LSTMs, employ gates to control the flow of information 
to tackle the problem of short-term memory. These models feature procedures for deciding 
whether or not to maintain the information, allowing them to keep vital data for a long period. 
They are widely employed in machine translation, speech recognition, handwriting recognition 
and creation, language modeling and translation, speech synthesis, and many other deep 
learning applications due to their capacity to learn long-term dependencies.

Using LSTM, we can build a model and train it to generate text in the style of the text used
to train the model.

To build, train and run the model, the following things need to be done.
1. Data Pre-processing involves the following steps,
    - Take a novel or any other form of literature in the form of a text file, and load it into the program in the form of a string. By assigning numbers to each character, we can represent the text in the form of numbers so that it can be passed through the model. This is what is done in tokenization. 
    - Make mini-batches out of the pre-processed data for batch learning. 
2. Define the LSTM model that can be trained on the data, and then train the model for a desired number of epochs. Tune the hyperparameters to get the best result out of the model.
3. Define a predict function that instantiates the model, takes in the argument string (the initial word that the user provides), and then predicts the desired number of characters succeeding the initial word.

All in all, the data is pre-processed to be represented in the form of numbers, then the model is trained on this data in the form of mini-batches, and then a prompt word is sent to the model which then predicts the next character based on the data it has been trained on.

### Import Resources
```buildoutcfg
import numpy as np
import torch
from torch import nn
import torch.nn.functional as F
```

### Load in Data
```buildoutcfg
# open text file and read in data as `text`
with open('data/anna.txt', 'r') as f:
    text = f.read()
```
The novel Anna Karenina is used to train this character-wise RNN. That needs to be loaded. All the characters from the text file are loaded onto the string, txt.

### Tokenization
```buildoutcfg
chars = tuple(set(text))
int2char = dict(enumerate(chars))
char2int = {ch: ii for ii, ch in int2char.items()}

# encode the text
encoded = np.array([char2int[ch] for ch in text])
```
1. ``set(text)`` casts the string datatype which is ``text`` into a set, which removes all duplicate characters, and then this is cast into a tuple.
2. `enumerate(chars)` assigns a number for each character in the tuple, which is used as the numerical equivalent of each character to be sent through the model after encoding, and this is cast into a dictionary as casting it into a list gives a list of tuples with the number and the corresponding character. This gives a dictionary mapping from numbers to characters.
3. Through dictionary comprehension, another dictionary is created which gives a mapping from character to number. Using these two dictionaries, it is possible to obtain the number equivalent for a character and vice versa
4. The characters in the text string are encoded by obtaining their numerical equivalent from the character to integer dictionary, which is then cast into a `numpy` array.

### Pre-processing the data
To send the data through the model, each input needs to be one-hot encoded,
```buildoutcfg
def one_hot_encode(arr, n_labels):
    
    # Initialize the encoded array
    one_hot = np.zeros((arr.size, n_labels), dtype=np.float32)
    
    # Fill the appropriate elements with ones
    one_hot[np.arange(one_hot.shape[0]), arr.flatten()] = 1.
    
    # Finally reshape it to get back to the original array
    one_hot = one_hot.reshape((*arr.shape, n_labels))
    
    return one_hot
```
1. In `one_hot = np.zeros((arr.size, n_labels), dtype=np.float32)`, a zero matrix is created that has **as many rows as the number of elements in the encoded array**, each row having as many elements as the number of labels. Each row can be changed to a one-hot vector for each of the corresponding elements in the encoded array. 
2. In `one_hot[np.arange(one_hot.shape[0]), arr.flatten()] = 1`, 
    1. `np.arange(one_hot.shape[0])`, 
        1. `one_hot.shape[0]` gives the number of rows in the one-hot vector created in the last step,
        2. `np.arange()` is used to obtain evenly spaced values in a given interval. For eg., `np.arange(3)` gives `[0,1,2]`. As the argument given is the number of elements in the encoded array/number of rows in the one-hot vector, it gives a list of integers from 0 to that number. 
    2. `arr.flatten()` returns a copy of the array collapsed into one dimension. Therefore, the output will have a single dimension, i.e., a single row with all the elements of the matrix in that row.
    
    Through indexing, the first argument is used to invoke each of the rows, the second argument is used to invoke the element in that row which has an index equal to the numerical values in $arr$, which is supposed to be the encoded array when this function is used for one-hot encoding.
    
3. In `one_hot = one_hot.reshape((*arr.shape, n_labels))` , the shape of the matrix with a one-hot vector is reshaped to the shape of the encoded array.

### Making Training mini-batches
```buildoutcfg
def get_batches(arr, batch_size, seq_length):
    '''Create a generator that returns batches of size
       batch_size x seq_length from arr.
       
       Arguments
       ---------
       arr: Array you want to make batches from
       batch_size: Batch size, the number of sequences per batch
       seq_length: Number of encoded chars in a sequence
    '''
    
    batch_size_total = batch_size * seq_length
    # total number of batches we can make
    n_batches = len(arr)//batch_size_total
    
    # Keep only enough characters to make full batches
    arr = arr[:n_batches * batch_size_total]
    # Reshape into batch_size rows
    arr = arr.reshape((batch_size, -1))
    
    # iterate through the array, one sequence at a time
    for n in range(0, arr.shape[1], seq_length):
        # The features
        x = arr[:, n:n+seq_length]
        # The targets, shifted by one
        y = np.zeros_like(x)
        try:
            y[:, :-1], y[:, -1] = x[:, 1:], arr[:, n+seq_length]
        except IndexError:
            y[:, :-1], y[:, -1] = x[:, 1:], arr[:, 0]
        yield x, y
```
1. **The first thing we need to do is discard some of the text so we **only have full mini-batches**.**
    1. `batch_size_total` which is the total batch size is the product of the number of sequences 
       in a batch and the number of elements in each sequence is calculated first.
    2. `n_batches`  which is used to calculate how many batches can be made from the data 
       by getting an integer as the quotient of the division of the total size of the data 
       and the number of elements in each batch.
    3. The data is redefined to contain only as many elements as can be used to make the 
       required number of batches. The elements, in the end, are omitted.
2. **After that, we need to split `arr` into `N` batches.**
    1. `N` is the number of sequences in each batch which is represented by `batch_size` that
       is sent to the function. This is taken as the first dimension of the data by reshaping
       the data to divide it into as many rows as the number of sequences. 
3. **Now that we have this array, we can iterate through it to get our mini-batches.** <br>
       Since this is a generator function, we can iterate over the data and send a single 
       minibatch each time. We can use the range function for the division of the data into mini-batches. We can set a variable $n$ that ranges between 0 and the total number 
       of elements in each (full) sequence/each 'batch', and increments by the sequence 
       length, `seq_length` .
### Defining the network
```buildoutcfg
class CharRNN(nn.Module):
    
    def __init__(self, tokens, n_hidden=256, n_layers=2,
                               drop_prob=0.5, lr=0.001):
        super().__init__()
        self.drop_prob = drop_prob
        self.n_layers = n_layers
        self.n_hidden = n_hidden
        self.lr = lr
        
        # creating character dictionaries
        self.chars = tokens
        self.int2char = dict(enumerate(self.chars))
        self.char2int = {ch: ii for ii, ch in self.int2char.items()}
        
        ## define the LSTM
        self.lstm = nn.LSTM(len(self.chars), n_hidden, n_layers, 
                            dropout=drop_prob, batch_first=True)
        
        ## define a dropout layer
        self.dropout = nn.Dropout(drop_prob)
        
        ## define the final, fully-connected output layer
        self.fc = nn.Linear(n_hidden, len(self.chars))
      
    
    def forward(self, x, hidden):
        ''' Forward pass through the network. 
            These inputs are x, and the hidden/cell state `hidden`. '''
                
        ## Get the outputs and the new hidden state from the lstm
        r_output, hidden = self.lstm(x, hidden)
        
        ## pass through a dropout layer
        out = self.dropout(r_output)
        
        # Stack up LSTM outputs using view
        # you may need to use contiguous to reshape the output
        out = out.contiguous().view(-1, self.n_hidden)
        
        ## put x through the fully-connected layer
        out = self.fc(out)
        
        # return the final output and the hidden state
        return out, hidden
    
    
    def init_hidden(self, batch_size):
        ''' Initializes hidden state '''
        # Create two new tensors with sizes n_layers x batch_size x n_hidden,
        # initialized to zero, for hidden state and cell state of LSTM
        weight = next(self.parameters()).data
        
        if (train_on_gpu):
            hidden = (weight.new(self.n_layers, batch_size, self.n_hidden).zero_().cuda(),
                  weight.new(self.n_layers, batch_size, self.n_hidden).zero_().cuda())
        else:
            hidden = (weight.new(self.n_layers, batch_size, self.n_hidden).zero_(),
                      weight.new(self.n_layers, batch_size, self.n_hidden).zero_())
        
        return hidden
```
1. In the `_init_` method,
    1. The arguments that are taken in the `_init_` method are tokens which are the inputs, 
       `n_hidden` which is the dimension of the hidden state, `n_layers` which is the 
       number of LSTM layers that are stacked upon one another, `drop_prob` which is the 
       dropout probability to be used in dropout layer, `lr` which is the learning rate used
       in training.
    2.  The `super().__init__()` **super** corresponds to the methods and attributes of
        the parent class, it is used to initialize the methods and attributes of the parent 
        class `(nn.Module())`.
    4. The character dictionaries are created to convert characters to integers and vice
       versa. 
    5. The LSTM layer is defined as a network parameter.
    6. The dropout layer is defined using the dropout parameter.
    7. A fully connected layer, which is the last layer, is defined, with the arguments as 
       the input dimension which is the hidden state dimension which is the output of the 
       LSTM layers, and the output dimension which is the same as the dimension of the 
       inputs passed into the network.
2. In the `forward` method,
    1. The input and the initial hidden state are passed through the LSTM layer, and the 
       output and the final hidden state are obtained.
    2. The output is then passed through the dropout layer.
    3. The output is reshaped before it is passed through the fully connected layer, as the 
       output is of the dimension `(self.n_layers,batch_size,self.n_hidden)` and it is 
       squished. 
        
    4. The reshaped output is passed through the fully connected layer to obtain the final 
       output.
    5. The final output and the final hidden state are returned from this method. 
3. In the `init_hidden` method,
    1. The hidden tuple which consists of the hidden state and the cell state is initialized to zero.

### Training the model
```buildoutcfg
def train(net, data, epochs=10, batch_size=10, seq_length=50, lr=0.001, clip=5, val_frac=0.1, print_every=10):
    ''' Training a network 
    
        Arguments
        ---------
        
        net: CharRNN network
        data: text data to train the network
        epochs: Number of epochs to train
        batch_size: Number of mini-sequences per mini-batch, aka batch size
        seq_length: Number of character steps per mini-batch
        lr: learning rate
        clip: gradient clipping
        val_frac: Fraction of data to hold out for validation
        print_every: Number of steps for printing training and validation loss
    
    '''
    net.train()
    
    opt = torch.optim.Adam(net.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()
    
    # create training and validation data
    val_idx = int(len(data)*(1-val_frac))
    data, val_data = data[:val_idx], data[val_idx:]
    
    if(train_on_gpu):
        net.cuda()
    
    counter = 0
    n_chars = len(net.chars)
    for e in range(epochs):
        # initialize hidden state
        h = net.init_hidden(batch_size)
        
        for x, y in get_batches(data, batch_size, seq_length):
            counter += 1
            
            # One-hot encode our data and make them Torch tensors
            x = one_hot_encode(x, n_chars)
            inputs, targets = torch.from_numpy(x), torch.from_numpy(y)
            
            if(train_on_gpu):
                inputs, targets = inputs.cuda(), targets.cuda()

            # Creating new variables for the hidden state, otherwise
            # we'd backprop through the entire training history
            h = tuple([each.data for each in h])

            # zero accumulated gradients
            net.zero_grad()
            
            # get the output from the model
            output, h = net(inputs, h)
            
            # calculate the loss and perform backprop
            loss = criterion(output, targets.view(batch_size*seq_length).long())
            loss.backward()
            # `clip_grad_norm` helps prevent the exploding gradient problem in RNNs / LSTMs.
            nn.utils.clip_grad_norm_(net.parameters(), clip)
            opt.step()
            
            # loss stats
            if counter % print_every == 0:
                # Get validation loss
                val_h = net.init_hidden(batch_size)
                val_losses = []
                net.eval()
                for x, y in get_batches(val_data, batch_size, seq_length):
                    # One-hot encode our data and make them Torch tensors
                    x = one_hot_encode(x, n_chars)
                    x, y = torch.from_numpy(x), torch.from_numpy(y)
                    
                    # Creating new variables for the hidden state, otherwise
                    # we'd backprop through the entire training history
                    val_h = tuple([each.data for each in val_h])
                    
                    inputs, targets = x, y
                    if(train_on_gpu):
                        inputs, targets = inputs.cuda(), targets.cuda()

                    output, val_h = net(inputs, val_h)
                    val_loss = criterion(output, targets.view(batch_size*seq_length).long())
                
                    val_losses.append(val_loss.item())
                
                net.train() # reset to train mode after iterationg through validation data
                
                print("Epoch: {}/{}...".format(e+1, epochs),
                      "Step: {}...".format(counter),
                      "Loss: {:.4f}...".format(loss.item()),
                      "Val Loss: {:.4f}".format(np.mean(val_losses)))
```
1. The model is set to training mode using `net.train()` which allows using the gradients
   for backpropagation.
2. The optimizer and the loss functions are defined, and the loss function is taken to be a cross-entropy loss.
3. Some amount of data is set aside to calculate the validation loss at each epoch.
4. Inside the for loop that iterates through the number of epochs,
    1. The initial hidden state is obtained from the `init_hidden` method that sets all the
       elements to zero.
    2. Inside the for loop that is used to iterate over all the batches of data, 
       (`get_batches()` is a generator function so at each iteration the next batch 
       is used)
        1. The input data is one-hot encoded using the function that has been already 
           defined,
        2. The input and target arrays are cast into tensors to be sent through the PyTorch-defined network,
        3. The hidden variable is redefined to **avoid backpropagating through the entire 
           training history**,
        4. The accumulated gradients are set to zero,
        5. The output and the next hidden state are obtained from passing the inputs and 
           the previous hidden state through the model,
        6. The loss is calculated by calling the loss function and passing the outputs and 
           the target tensors as arguments, (As the outputs have the squished shape from 
           before, the targets are also squished to make the batch size and sequence length 
           into one dimension)
        7. Backpropagation is done using the loss calculated,
        8. As RNN has the problem of exploding gradients, they are clipped when they go 
           past a certain value that is defined as 5 here, using the 
           `clip_grad_norm_()` function that takes in the network parameters and the value 
           of the clip as arguments,
        9. The optimizer is used to upgrade the weights by calling the `opt.step()` function,
        10. When the counter value equals the number of steps for which the training details 
            need to be printed,
            All the steps as training are done for the validation data, only 
            backpropagation and up-gradation of weights are not done. Note that the network 
            needs to be set to evaluation mode by `net.eval()` and then back to training 
            mode by `net.train()`. In evaluation mode, the gradients do not need to be used.
            
            All the training details are then printed.

### Instantiating the model

```buildoutcfg
n_hidden=512
n_layers=2

net = CharRNN(chars, n_hidden, n_layers)

batch_size = 128
seq_length = 100
n_epochs = 5 # start smaller if you are just testing initial behavior

# train the model

train(net, encoded, epochs=n_epochs, batch_size=batch_size, seq_length=seq_length, lr=0.001, print_every=10)
```

### Making Predictions
```buildoutcfg
def predict(net, char, h=None, top_k=None):
        ''' Given a character, predict the next character.
            Returns the predicted character and the hidden state.
        '''
        
        # tensor inputs
        x = np.array([[net.char2int[char]]])
        x = one_hot_encode(x, len(net.chars))
        inputs = torch.from_numpy(x)
        
        if(train_on_gpu):
            inputs = inputs.cuda()
        
        # detach hidden state from history
        h = tuple([each.data for each in h])
        # get the output of the model
        out, h = net(inputs, h)

        # get the character probabilities
        p = F.softmax(out, dim=1).data
        if(train_on_gpu):
            p = p.cpu() # move to cpu
        
        # get top characters
        if top_k is None:
            top_ch = np.arange(len(net.chars))
        else:
            p, top_ch = p.topk(top_k)
            top_ch = top_ch.numpy().squeeze()
        
        # select the likely next character with some element of randomness
        p = p.numpy().squeeze()
        char = np.random.choice(top_ch, p=p/p.sum())
        
        # return the encoded value of the predicted char and the hidden state
        return net.int2char[char], h
```
### Priming and Generating Text
```buildoutcfg
def sample(net, size, prime='The', top_k=None):
        
    if(train_on_gpu):
        net.cuda()
    else:
        net.cpu()
    
    net.eval() # eval mode
    
    # First off, run through the prime characters
    chars = [ch for ch in prime]
    h = net.init_hidden(1)
    for ch in prime:
        char, h = predict(net, ch, h, top_k=top_k)

    chars.append(char)
    
    # Now pass in the previous character and get a new one
    for ii in range(size):
        char, h = predict(net, chars[-1], h, top_k=top_k)
        chars.append(char)

    return ''.join(chars)
```
```buildoutcfg
print(sample(net, 1000, prime='Anna', top_k=5))
```
Generated text,
![image](https://github.com/ChinmayaSharma-hue/Image_repo/blob/main/Untitled.png?raw=true)

As you can see, the generated text has some gibberish words, but all in all, it reflects a sort 
of efficiency of RNNs in generating text through sequential learning. 
