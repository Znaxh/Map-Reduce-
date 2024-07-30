from collections import defaultdict

def map_function(document):
    for word in document.split():
        yield (word, 1)

def shuffle_function(mapped_pairs):
    shuffled_pairs = defaultdict(list)
    for word, count in mapped_pairs:
        shuffled_pairs[word].append(count)
    return shuffled_pairs

def reduce_function(shuffled_pairs):
    word_count_dict = defaultdict(int)
    for word, counts in shuffled_pairs.items():
        word_count_dict[word] = sum(counts)
    return word_count_dict

def map_reduce(document):
    mapped = map_function(document)
    mapped_pairs = list(mapped)
    shuffled = shuffle_function(mapped_pairs)
    reduced = reduce_function(shuffled)

    return reduced

if __name__ == "__main__":
    document = """hello world hello map reduce map reduce map map"""
    word_counts = map_reduce(document)
    for word, count in word_counts.items():
        print(f"{word}: {count}")

    document1 = """this is a test document to test the map reduce implementation"""
    word_counts1 = map_reduce(document1)
    for word, count in word_counts1.items():
        print(f"{word}: {count}")

    document2 = """this is another document to test the map reduce implementation"""
    word_counts2 = map_reduce(document2)
    for word, count in word_counts2.items():
        print(f"{word}: {count}")
