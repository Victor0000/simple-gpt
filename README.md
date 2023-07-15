# Simple-gpt
A super simple lightwight llm api wrapper, call llm with only 4 lines of code

# examples:
```python
from simple_gpt import simple_gpt

llm = simple_gpt()
llm.memory_append = ["Who are you?", "user"]
completion = llm.complete()
```
# Road Map
## llm support
- Support openai api calls
- Support other llms

## Tools
- Support more tools that can be performed by agents

## Suports external apis
- Discord bot
- Instagram / messenger api
