# Featurize function
def featurize(df):
    # explicit mappings for each categorical variable -> numerical values
    gender_mapping = {'male': 0, 'female': 1, 'non-binary': 2}
    platform_mapping = {'Instagram': 0, 'Facebook': 1, 'YouTube': 2}
    interests_mapping = {'Sports': 0, 'Travel': 1, 'Lifestlye': 2}
    location_mapping = {'United States': 0, 'United Kingdom': 1, 'Australia': 2}
    demographics_mapping = {'Urban': 0, 'Sub_Urban': 1, 'Rural': 2}
    profession_mapping = {'Software Engineer': 0, 'Student': 1, 'Marketer Manager': 2}
    age_mapping = {'Young': 0, 'Adult': 1, 'Old': 2}
    income_mapping = {'Poor': 0, 'Mid': 1, 'Rich': 2}

    # Transferring mappings to dataframe
    df['gender'] = df['gender'].map(gender_mapping)
    df['platform'] = df['platform'].map(platform_mapping)
    df['interests'] = df['interests'].map(interests_mapping)
    df['location'] = df['location'].map(location_mapping)
    df['demographics'] = df['demographics'].map(demographics_mapping)
    df['profession'] = df['profession'].map(profession_mapping)
    df['age_range'] = df['age_range'].map(age_mapping)
    df['income_type'] = df['income_type'].map(income_mapping)

    # Including boolean values direct as binary
    df['indebt'] = df['indebt'].astype(int)
    df['isHomeOwner'] = df['isHomeOwner'].astype(int)
    df['Owns_Car'] = df['Owns_Car'].astype(int)

    # Return only the encoded columns
    return df