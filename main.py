import docx
import os
import pandas as pd
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
from info_extractor import InfoExtractor


weights = {'python': 3.5, 'java': 1.5, 'machine learning': 2, 'data Analysis': 2.5, 'sql': 1.5, 'project management': 1}

predefined_skills = ['Python', 'Java', 'Machine Learning', 'Data Analysis', 'SQL', 'Project Management']

directory = "./resumes"


def convert_pdf_to_txt(path):
    pdf_manager = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(pdf_manager, retstr, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(pdf_manager, device)
    password = ""
    max_pages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=max_pages, password=password,
                                  caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text


def extract_text_from_docx(docx_path):
    doc = docx.Document(docx_path)
    text = '\n'.join([paragraph.text for paragraph in doc.paragraphs])
    return text


def calculate_score(resume_skills, job_skills, weights_input):
    total_score = 0
    job_skills = [skill.lower() for skill in job_skills]
    resume_skills = [skill.lower() for skill in resume_skills]
    for skill in job_skills:
        if skill in resume_skills:
            print(f"{skill}, importance: {weights_input.get(skill, 1)}")
            total_score += weights_input.get(skill, 1)
    max_score = sum(weights_input.values())
    return (total_score / max_score) * 100


resumes_to_be_processed = []
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".pdf"):
        file_path = os.path.join(directory, filename)
        # Convert PDF to str
        resumes_to_be_processed.append(convert_pdf_to_txt(file_path))
    elif filename.endswith(".docx"):
        file_path = os.path.join(directory, filename)
        # Convert docx to str
        resumes_to_be_processed.append(extract_text_from_docx(file_path))

info_dicts = []
for resume in resumes_to_be_processed:
    # Process resume text and extract info with AI
    info_extracted = InfoExtractor(resume)
    info_dict = info_extracted.info_dict
    # Calculate skill score
    skill_score = calculate_score(info_dict["skills"], predefined_skills, weights)
    info_dict["Skill score %"] = skill_score
    print(f"skill score: {'%.2f' % skill_score}%")
    print(info_dict)
    # Create a dict containing all info dicts
    info_dicts.append(info_dict)

try:
    resume_info_df = pd.read_csv("Resume Database.csv", index_col=False)
    resume_info_df = pd.concat([resume_info_df, pd.DataFrame(info_dicts)])
    resume_info_df.style.format({'column_name': '{:.2f}%'.format})
    if resume_info_df.duplicated(subset=['email']).any():
        print("Removing duplicates...")
        resume_info_df.drop_duplicates(subset=['email'], inplace=True)
    resume_info_df.to_csv("Resume Database.csv", index=False)
except FileNotFoundError:
    # Create a dict containing key values from all dicts as lists
    big_info_dict = {k: [d[k] for d in info_dicts] for k in info_dicts[0]}
    resume_info_df = pd.DataFrame.from_dict(big_info_dict)
    resume_info_df.style.format({'column_name': '{:.2f}%'.format})
    resume_info_df.to_csv("Resume Database.csv", index=False)
