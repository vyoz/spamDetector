import sys
from sep_char import separate_chinese_and_english 

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_file")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            input_text = f.read()

        # Process the text while keeping "\n" for each line
        lines = input_text.split('\n')
        result_lines = []
        for line in lines:
            result_lines.append(separate_chinese_and_english(line))
        
        result = '\n'.join(result_lines)

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(result)

        print("Output written to", output_file)

    except FileNotFoundError:
        print("Input file not found.")
        sys.exit(1)
    except Exception as e:
        print("An error occurred:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()

