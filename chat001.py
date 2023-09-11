"""
At the command line, only need to run once to install the package via pip:
$ pip install google-generativeai
"""

import google.generativeai as palm

palm.configure(api_key="AIzaSyBsUWUWFT1_0WvLXcRSjdmPkjHsYoYeIgo")

defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.6,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}
context = "You are a world class expert on everything. Not only that, you love to help other people and you just say: \"I don't know\"if you don't know."
examples = [
  [
    "hi\n",
    "Hi! I'm chat-001. I can help with simple tasks and I say \"I don't know\" When I don't know."
  ]
]
messages = [
  "hi",
  "Hi! How can I help you today?",
  "hi",
  "Hi there! How can I help you today?"
]
messages.append("NEXT REQUEST")
response = palm.chat(
  **defaults,
  context=context,
  examples=examples,
  messages=messages
)
print(response.last) # Response of the AI to your most recent request
