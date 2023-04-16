def detail_urls_chunker(total_elements):
    chunk_size = 400
    chunks = [total_elements[i:i + chunk_size] for i in range(0, len(total_elements), chunk_size)]
    return chunks

