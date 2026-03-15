# Computer Vision Architectures: Real-time Perception & Segmentation

[![Standard](https://img.shields.io/badge/Standard-CTO--Ready-blue)](https://github.com/Krishnaandey25/Computer-Vision-Architectures)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

Advanced Computer Vision models for object detection, facial recognition, and medical imaging built with 'CTO Standard' architectural patterns.

## 🚀 Quick Start

Ensure you have Python 3.9+ and run:

`ash
make install
`

To run a sample execution:
`ash
python src/main.py
`

## 🏗️ Architecture Decision Records (ADR)

- **VisionModel (ABC):** Unified interface for all CV backends.
- **ModelFactory:** Decouples model instantiation from runtime logic.
- **VisionProcessor:** Orchestrates image preprocessing and model inference.

## 🧪 Development

- **Lint:** make lint
- **Format:** make format
- **Test:** make test

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.