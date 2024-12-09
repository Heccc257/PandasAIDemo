import os
import pandas as pd
from pandasai import Agent

# Sample DataFrame
sales_by_country = pd.DataFrame({
    "country": ["United States", "United Kingdom", "France", "Germany", "Italy", "Spain", "Canada", "Australia", "Japan", "China"],
    "revenue": [5000, 3200, 2900, 4100, 2300, 2100, 2500, 2600, 4500, 7000]
})
# By default, unless you choose a different LLM, it will use BambooLLM.
# You can get your free API key signing up at https://pandabi.ai (you can also configure it in your .env file)
os.environ["PANDASAI_API_KEY"] = "$2a$10$KxglpkIOgEH2MfC.WiSlQuz4x7UiL7z0bDpZSczwQFSnxfj/I2wei"

agent = Agent(sales_by_country)

answer = agent.chat(
    'Which are the top 5 countries by revenue?',
)
print(answer)