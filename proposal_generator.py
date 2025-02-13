class ProposalGeneratorAgent:
    def __init__(self, company_name, use_cases, resource_links):
        self.company_name = company_name
        self.use_cases = use_cases
        self.resource_links = resource_links

    def generate_final_proposal(self):
         """Generates and returns the final proposal for the company."""
        proposal_text = f"AI Proposal for {self.company_name}\n"
        proposal_text += "=" * 40 + "\n\n"
        proposal_text += "Executive Summary:\n"
        proposal_text += f"The proposal aims to integrate AI/ML technologies into {self.company_name}'s operations.\n\n"
        proposal_text += "Proposed Use Cases:\n"
        for idx, use_case in enumerate(self.use_cases, 1):
            proposal_text += f"{idx}. {use_case}\n"
        
        proposal_text += "\nResource Links:\n"
        for use_case, link in self.resource_links:
            proposal_text += f"- {use_case}: {link}\n"
        
        return proposal_text

    def save_to_file(self, filename="final_proposal.txt"):
        with open(filename, 'w') as f:
            f.write(f"Final Proposal for {self.company_name}\n\n")
            f.write("Top AI/ML Use Cases:\n\n")
            for idx, use_case in enumerate(self.use_cases, 1):
                f.write(f"{idx}. {use_case}\n")

            f.write("\nRelevant Datasets and Resources:\n\n")
            for idx, (use_case, link) in enumerate(self.resource_links, 1):
                f.write(f"{idx}. {use_case}: {link}\n")

        print(f"Proposal saved to {filename}")

# Main function to run the Proposal Generator Agent
if __name__ == "__main__":
    use_cases = [
        "AI-powered demand forecasting for inventory management.",
        "Personalized customer recommendations using machine learning and GenAI.",
        "GenAI for automating customer service chatbots and virtual assistants.",
        "Predictive analytics for supply chain and logistics optimization.",
        "AI-driven price optimization for competitive product pricing."
    ]
    
    resource_links = [
        ("AI-powered demand forecasting for inventory management.", "https://www.kaggle.com/datasets/robikscube/sales-demand-forecasting"),
        ("Personalized customer recommendations using machine learning and GenAI.", "https://www.kaggle.com/datasets/kc-house-data"),
        ("GenAI for automating customer service chatbots and virtual assistants.", "https://www.kaggle.com/datasets/deepcontractor/customer-support-on-twitter"),
        ("Predictive analytics for supply chain and logistics optimization.", "https://www.kaggle.com/datasets/prajitdatta/gdansk-supply-chain-logistics"),
        ("AI-driven price optimization for competitive product pricing.", "https://www.kaggle.com/datasets/mtszkw/five-years-of-consumer-price-index-data")
    ]

    proposal_agent = ProposalGeneratorAgent("Walmart", use_cases, resource_links)
    proposal_agent.generate_final_proposal()
    proposal_agent.save_to_file("Walmart_AI_Proposal.txt")
