text = "The sun is the most prominent feature in our solar system. It is the largest object which contains approximately 98% of the total mass."
print(text)
input = input("Type the following text as fast as you can ")
b= 0
for i in  range(0, len(text)):
    if input[i]== text[i]:
        b+=1

score = (b/len(text))*100
print("Your score is "+ str(score))