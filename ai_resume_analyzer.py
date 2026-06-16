print("AI Resume Analyzer")
print("-------------------")

resume_skills = ["Python", "SQL", "Power BI", "Excel"]
job_skills = ["Python", "SQL", "Machine Learning", "Power BI"]

matched = []
missing = []

for skill in job_skills:
    if skillkinlresume_skills:
        matched.append(skill)
    else:
        missing.append(skill)

score = (len(matched) / len(job_skills)) * 100

print(f"ATS Match Score: {score}%")
print("\nMatched Skills:")
for skill in matched:
    print("-", skill)

print("\nMissing Skills:")
for skill in missing:
    print("-", skill) 
