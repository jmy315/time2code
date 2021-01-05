from datetime import datetime
import sys

def sort_file_by_date(filename):
    file_date = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                words = line.split()
                date_str = ' '.join(words[2:5])
                date_obj = datetime.strptime(date_str, '%B %d, %Y')
                name = words[-1]
                file_date.append((name, date_obj))
    except IOError:
        print(f'Cannot open file: {filename}')
    
    file_date.sort(key=lambda x: x[1], reverse=True)
    for name, date_obj in file_date:
        # - in strftime means do not pad a numeric result string
        print(f'{name}, {date_obj.strftime("%B %-d, %Y")}')
    


sort_file_by_date(sys.argv[1])
