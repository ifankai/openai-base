import os
from openai import OpenAI

# 加载  .env 到环境变量
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

# 配置 OpenAI 服务

client = OpenAI()

response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "讲个笑话"
        }
    ],
    model="gpt-3.5-turbo" # gpt-4
)

print(response)
print(response.choices[0].message.content)
