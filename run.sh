#!/bin/bash

# Activar entorno virtual
source venv/bin/activate

# execute pipeline
python3 process_data.py

deactivate