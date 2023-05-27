from src.pdf_reader.pdf_reader import process_pdf
from src.semantic_search.semantic_search import process_semantic_search
from utils.json_writer import write_results_to_json


def main():
    fact = "AI large language models can be used in research purposes"
    pdf_content = process_pdf()
    semantics_results = process_semantic_search(fact, pdf_content)
    status = write_results_to_json(fact, semantics_results)
    print(status)


if __name__ == '__main__':
    main()
