# app.py
import streamlit as st
import requests

# Configure page
st.set_page_config(
    page_title="Cover Letter Generator",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def generate_with_ollama(prompt, temperature=0.7):
    """Generate text using Ollama API"""
    try:
        response = requests.post('http://localhost:11434/api/generate',
                               json={
                                   'model': 'coverletter-custom',
                                   'prompt': prompt,
                                   'temperature': temperature,
                                   'stream': False
                               })
        if response.status_code == 200:
            return response.json()['response']
        else:
            raise Exception(f"Error: {response.status_code}")
    except Exception as e:
        raise Exception(f"Failed to generate: {str(e)}")

# Add custom CSS for better text contrast
st.markdown("""
    <style>
    /* Overall theme */
    .stApp {
        background-color: #1e1e1e;
        color: #ffffff;
    }
    
    /* Input text color */
    .stTextInput > div > div > input {
        background-color: #2b303b !important;
        color: #ffffff !important;
        border: 1px solid #4b5563 !important;
    }
    
    /* Textarea text color */
    .stTextArea > div > div > textarea {
        background-color: #2b303b !important;
        color: #ffffff !important;
        border: 1px solid #4b5563 !important;
    }
    
    /* Placeholder text color */
    .stTextInput > div > div > input::placeholder,
    .stTextArea > div > div > textarea::placeholder {
        color: #9ca3af !important;
    }
    
    /* Focus states */
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #4CAF50 !important;
        box-shadow: 0 0 0 1px #4CAF50 !important;
    }

    /* Make sure text remains visible during input */
    input, textarea {
        color: #ffffff !important;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #ffffff !important;
    }
    
    /* Labels */
    label {
        color: #e5e7eb !important;
    }

    /* Success message */
    .success {
        background-color: #1a472a !important;
        color: #ffffff !important;
    }
    
    /* Error message */
    .error {
        background-color: #471a1a !important;
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Create the web interface
st.title("🎯 Professional Cover Letter Generator")
st.markdown("Generate customized cover letters based on job descriptions and your profile.")

# Check if Ollama is running
try:
    response = requests.get('http://localhost:11434')
    if response.status_code == 200:
        st.success("✅ Connected to Ollama successfully!")
except:
    st.error("❌ Failed to connect to Ollama. Please make sure Ollama is running.")
    st.stop()

# Create two columns for input fields
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Job Details")
    job_title = st.text_input("Job Title", placeholder="e.g., Software Engineer")
    company = st.text_input("Company Name", placeholder="e.g., Tech Corp")
    preferred_quals = st.text_area(
        "Preferred Qualifications", 
        placeholder="List the key qualifications from the job posting",
        height=150
    )

with col2:
    st.subheader("👤 Your Information")
    applicant_name = st.text_input("Your Name", placeholder="e.g., John Doe")
    current_exp = st.text_area(
        "Current Experience", 
        placeholder="Describe your current role and responsibilities",
        height=100
    )
    past_exp = st.text_area(
        "Past Experience",
        placeholder="Summarize your relevant past experience",
        height=100
    )
    skills = st.text_area(
        "Skills", 
        placeholder="List your relevant skills",
        height=100
    )
    qualifications = st.text_area(
        "Qualifications", 
        placeholder="Your educational background and certifications",
        height=100
    )

# Generation settings
with st.expander("⚙️ Advanced Settings"):
    temperature = st.slider("Temperature (Creativity)", min_value=0.1, max_value=1.0, value=0.7, step=0.1)

# Define prompt template
prompt_template = """Below is a job application context. Write a professional cover letter based on the provided information.
### Job Details:
Title: {job_title}
Preferred Qualifications: {preferred_quals}
Company: {company}

### Applicant Information:
Name: {applicant_name}
Past Experience: {past_exp}
Current Experience: {current_exp}
Skills: {skills}
Qualifications: {qualifications}

### Cover Letter:
"""

# Generate button
if st.button("✨ Generate Cover Letter", type="primary", use_container_width=True):
    if not all([job_title, company, applicant_name]):
        st.error("⚠️ Please fill in at least the Job Title, Company Name, and Your Name.")
    else:
        with st.spinner("🤖 Generating your cover letter..."):
            try:
                # Prepare input prompt
                prompt = prompt_template.format(
                    job_title=job_title,
                    preferred_quals=preferred_quals,
                    company=company,
                    applicant_name=applicant_name,
                    past_exp=past_exp,
                    current_exp=current_exp,
                    skills=skills,
                    qualifications=qualifications
                )
                
                # Generate cover letter
                generated_text = generate_with_ollama(prompt, temperature)
                
                # Display the result in a nice box
                st.success("✨ Cover Letter Generated Successfully!")
                st.markdown("### 📝 Your Generated Cover Letter")
                st.markdown("""---""")
                
                # Create columns for the result area
                result_col1, result_col2 = st.columns([3, 1])
                
                with result_col1:
                    st.markdown(generated_text)
                
                with result_col2:
                    # Add download options
                    st.markdown("### 💾 Download Options")
                    
                    # Plain text download
                    st.download_button(
                        label="📄 Download as TXT",
                        data=generated_text,
                        file_name="cover_letter.txt",
                        mime="text/plain"
                    )
                    
                    # Markdown download
                    st.download_button(
                        label="📑 Download as MD",
                        data=generated_text,
                        file_name="cover_letter.md",
                        mime="text/markdown"
                    )
                    
            except Exception as e:
                st.error(f"Error during generation: {str(e)}")

# Add helpful instructions at the bottom
with st.expander("ℹ️ How to use this tool"):
    st.markdown("""
    1. Fill in the job details from the job posting you're applying to
    2. Add your personal information and experience
    3. Optionally adjust the temperature setting for generation
    4. Click 'Generate Cover Letter' to create a customized cover letter
    5. Review and edit the generated letter as needed
    6. Download the letter in your preferred format
    
    **Tips:**
    - Be specific in your job details and qualifications
    - Include relevant skills and experience that match the job requirements
    - Review and personalize the generated letter before sending
    - Adjust the temperature setting if you want more creative or more focused output
    """)

# Footer
st.markdown("""---""")
st.markdown(
    """
    <div style='text-align: center'>
        <p>Built with ❤️ using Streamlit and Ollama</p>
    </div>
    """,
    unsafe_allow_html=True)