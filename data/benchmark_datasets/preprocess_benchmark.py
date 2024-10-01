import json
def load_jsonl(file_path: str) -> list:
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            data_entry = json.loads(line)
            data.append(data_entry)
    return data

def process_bigcodebench(entry):
    return {
        'task_id': entry['task_id'],
        'prompt': entry['complete_prompt'],
        'solution': entry['canonical_solution'],
        'test_cases': entry['test']
    }

def process_mbpp(entry):
    return {
        'task_id': entry['task_id'],
        'prompt': entry['text'],
        'solution': entry['code'],
        'test_cases': entry['test_list']
    }
def process_data(data):
    if 'complete_prompt' in data[0]:  # Dữ liệu từ bigcodebench
        processed_data = [process_bigcodebench(entry) for entry in data]
    elif 'text' in data[0]:  # Dữ liệu từ mbpp
        processed_data = [process_mbpp(entry) for entry in data]

    return processed_data


def save_to_json(data, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

bigcodebench_path = r'E:\Repo\ChatGPT-CodeGenAnalysis\data\benchmark_datasets\bigcodebenchv0.1.2.jsonl'
mbpp_path = r'E:\Repo\ChatGPT-CodeGenAnalysis\data\benchmark_datasets\mbpp.jsonl'

bigcodebench_output = r'E:\Repo\ChatGPT-CodeGenAnalysis\data\benchmark_datasets\processed_data\bigcodebench_processed.json'
mbpp_output = r'E:\Repo\ChatGPT-CodeGenAnalysis\data\benchmark_datasets\processed_data\mbpp_processed.json'

dataset_bigcodebench = load_jsonl(bigcodebench_path)
dataset_mbpp = load_jsonl(mbpp_path)

processed_bigcodebench = process_data(dataset_bigcodebench)
save_to_json(processed_bigcodebench, bigcodebench_output)

processed_mbpp = process_data(dataset_mbpp)
save_to_json(processed_mbpp, mbpp_output)


