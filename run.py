import os
import requests
from io import BytesIO
from dotenv import load_dotenv
from PIL import Image

# ទាញយក Token ពីឯកសារ .env
load_dotenv()
HF_TOKEN = os.environ.get("HF_TOKEN")

# កំណត់ម៉ូដែល AI សម្រាប់បង្កើតរូបភាព (Stable Diffusion XL)
API_URL = "https://router.huggingface.co/hf-inference/models/black-forest-labs/FLUX.1-schnell"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

print("--- ចាប់ផ្តើមសាកល្បងភ្ជាប់ទៅកាន់ Hugging Face API ---")

# វាយអត្ថបទបញ្ជា (Prompt) ដែលចង់ឱ្យ AI បង្កើតនៅទីនេះ
prompt_text = "A cinematic shot of a beautiful sunset over the mountains of Cambodia, 4k resolution"

try:
    image_bytes = query({"inputs": prompt_text})
    
    # បើក និងរក្សាទុករូបភាពដែល AI បង្កើតបានចូលក្នុង Folder ផ្ទាល់
    image = Image.open(BytesIO(image_bytes))
    image.save("ai_generated_image.png")
    
    print("🎉 ជោគជ័យ ១០០%! រូបភាពត្រូវបានបង្កើត និងរក្សាទុកក្នុងឈ្មោះ 'ai_generated_image.png'")

except Exception as e:
    print("❌ ការភ្ជាប់បរាជ័យ! មូលហេតុ៖", e)
