import re

sample = "student turns 16,&quot; Dr. Delma Blinson, superintendent of the city schools remarked. &quot;But the problem basically goes back"
sample2 = "student turns 16,&quot; Dr. Delma Blinson, &nbsp;superintendent of the city schools remarked. ^^ &nbsp;But the problem basically goes back"
output = sample
output2 = sample2

input_text = open("files/example2.txt", "r")
output_text = input_text.read()
output_file = open("files/output.txt", "w")

patterns = ["&quot;", "&nbsp;", "&gt;", "&lt;", "&amp;"]
replaces = ['"', " ", ">", "<", "&"]
replaces_counter = 0

for pat in patterns:    
    print(pat)
    print(replaces_counter)
    if pat in output_text:
        output_text = re.sub(pat, replaces[replaces_counter], output_text)
    replaces_counter += 1
    
# having trouble with removing carets via regex despite using escape chars. workaround.
output_text = output_text.replace("^", "")

output_file.write(output_text)

input_text.close()
output_file.close()

#print(input_text)