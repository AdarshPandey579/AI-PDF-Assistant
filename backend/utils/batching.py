def batch_items(items, batch_size):
    
    return [
        items[i:i + batch_size]
        for i in range(0, len(items), batch_size)
    ]