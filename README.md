# Letter Llama 🦙

An AI-powered cover letter generator that creates personalized cover letters using fine-tuned LLaMA models. This project combines a Streamlit web interface with a fine-tuned LLaMA 3.2 model for generating professional cover letters tailored to specific job applications.

## Model Information 🧠

The model used in this project is available on HuggingFace:
- Model: [Atharva2099/cover-letter-llama-3.2-lora](https://huggingface.co/Atharva2099/cover-letter-llama-3.2-lora)
- Base Model: LLaMA 3.2 3B
- Fine-tuning: LoRA adaptation
- Training Dataset: [ShashiVish/cover-letter-dataset](https://huggingface.co/datasets/ShashiVish/cover-letter-dataset)
- Training Framework: [Unsloth](https://github.com/unslothai/unsloth)

## Features 🌟
- Customized cover letter generation
- User-friendly Streamlit interface
- Dark mode UI
- Multiple download formats (TXT, MD)
- Local model inference using Ollama

## Setup 🚀

### Prerequisites
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install [Ollama](https://ollama.ai/)

3. Set up the model:
```bash
# Create Modelfile
echo "FROM llama3.2:3b
ADAPTER /path/to/downloaded/lora/weights" > Modelfile

# Create custom model
ollama create coverletter-custom -f Modelfile
```

4. Run the application:
```bash
streamlit run app.py
```

## Usage 📝

1. Fill in job details:
   - Job title
   - Company name
   - Required qualifications

2. Add your information:
   - Name
   - Experience
   - Skills
   - Qualifications

3. Generate and download your cover letter

## Model Training Details 🔬

The model was fine-tuned using:
- Unsloth framework for efficient training
- LoRA fine-tuning technique
- Training parameters:
  ```python
  lora_config = {
      "r": 16,
      "target_modules": ["q_proj", "k_proj", "v_proj", "o_proj",
                        "gate_proj", "up_proj", "down_proj"],
      "lora_alpha": 16,
      "lora_dropout": 0
  }
  ```

## Project Structure 📁
```
letter-llama/
├── app.py              # Main Streamlit application
├── upload_model.py     # HuggingFace upload utility
├── requirements.txt    # Project dependencies
└── README.md          # Documentation
```

## Acknowledgments 👏
- [ShashiVish](https://huggingface.co/datasets/ShashiVish/cover-letter-dataset) for the training dataset
- [Unsloth](https://github.com/unslothai/unsloth) for the efficient training framework
- [Ollama](https://ollama.ai/) for local model serving

## Links 🔗
- [HuggingFace Model](https://huggingface.co/Atharva2099/cover-letter-llama-3.2-lora)
- [Training Dataset](https://huggingface.co/datasets/ShashiVish/cover-letter-dataset)
- [Unsloth Framework](https://github.com/unslothai/unsloth)


## License 📄
This project follows the same license as LLaMA and is intended for research purposes.

## Note ⚠️
The generated cover letters should be reviewed and edited before use. 