import json

# Load rules from JSON file
with open("prompt_rules.json", "r") as file:
    rules = json.load(file)

def analyze_prompt(prompt):
    prompt = prompt.lower()

    detected = []

    # Check Prompt Injection
    for rule in rules["prompt_injection"]:
        if rule.lower() in prompt:
            detected.append(("Prompt Injection", rule))

    # Check Jailbreak
    for rule in rules["jailbreak"]:
        if rule.lower() in prompt:
            detected.append(("Jailbreak", rule))

    # Check Sensitive Data
    for rule in rules["sensitive_data"]:
        if rule.lower() in prompt:
            detected.append(("Sensitive Data Request", rule))

    return detected
