from simple_gpt import simple_gpt

llm = simple_gpt()

while True:
     user = input("user> ")
     llm.memory_append = [user, "user"]
     print(llm.complete())
     