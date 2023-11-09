import pandas as pd

df = pd.DataFrame(
    [[99, 89, 81],
        [91, 98, 90],
        [95, 97, 85],
        [83, 96, 94]],
    index=[1, 2, 3, 4],
    columns=['KOR', 'ENG', 'MAT']
)

scores = [
    [99, 89, 81],
    [91, 98, 90],
    [95, 97, 85],
    [83, 96, 94]
]
index = [1, 2, 3, 4]
columns = ['KOR', 'ENG', 'MAT']

for c in columns:
    print(f'{c}', end=' ')
print()
for i in range(4):
    print(index[i], end=' ')
    for j in range(3):
        print(scores[i][j], end=" ")
        scores[i][j] = scores[i][j]+1
    print()

print()

for c in columns:
    print(f'{c}', end=' ')
print()
for i in range(4):
    print(index[i], end=' ')
    for j in range(3):
        print(scores[i][j], end=" ")
    print()

def scale_score(n):
    return n + 1
#
# print(df)
# df = df.apply(scale_score)
# print(df)

# print(df)
# df = df.apply(lambda n: n+1)
# print(df)

#국어, 수학 칼럼을 추출
# 조건은 국어 성적이 95점 이상인 경우
# df_copy = df.loc[df['KOR'] >= 95, ['KOR', 'MAT']]
# print(df_copy)

# print(df.mean()) # 평균 출력
# print(df.max()) # 최대 값 출력
# print(df)
# df_copy = df.iloc[:, [0, 2]]
# df_copy = df.loc[:, ['KOR', 'MAT']]
# df_copy = df.loc[:, 'KOR':'MAT':2] #loc는 마지막으로 지정한 항목까지 포함해서 출력

#1번 학생의 수학성적(100) 출력
# print(df.at[1, 'MAT'])
# print(df.iat[0, 2]) #iat은 index로 사용하기 때문에 loc처럼 행열을 가져오지 않음

# 국어, 영어 성적 둘 다 95점 이상인 경우
# print(df.query('KOR>=95 and ENG>=95'))

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

