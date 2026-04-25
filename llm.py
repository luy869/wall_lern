import json
import os
import ollama
from dotenv import load_dotenv

load_dotenv()

client = ollama.Client(host=os.environ["ollama_api"])
MODEL = "qwen3.6:27b"


def generate_outline(theme: str) -> dict:
    prompt = f"""以下のテーマを段階的に学ぶための学習アウトラインを JSON のみで返してください。
説明や前置きは不要です。JSON だけを出力してください。

テーマ: {theme}

出力形式:
{{
  "title": "セッションのタイトル",
  "tags": ["タグ1", "タグ2"],
  "topics": [
    {{"order": 1, "name": "トピック名", "summary": "このトピックで学ぶこと"}},
    {{"order": 2, "name": "トピック名", "summary": "このトピックで学ぶこと"}}
  ]
}}"""

    response = client.chat(
        model=MODEL,
        options={"temperature": 0.2, "num_ctx": 4096},
        messages=[{"role": "user", "content": prompt}],
    )

    content = response["message"]["content"]

    # <think>...</think> タグを除去（qwen3 の thinking モード対策）
    if "<think>" in content:
        content = content[content.rfind("</think>") + len("</think>"):]

    content = content.strip()
    # ```json ... ``` のコードブロックを除去
    if content.startswith("```"):
        content = content.split("```")[1]
        if content.startswith("json"):
            content = content[4:]

    try:
        return json.loads(content.strip())
    except json.JSONDecodeError as e:
        raise ValueError(f"LLM が有効な JSON を返しませんでした: {e}\n出力: {content}")
