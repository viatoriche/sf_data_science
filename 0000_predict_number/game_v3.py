import numpy as np

# Let's take a random number
number = np.random.randint(1, 101)
count = 0


def random_predict(number: int = 1) -> int:
    """Trying to predict the number

    Args:
        number (int, optional): Predicted number. Defaults to 1.

    Returns:
        int: Count of tries
    """

    count: int = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return count


def game_core_v2(number: int = 1) -> int:
    """Let's set random number, after that let's decrease or increase it if the number is less or greater than predicted.

    Args:
        number (int, optional): Predicted number. Defaults to 1.

    Returns:
        int: Count of tries
    """
    count = 0
    predict = np.random.randint(1, 101)

    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count


def game_core_v3(number: int = 1) -> int:
    """Logarithmic searcher

    Presets:
        predict = 50 as maximum divided to 2
        mode = 25 as predict divided to 2
    Algo:
        Condition:
            * Increase `predict` to `mode` if `predict` greater than `number`
            * Decrease `predict` to `mode` if `predict` less than `number`
        Divide `mode` to 2
        Repeat algo
        Check that predict is equal to number and stop iteration if yes

    Performance:
       Your algo predicts the number for: 4 tries in average

    Args:
        number (int, optional): Predicted number. Defaults to 1.

    Returns:
        int: Count of tries
    """

    count = 0
    # set predict as max value divided by 2
    predict = 50
    # set mode as predict divided by 2
    mode = 25

    while number != predict:
        count += 1
        if number > predict:
            predict += mode
        elif number < predict:
            predict -= mode
        mode = int(mode / 2)
        # mode shouldn't be less than 1 for math reasons (it should be used to decrease or increase the value predict)
        if mode == 0:
            mode = 1

    return count


def score_game(random_predict) -> int:
    """The average count of tries to predict the number for 1000 calls

    Args:
        random_predict ([type]): predict function

    Returns:
        int: average count of tries
    """

    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))

    print(f'Your algo predicts the number for: {score} tries in average')
    return (score)


if __name__ == "__main__":
    score_game(game_core_v3)
