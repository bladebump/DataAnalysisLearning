import numpy as np
import pandas as pd


def answer_one():
    energy = pd.read_excel("data/Energy Indicators.xls", skiprows=17, skipfooter=38, usecols=[2, 3, 4, 5])
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy['Country'] = energy['Country'].str.replace('\d+', '')
    energy['Country'] = energy['Country'].str.replace(r" \(.*\)", '')
    energy = energy.replace('...', np.nan)
    energy['Energy Supply'] *= 1000000
    energy['Country'].replace({'Republic of Korea': 'South Korea', 'United States of America': 'United States',
                               'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
                               'China, Hong Kong Special Administrative Region': 'Hong Kong'}, inplace=True)
    GDP = pd.read_csv("data/world_bank.csv", skiprows=4)
    GDP['Country Name'].replace(
        {'Korea, Rep.': 'South Korea', 'Iran, Islamic Rep.': 'Iran', 'Hong Kong SAR, China': 'Hong Kong'}, inplace=True)
    GDP = GDP[['Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    ScimEn = pd.read_excel("data/scimagojr-3.xlsx")
    df = pd.merge(ScimEn, energy, left_on='Country', right_on='Country')
    df = pd.merge(df, GDP, left_on='Country', right_on='Country Name')
    df.drop('Country Name', axis=1, inplace=True)
    df = df.set_index('Country')
    return df[df['Rank'] < 16]


def answer_two():
    energy = pd.read_excel("data/Energy Indicators.xls", skiprows=17, skipfooter=38, usecols=[2, 3, 4, 5])
    energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
    energy['Country'] = energy['Country'].str.replace('\d+', '')
    energy['Country'] = energy['Country'].str.replace(r" \(.*\)", '')
    energy = energy.replace('...', np.nan)
    energy['Energy Supply'] *= 1000000
    energy['Country'].replace({'Republic of Korea': 'South Korea', 'United States of America': 'United States',
                               'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
                               'China, Hong Kong Special Administrative Region': 'Hong Kong'}, inplace=True)
    GDP = pd.read_csv("data/world_bank.csv", skiprows=4)
    GDP['Country Name'].replace(
        {'Korea, Rep.': 'South Korea', 'Iran, Islamic Rep.': 'Iran', 'Hong Kong SAR, China': 'Hong Kong'}, inplace=True)
    GDP = GDP[['Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    ScimEn = pd.read_excel("data/scimagojr-3.xlsx")
    df1 = pd.merge(ScimEn, energy, left_on='Country', right_on='Country', how='inner')
    df1 = pd.merge(df1, GDP, left_on='Country', right_on='Country Name', how='inner')
    df2 = pd.merge(ScimEn, energy, left_on='Country', right_on='Country', how='outer')
    df2 = pd.merge(df2, GDP, left_on='Country', right_on='Country Name', how='outer')
    return len(df2) - len(df1)


def answer_three():
    Top15 = answer_one()
    row = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']
    Top15['avgGDP'] = np.mean(Top15[row], axis=1)
    return Top15['avgGDP'].sort_values(ascending=False)


def answer_four():
    Top15 = answer_one()
    avgGDP = answer_three()
    name = avgGDP.index[5]
    return Top15.loc[name]['2015'] - Top15.loc[name]['2006']


def answer_five():
    Top15 = answer_one()
    return Top15['Energy Supply per Capita'].mean()


def answer_six():
    Top15 = answer_one()
    return Top15['% Renewable'].idxmax(), Top15['% Renewable'].max()


def answer_seven():
    Top15 = answer_one()
    Top15['Ratio citations'] = Top15['Self-citations'] / Top15['Citations']
    return Top15['Ratio citations'].idxmax(), Top15['Ratio citations'].max()


def answer_eight():
    Top15 = answer_one()
    Top15['Pop Est'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    return Top15['Pop Est'].sort_values(ascending=False).index[2]


def answer_nine():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
    return Top15['Citable docs per Capita'].corr(Top15['Energy Supply per Capita'])


def answer_ten():
    Top15 = answer_one()
    return (Top15['% Renewable'] >= Top15['% Renewable'].median()).astype(int)


def answer_eleven():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    ContinentDict = pd.Series({'China': 'Asia',
                               'United States': 'North America',
                               'Japan': 'Asia',
                               'United Kingdom': 'Europe',
                               'Russian Federation': 'Europe',
                               'Canada': 'North America',
                               'Germany': 'Europe',
                               'India': 'Asia',
                               'France': 'Europe',
                               'South Korea': 'Asia',
                               'Italy': 'Europe',
                               'Spain': 'Europe',
                               'Iran': 'Asia',
                               'Australia': 'Australia',
                               'Brazil': 'South America'})
    Top15['Continent'] = ContinentDict
    ans = Top15.groupby('Continent')['PopEst'].agg([np.size, np.sum, np.average, np.std])
    return ans


def answer_twelve():
    Top15 = answer_one()
    ContinentDict = pd.Series({'China': 'Asia',
                               'United States': 'North America',
                               'Japan': 'Asia',
                               'United Kingdom': 'Europe',
                               'Russian Federation': 'Europe',
                               'Canada': 'North America',
                               'Germany': 'Europe',
                               'India': 'Asia',
                               'France': 'Europe',
                               'South Korea': 'Asia',
                               'Italy': 'Europe',
                               'Spain': 'Europe',
                               'Iran': 'Asia',
                               'Australia': 'Australia',
                               'Brazil': 'South America'})
    Top15['Continent'] = ContinentDict
    Top15['Bin'] = pd.cut(Top15['% Renewable'], 5)
    return Top15.groupby(['Continent', 'Bin']).count().dropna()['Rank']


def answer_thirteen():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    return Top15.apply(lambda x: "{:,}".format(x['PopEst']), axis=1)


if __name__ == "__main__":
    ans1 = answer_one()
    ans2 = answer_two()
    ans3 = answer_three()
    ans4 = answer_four()
    ans5 = answer_five()
    ans6 = answer_six()
    ans7 = answer_seven()
    ans8 = answer_eight()
    ans9 = answer_nine()
    ans10 = answer_ten()
    ans11 = answer_eleven()
    ans12 = answer_twelve()
    ans13 = answer_thirteen()
