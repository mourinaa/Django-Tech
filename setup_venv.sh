#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "Virtualenv created in ./venv. Activate with: source venv/bin/activate"
