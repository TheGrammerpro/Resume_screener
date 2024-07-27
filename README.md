**Resume Screening Automation:**

This repository contains a Python script for automating the resume screening process. The script extracts text from PDF and DOCX resumes, processes the information to extract key details, and calculates a skill score based on predefined skills and their weights. The results are then stored in a CSV file for further analysis.


**Features:**
-PDF and DOCX Extraction: Extracts text from resumes in PDF and DOCX formats.
-Skill Scoring: Calculates a skill score based on the presence of predefined skills and their importance.
-Information Extraction: Extracts key information such as name, email, phone number, skills, and experience from resumes.
-CSV Storage: Stores the extracted information and skill scores in a CSV file.


**Installation:**
Clone the repository:
*git clone https://github.com/yourusername/resume-screening-automation.git
*cd resume-screening-automation

**Install the required dependencies:**
*pip install -r requirements.txt

**Usage:**
Add your open AI API to a environment variable under the name "OPENAI_API_KEY"
Place the resumes to be processed in the resumes directory.

**Run the script:**
python main.py
The processed information and skill scores will be saved in Resume Database.csv.

**Configuration**
Predefined Skills and Weights: Edit the weights dictionary in main.py to update the skills and their corresponding weights.

weights = {'python': 3.5, 'java': 1.5, 'machine learning': 2, 'data analysis': 2.5, 'sql': 1.5, 'project management': 1}
predefined_skills = ['Python', 'Java', 'Machine Learning', 'Data Analysis', 'SQL', 'Project Management']

**Example**
Here is an example of how the processed information will be stored in the CSV file:

Name	Email	Phone Number	County & City	Companies Worked At	Experience (Years)	Degrees	Skills	Skill Score %
JANE KNIGHTLEY	jane.knightley@email.com	(123) 456-7890	USA, Seattle	['Yelp: IT Technician Intern (2020-current)', 'Washington State University Help Desk: Support Technician (2019-2020)']	7	['Bachelor of Science in Computer Science at Washington State University']	['SQL', 'Network Infrastructure', 'Customer Service', 'Conflict Resolution', 'Python', 'Interpersonal Communication']	41.67
Coleman Guthrie	cole.guthrie@email.com	(123) 456-7890	USA, San Francisco, CA	['Genovice: tech field (2019-current)', 'Federal Reserve Bank of Boston: tech field (2014-2019)', 'NetApp: tech field (2010-2014)']	13	['Bachelor of Science in Computer Engineering at University of California, San Diego']	['Server Maintenance', 'SQL', 'APIs', 'CRM', 'Microsoft 365', 'Programming', 'C++', 'Java', 'Python', 'Project Management']	70.83

**Acknowledgements**
PDFMiner
python-docx
pandas
Contact

For any questions or feedback, please contact The Grammer Pro (https://www.linkedin.com/in/mohcine-ben-karmel-96600321b/).
