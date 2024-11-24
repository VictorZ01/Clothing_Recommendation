#Clothing Recommendation Experiment
This project explores the combination of ResNet-50 and K-Nearest Neighbors (KNN) for a clothing recommendation system. The goal was to leverage ResNet-50's feature extraction capabilities and use KNN to identify visually similar clothing items. 
The results were not applicable. 

Overview
For the purpose of experimentation, a KNN model was used. KNN are considered bad for high dimensional data, where the curse of dimensionality appears. I wanted to observe how much of a problem that would cause. 
Feature Extraction: Used ResNet-50, pre-trained on ImageNet, to extract high-dimensional feature vectors from clothing images.
Similarity Search: Applied K-Nearest Neighbors (KNN) to find visually similar items based on extracted features.

Dataset: The point of the dataset was to extract images using a Webscrapper and pull images from Uniqlo for a person to rate. However, there was not a large enough dataset for training. 

Method and Failure:
Using a seperate online dataset of images, ResNet50 was used to extract features. These features were then comapred with the features of the Uniqlo images and found the closest neighbors using KNN.
All images had the same closest neighbors, meaing that the distance between images was not significant. 

Incorporating fine-tuning of ResNet-50 on a domain-specific dataset to improve feature relevance.
Experimenting with alternative similarity measures, such as cosine similarity or more advanced methods like Locality Sensitive Hashing (LSH).
Testing other algorithms, such as clustering-based methods or deep learning-based recommendation frameworks.
Future Directions
While this experiment didn't yield successful results, it highlighted new opportunities for exploration:

Building a custom dataset tailored to clothing recommendation.
Using convolutional layers from ResNet-50 in combination with fine-tuned neural networks for end-to-end recommendations.
Exploring more advanced models, such as Siamese networks or triplet loss, for improved similarity learning.
