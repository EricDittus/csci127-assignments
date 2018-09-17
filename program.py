def capitalize(name):
    """
    input: name --> a string in the form "first last"
    output: returns a string with each of the two words capitalized
    note: this is the one we started in class
    """
    FI=name[0]
    FI=FI.capitalize()
    Space=name.find(' ')
    SI=name[Space+1]
    SI=SI.capitalize()
    NewName= FI+name[1:Space]+" "+ SI+ name[Space+2:]
    return NewName


def init(name):
    """
    Input: name --> a string in the form "first last"
    Returns: a string in the form "F. Last" where it's a capitalized first inital 
    and capitalized last name
    """
    FI=name[0].capitalize()
    Space=name.find(' ')
    LI=name[Space+1:].capitalize()
    NewName=FI+". "+LI
    return NewName

def part_pig_latin(name):
    """
    Input: A string that is a single lower case word
    Returns: that string in fake pig latin -> move the first letter of the word to the end and add "ay"
    so: "hello" --> "ellohay"
    """
    NewWord= name[1:]+name[0]+"ay"
    return NewWord

def make_out_word(string,word):
    tag=string[0:2]+word+string[2:]
    return tag
    
def make_tags(first,second):
    tag="<"+first+">"+second+"</"+first+">"
    return tag
 
print(capitalize("eric dittus"))

print(init("eric dittus"))

print(part_pig_latin("eric"))

print(make_out_word("<<>>","eric"))

print(make_tags("yay","eric"))