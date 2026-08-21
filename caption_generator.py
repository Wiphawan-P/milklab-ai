"""Daily White Laundry Caption Generator (S1).

Usage:
    python caption_generator.py

Reads GOOGLE_API_KEY from env. Generates a Thai caption for a laundry service.
"""

import os
import sys

from dotenv import load_dotenv
from google import genai


PROMPT_TEMPLATE = """\
คุณคือ social media manager ของร้าน Daily White Laundry ร้านซักรีดครบวงจร

จงเขียนแคปชั่นภาษาไทย 2 ถึง 3 ประโยคเพื่อโปรโมตบริการซักรีด: {service}
เน้นเสื้อผ้าที่สะอาด หอม และดูแลอย่างพิถีพิถัน รวมถึงบริการรับ-ส่งผ้าถึงที่พัก

เงื่อนไข:
- โทนเป็นมิตร ใช้คำง่าย สื่อถึงความสะอาดและความหอม ใส่ emoji ได้
- ระบุประเภทบริการหรือราคาได้เมื่อมีข้อมูลที่เกี่ยวข้อง
- กล่าวถึงบริการรับ-ส่งผ้าเมื่อเหมาะสม
- ต้องมี call-to-action ปิดท้าย เช่น สั่งเลย หรือ ทักแชท
- ห้ามใช้ em dash
"""


def generate_caption(service: str, api_key: str | None = None) -> str:
    """Generate a Thai caption for the given laundry service."""
    key = api_key or os.environ.get("GOOGLE_API_KEY")
    if not key:
        raise RuntimeError("GOOGLE_API_KEY not set in env or argument")
    client = genai.Client(api_key=key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=PROMPT_TEMPLATE.format(service=service),
    )
    return response.text or ""


def main() -> int:
    load_dotenv()
    service = input("บริการที่จะโปรโมต: ").strip()
    if not service:
        print("กรุณาใส่ชื่อบริการ")
        return 1
    caption = generate_caption(service)
    print()
    print(caption)
    return 0


if __name__ == "__main__":
    sys.exit(main())
