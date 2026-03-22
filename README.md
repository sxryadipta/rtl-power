# ML-Based RTL Power Prediction

## Pipeline
RTL (Verilog) → Yosys → Feature Extraction → ML Models

## Models Used
- SVR
- KNN
- Random Forest
- XGBoost

## Features
- Cell count
- Wire count
- Gate counts

## Target
Synthetic power estimation based on structural features

## Run

1. Add Verilog files in `data/raw/`
2. Run:
   python scripts/run_yosys.py
   python scripts/extract_features.py
   python models/train.py