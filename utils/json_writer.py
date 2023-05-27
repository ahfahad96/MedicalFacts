import json


def write_results_to_json(fact, content):
    try:
        fact_string = f"Fact : {fact}"
        with open('semantic_output.json', 'w') as file:
            json.dump(fact_string, file, indent=4)
            file.write('\n')
        with open('semantic_output.json', 'a') as file:
            json.dump(content, file, indent=4)
        return "Successfully written to JSON"
    except Exception as e:
        print(e)
        return "Unsuccessful"
