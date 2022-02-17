import re 

output_file = open("C:/Users/gadhv/Desktop/genome_project/genome_output.txt", "w")
output_file.write('\n')



####################################################################################
# Function name: ReverseComplement()
# Objective: For Reversing and finding complement for pattern which are max in number
#########################################################################################

def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern

####################################################################################
# Function name: Reverse()
# Objective: For Reversing 
#######################################################################################

def Reverse(Pattern):
    reverse=Pattern[::-1]
    #print(reverse)
    return reverse

####################################################################################
# Function name: Cmplement()
# Objective: To find Complement of those patterns
#######################################################################################

def Complement(Pattern):
    complement  = { "A":"T", "T":"A", "C":"G", "G":"C" }
    ReverseComplement = ""
    for char in Pattern:
         ReverseComplement = ReverseComplement + complement.get(char)

    return ReverseComplement


################################################################
# Function name: PatternCount()
# Objective:  To return to find frequent words in the replication origin.
################################################################

def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text)-len(Pattern)+1):
        if Text[i:i+len(Pattern)] == Pattern:
            count = count+1
    return count 

####################################################################################
# Function name: PatternMatching()
# Objective: To find the starting indices where pattern matches 
#######################################################################################

def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)] == Pattern:
            positions.append(i)
    return positions


################################################################
# Function name: Frequencymap()
# Objective: To return the number of times each k-mer is repeated
# Input : 
# Output:
################################################################

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        count1 = 0
        count2 = 0
        RCPattern = ReverseComplement(Pattern)
        freq[Pattern] = 0
        count1 = len(re.findall(Pattern, Text))
        count2 = len(re.findall(RCPattern, Text))
        freq[Pattern] = count1 + count2
    return freq    


####################################################################################
# Function name: FrequentWords()
# Objective: To return the maximum pattern repeated and append in list given.
#########################################################################################
def FrequentWords(freq, k):
    words = []
    m = max(freq.values())
    if(m > 2):
        output_file.write("\nMax count value for this genome window is: ")
        output_file.write(str(m))
        for key in freq:
            if freq[key] == m:
                words.append(key)
        output_file.write("\n 9-mer Patterns: ")
        output_file.write(str(words))
    return words

def split_genome(Text):
    mylist= []
    for i in range(0, len(Text),500):
        mylist.append(Text[i:i+500])
    print(mylist)
    return mylist



# Execution starts here

# Read the Genome text file and store it to a string-Genome
text_file = open("C:/Users/gadhv/Desktop/genome_project/genome_input.txt", "r")
Genome = text_file.read()
text_file.close()

# Cleanup the Genome string
Genome = Genome.replace('\n',""); 
print("Length of Genome is: ", len(Genome))


# Split the Genome in to the chunks of 500 nucleotides
genome_window_list = split_genome(Genome);

# to analyze 9-mers in the Genome select k = 9
k = 9
print("Len of genome_window_list: ", len(genome_window_list))
for i in range(0, len(genome_window_list)):
    freq = FrequencyMap(genome_window_list[i],k)
    Max_count_pattern = FrequentWords(freq, k)
    for j in range(0, len(Max_count_pattern)):
        Ori_indices = PatternMatching(Max_count_pattern[j], genome_window_list[i])
        output_file_str = "\n-----------------------------------------\n" + "Indices for genome window #" + str(i) + " and pattern :" + str(Max_count_pattern[j]) + "\n-----------------------------------------\n"
        output_file.write(output_file_str)
        output_file.write(str(Ori_indices))
        output_file.write('\n')





















































