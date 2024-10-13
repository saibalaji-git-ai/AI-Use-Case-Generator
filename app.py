import streamlit as st
from research import ResearchAgent
from use_case_generator import UseCaseGenerationAgent
from resource_collector import ResourceCollectorAgent
from proposal_generator import ProposalGeneratorAgent
import io

def main():
    st.title("AI Use Case Generator")

    # Input fields for company and industry
    company_name = st.text_input("Enter the company name", "Walmart")
    industry = st.text_input("Enter the industry", "Retail")

    if st.button("Generate AI Proposal"):
        try:
            # Step 1: Research Phase
            st.subheader("Step 1: Research Phase")
            research_agent = ResearchAgent(company_name, industry)
            research_agent.collect_data()
            research_data = research_agent.analyze_data()
            st.write("Collected Data:")
            st.write(research_data)

            # Step 2: Use Case Generation Phase
            st.subheader("Step 2: Use Case Generation Phase")
            use_case_agent = UseCaseGenerationAgent(company_name, industry)
            generated_use_cases = use_case_agent.generate_report()
            st.write("Generated Use Cases:")
            st.write(generated_use_cases)

            # Step 3: Resource Collection Phase
            st.subheader("Step 3: Resource Collection Phase")
            resource_collector_agent = ResourceCollectorAgent(generated_use_cases)
            resource_links = resource_collector_agent.generate_report()
            st.write("Relevant Datasets:")
            st.write(resource_links)

            # Step 4: Proposal Generation Phase
            st.subheader("Step 4: Proposal Generation Phase")
            proposal_agent = ProposalGeneratorAgent(company_name, generated_use_cases, resource_links)
            proposal_text = proposal_agent.generate_final_proposal()

            # Display the proposal
            st.write("AI Proposal Generated:")
            st.write(proposal_text)

            # Provide option to download proposal as a text file
            buffer = io.StringIO()
            buffer.write(proposal_text)
            buffer.seek(0)
            st.download_button(label="Download AI Proposal",
                               data=buffer,
                               file_name=f"{company_name}_AI_Proposal.txt",
                               mime="text/plain")

        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
