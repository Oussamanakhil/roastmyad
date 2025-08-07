from services.roastbot_client import roast_with_gpt_oss

def generate_roast(prompt: str) -> str:
    """
    Calls the RoastBot (GPT-OSS 20B) model deployed on RunPod to generate a roast.
    """
    return roast_with_gpt_oss(prompt)
