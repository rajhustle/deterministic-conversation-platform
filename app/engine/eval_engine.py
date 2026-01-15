def evaluate_script(text: str):
    issues = []

    clean_text = text.strip()
    char_count = len(clean_text)

    # 1. Extremely small script
    if char_count < 500:
        issues.append("Script content is very small. Expect frequent expert callbacks.")

    # 2. No guided options
    if not any(x in text for x in ["Option", "Choose", "A.", "B.", "1.", "2."]):
        issues.append("No guided options found. Users may ask open-ended questions.")

    # 3. Pricing risk
    if any(x in text.lower() for x in ["price", "cost", "amount", "fee"]):
        issues.append("Pricing-related terms detected. Bot must avoid committing answers.")

    # 4. Geography risk
    if any(x in text.lower() for x in ["country", "region", "location", "available in"]):
        issues.append("Geography-related terms detected. Expect availability questions.")

    return {
        "char_count": char_count,
        "issues": issues
    }
