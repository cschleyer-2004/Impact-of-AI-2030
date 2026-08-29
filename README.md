AI Impact on Jobs 2030 — Data Analysis

A Python data analysis project exploring how AI and automation are projected to affect different jobs by 2030. The script downloads a Kaggle dataset, cleans it, and produces a series of visualizations and statistical summaries covering automation risk, AI exposure, required skills, experience, salary, and education level.

Dataset
Source: khushikyad001/ai-impact-on-jobs-2030 (via kagglehub)
File used: AI_Impact_on_Jobs_2030.csv

Key columns referenced by the script:

Column	Description
Job_Title	Name of the job/role
Automation_Probability_2030	Estimated probability the role is automated by 2030
AI_Exposure_Index	Degree of exposure of the role to AI technologies
Skill_*	One or more columns capturing required skill levels
Years_Experience	Years of experience associated with the role
Average_Salary	Average salary for the role
Education_Level	Minimum/typical education level for the role
Project Structure
.
├── main.py                                       # Main analysis script
├── AI_Impact_on_Jobs_2030.csv                    # Downloaded dataset
├── Automation_prob_by_edu_lvl.png                # Bar chart: automation probability by education level
├── Automation_prob_by_job-title.png              # Bar chart: automation probability by job title
├── AVG_Skill_lvl_vs_automation_probability.png   # Scatter: average skill level vs automation probability
├── Correlation_between_AI_Exposure_and_automation_risk.png  # Scatter: AI exposure vs automation probability
├── Distribution_of_automation_prob_amongst_jobs.png          # Histogram: automation probability distribution
├── Experience_VS_Automation_Probability.png      # Scatter: years of experience vs automation probability
├── Salary_Distribution.png                       # Histogram: salary distribution
├── Probability and Applied Stats Final Presentation.pdf  # Project presentation
└── Probability and Applied Stats Final Project.docx       # Written report
Requirements
Python 3.8+
pandas
matplotlib
kagglehub

Install dependencies:

bash
pip install pandas matplotlib kagglehub

You'll also need a Kaggle account and API credentials configured for kagglehub to download the dataset (see kagglehub docs).

Usage

Run the analysis script:

bash
python main.py

The script will:

Download the dataset from Kaggle and locate the CSV file.
Load the data and print a preview, info summary, and descriptive statistics.
Drop duplicate rows and report missing values.
Generate and display several plots (each opens in its own window).
Print key statistics and correlations to the console.
Analysis Performed
Automation Probability by Job Title — bar chart comparing automation risk across roles.
Automation Probability Distribution — histogram showing the overall spread of automation risk.
AI Exposure vs Automation Probability — scatter plot plus a manually computed Pearson correlation coefficient.
Average Skill Level vs Automation Probability — computes an average across all Skill_* columns per job and plots it against automation risk.
Experience vs Automation Probability — scatter plot of years of experience against automation risk.
Salary Distribution — histogram of average salaries across roles.
Automation Probability by Education Level — bar chart of average automation risk grouped by education level.
Top 10 Most/Least Automatable Jobs — job titles ranked by average automation probability.
Sampling Analysis — compares the mean automation probability of a random 100-row sample against the full population mean.
Notes
Correlation and averaging functions (mean, correlation, avg_skill, get_edu_automation) are implemented manually (without numpy/pandas built-ins) for instructional purposes.
Each plt.show() call blocks until the plot window is closed; close each window to proceed to the next chart.
This project accompanies a written report (Probability and Applied Stats Final Project.docx) and presentation (Probability and Applied Stats Final Presentation.pdf).
