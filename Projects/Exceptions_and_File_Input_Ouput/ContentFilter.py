class ContentFilter:
    def __init__(self, filename):
        while True:
            try:
                self.file = open(filename, 'r')
                self.name = filename
                self.contents = self.file.read()
                self.file.close()
                break
            except (FileNotFoundError, TypeError, OSError):
                filename = input("Please enter a valid file name: ")

    def uniform(self, outfile, mode='w', case="upper"):

        if mode not in ['w', 'x', 'a']:
            raise ValueError("Invalid mode. Mode must be 'w', 'x', or 'a'.")
        if case not in ['upper', 'lower']:
            raise ValueError("Invalid case. Case must be 'upper' or 'lower'.")

        with open(outfile, mode) as out_file:
            lines = self.contents.split('\n')
            if case == 'upper':
                lines = [line.upper() for line in lines]
            else:
                lines = [line.lower() for line in lines]

            out_file.write('\n'.join(lines)+'\n')

    def reverse(self, outfile, mode='w', unit="line"):
        if mode not in ['w', 'x', 'a']:
            raise ValueError("Invalid mode. Mode must be 'w', 'x', or 'a'.")
        if unit not in ['word', 'line']:
            raise ValueError("Invalid unit. Unit must be 'word' or 'line'.")

        with open(outfile, mode) as out_file:
            lines = self.contents.split('\n')
            if unit == 'word':
                reversed_lines = [' '.join(line.split()[::-1]) for line in lines]
            else:
                reversed_lines = lines[::-1]

            out_file.write('\n'.join(reversed_lines)+'\n')

    def transpose(self, outfile, mode='w'):
        if mode not in ['w', 'x', 'a']:
            raise ValueError("Invalid mode. Mode must be 'w', 'x', or 'a'.")

        with open(outfile, mode) as out_file:
            matrix = [line.split() for line in self.contents.split('\n')]
            transposed_matrix = zip(*matrix)
            transposed_lines = [' '.join(row) for row in transposed_matrix]
            out_file.write('\n'.join(transposed_lines))

    def __str__(self):
        lines = self.contents.split('\n')
        total_chars = sum(len(line) for line in lines)
        alphabetic_chars = sum(c.isalpha() for line in lines for c in line)
        numeric_chars = sum(c.isdigit() for line in lines for c in line)
        whitespace_chars = sum(c.isspace() for line in lines for c in line)
        num_lines = len(lines)

        result = f"Source file: {self.name}\n" \
                 f"Total characters: {total_chars}\n" \
                 f"Alphabetic characters: {alphabetic_chars}\n" \
                 f"Numerical characters: {numeric_chars}\n" \
                 f"Whitespace characters: {whitespace_chars}\n" \
                 f"Number of lines: {num_lines}"
        return result