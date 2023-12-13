import pandas as pd

def read_data():
    read_linting_results = pd.read_csv('data/blast_linting_results.csv')
    read_review_test_results = pd.read_csv('data/blast_review_test_results.csv')
    read_reviews = pd.read_csv('data/blast_reviews.csv')
    data_tests = pd.read_csv('data/blast_tests.csv')
    read_code_blast_tests = pd.read_csv('data/code_blast_tests.csv')
    read_exercises = pd.read_csv('data/exercises.csv')
    data_implementation_exercise = pd.read_csv('data/implementation_exercise.csv')

    return read_linting_results, read_review_test_results, read_reviews, data_tests, read_code_blast_tests, read_exercises, data_implementation_exercise

def clean_linting_results(data):
    cleaned_data = data[['blast_review_id', 'file_name', 'message', 'type', 'line', 'column']]
    cleaned_data = cleaned_data[cleaned_data['type'].str.lower().isin(['error'])]

    return cleaned_data


def clean_review_test_results(data):
    cleaned_data = data[['blast_review_id', 'test_id', 'human_error_message', 'test_language']]

    return cleaned_data

def clean_data_reviewss(data):
    cleaned_data = data[['id', 'implementation_id', 'state', 'created_on']]

    return cleaned_data

def clean_data_exercises(data):
    cleaned_data = data[['id', 'title', 'files_to_turn_in']]
    
    return cleaned_data

def clean_data_code_blast_tests(data):
    cleaned_data = data[['id', 'exercise_id', 'title', 'test_type', 'created_on', 'language']]
    
    return cleaned_data
