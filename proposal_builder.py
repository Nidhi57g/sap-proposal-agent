def build_outline(answers):
    slides = []

    slides.append({
        "title": "Executive Summary",
        "content": [
            f"Client Industry: {answers.get('What is the client industry?', '')}",
            f"SAP Scope: {answers.get('Which SAP modules are in scope?', '')}"
        ]
    })

    slides.append({
        "title": "Project Overview",
        "content": [
            f"Implementation Type: {answers.get('Is this Greenfield, Brownfield, or Selective carve-out?', '')}",
            f"Project Duration: {answers.get('Expected project duration?', '')}",
            f"Target Go-live: {answers.get('Target go-live date?', '')}"
        ]
    })

    slides.append({
        "title": "Commercial Model",
        "content": [
            f"Pricing Model: {answers.get('Preferred pricing model (Fixed / T&M)?', '')}"
        ]
    })

    return slides
