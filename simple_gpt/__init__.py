import openai
class simple_gpt:
     def __init__(
          self, 
          llm: str = "open-ai",
          llm_format: str = "chat",   
          llm_model: str = "gpt-3.5-turbo", 
          temperature: float = 0.7,
          max_tokens: int = 150,
          llm_key: str = "",
     ) -> None:
          
          # llm setup
          self.__llm = llm
          self.__llm_format = llm_format
          self.__llm_key = llm_key
          self.__llm_model = llm_model
          self.__temperature = temperature
          self.__max_tokens = max_tokens
          
          # llm specific setup
          if self.__llm == "open-ai":
               openai.api_key = self.__llm_key
          
          # memory
          self.__protected_memory = []
     
     @property
     def memory(self):
          return self.__protected_memory

     @memory.setter
     def memory_append(self, set):
          if self.__llm_format == "chat":
               prompt, type = set
               self.__protected_memory.append({"role": type, "content": prompt})

     # Global completion call to the llm
     def complete(self):
          if self.__llm == "open-ai" and self.__llm_format == "chat":
               completion = self.__llm_open_ai()
               self.memory_append = [completion,"assistant"]
               return completion
                              
     # Open AI completion call
     def __llm_open_ai(self) -> str:
          for attempt in range(5):
               try:
                    return openai.ChatCompletion.create(
                         model=self.__llm_model, 
                         messages=self.memory_append, 
                         temperature=self.__temperature,
                         max_tokens=self.__max_tokens,
                    ).choices[0].message.content
               except:
                    print("Trying again...")
                    
               print("max attempt reached llm_open_ai error") 
