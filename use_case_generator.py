import random

class UseCaseGenerationAgent:
    def __init__(self, company_name, industry):
        self.company_name = company_name
        self.industry = industry
    
    def generate_use_cases(self):
        # Based on the retail industry and Walmart's focus, we generate relevant AI use cases
        use_cases = [
            "AI-powered demand forecasting for inventory management.",
            "Personalized customer recommendations using machine learning and GenAI.",
            "Automating product categorization with computer vision.",
            "GenAI for automating customer service chatbots and virtual assistants.",
            "Predictive analytics for supply chain and logistics optimization.",
            "Fraud detection in online transactions using machine learning.",
            "Automated content generation for personalized marketing campaigns.",
            "AI-driven price optimization for competitive product pricing.",
            "Natural language processing (NLP) for customer feedback analysis.",
            "AI-based dynamic ad targeting for Walmart's e-commerce platform."
        ]
        
        # Randomly select 5 use cases for the proposal
        selected_use_cases = random.sample(use_cases, 5)
        return selected_use_cases

    def generate_report(self):
        print(f"Generating AI/ML Use Cases for {self.company_name} in the {self.industry} industry...")
        use_cases = self.generate_use_cases()
        print("\nProposed AI/ML Use Cases:")
        for idx, use_case in enumerate(use_cases, 1):
            print(f"{idx}. {use_case}")
        return use_cases

# Main function to run the Use Case Generation Agent
if __name__ == "__main__":
    use_case_agent = UseCaseGenerationAgent("Walmart", "Retail")
    use_case_agent.generate_report()
