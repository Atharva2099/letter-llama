# Letter Llama 🦙

An AI-powered cover letter generator that creates personalized cover letters using fine-tuned LLaMA models.

## Model Details 🧠
This project uses a fine-tuned version of LLaMA 3.2 3B, trained on the [ShashiVish/cover-letter-dataset](https://huggingface.co/datasets/ShashiVish/cover-letter-dataset) using [Unsloth](https://github.com/unslothai/unsloth) for efficient training.

### Training Details
- Base Model: LLaMA 3.2 3B
- Dataset: [Cover Letter Dataset](https://huggingface.co/datasets/ShashiVish/cover-letter-dataset)
- Training Framework: Unsloth
- Training Type: LoRA fine-tuning

## Features 🌟
- Custom cover letter generation
- Ollama integration for local LLM inference
- Dark mode UI
- Multiple download formats
- Easy-to-use interface

## Setup 🚀
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install Ollama from https://ollama.ai/

3. Set up the model:
```bash
# Create Modelfile
echo "FROM llama3.2:3b
ADAPTER /path/to/your/model" > Modelfile

# Create custom model
ollama create coverletter-custom -f Modelfile
```

4. Run the app:
```bash
streamlit run app.py
```

## Usage 📝
1. Fill in job details
2. Add your information
3. Click Generate
4. Download your cover letter

## Tech Stack 💻
- Python
- Streamlit
- Ollama
- LLaMA 3.2
- Unsloth (for training)

## Model Training 🔬
The model was fine-tuned using Unsloth, an efficient training framework for LLMs. Training details and code can be found in the `training` directory. The dataset used contains various professional cover letters, helping the model learn proper structure and content.


## Acknowledgments 👏
- [ShashiVish](https://huggingface.co/ShashiVish) for the cover letter dataset
- [Unsloth](https://github.com/unslothai/unsloth) for the efficient training framework
- [Ollama](https://ollama.ai/) for the local model serving