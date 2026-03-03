# CLI currency converter
A simple command line tool to convert currency using [ExchangeRate API](https://www.exchangerate-api.com/).

---
## Requirements
- Python installation
- Free API key from [exchangerate-api.com](https://www.exchangerate-api.com/)

## Installation

### 1. Klon projektet

```bash
git@github.com:itsHarning/python-valuta-converter.git
cd python-valuta-converter
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate virtual environment

**Mac/Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### 4. Install dependencies
**via pip**
```bash
pip install -r requirements.txt
```

---

## Use guide

### First time you run the script - add an API key

```bash
python3 valuta.py -key YOUR_API_KEY
```

This will save the key in a `.env` file, så you don't have to input it again

### Afterwards

```bash
python3 valuta.py
```

The program will guide you through the rest:

```
Input valuta to convert from: DKK
Input valuta to convert to: EUR
amount is optional, if you just want to see convertion rate
Input amount to convert: 100

Convertion rate: 0.134
100DKK is: 13.40EUR
```

---

## Deactivate virtual environment

When you're finished you can deactivate the virtual environment with:

```bash
deactivate
```