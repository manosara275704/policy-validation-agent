def generate_explanation(validation_results):

    explanations = []

    for item in validation_results:

        policy = item["policy"]

        if item["status"] == "Aligned":
            explanation = (
                f"The policy '{policy}' meets the required standards."
            )

        elif item["status"] == "Partial":
            explanation = (
                f"The policy '{policy}' partially meets the requirements but needs improvement."
            )

        else:
            explanation = (
                f"The policy '{policy}' does not meet the required standards."
            )

        explanations.append({
            "policy": policy,
            "status": item["status"],
            "explanation": explanation
        })

    return explanations