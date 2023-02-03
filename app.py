import os
from pathlib import Path
from typing import Union
import openai
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
openai.api_key = os.getenv("OPENAI_API_KEY")


def img_variation(file_path: Union[str, Path]) -> str:
    response = openai.Image.create_variation(
        image=open(file_path, "rb"),
        n=1,
        size="256x256"
    )
    image_url = response['data'][0]['url']
    return image_url


def save_to_md(file_name: str, url: str) -> None:
    with open('ai_img.md', mode='a+', encoding='utf-8') as file:
        file.write(f'[{file_name}]({url})\n')


if __name__ == '__main__':
    file = Path('pilar_valeria_escobar_carrasco.jpg')
    url = img_variation(file)
    save_to_md(file, url)
