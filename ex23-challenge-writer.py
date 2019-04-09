import sys
script, input_encoding, error = sys.argv

out_file = open('ex23-challenge.txt', 'w')

def main(language_file, encoding, errors):
    line = language_file.readline()
    
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
        
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors = errors)
    out_file.write(str(raw_bytes)+'\n')
    
languages = open("languages.txt", encoding = "utf-8")

main(languages, input_encoding, error)
out_file.close()