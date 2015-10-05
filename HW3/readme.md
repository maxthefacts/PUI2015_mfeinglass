# PUI 2015 Homework 3

First, I imported os, numpy, pandas, and pyplot.  I further used a pylab inline magic line and a random seed to ensure repeatability.

I created a sample size array, called N, which consisted of 100 random integers generated between 10 and 2000.
Next, I stet a population mean that all distributions could share.  I chose 5 for no important reason.

Since we will be plotting the sample sizes of the distributions against their measured means, I initialized two tables for each selected distribution.  One was a table of means, the other of sample sizes.  I selected the Normal, Possion, Binomial, Chi Square, Log Normal, and Exponential distributions.

I then created a for loop that calculated a random generated model for each distribution using a parameter of a mean equaling 5 and a sample size determined by stepping through the sample array created earlier, N.  At each step, I would find the mean of the randomly generated distribution array and store it, along with the sample size used for that particular model run, in the tables initialized earlier.  This created 100 distributions of each type, or 600 total.

All that remained was to create scatter plots of the mean vs the distribution sample size for each distribution.  This histogram involved changing the “alpha” transparency of each histogram to layer them on top of one another. 
