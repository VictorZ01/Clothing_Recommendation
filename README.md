# Clothing Recommendation Experiment  

This project explores the combination of **ResNet-50** and **K-Nearest Neighbors (KNN)** for a clothing recommendation system. The goal was to leverage ResNet-50's feature extraction capabilities and use KNN to identify visually similar clothing items. The results, however, were not applicable in a practical setting.  

---

## Overview  

For the purpose of experimentation, a **KNN model** was used.  
- KNN models are known to struggle with high-dimensional data due to the **curse of dimensionality**.  
- This project aimed to evaluate how significant these limitations would be in this context.  

### **Steps Involved**  
1. **Feature Extraction**:  
   - Utilized **ResNet-50**, pre-trained on ImageNet, to extract high-dimensional feature vectors from clothing images.  

2. **Similarity Search**:  
   - Applied **K-Nearest Neighbors (KNN)** to find visually similar items based on the extracted features.  

---

## Dataset  

The dataset consisted of two parts:  
1. **Scraped Images**: A web scraper was used to pull images from Uniqlo for rating purposes.  
2. **Supplemental Online Dataset**: Additional images from an external dataset were used for experimentation.  

**Challenges**:  
- The Uniqlo dataset was too small for effective training and evaluation.  
- Variations in style, lighting, and backgrounds further complicated the task.  

---

## Method and Challenges  

1. Extracted features from images using **ResNet-50**.  
2. Compared these features with Uniqlo images using **KNN** to find the closest neighbors.  
3. Observed that:  
   - All images had the same closest neighbors.  
   - The distances between images were not meaningful, likely due to high-dimensional feature space challenges.  

KNN struggled to differentiate images in high-dimensional space, making it unsuitable for this task without further optimization.  

---

## Future Directions  

While this experiment didn’t yield successful results, it opened doors for future exploration:  

1. **Fine-Tuning Models**:  
   - Fine-tune ResNet-50 on a domain-specific dataset to improve feature relevance.  

2. **Alternative Similarity Measures**:  
   - Experiment with measures like **cosine similarity** or advanced methods like **Locality Sensitive Hashing (LSH)**.  

3. **Algorithm Improvements**:  
   - Explore clustering-based methods or deep learning frameworks tailored for recommendation tasks.  

4. **Custom Datasets**:  
   - Build a larger, more tailored dataset for training and evaluation.  

5. **Advanced Models**:  
   - Investigate approaches like **Siamese networks** or **triplet loss** for improved similarity learning.  

---