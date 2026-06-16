# AI Resume Analyzer

with open("resume.txt", "r") as file:
    resume = file.read()

with open("job_description.txt", "r") as file:
    job = file.read()

skills = [
    "Python",
    "SQL",
    "Power BI",
    "Tableau",
    "Azure",
    "Machine Learning",
    "Deep Learning",
    "Git",
    "Streamlit",
    "Data Analysis",
    "Microsoft 365"
]

resume_skills = []
job_skills = []

for skill in skills:

    if skill.lower() in resume.lower():
        resume_skills.append(skill)

    if skill.lower() in job.lower():
        job_skills.append(skill)

missing_skills = []

for skill in job_skills:

    if skill not in resume_skills:
        missing_skills.append(skill)

matched_skills = len(job_skills) - len(missing_skills)

ats_score = (matched_skills / len(job_skills)) * 100

print("=" * 50)
print("AI RESUME ANALYZER")
print("=" * 50)

print("\nSkills Found:")

for skill in resume_skills:
    print("✓", skill)

print("\nMissing Skills:")

for skill in missing_skills:
    print("✗", skill)

print(f"\nATS Match Score: {ats_score:.2f}%")

if ats_score >= 80:
    print("Excellent Match")
elif ats_score >= 60:
    print("Good Match")
else:
    print("Needs Improvement")
