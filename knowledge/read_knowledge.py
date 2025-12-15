from pptx import Presentation
import os

KNOWLEDGE_DIR = "knowledge"

def read_proposals():
    if not os.path.exists(KNOWLEDGE_DIR):
        print("❌ Knowledge folder not found")
        return

    files = [f for f in os.listdir(KNOWLEDGE_DIR) if f.endswith(".pptx")]

    print(f"✅ Found {len(files)} SAP proposal files\n")

    for file in files:
        path = os.path.join(KNOWLEDGE_DIR, file)
        prs = Presentation(path)
        print(f"{file} → {len(prs.slides)} slides")

if __name__ == "__main__":
    read_proposals()
