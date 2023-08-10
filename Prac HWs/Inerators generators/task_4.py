

def WordContextGenerator(words, window_size):
    for w in range(len(words)):
        word = words[w]
        for n in [words[i] for i in range(w - window_size
                  if w - window_size >= 0 else 0,
                  w + window_size + 1 if w + window_size < len(words)
                  else len(words)) if words[i] != word]:
            yield word, n
