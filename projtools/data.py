import pandas as pd
raw_data = pd.read_csv('CompasAnalysis/compas-scores-two-years.csv')
df = raw_data[['age','c_charge_degree', 'race', 'age_cat', 'score_text', 'sex', 'priors_count','days_b_screening_arrest', 'decile_score', 'is_recid', 'two_year_recid', 'c_jail_in', 'c_jail_out']]
df = df[df['days_b_screening_arrest'] <= 30]
df = df[df['days_b_screening_arrest'] >= -30]
df = df[df['is_recid'] != -1]
df = df[df['c_charge_degree'] != '0']
df = df[df['score_text'] != 'N/A']
#Combining Medium and High scores
df['score_text_low/high'] = df['score_text'].apply(lambda x : 'HighScore' if x != 'Low' else 'LowScore')
#Creating dummy variables and setting reference category
dummy_df = pd.get_dummies(df[['c_charge_degree','age_cat','race','sex','score_text_low/high']], dtype='int')
dummy_df = dummy_df.drop(['age_cat_25 - 45', 'race_Caucasian','sex_Male','score_text_low/high_LowScore','c_charge_degree_F'], axis=1)
df = pd.concat([df, dummy_df], axis=1)
#Renaming columns to comply with smf constraints
rename_dict = {
    'score_text_low/high_HighScore': 'score_text_low_high_HighScore',
    'age_cat_Less than 25': 'age_cat_Less_than_25',
    'age_cat_Greater than 45': 'age_cat_Greater_than_45',
    'race_African-American': 'race_African_American',
    'race_Native American': 'race_Native_American'
}
df.rename(columns=rename_dict, inplace=True)
assert len(df) == 6172

#---

raw_data_violent = pd.read_csv('CompasAnalysis/compas-scores-two-years-violent.csv')
violent_df = raw_data_violent[['age','c_charge_degree', 'race', 'age_cat', 'v_score_text', 'sex', 'priors_count','days_b_screening_arrest', 'v_decile_score', 'is_recid', 'two_year_recid']]
violent_df = violent_df[violent_df['days_b_screening_arrest'] <= 30]
violent_df = violent_df[violent_df['days_b_screening_arrest'] >= -30]
violent_df = violent_df[violent_df['is_recid'] != -1]
violent_df = violent_df[violent_df['c_charge_degree'] != '0']
violent_df = violent_df[violent_df['v_score_text'] != 'N/A']
#combining Medium and High scores
violent_df['v_score_text_low/high'] = violent_df['v_score_text'].apply(lambda x : 'HighScore' if x != 'Low' else 'LowScore')
#creating dummy variables and setting reference category
dummy_violent_df = pd.get_dummies(violent_df[['c_charge_degree','age_cat','race','sex','v_score_text_low/high']], dtype='int')
dummy_violent_df = dummy_violent_df.drop(['age_cat_25 - 45', 'race_Caucasian','sex_Male','v_score_text_low/high_LowScore','c_charge_degree_F'], axis=1)
violent_df = pd.concat([violent_df, dummy_violent_df], axis=1)
#Renaming columns to comply with smf constraints
rename_dict = {
    'v_score_text_low/high_HighScore': 'v_score_text_low_high_HighScore',
    'age_cat_Less than 25': 'age_cat_Less_than_25',
    'age_cat_Greater than 45': 'age_cat_Greater_than_45',
    'race_African-American': 'race_African_American',
    'race_Native American': 'race_Native_American'
}
violent_df.rename(columns=rename_dict, inplace=True)
assert len(violent_df) == 4020

#---

raw_data_cox = pd.read_csv('CompasAnalysis/cox-parsed.csv')
cox_df = raw_data_cox[raw_data_cox['score_text'] != 'N/A']
cox_df = cox_df[cox_df['end'] > cox_df['start']]
#Creating dummy variables and setting reference category
dummy_cox_df = pd.get_dummies(cox_df[['race','score_text']], dtype='int')
dummy_cox_df = dummy_cox_df.drop(['race_Caucasian','score_text_Low'], axis=1)
cox_df = pd.concat([cox_df, dummy_cox_df], axis=1)
cox_df = cox_df.drop_duplicates(subset=['id'], keep = 'first')
cox_df = cox_df[~cox_df['score_text'].isna()]
cox_df = cox_df.drop_duplicates(subset=['name', 'dob'], keep='first')
cox_df['duration'] = cox_df['end'] - cox_df['start']
assert len(cox_df) == 10314

#---

raw_data_cox_violent = pd.read_csv('CompasAnalysis/cox-violent-parsed.csv')
cox_df_violent = raw_data_cox_violent[raw_data_cox_violent['score_text'] != 'N/A']
cox_df_violent = cox_df_violent[~cox_df_violent['score_text'].isna()]
cox_df_violent = cox_df_violent[cox_df_violent['end'] > cox_df_violent['start']]
cox_df_violent = cox_df_violent.drop_duplicates(subset=['name', 'dob'], keep='first')
cox_df_violent['duration'] = cox_df_violent['end'] - cox_df_violent['start']
#this finds the total lifetime per person
lifetimes_df =  pd.DataFrame(cox_df_violent.groupby('id')[['start','end']].sum().apply(lambda x: x['end'] - x['start'], axis=1)).rename(columns={0:'lifetime'})
lifetimes = lifetimes_df['lifetime']
#removing duplicate ID rows
cox_df_violent = cox_df_violent[~cox_df_violent['id'].duplicated(keep='first')]
cox_df_violent['lifetime'] = lifetimes
#if recidivist filter lifetimes so only contains people under two years - otherwise contain people who did not recidivise for over two years
cox_df_violent = cox_df_violent[((cox_df_violent['lifetime'] <= 730) & (cox_df_violent['is_violent_recid'] == 1)) | (cox_df_violent['lifetime'] > 730)]
display('All tests passed. Your dataframes are: \'df\', \'violent_df\', \'cox_df\' and \'cox_df_violent\'')
