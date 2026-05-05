import os
import shutil
import csv
from datetime import datetime

# Log file
log_file = 'log.txt'

def write_log(message):
    with open(log_file, 'a') as log:
        log.write(f"{datetime.now()} - {message}\n")

def setup_demo(base_dir):
    try:
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
            print(f"Created directory: {base_dir}")
            write_log(f"Directory created: {base_dir}")

        input_file = os.path.join(base_dir, 'sample.txt')
        csv_file = os.path.join(base_dir, 'data.csv')

        with open(input_file, 'w') as f:
            f.write("Hello, this is a sample file.")

        with open(csv_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Name', 'Status'])
            writer.writerow([1, 'Task_A', 'Completed'])
            writer.writerow([2, 'Task_B', 'Pending'])

        print("Sample files created.")
        write_log("Sample files created")

    except Exception as e:
        print(f"Error: {e}")
        write_log(f"Error in setup: {e}")

def automate_files(base_dir):
    try:
        input_file = os.path.join(base_dir, 'sample.txt')
        moved_file = os.path.join(base_dir, 'archived_sample.txt')
        csv_file = os.path.join(base_dir, 'data.csv')

        # Read file
        with open(input_file, 'r') as f:
            content = f.read()
            print("File content:", content)
            write_log("Read sample.txt")

        # Move file
        if os.path.exists(input_file):
            shutil.move(input_file, moved_file)
            print("File moved successfully")
            write_log("File moved and renamed")

        # Read CSV
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            count = 0
            for row in reader:
                print(row)
                count += 1
            print("Total tasks:", count)
            write_log(f"Processed {count} tasks")

    except FileNotFoundError:
        print("File not found")
        write_log("File not found error")
    except Exception as e:
        print(f"Error: {e}")
        write_log(f"Unexpected error: {e}")

def clean_directory(base_dir):
    try:
        files = os.listdir(base_dir)
        for file in files:
            if file.endswith('.txt'):
                os.remove(os.path.join(base_dir, file))
                print(f"Deleted: {file}")
                write_log(f"Deleted file: {file}")
    except Exception as e:
        print(f"Cleanup error: {e}")
        write_log(f"Cleanup error: {e}")

# USER INPUT
print("Enter folder name to create:")
base_dir = input()

setup_demo(base_dir)
automate_files(base_dir)

# Optional cleaning
choice = input("Do you want to clean .txt files? (yes/no): ")
if choice.lower() == 'yes':
    clean_directory(base_dir)

# Show final files
if os.path.exists(base_dir):
    files = os.listdir(base_dir)
    print("Final files:", files)
    write_log(f"Final files: {files}")
