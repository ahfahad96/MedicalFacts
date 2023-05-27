from sentence_transformers import SentenceTransformer, util
import torch

embedder = SentenceTransformer('all-MiniLM-L6-v2')


class SemanticSearch:
    def __init__(self) -> None:
        pass

    def similarity_computation(self, fact, content):
        try:
            # Corpus with example sentences
            corpus = content
            corpus_embeddings = embedder.encode(corpus, convert_to_tensor=True)

            # Find the closest 5 sentences of the corpus for each query sentence based on cosine similarity
            top_k = min(5, len(corpus))
            fact_embedding = embedder.encode(fact, convert_to_tensor=True)

            # We use cosine-similarity and torch.topk to find the highest 5 scores
            cos_scores = util.cos_sim(fact_embedding, corpus_embeddings)[0]
            top_results = torch.topk(cos_scores, k=top_k)

            semantics_data = []
            for score, idx in zip(top_results[0], top_results[1]):
                semantics_dict = {}
                semantics_dict['Content'] = corpus[idx]
                semantics_dict['Score'] = "{:.4f}".format(score)
                semantics_data.append(semantics_dict)
            return semantics_data
        except Exception as e:
            print(e)
            return None


def process_semantic_search(fact, content):
    similarity_obj = SemanticSearch()
    semantic_search_results = similarity_obj.similarity_computation(
        fact, content)
    if semantic_search_results:
        return semantic_search_results
    else:
        return None
