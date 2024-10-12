from research import ResearchAgent
from use_case_generator import UseCaseGenerationAgent
from resource_collector import ResourceCollectorAgent
from proposal_generator import ProposalGeneratorAgent

def main():
    # Step 1: Research Phase
    company_name = "Walmart"
    industry = "Retail"
    
    # Instantiate and collect research data
    research_agent = ResearchAgent(company_name, industry)
    research_agent.collect_data()  # Collect Walmart-specific data (offerings, focus, industry trends)
    research_agent.analyze_data()  # Display research data

    # Step 2: Use Case Generation Phase
    use_case_agent = UseCaseGenerationAgent(company_name, industry)
    generated_use_cases = use_case_agent.generate_report()  # Generate and print use cases

    # Step 3: Resource Collection Phase
    resource_collector_agent = ResourceCollectorAgent(generated_use_cases)
    resource_links = resource_collector_agent.generate_report()  # Search and print dataset links
    
    # Step 4: Proposal Generation Phase
    proposal_agent = ProposalGeneratorAgent(company_name, generated_use_cases, resource_links)
    proposal_agent.generate_final_proposal()  # Generate and print the final proposal
    proposal_agent.save_to_file(f"{company_name}_AI_Proposal.txt")  # Save proposal to a file

if __name__ == "__main__":
    main()
