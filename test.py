from pprint import pprint
import toml

a = toml.load("./config.toml")
# pprint(a)




SS = "1234567890qwertyuio"
LENGTH = 6
FILE = "y"
save_memory = False


TOTAL = 0       # nom of words
ALL_CHARS = 0   # nom of all chars
mem = 0  
    # str:  empty:49    +1 per additional character (49+total length of characters)
    #list:  empty:56    +8 per additional item in a list ( 56 + 8*total length of characters )
for i in range(1, LENGTH+1):
    wwil = len(SS)**i #words with i length
    TOTAL += wwil
    ALL_CHARS += len(SS)**i * (i+2)
    
    mem_str = 49 + i
    moil = 8*wwil + mem_str*wwil  # memory of i length
    mem +=  moil
    # print(f"{i} {wwil} {moil}")
mem+=56

print()
print(TOTAL)
print(ALL_CHARS)
print(mem)






