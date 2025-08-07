import requests

def roast_with_gpt_oss(prompt_text):
    url = "https://your-runpod-api/generate"  # ⬅️ replace with your actual RunPod URL
    try:
        res = requests.post(url, json={"text": prompt_text}, timeout=30)
        res.raise_for_status()
        return res.json()["response"]
    except Exception as e:
        print("❌ RoastBot error:", e)
        return "RoastBot failed to respond."
