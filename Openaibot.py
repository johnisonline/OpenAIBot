#script to connect to openai api and print the response
import openai
import os
import json
from openai import OpenAI

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "assistant",
            "content": """I'm giving you two member records in a JSON format. Call Json 1 as incoming record from customer. Json2 to as existing record in my system. I need you take role of a smart matching system to compare and look at all attributes that are same and those that are different. Avoid terms like object and array in your response.  summarize very briefly what's different (show values) and what's same (dont show values) by just listing it out in a single sentence.

            Example Output:
            The values that are different between incoming record and existing record are the lastName (Cruise and cena) and the zipcode (55315 and 55318), while the values that are the same between them are the id, firstName, SSN, streetname, city, and state.  
            ///Json 1
            {
  "employees": {
    "employee": [
      {
        "id": "1",
        "firstName": "Tom",
        "lastName": "Seck",
        "SSN": "123456789",
        "address": {
          "streetname": "123 street",
          "city": "carver",
          "state": "mn",
          "zipcode": "55315"
        }
      }
    ]
  }
}

///Json 2
{
  "employees": {
    "employee": [
      {
        "id": "1",
        "firstName": "Tom",
        "lastName": "cena",
        "SSN": "123456789",
        "address": {
          "streetname": "123 street",
          "city": "carver",
          "state": "AZ",
          "zipcode": "55315"
        }
      }
    ]
  }
}

""",
        }
    ],
    model="gpt-3.5-turbo",
)
print(chat_completion.choices[0].message.content)

