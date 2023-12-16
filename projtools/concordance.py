def concordance_decile_score(df,columns,sample_size):
    identifier, score = columns
    true_count = 0
    false_count = 0
    concordance_df = df[columns]
    concordance_df = concordance_df.sample(sample_size)
    concordance_df = concordance_df.reset_index()
    index_pairs = list(combinations(concordance_df.index, 2))
    for pair in index_pairs:
        index1, index2 = pair
        row1, row2 = df.iloc[index1], df.iloc[index2]
        if row1[identifier] > row2[identifier]:
            if row1[score] > row2[score]:
                true_count += 1
            elif row1[score] < row2[score]:
                false_count += 1
        elif row1[identifier] < row2[identifier]:
            if row1[score] < row2[score]:
                true_count += 1
            elif row1[score] > row2[score]:
                false_count += 1
    concordance = true_count / (true_count + false_count)
    return concordance * 100

def concordance_text_score(df,columns,sample_size):
    identifier, score = columns
    true_count = 0
    false_count = 0
    concordance_df = df[columns]
    concordance_df = concordance_df.sample(sample_size)
    concordance_df = concordance_df.reset_index()
    concordance_df[score] = concordance_df[score].replace(['Low','Medium','High'],[0,1,1])
    index_pairs = list(combinations(concordance_df.index, 2))
    for pair in index_pairs:
        index1, index2 = pair
        row1, row2 = df.iloc[index1], df.iloc[index2]
        if row1[identifier] > row2[identifier]:
            if row1[score] > row2[score]:
                true_count += 1
            elif row1[score] < row2[score]:
                false_count += 1
        elif row1[identifier] < row2[identifier]:
            if row1[score] < row2[score]:
                true_count += 1
            elif row1[score] < row2[score]:
                false_count += 1
    concordance = true_count / (true_count + false_count)
    return concordance * 100