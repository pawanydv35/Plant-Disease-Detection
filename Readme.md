# Plant Disease Detection 

## Overview

Plant diseases pose a significant challenge to global agriculture by reducing crop yield and quality. Early and accurate disease identification enables timely intervention, helping farmers minimize losses and improve productivity.

This project presents an automated **Plant Disease Detection System** using **Transfer Learning** with a pretrained **AlexNet** model. Instead of training a deep convolutional neural network from scratch, the project leverages knowledge learned from the **ImageNet-1K** dataset and fine-tunes the model for plant disease classification using the **PlantVillage** dataset.

The implementation is developed in **PyTorch** and demonstrates how transfer learning can achieve high classification performance while reducing computational cost and training time.

---

# Features

* Transfer Learning using a pretrained AlexNet model
* Plant disease classification from leaf images
* Data preprocessing and augmentation
* ImageNet normalization
* Automatic dataset splitting into training, validation, and testing sets
* Model evaluation using classification metrics
* Trained model saved for future inference
* Implemented entirely using PyTorch

---

# Dataset

The project uses the **PlantVillage** dataset, one of the most widely used benchmark datasets for plant disease classification.

### Dataset Characteristics

* More than **50,000** labeled leaf images
* Multiple plant species
* Healthy and diseased leaf categories
* RGB images
* Multi-class image classification problem

---

# Methodology

The project follows the workflow below:

1. Download and load the PlantVillage dataset
2. Apply image preprocessing and augmentation
3. Split the dataset into training, validation, and testing sets
4. Load a pretrained AlexNet model
5. Freeze the convolutional feature extraction layers
6. Replace the final classification layer
7. Train the custom classifier
8. Evaluate the trained model
9. Save the trained model for deployment

---

# Data Preprocessing

To improve the model's learning capability and generalization, the following preprocessing techniques are applied:

* Resize images to **224 × 224** pixels
* Random Horizontal Flip
* Random Rotation (10°)
* Random Resized Crop
* Color Jitter (Contrast Enhancement)
* Convert images to PyTorch tensors
* Normalize images using ImageNet mean and standard deviation

These preprocessing steps help improve robustness against variations in image orientation, scale, and lighting conditions.

---

# Transfer Learning

This project utilizes **Transfer Learning** with the pretrained **AlexNet** architecture available in the PyTorch `torchvision.models` library.

The model is initialized using weights pretrained on the **ImageNet-1K** dataset.

The transfer learning strategy consists of:

* Loading pretrained ImageNet weights
* Freezing all convolutional feature extraction layers
* Replacing the original output layer with a new fully connected layer matching the number of plant disease classes
* Training only the newly added classifier layer

This approach significantly reduces training time while maintaining strong classification performance.

---

# Model Architecture

The implemented model consists of:

* Pretrained AlexNet Feature Extractor
* Five Convolutional Layers
* ReLU Activation Functions
* Max Pooling Layers
* Fully Connected Classifier
* Custom Output Layer
* Softmax Classification

Only the final classification layer is retrained for the PlantVillage dataset.

---

# Technologies Used

| Category                | Technology                      |
| ----------------------- | ------------------------------- |
| Programming Language    | Python                          |
| Deep Learning Framework | PyTorch                         |
| Computer Vision         | Torchvision                     |
| Numerical Computing     | NumPy                           |
| Data Visualization      | Matplotlib                      |
| Dataset Download        | KaggleHub                       |
| Development Environment | Google Colab / Jupyter Notebook |

---

# Training Configuration

| Parameter          | Value            |
| ------------------ | ---------------- |
| Model              | AlexNet          |
| Pretrained Weights | ImageNet-1K      |
| Framework          | PyTorch          |
| Input Image Size   | 224 × 224        |
| Batch Size         | 32               |
| Optimizer          | Adam             |
| Learning Rate      | 0.0001           |
| Loss Function      | CrossEntropyLoss |
| Epochs             | 20               |

---

# Performance Evaluation

The trained model is evaluated using standard classification metrics, including:

* Classification Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

These metrics provide a comprehensive assessment of the model's ability to correctly classify healthy and diseased plant leaves.

---

# Project Structure

```text
Plant-Disease-Detection/
│
├── dataset/
│
├── Plant_detection_disease_pytorch.ipynb
│
├── models/
│   └── plant_disease_alexnet.pth
│
├── images/
│
├── requirements.txt
│
├── README.md
│
└── LICENSE
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/your-username/Plant-Disease-Detection.git
cd Plant-Disease-Detection
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Usage

1. Download the PlantVillage dataset.
2. Open the project notebook in Google Colab or Jupyter Notebook.
3. Execute all cells sequentially.
4. The notebook will:

   * Load and preprocess the dataset
   * Apply data augmentation
   * Split the dataset into training, validation, and testing sets
   * Load the pretrained AlexNet model
   * Train the classifier
   * Evaluate the model
   * Save the trained model as **plant_disease_alexnet.pth**

---

# Workflow

```text
                PlantVillage Dataset
                        │
                        ▼
             Image Preprocessing
                        │
                        ▼
              Data Augmentation
                        │
                        ▼
          Train / Validation / Test Split
                 (80% / 10% / 10%)
                        │
                        ▼
      Pretrained AlexNet (ImageNet-1K)
                        │
                        ▼
      Freeze Feature Extraction Layers
                        │
                        ▼
      Replace Final Classification Layer
                        │
                        ▼
                Model Training
                        │
                        ▼
             Validation & Testing
                        │
                        ▼
          Save Trained Model (.pth)
```

---

# Future Enhancements

The project can be extended by incorporating:

* Fine-tuning additional AlexNet layers
* Deployment using Streamlit or Flask
* Mobile application integration
* Real-time disease detection using a smartphone camera
* Support for field-acquired images
* Comparison with advanced architectures such as ResNet, EfficientNet, DenseNet, and Vision Transformers

---

# References

* PlantVillage Dataset
* ImageNet-1K Dataset
* Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). *ImageNet Classification with Deep Convolutional Neural Networks.*
* PyTorch Documentation
* Torchvision Documentation

---

# Author

**Pawan Yadav**

This project demonstrates the application of **Transfer Learning** and **Deep Convolutional Neural Networks (CNNs)** for automated plant disease classification. By leveraging pretrained ImageNet features through AlexNet, the model provides an efficient and scalable solution for intelligent agricultural disease diagnosis.
