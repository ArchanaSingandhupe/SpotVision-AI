# SpotVisionAI
Our cutting-edge application harnesses the power of deep learning and computer vision to analyze skin images and predict potential diseases with remarkable accuracy of 80%.

## Running

1. Create a virtual environment

    ```bash
    conda create -n your_env_name python==3.10
    ```

1. Activate the virtual environment

    ```bash
    conda activate your_env_name
    ```

1. Install dependencies

    ```bash
    pip install poetry
    poetry install
    ```
2. Optional, Sometimes on windows, you need to install tensorflow again.

    ```bash
    pip install tensorflow
    ```

1. Run the app

    ```bash
    streamlit run ./About.py
    ```
