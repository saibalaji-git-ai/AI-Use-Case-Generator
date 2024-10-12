import webbrowser

class ResourceCollectorAgent:
    def __init__(self, use_cases):
        self.use_cases = use_cases
        self.dataset_links = []

    def search_datasets(self):
        print("Searching for relevant datasets...")
        # Placeholder dataset links (can be expanded to integrate with actual APIs)
        dataset_sources = {
            "AI-powered demand forecasting": "https://www.kaggle.com/datasets/robikscube/sales-demand-forecasting",
            "Personalized customer recommendations": "https://www.kaggle.com/datasets/kc-house-data",
            "Automating product categorization": "https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-small",
            "Customer service chatbots": "https://www.kaggle.com/datasets/deepcontractor/customer-support-on-twitter",
            "Supply chain optimization": "https://www.kaggle.com/datasets/prajitdatta/gdansk-supply-chain-logistics",
            "Price optimization": "https://www.kaggle.com/datasets/mtszkw/five-years-of-consumer-price-index-data",
        }

        for use_case in self.use_cases:
            for key, link in dataset_sources.items():
                if key in use_case:
                    self.dataset_links.append((use_case, link))

        return self.dataset_links

    def generate_report(self):
        links = self.search_datasets()
        print("\nResource Asset Links:")
        for use_case, link in links:
            print(f"- {use_case}: {link}")
        return links

    def open_links_in_browser(self):
        for _, link in self.dataset_links:
            webbrowser.open(link)

# Main function to run the Resource Collector Agent
if __name__ == "__main__":
    use_cases = [
        "AI-powered demand forecasting for inventory management.",
        "Personalized customer recommendations using machine learning and GenAI.",
        "GenAI for automating customer service chatbots and virtual assistants.",
        "Predictive analytics for supply chain and logistics optimization.",
        "AI-driven price optimization for competitive product pricing."
    ]
    resource_collector = ResourceCollectorAgent(use_cases)
    resource_collector.generate_report()
    # Optionally open links in browser
    # resource_collector.open_links_in_browser()
