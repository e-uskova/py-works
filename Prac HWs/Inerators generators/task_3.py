import random


def BatchGenerator(list_of_sequences, batch_size, shuffle=False):
    offset = 0
    while offset < len(list_of_sequences[0]):
        ret_batch = [list_of_sequences[j][offset: batch_size + offset]
                     for j in range(len(list_of_sequences))]
        if shuffle:
            random.shuffle(ret_batch)
        offset += batch_size
        yield ret_batch
