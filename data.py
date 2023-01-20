import pandas as pd

dfa = pd.read_csv('amazon_prime_titles-score.csv')
dfa['id'] ='a' + dfa['show_id'].astype(str)
dfa['plataforma'] = 'amazon'
dfa['rating'].fillna('G', inplace=True)
dfa["date_added"] = pd.to_datetime(dfa["date_added"]).dt.strftime('%Y-%m-%d')
dfa1 = dfa[['type','title','director','cast','listed_in','description','rating','duration', 'country']].apply(lambda x: x.astype(str).str.lower())
dfa.loc[:, ['type','title','director','cast','listed_in','description','rating','duration', 'country']] = dfa1[['type','title','director','cast','listed_in','description','rating','duration', 'country']]
dfa[['duration_int', 'duration_type']] = dfa['duration'].str.split(' ', expand=True)
dfa['duration_int'] = pd.to_numeric(dfa['duration_int'],errors='coerce').astype(pd.Int64Dtype())
dfa['duration_type'] = dfa['duration_type'].convert_dtypes()
dfa['duration'] = dfa['duration'].replace(['seasons'], 'season', regex = True)
dfa.to_csv('amazon_prime_titles-score.csv', index=False)


dfd = pd.read_csv('disney_plus_titles-score.csv')
dfd['id'] ='d' + dfd['show_id'].astype(str)
dfd['plataforma'] = 'disney'
dfd['rating'].fillna('G', inplace=True)
dfd["date_added"] = pd.to_datetime(dfd["date_added"]).dt.strftime('%Y-%m-%d')
dfd1 = dfd[['type','title','director','cast','listed_in','description','rating','duration', 'country']].apply(lambda x: x.astype(str).str.lower())
dfd.loc[:, ['type','title','director','cast','listed_in','description','rating','duration', 'country']] = dfd1[['type','title','director','cast','listed_in','description','rating','duration', 'country']]
dfd[['duration_int', 'duration_type']] = dfd['duration'].str.split(' ', expand=True)
dfd['duration_int'] = pd.to_numeric(dfd['duration_int'],errors='coerce').astype(pd.Int64Dtype())
dfd['duration_type'] = dfd['duration_type'].convert_dtypes()
dfd['duration'] = dfd['duration'].replace(['seasons'], 'season', regex = True)
dfd.to_csv('disney_plus_titles-score.csv', index=False)


dfh = pd.read_csv('hulu_titles-score (2).csv')
dfh['id'] ='h' + dfh['show_id'].astype(str)
dfh['plataforma'] = 'hulu'
dfh['rating'].fillna('G', inplace=True)
dfh["date_added"] = pd.to_datetime(dfh["date_added"]).dt.strftime('%Y-%m-%d')
dfh1 = dfh[['type','title','director','cast','listed_in','description','rating','duration','country']].apply(lambda x: x.astype(str).str.lower())
dfh.loc[:, ['type','title','director','cast','listed_in','description','rating','duration', 'country']] = dfh1[['type','title','director','cast','listed_in','description','rating','duration', 'country']]
dfh[['duration_int', 'duration_type']] = dfh['duration'].str.split(' ', expand=True)
dfh['duration_int'] = pd.to_numeric(dfh['duration_int'],errors='coerce').astype(pd.Int64Dtype())
dfh['duration_type'] = dfh['duration_type'].convert_dtypes()
dfh['duration'] = dfh['duration'].replace(['seasons'], 'season', regex = True)
dfh.to_csv('hulu_titles-score (2).csv', index=False)

dfn = pd.read_csv('netflix_titles-score.csv')
dfn['id'] ='n' + dfn['show_id'].astype(str)
dfn['plataforma'] = 'netflix'
dfn['rating'].fillna('G', inplace=True)
dfn["date_added"] = pd.to_datetime(dfn["date_added"]).dt.strftime('%Y-%m-%d')
dfn1 = dfn[['type','title','director','cast','listed_in','description','rating','duration','country']].apply(lambda x: x.astype(str).str.lower())
dfn.loc[:, ['type','title','director','cast','listed_in','description','rating','duration','country']] = dfn1[['type','title','director','cast','listed_in','description','rating','duration', 'country']]
dfn[['duration_int', 'duration_type']] = dfn['duration'].str.split(' ', expand=True)
dfn['duration_int'] = pd.to_numeric(dfn['duration_int'],errors='coerce').astype(pd.Int64Dtype())
dfn['duration_type'] = dfn['duration_type'].convert_dtypes()
dfn['duration'] = dfn['duration'].replace(['seasons'], 'season', regex = True)
dfn.to_csv('netflix_titles-score.csv', index=False)


df_total = pd.concat([dfa, dfd, dfh, dfn])


