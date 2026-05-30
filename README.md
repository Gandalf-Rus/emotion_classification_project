# Text Emotion, Sentiment, and Formality Analysis System

A comprehensive, multi-level Natural Language Processing (NLP) pipeline designed to extract semantic and stylistic dimensions from text. The project processes text through three distinct analytical lenses, scaling from traditional Machine Learning baselines to deep neural networks and state-of-the-art Transformer architectures.

## Project Architecture Overview

The system consists of three specialized sub-models evaluating distinct semantic layers:
* **Model A (Sentiment Analysis):** 3-class classification (Positive / Negative / Neutral) utilizing balanced IMDB reviews and GoEmotions subsets.
* **Model B (Emotion Detection):** 9-class multi-label classification tracking complex emotional overlaps (*sadness, anger, fear, disgust, anticipation, joy, surprise, gratitude, love*) based on GoEmotions dataset.
* **Model C (Formality Style):** Binary classification (Formal / Informal) mapping structural syntax registers using the GYAFC dataset.

---

## Project Repository Structure
The directory layout follows the **Cookiecutter Data Science** standard. Enforcing a strict separation between executable code (`src/`), experiment logs (`notebooks/`), and immutable data artifacts (`data/`).

```text
emotion_classification_project/
├── data/
│   ├── raw/          # Immutable, raw downloaded datasets (GoEmotions, GYAFC, IMDB)
│   ├── processed/    # Normalized and tokenized text outputs
│   ├── splits/       # Reproducible Train / Validation / Test partitions
│   └── features/     # Vectorized mathematical representations (.npz sparse matrices, targets)
├── models/           # Serialized physical artifacts, model weights, and vectorizers (.pkl, .pt)
├── notebooks/        # Monolithic Jupyter Notebooks for EDA and iterative modeling
└── src/              # Modular, production-ready pipeline source code (under development)
    ├── data/         # RegEx-based text cleaning and SpaCy tokenization routines
    ├── features/     # Feature extraction classes (TF-IDF vectorizers, custom vocab mapping)
    ├── models/       # Model architectures, training definitions, and inference wrappers
    └── evaluation/   # Macro-metric metrics aggregation and error forensics

```

---

## Development Pipeline (Jupyter Notebooks)

The project was built incrementally across 7 operational stages:

### 01. Exploratory Data Analysis (EDA)

* Analyzed raw class balances and token distributions.
* Discovered explicit structural variances (e.g., Formal text averages ~21 words, while Informal averages ~9 words).
* Mapped 27 native GoEmotions categories into 9 high-signal targeted labels.

### 02. Core Text Preprocessing

* Engineered a modular cleaning pipeline: HTML tag stripping, RegEx noise filtration, and custom emoji conversion.
* Utilized **SpaCy (`en_core_web_sm`)** for deterministic tokenization and lemmatization.

### 03. Text Representation & Feature Engineering

* Transformed string sequences into numeric sparse matrices using **TF-IDF Vectorization** (capped at `max_features=10,000`).
* Preserved negative contexts and collocations via Bigrams (`ngram_range=(1,2)`) combined with curated stop-word overrides (e.g., retaining "not", "no").
* Enforced strict stratification parameters (`stratify=y`) on Models A & C to prevent data leakage.

### 04. Baseline ML Models

* Established rigid statistical performance thresholds using **Linear Support Vector Classifiers (Linear SVC)**, **Logistic Regression** and **Naive Bayes classifier**.
* The Bag-of-Words approach combined with optimized linear hyperplanes served as the mathematical benchmark for subsequent deep learning tasks.

### 05. Dense Neural Embeddings

* Tested the spatial continuity hypothesis by swapping sparse TF-IDF matrices with pre-trained **Word2Vec** and **FastText** 300-dimensional embeddings.
* Determined that arithmetic mean pooling degrades sequential contexts, causing a performance drop under linear classifiers and establishing the need for sequence-aware topologies.

### 06. Deep Learning & Transformer Architectures

* Implemented all NN architectures in PyTorch (**FFNN**, **CNN**, **RNN**, **LSTM**, **Bi-LSTM** and **Bi-GRU**) with custom Vocabulary mapping layers.
* Fine-tuned **BERT (Bidirectional Encoder Representations from Transformers)** as the peak context extraction engine.

### 07. Forensic Evaluation & Threshold Optimization

* Exposed blind spots (e.g., model sensitivity to sarcasm/double negations) through high-confidence error forensics.
* Calibrated Multi-Label Sigmoid thresholds for Model B to counter severe class imbalances, optimizing the Macro F1 metric across overlapping emotions.


## Model Evaluation Summary & Production Strategy

| Layer | Target Task | Production Champion Model | Performance Metric |
| --- | --- | --- | --- | --- |
| **Model A** | Sentiment (3 classes) | **Linear SVC + TF-IDF** *(Alt: Bi-GRU)* | **0.96 Macro F1** |
| **Model B** | Emotions (9 classes, Multi-label) | **Fine-Tuned BERT** | **0.76 Macro F1** |
| **Model C** | Formality (2 classes) | **Fine-Tuned BERT** *(Alt: Bi-GRU)* | **0.90 Macro F1** |

### Production Ensemble Strategy (for Future)

For low-latency API deployment or Telegram Bot inference, the system runs a **Hybrid Pipeline Ensemble**:

1. **Rapid Routing:** Inputs pass through the lightweight **Linear SVC** model first to fetch instantaneous Sentiment polarity.
2. **Deep Context Extraction:** Text is concurrently routed to the **Fine-Tuned BERT Heads** to isolate localized granular Emotion profiles and Formality registers.

---

*Developed as a graduation thesis exploring NLP Model Representation, Evaluation, and Optimization Strategies.*
