vector_store = None


def get_vector_store():
    return vector_store


def set_vector_store(vs):
    global vector_store
    vector_store = vs
