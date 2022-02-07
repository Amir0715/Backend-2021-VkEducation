import numpy as np


def levenshtein_distance(word_a: str, word_b: str) -> int:
    """Считает растояние Левенштейна
    ```
    Args:
        word_a (str): Слово a
        word_b (str): Слово b

    Returns:
        int: растояние левеншейна
    ```
    """
    if len(word_a) == 0 or len(word_b) == 0:
        return max(len(word_a), len(word_b))

    # Initialize matrix of zeros
    rows = len(word_a) + 1
    cols = len(word_b) + 1
    calc_distance = np.zeros((rows, cols), dtype=int)

    # Populate matrix of zeros with the indeces of each character of both strings
    for i in range(1, rows):
        for k in range(1, cols):
            calc_distance[i][0] = i
            calc_distance[0][k] = k

    for col in range(1, cols):
        for row in range(1, rows):
            calc_distance[row][col] = min(calc_distance[row-1][col] + 1,    # Cost of deletions
                                          calc_distance[row][col-1] + 1,    # Cost of insertions
                                          calc_distance[row-1][col-1] + 1)  # Cost of substitutions

    return calc_distance[row][col]


if __name__ == "__main__":
    print(levenshtein_distance('      ', '    '))
