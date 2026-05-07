import pandas as pd
import matplotlib.pyplot as plt
import kagglehub
import os

# ---------------------------------------------------
# DOWNLOAD DATASET
# ---------------------------------------------------

path = kagglehub.dataset_download("khushikyad001/ai-impact-on-jobs-2030")
print("Dataset folder:", path)

# Find the CSV file inside the downloaded folder
files = os.listdir(path)
csv_files = [f for f in files if f.endswith(".csv")]

if not csv_files:
    raise FileNotFoundError("No CSV file found in the downloaded dataset folder.")

csv_path = os.path.join(path, csv_files[0])
print("Using CSV file:", csv_path)

# ---------------------------------------------------
# LOAD DATASET
# ---------------------------------------------------

df = pd.read_csv(csv_path)

print(df.head())
print("\nDataset Information:")
print(df.info())
print("\nSummary Statistics:")
print(df.describe())


# ---------------------------------------------------
# DATA CLEANING
# ---------------------------------------------------
df = df.drop_duplicates()
print("\nMissing Values:")
print(df.isnull().sum())

# ---------------------------------------------------
# AUTOMATION PROBABILITY BY JOB TITLE
# ---------------------------------------------------
plt.figure(figsize=(10, 8))
plt.bar(df['Job_Title'], df['Automation_Probability_2030'], color='skyblue')
plt.xlabel('Job Title')
plt.ylabel('Automation Probability by 2030')
plt.title('Automation Probability by Job Title in 2030')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# ---------------------------------------------------
# AUTOMATION PROBABILITY DISTRIBUTION
# ---------------------------------------------------
plt.figure(figsize=(10, 6))
plt.hist(df['Automation_Probability_2030'], bins=20, edgecolor='black')
plt.xlabel('Automation Probability')
plt.ylabel('Frequency')
plt.title('Distribution of Automation Probability Across Jobs')
plt.tight_layout()
plt.show()

# ---------------------------------------------------
# AI EXPOSURE VS AUTOMATION PROBABILITY
# ---------------------------------------------------
plt.figure(figsize=(10, 6))
plt.scatter(df['AI_Exposure_Index'], df['Automation_Probability_2030'], alpha=0.6, color='green')
plt.xlabel('AI Exposure Index')
plt.ylabel('Automation Probability')
plt.title('Correlation between AI Exposure and Automation Risk')
plt.tight_layout()
plt.show()

# Correlation
def mean(values):
    total = 0
    for v in values:
        total += v
    return total / len(values)

def correlation(x, y):
    mean_x = mean(x)
    mean_y = mean(y)

    num = 0
    denom_x = 0
    denom_y = 0

    for i in range(len(x)):
        dx = x[i] - mean_x
        dy = y[i] - mean_y
        num += dx * dy
        denom_x += dx ** 2
        denom_y += dy ** 2

    return num / ((denom_x * denom_y) ** 0.5)

corr_ai_auto = correlation(
    df['AI_Exposure_Index'].to_list(),
    df['Automation_Probability_2030'].to_list()
)

print("\nCorrelation (AI Exposure vs Automation Probability):", corr_ai_auto)

# ---------------------------------------------------
# SKILL LEVEL VS AUTOMATION PROBABILITY
# ---------------------------------------------------
def avg_skill(row):
    total = 0
    count = 0
    for col in df.columns:
        if 'Skill_' in col:
            total += row[col]
            count += 1
    return total / count

df['Average_Skill_Level'] = df.apply(avg_skill, axis=1)

plt.figure(figsize=(10, 6))
plt.scatter(df['Average_Skill_Level'], df['Automation_Probability_2030'], alpha=0.6)
plt.xlabel('Average Skill Level')
plt.ylabel('Automation Probability')
plt.title('Average Skill Level vs Automation Probability')
plt.tight_layout()
plt.show()

# ---------------------------------------------------
# EXPERIENCE VS AUTOMATION PROBABILITY
# ---------------------------------------------------
plt.figure(figsize=(10, 6))
plt.scatter(df['Years_Experience'], df['Automation_Probability_2030'], alpha=0.6)
plt.xlabel('Years of Experience')
plt.ylabel('Automation Probability')
plt.title('Experience vs Automation Probability')
plt.tight_layout()
plt.show()

# ---------------------------------------------------
# SALARY DISTRIBUTION
# ---------------------------------------------------
plt.figure(figsize=(10, 6))
plt.hist(df['Average_Salary'], bins=20, edgecolor='black', color='purple')
plt.xlabel('Average Salary')
plt.ylabel('Frequency')
plt.title('Distribution of Salaries')
plt.tight_layout()
plt.show()

# ---------------------------------------------------
# AUTOMATION PROBABILITY BY EDUCATION LEVEL
# ---------------------------------------------------
def get_edu_automation(edu_level):
    total = 0
    count = 0
    for i in range(len(df)):
        if df.loc[i, 'Education_Level'] == edu_level:
            total += df.loc[i, 'Automation_Probability_2030']
            count += 1
    return total / count

edu_levels = df['Education_Level'].unique()
avg_auto = [get_edu_automation(level) for level in edu_levels]

plt.figure(figsize=(10, 6))
plt.bar(edu_levels, avg_auto, color='red')
plt.xlabel('Education Level')
plt.ylabel('Average Automation Probability')
plt.title('Automation Probability by Education Level')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("\nAverage Automation Probability by Education Level:")
for level, auto in zip(edu_levels, avg_auto):
    print(f"{level}: {auto:.2f}")

# ---------------------------------------------------
# TOP 10 MOST & LEAST AUTOMATABLE JOBS
# ---------------------------------------------------
job_avg = (
    df.groupby('Job_Title')['Automation_Probability_2030']
      .mean()
      .sort_values(ascending=False)
)

print("\nTop 10 Jobs Most at Risk (Averaged):")
print(job_avg.head(10))

print("\nTop 10 Jobs Least at Risk (Averaged):")
print(job_avg.tail(10))

# ---------------------------------------------------
# SAMPLING ANALYSIS
# ---------------------------------------------------
sample = df.sample(100)

sample_mean = mean(sample['Automation_Probability_2030'].to_list())
population_mean = mean(df['Automation_Probability_2030'].to_list())

print("\nSample Mean:", sample_mean)
print("Population Mean:", population_mean)

# ---------------------------------------------------
# END OF ANALYSIS
# ---------------------------------------------------