import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National',
          'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana',
          'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho',
          'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan',
          'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico',
          'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa',
          'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana',
          'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California',
          'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island',
          'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia',
          'ND': 'North Dakota', 'VA': 'Virginia'}


def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ],
    columns=["State", "RegionName"]  )

    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''
    import re
    columns = ["State", "RegionName"]
    df = pd.DataFrame(columns=columns)
    with open("data/university_towns.txt") as f:
        for line in f.readlines():
            if "[edit]" in line:
                state_name = line[:-7]
            else:
                region_name = re.sub(r' \((\S|\s)*', '', line)
                df = df.append({'State': state_name, 'RegionName': region_name}, ignore_index=True)
    return df


def get_GDP():
    df_GDP = pd.read_excel('data/gdplev.xls', skiprows=8, usecols=[4, 6], names=['quarter', 'GDP'], header=None)
    df_GDP = df_GDP[df_GDP['quarter'] > '2000']
    return df_GDP


def get_recession_start():
    '''Returns the year and quarter of the recession start time as a
    string value in a format such as 2005q3'''
    df_gdp = get_GDP()
    GDP_1 = df_gdp.iloc[0]['GDP']
    flag = False
    start_quarter = df_gdp.iloc[0]['quarter']
    for index, row in df_gdp[1:].iterrows():
        GDP_2 = row['GDP']
        if GDP_2 < GDP_1:
            if flag is True:
                return start_quarter
            else:
                flag = True
        else:
            flag = False
        GDP_1 = GDP_2
        start_quarter = row['quarter']
    return "No recession found"


def get_recession_end():
    '''Returns the year and quarter of the recession end time as a
    string value in a format such as 2005q3'''
    df_gdp = get_GDP()
    recession_start = get_recession_start()
    df_gdp = df_gdp[df_gdp['quarter'] > recession_start]
    GDP_1 = df_gdp.iloc[0]['GDP']
    flag = False
    for index, row in df_gdp[1:].iterrows():
        GDP_2 = row['GDP']
        if GDP_2 > GDP_1:
            if flag is True:
                return row['quarter']
            else:
                flag = True
        else:
            flag = False
        GDP_1 = GDP_2
    return "No recession found"


def get_recession_bottom():
    '''Returns the year and quarter of the recession bottom time as a
    string value in a format such as 2005q3'''
    df_GDP = get_GDP()
    recession_start = get_recession_start()
    recession_end = get_recession_end()
    df_GDP = df_GDP[df_GDP['quarter'] >= recession_start]
    df_GDP = df_GDP[df_GDP['quarter'] < recession_end]
    return df_GDP.loc[df_GDP['GDP'].idxmin()]['quarter']


def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].

    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.

    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''
    df_homes = pd.read_csv('data/City_Zhvi_AllHomes.csv').drop(['RegionID', 'Metro', 'CountyName', 'SizeRank'], axis=1)
    df_homes['State'] = df_homes['State'].map(states)
    columns = df_homes.columns[2:]
    columns = columns[columns < '2000']
    df_homes = df_homes.drop(columns, axis=1)

    columns = df_homes.columns[2:]
    quarters = list(get_GDP()['quarter']) + ['2016q3']
    df = pd.DataFrame(columns=["State", "RegionName"] + quarters)
    df[["State", "RegionName"]] = df_homes[["State", "RegionName"]]
    for i in range(len(quarters)):
        df[quarters[i]] = df_homes[columns[i * 3:i * 3+3]].mean(axis=1)
    df = df.set_index(['State', 'RegionName'])
    return df


def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values,
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence.

    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''
    df = convert_housing_data_to_quarters()
    recession_start = get_recession_start()
    recession_bottom = get_recession_bottom()
    df['price_ratio'] = df[recession_start] / df[recession_bottom]
    df_town = get_list_of_university_towns().set_index(['State', 'RegionName'])

    same = df.index.intersection(df_town.index)
    different = df.index.difference(df_town.index)

    is_uni = (df.loc[same])['price_ratio'].dropna().values
    not_uni = (df.loc[different])['price_ratio'].dropna().values

    ttest_result = ttest_ind(is_uni, not_uni)
    p = ttest_result[1]
    difference = (p < .01)

    if np.average(is_uni) > np.average(not_uni):
        better = "non-university town"
    else:
        better = "university town"
    return difference, p, better


if __name__ == "__main__":
    ans = run_ttest()
