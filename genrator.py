import yaml
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import requests
from PIL import Image
from io import BytesIO


# load_dotenv()

model = "llama3-8b-8192"
groq_chat = ChatGroq(
    model=model,
    groq_api_key="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"
    # os.getenv("GROQ_API_KEY")
)

def load_temp(path="templates.yaml"):
    with open(path,"r") as f :
        return yaml.safe_load(f)
    
def generate_post(platform,topic,tone,audience,language):
    templates = load_temp()
    base_template = templates[platform]["template"]

    prompt_text = base_template + "\nTarget audience: {audience}\nRespond in {language}."
    prompt = ChatPromptTemplate.from_template(prompt_text)
    chain = prompt | groq_chat 

    return chain.invoke({"topic": topic, "tone": tone, "audience": audience, "language": language})


API_KEY = "6f0ed93e9a64bbd7824f3b57854a06e14e379abcf3039b27addcbb9810ff8f80da862b5ff6acfb81b89be9c68085b809"  # 🔁 Replace with your actual Clipdrop key
API_URL = "https://clipdrop-api.co/text-to-image/v1"
HEADERS = {"x-api-key": API_KEY}


def generate_image(prompt: str) -> Image.Image:
    response = requests.post(
        API_URL,
        headers=HEADERS,
        files={"prompt": (None, prompt)}
    )

    if response.status_code == 200:
        return Image.open(BytesIO(response.content))  # ⬅️ Load image in memory
    else:
        raise Exception(f"Request failed: {response.status_code} - {response.text}")



# def generate_image(prompt: str, output_path="output.png"):
#     pipe = StableDiffusionPipeline.from_pretrained(
#         "CompVis/stable-diffusion-v1-4",
#         torch_dtype=torch.float16,
#         revision="fp16",
#         use_safetensors=False
#     )
#     pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    
#     image = pipe(prompt).images[0]
#     image.save(output_path)
#     return output_path
