# upload_model.py
from huggingface_hub import HfApi, create_repo
import os

def verify_file_exists(filepath):
    """Verify if a file exists and print its status"""
    exists = os.path.exists(filepath)
    print(f"Checking {filepath}: {'✅ Found' if exists else '❌ Not found'}")
    return exists

# Get token from environment or input
print("💡 Please paste your write-enabled token from https://huggingface.co/settings/tokens")
token = input("Enter your Hugging Face write token: ").strip()

# Initialize the Hugging Face API with token
api = HfApi(token=token)

# Your repository name on Hugging Face (corrected username)
repo_id = "Atharva2099/cover-letter-llama-3.2-lora"

print("\n🏗️ Verifying repository access...")
try:
    api.repo_info(repo_id=repo_id)
    print("✅ Repository access verified successfully!")
except Exception as e:
    print(f"❌ Error accessing repository: {str(e)}")
    exit(1)

# List of files to upload
files_to_upload = [
    "adapter_config.json",
    "adapter_model.safetensors",
    "tokenizer_config.json",
    "special_tokens_map.json",
    "tokenizer.json"
]

print("\n🔍 Verifying files...")
# Check all files exist before attempting upload
all_files_exist = True
for file in files_to_upload:
    filepath = os.path.join("final_model", file)
    if not verify_file_exists(filepath):
        all_files_exist = False

if not all_files_exist:
    print("❌ Some files are missing. Please check the paths above.")
    exit(1)

print("\n📤 Starting upload process...")
# Upload each file
for file in files_to_upload:
    filepath = os.path.join("final_model", file)
    print(f"\nUploading {file}...")
    try:
        api.upload_file(
            path_or_fileobj=filepath,
            path_in_repo=file,
            repo_id=repo_id,
            token=token
        )
        print(f"✅ Successfully uploaded {file}")
    except Exception as e:
        print(f"❌ Error uploading {file}: {str(e)}")
        print("💡 Detailed error:", str(e))

print("\n✨ Upload process completed!")