# Importing Libraries
import ast
import pandas as pd
from datasets import load_dataset

def load_job_data():
  # Loading Data
  dataset = load_dataset('lukebarousse/data_jobs')
  df = dataset['train'].to_pandas()

  # Data Cleanup
  df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
  df['job_skills'] = df['job_skills'].apply(
    lambda x: ast.literal_eval(x) if pd.notna(x) else x
  )

  return df


