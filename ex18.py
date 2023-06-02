import pandas as pd
sd = pd.Series([1,2, None, 4], index = ['a', 'b', 'c', 'd'])
print(sd)
print(sd.shape)
print(sd.size)
print(sd.isna())
print(f'sd[0] : {sd[0]}')
# def function() -> None:
#     a = 10
#     return None
print(f"sd[0] : {sd['a']}")
print(f"sd[1] : {sd['b']}")
print(f"sd[2] : {sd['c'] + 0}")
print(f"sd[4] : {sd['d']}")