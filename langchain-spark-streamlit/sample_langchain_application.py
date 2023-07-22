from pyspark_ai import SparkAI
from langchain.chat_models import ChatOpenAI

# spark_ai = SparkAI()

spark_ai = SparkAI(llm=ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0))
spark_ai.activate()  # active partial functions for Spark DataFrame

auto_df = spark_ai.create_df("https://www.carpro.com/blog/full-year-2022-national-auto-sales-by-brand")

auto_df.show(n=5)

auto_top_growth_df=auto_df.ai.transform("brand with the highest growth")

auto_top_growth_df.show()