import numpy as np
import pandas as pd

data = np.array([
    [1, 5, 9],
    [2, np.nan, 10],
    [np.nan, 7, 11],
    [4, 8, np.nan]
])
print(data)

means = np.nanmean(data, axis=0) # 각 column의 평균 값들
for i in range(data.shape[1]):
    #print(i)
    mask = np.isnan(data[:, i])
    #print(mask) # True, False 값을 갖는 배열 생성
    data[mask, i] = means[i]
print(data)



# df = pd.DataFrame({
#     'A': [1, 2, np.nan, 4],
#     'B': [5, np.nan, 7, 8],
#     'C': [9, 10, 11, np.nan]
# })

#1
# df.fillna(df.mean(), inplace=True)
# print(df)

#2
# for col in df.columns:
#     #print(col)
#     df[col] = np.where(pd.isnull(df[col]), np.mean(df[col]), df[col])
#     print(df)

#3
# from sklearn.impute import SimpleImputer # 결측치 전용 처리 클래스
# i = SimpleImputer(strategy='median')
# df = pd.DataFrame(i.fit_transform(df), columns=df.columns)
# print(df)

# def info(x):
#     print(f"배열의 차원은 {x.ndim}입니다.")
#     print(f"배열의 shape는 {x.shape}입니다.")
#     print(f"원소의 개수는 {x.size}개 입니다.")
#
# np_1d = np.arange(1, 20, 2)
# print(np_1d)
# info(np_1d)
# np_1d = np_1d.reshape(1, 2, 5)
# print(np_1d)
# info(np_1d)
