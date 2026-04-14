# Reality Check — Real vs AI-Generated Image Classifier

A mini-project submitted to **KIIT Deemed to be University** in partial fulfilment of the Bachelor's Degree in Computer Science & Engineering (2025–2026)

---

## Team

| Name | Roll Number |
|---|---|
| Anula Mishra | 2305843 |
| Swayamshree Mohanty | 2305661 |
| Arundhati Das | 2305847 |
| Asmi Dutta | 23052558 |
| Aviskha Dey | 23052876 |

**Guide:** Prof. Sunil Kumar Sawant, School of Computer Engineering, KIIT University

---

## Overview

**Reality Check** is a binary image classification system that detects whether a given image is **real (authentic)** or **AI-generated (fake)**. With the rapid proliferation of generative AI tools like GANs and diffusion models, distinguishing real from synthetic images has become increasingly critical to combating misinformation and digital fraud.

The system implements and compares two approaches:
- **CNN (Convolutional Neural Network)** using MobileNetV2 via transfer learning
- **SVM (Support Vector Machine)** using handcrafted image features

A web interface built with **Streamlit** allows real-time image classification.

---

## Tech Stack

| Category | Tools / Libraries |
|---|---|
| Language | Python 3.x |
| Deep Learning | TensorFlow, Keras, MobileNetV2 |
| Machine Learning | Scikit-learn (SVM, StandardScaler) |
| Image Processing | OpenCV, PIL, NumPy |
| Feature Extraction | Scikit-image (LBP, GLCM), SciPy (FFT) |
| Web Interface | Streamlit |
| Training Environment | Google Colab |

---

## Models

### CNN Model (MobileNetV2)
- Base: Pre-trained MobileNetV2 (ImageNet weights)
- Custom dense layers added for binary classification
- Input size: 128 x 128 pixels
- Loss: Binary Cross-Entropy | Optimizer: Adam (lr=0.001)
- Callbacks: EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
- Batch size: 32 | Max epochs: 30

### SVM Model
- Input: Handcrafted feature vector per image (resized to 224 x 224 RGB)
- Features used:
  - Color Histogram (96-dim)
  - Color Stats (mean, std, skew)
  - LBP — texture pattern
  - GLCM — contrast, energy
  - FFT — frequency spectrum
  - Noise residual stats
- Feature normalization: StandardScaler
- Kernel: RBF | Handles class imbalance via class weighting

---

## Results

| Model | Performance |
|---|---|
| CNN (MobileNetV2) | >= 85% accuracy on test set |
| SVM (RBF Kernel) | Outperformed CNN on this dataset due to effective handcrafted features |

Both models are evaluated on **accuracy, precision, recall, F1-score**, and a **confusion matrix**.

The SVM classifier achieved stronger results overall, demonstrating that well-designed handcrafted features can rival deep learning on constrained datasets.

---

## Dataset Structure

Organize your dataset as follows before training:
```
dataset/
├── Train/
│   ├── Real/
│   └── Fake/
└── Test/
    ├── Real/
    └── Fake/
```

The dataset was stored on Google Drive and accessed via Google Colab during training.

---

## Data Preprocessing and Augmentation

- Corrupted images removed automatically
- All images resized to 128 x 128 (CNN) or 224 x 224 (SVM)
- Pixel values normalized to [0, 1]
- Augmentation applied during CNN training: Rotation +/-15 degrees, Width/Height shift 10%, Shear 10%, Zoom 10%, Horizontal flip

---

## Testing

| Test ID | Test Case | Expected Result |
|---|---|---|
| T01 | Upload a real image | Predicts "Real" |
| T02 | Upload an AI-generated image | Predicts "Fake" |
| T03 | Upload a non-image file | Displays error message |

---

## Future Scope

- Train on larger, more diverse datasets for better generalization
- Explore ResNet, EfficientNet, or Vision Transformers for improved accuracy
- Extend to video deepfake detection
- Support multi-class classification (GAN-based, diffusion-based, etc.)
- Deploy as a browser extension or mobile application
- Integrate Explainable AI (XAI) techniques to provide reasoning behind predictions

---

## License

This project was developed for academic purposes at KIIT Deemed to be University. All rights reserved by the authors.

---

*School of Computer Engineering, KIIT Deemed to be University, Bhubaneswar, Odisha — April 2026*
