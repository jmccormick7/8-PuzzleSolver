
## John McCormick 
## jcm258
## CSDS 391: Programming Assignment 1
## Due: September 26th, 2023 18:00:00


# List of files to process
file_paths = [
    'MetricsTest1.txt',
    'MetricTest2.txt',
    'MetricTest3.txt',
    'MetricTest4.txt',
    'MetricTest5.txt',
    'MetricTest6.txt',
    'MetricTest7.txt',
    'MetricTest8.txt',
    'MetricTest9.txt',
    'MetricTest10.txt'
]

def parse_and_summarize_file_content(content):
    """Parse the given content and return summarized data."""
    # Split content into sections
    sections = content.strip().split("\n\n")

    # Data structure to hold parsed data
    parsed_data = {}

    # Iterate over each section
    for section in sections:
        # Split the section into lines
        lines = section.split("\n")

        
        time_taken = float(lines[5])
        test_name = lines[0]


        # Extract other metrics
        successes = int(lines[1].split(": ")[1])
        failures = int(lines[2].split(": ")[1])
        moves = int(lines[4].split(": ")[1]) 

        # Populate the parsed_data dictionary
        if test_name not in parsed_data:
            parsed_data[test_name] = {
                "time": 0,
                "successes": 0,
                "failures": 0,
                "moves": 0
            }
        
        parsed_data[test_name]["time"] += time_taken
        parsed_data[test_name]["successes"] += successes
        parsed_data[test_name]["failures"] += failures
        parsed_data[test_name]["moves"] += moves

    return parsed_data

# Function to aggregate the results from multiple files
def aggregate_results_from_files(file_paths):
    aggregated_data = {}

    for file_path in file_paths:
        with open(file_path, 'r') as file:
            content = file.read()
            parsed_data = parse_and_summarize_file_content(content)

            # Aggregate the parsed data
            for search_description, metrics in parsed_data.items():
                if search_description not in aggregated_data:
                    aggregated_data[search_description] = {'time': 0, 'successes': 0, 'failures': 0, 'moves': 0}

                aggregated_data[search_description]['time'] += metrics['time']
                aggregated_data[search_description]['successes'] += metrics['successes']
                aggregated_data[search_description]['failures'] += metrics['failures']
                aggregated_data[search_description]['moves'] += metrics['moves']

    return aggregated_data

# Aggregate the results from all the files
aggregated_results = aggregate_results_from_files(file_paths)
print(aggregated_results)