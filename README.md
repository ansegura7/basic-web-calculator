# Basic Web Calculator

A simple web application to demonstrate the interaction between a front-end and a back-end. Users can input two numbers, select a math operation (addition, subtraction, multiplication, or division), and get the result via a REST API built with FastAPI.

## Features
- Input two numbers and choose an operation (`add`, `subtract`, `multiply`, `divide`).
- Communicates between the front-end and back-end using a REST API.
- Built with:
  - **Front-end**: HTML, CSS, JavaScript
  - **Back-end**: Python (FastAPI)

## Getting Started

### Prerequisites
- [Python 3.8+](https://www.python.org/downloads/)
- [FastAPI](https://fastapi.tiangolo.com/)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ansegura7/basic-web-calculator.git
   cd basic-web-calculator
   ```

### Manual Installation & Execution (Backend)

Follow these steps in order to run the FastAPI backend locally:

1. Create a virtual environment

   ```bash
   python -m venv .venv
   ```

2. Activate the virtual environment

   ```bash
   .\.venv\Scripts\activate
   ```

3. Upgrade pip

   ```bash
   python -m pip install --upgrade pip
   ```

4. Install the required packages

   ```bash
   pip install -r .\requirements.txt
   ```

5. Run the FastAPI application

   ```bash
   python .\backend\main.py
   ```

After running the application, the API will be available at:

- Swagger UI → http://127.0.0.1:8000/docs
- ReDoc → http://127.0.0.1:8000/redoc

## Author
- Created by <a href="https://github.com/ansegura7">Andrés Segura Tinoco</a>
- Created on Jan 14, 2025
- Last update on Nov 21, 2025

## License
This project is licensed under the terms of the <a href="https://github.com/ansegura7/basic-web-calculator/blob/main/LICENSE">Apache License 2.0</a>.
