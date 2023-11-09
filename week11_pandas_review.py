import pandas as pd

df = pd.DataFrame(
    [[99, 89, 100],
        [91, 98, 90],
        [100, 97, 85],
        [83, 100, 94]],
    index=[1, 2, 3, 4],
    columns=['KOR', 'ENG', 'MAT']
)
print(df)
# df_copy = df.iloc[:, [0, 2]]
# df_copy = df.loc[:, ['KOR', 'MAT']]
# df_copy = df.loc[:, 'KOR':'MAT':2] #loc는 마지막으로 지정한 항목까지 포함해서 출력

#국어, 수학 칼럼을 추출
# 조건은 국어 성적이 95점 이상인 경우
df_copy = df.loc[df['KOR'] >= 95, ['KOR', 'MAT']]
print(df_copy)

#1번 학생의 수학성적(100) 출력
print(df.at[1, 'MAT'])
print(df.iat[0, 2]) #iat은 index로 사용하기 때문에 loc처럼 행열을 가져오지 않음


# df1 = pd.DataFrame(
#     {
#         "KOR" : [99, 91, 100],
#         "ENG" : [89, 98, 97],
#         "MAT" : [100, 90, 85]
#     }, index=[1, 2, 3]
# )
# print(df1)
# print(df1.sort_values('MAT'))
# df1 = df1.drop(columns=['ENG'])
# print(df1)

# df = (pd.melt(df) #melt -> 데이터프레임을 바꿔주는 함수
#        .rename(columns={
#         'variable': 'subject', # 이름 변경
#         'value': 'score'})
#         .query('score >= 90') # score가 90점 이상인 데이터만 뽑아냄
#         .sort_values('score',ascending=False)
#        )
#
# print(df)
# print(df.iloc[:, [1]])

