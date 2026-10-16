import json
import os
from urllib.request import Request, urlopen


def ask(prompt: str) -> dict:
    base_url = os.environ["LLM_BASE_URL"].rstrip("/")
    api_key = os.environ["LLM_API_KEY"]
    body = json.dumps({"model": "demo-model", "messages": [{"role": "user", "content": prompt}]}).encode()
    request = Request(
        f"{base_url}/chat/completions",
        data=body,
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode())

if __name__ == "__main__":
    print(ask("Resuma o status de uma tarefa de exemplo."))
