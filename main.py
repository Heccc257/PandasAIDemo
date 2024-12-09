import os
import pandas as pd
from pandasai import Agent

# Sample DataFrame
revenue_by_country = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "revenue": [5000, 3200, 2900, 4100, 2300, 2100, 2500, 2600, 4500, 7000]
})

countries_updated = [
    "United States", "France", "Germany", "Italy", "Spain", 
    "Canada", "Australia", "Japan", "China", "India", "Brazil"
]

# 国家对应的面积数据（单位：平方公里），直接以列表形式提供
areas = [
    9833520,  # United States
    640679,   # France
    357022,   # Germany
    301336,   # Italy
    505992,   # Spain
    9984670,  # Canada
    7692024,  # Australia
    377972,   # Japan
    9596961,  # China
    3287590,  # India
    8515767   # Brazil
]

# 创建 DataFrame
area_by_country = pd.DataFrame({
    "country": countries_updated,
    "area": areas
})


people = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie", "David", "Emily", "Frank", "Grace", "Henry", "Ivy", "Jack"],
    "age": [25, 30, 35, 40, 45, 50, 35, 30, 35, 40],
    "country": ["United States", "United States", "United States", "Canada", "China", "Japan", "Germany", "Germany", "Spain", "Spain"],
    "salary": [5000, 6000, 4500, 2600, 90000, 100000, 4200, 4000, 2700, 2100],
})

# By default, unless you choose a different LLM, it will use BambooLLM.
# You can get your free API key signing up at https://pandabi.ai (you can also configure it in your .env file)
os.environ["PANDASAI_API_KEY"] = "$2a$10$KxglpkIOgEH2MfC.WiSlQuz4x7UiL7z0bDpZSczwQFSnxfj/I2wei"

agent = Agent([revenue_by_country, area_by_country, people])

# response = agent.chat(
#     'Among the top 4 countries by area, which two have the highest revenue?',
# )

# print(response)

# response = agent.chat(
#     'join two tables revenue_by_country and area by country'
# )
# print(response)

# response = agent.chat(
#     'join two tables revenue_by_country and people by country'
# )
# print(response)

response = agent.chat(
    'Who has salary higher than the revenue of their country?',
)
print(response)