import datetime

class TextAnalyzer:
   def __init__(self,file:str):
       self.__txt = file
       self.__total_operations = []
       self.__content = self.set_content(self.__txt)



   def __get_content(self):
       self.__total_operations.append([self.get_content.__name__,datetime.datetime.now()])
       return self.__content

   def get_name(self):
       self.__total_operations.append([self.get_name.__name__,datetime.datetime.now()])
       return self.__txt

   def set_content(self, new_file):
       self.__total_operations.append(
           [self.set_content.__name__,datetime.datetime.now()])
       with open(new_file) as u:
           return u.read()

   def number_of_words(self):
        self.__total_operations.append(
           [self.number_of_words.__name__, datetime.datetime.now()])
        count = 0
        with open(self.__txt, "r") as f:
            for line in f:
                for w in line.split():
                    count += 1
        return count

   def frequency_words(self):
           self.__total_operations.append(
            [self.frequency_words.__name__, datetime.datetime.now()])
           freq = {}
           with open(self.__txt, "r") as f:
               for line in f:
                   for word in line.split():
                       if word not in freq:
                           freq.update({word : 1})
                       else:
                           freq[word] += 1
           return freq

   def most_frequent_word(self):

           freq = self.frequency_words()
           most_used_word_counter = 0
           most_used_word = None
           self.__total_operations.append(
               [self.most_frequent_word.__name__,datetime.datetime.now()])

           for i in freq:
               if freq[i] >= most_used_word_counter:
                   most_used_word = i
                   most_used_word_counter = freq[i]
           return most_used_word

   def get_last_oper(self):
       m = self.__total_operations[-1]
       return m[0]

   def get_datetime(self):
       m = self.__total_operations[-1]
       return m[1]






if __name__ == "__main__":
    x = TextAnalyzer("sample_text.txt")
    print(x.number_of_words())
    print(x.frequency_words())
    print(x.most_frequent_word())
    print(x.get_last_oper())
    print(x.get_datetime())



