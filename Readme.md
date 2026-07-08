# Plant Disease Detection

## Overview

Plant diseases are one of the major factors affecting agricultural productivity and food security worldwide. Early and accurate identification of plant diseases enables timely intervention, reducing crop losses and improving yield quality.

This project presents a deep learning-based plant disease classification system developed using **Transfer Learning**. A pretrained **AlexNet** model, originally trained on the **ImageNet** dataset, is fine-tuned on the **PlantVillage** dataset to classify healthy and diseased plant leaves. By leveraging pretrained feature representations, the model achieves improved classification performance while significantly reducing training time and computational requirements compared to training a convolutional neural network from scratch.

---

## Features

* Transfer Learning using a pretrained AlexNet model
* Automatic plant disease classification from leaf images
* Image preprocessing and data augmentation pipeline
* Training, validation, and testing workflow
* Performance evaluation using multiple classification metrics
* Modular and easy-to-understand implementation
* Suitable for further deployment in web or mobile applications

---

## Dataset

The model is trained and evaluated using the **PlantVillage** dataset, a widely used benchmark dataset for plant disease classification.

### Dataset Highlights

* More than **50,000** labeled leaf images
* Multiple crop species
* Healthy and diseased leaf categories
* High-quality RGB images
* Multi-class classification problem

---

## Methodology

The project follows a standard deep learning workflow consisting of the following stages:

1. Dataset acquisition
2. Image preprocessing
3. Dataset splitting
4. Data augmentation
5. Transfer learning using a pretrained AlexNet model
6. Model fine-tuning
7. Performance evaluation
8. Prediction on unseen images

---

## Data Preprocessing

To improve model performance and training stability, the following preprocessing techniques are applied:

* Image resizing to **224 × 224 pixels**
* Pixel value normalization
* Dataset shuffling
* Training, validation, and test split
* Data augmentation on the training dataset:

  * Random horizontal flipping
  * Random rotation
  * Random zoom

---

## Transfer Learning

Instead of training an entire convolutional neural network from scratch, this project employs **Transfer Learning**.

The pretrained **AlexNet** model, trained on the **ImageNet** dataset, is used as a feature extractor. The original classification layer is replaced with a custom classifier corresponding to the number of plant disease classes in the PlantVillage dataset.

The training process consists of:

* Loading pretrained ImageNet weights
* Replacing the final classification layer
* Training the newly added classifier layers
* Fine-tuning selected pretrained layers to improve classification accuracy

This approach enables faster convergence while improving the model's generalization capability.

---

## Model Architecture

The implemented model consists of:

* Pretrained AlexNet convolutional feature extractor
* Fully connected classifier
* ReLU activation functions
* Dropout layers for regularization
* Softmax output layer for multi-class classification

---

## Technologies Used

| Category                   | Technologies                     |
| -------------------------- | -------------------------------- |
| Programming Language       | Python                           |
| Deep Learning Framework    | TensorFlow / Keras               |
| Transfer Learning          | AlexNet (Pretrained on ImageNet) |
| Image Processing           | OpenCV                           |
| Numerical Computing        | NumPy                            |
| Data Visualization         | Matplotlib                       |
| Machine Learning Utilities | Scikit-learn                     |
| Development Environment    | Google Colab / Jupyter Notebook  |

---

## Training Configuration

| Parameter          | Value                                 |
| ------------------ | ------------------------------------- |
| Input Image Size   | 224 × 224                             |
| Batch Size         | 32                                    |
| Optimizer          | Adam                                  |
| Loss Function      | Categorical Crossentropy              |
| Output Activation  | Softmax                               |
| Evaluation Metrics | Accuracy, Precision, Recall, F1-Score |

---

## Performance Evaluation

The trained model is evaluated using the following metrics:

* Classification Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

These metrics provide a comprehensive assessment of the model's classification performance across all disease categories.

---

## Project Structure

```text
Plant-Disease-Detection/
│
├── dataset/
│
├── notebooks/
│   └── Plant_Disease_Detection.ipynb
│
├── models/
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

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Plant-Disease-Detection.git
cd Plant-Disease-Detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

1. Download the PlantVillage dataset.
2. Place the dataset inside the `dataset/` directory.
3. Open the notebook in Google Colab or Jupyter Notebook.
4. Execute all cells to preprocess the data.
5. Train the transfer learning model.
6. Evaluate the trained model.
7. Use the trained model to predict diseases from new plant leaf images.

---

## Future Enhancements

The project can be extended in several directions:

* Support for real-world field images
* Mobile application deployment
* Web application using Streamlit or Flask
* Model optimization for edge devices
* Integration with cloud-based prediction services
* Real-time disease detection using smartphone cameras

---

## References

* PlantVillage Dataset
* ImageNet Dataset
* AlexNet: *ImageNet Classification with Deep Convolutional Neural Networks* (Krizhevsky, Sutskever, & Hinton, 2012)
* TensorFlow Documentation
* Keras Documentation

---

## Author

**Pawan Yadav**

**Project:** Plant Disease Detection Using Transfer Learning

This project demonstrates the application of transfer learning and deep convolutional neural networks for automated plant disease classification, providing a scalable and efficient solution for precision agriculture.
