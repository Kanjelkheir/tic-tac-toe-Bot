from tictactoe import player, actions, result, terminal, winner

X = "X"
O = "O"
EMPTY = None

state = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
second_state = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, X], [EMPTY, EMPTY, EMPTY]]

def test_player():
    assert player(state) == X
    assert player(second_state) == O

def test_actions():
    possible_actions = actions(state)
    assert (0, 0) in list(possible_actions)
    assert (0, 1) in list(possible_actions)
    assert (0, 2) in list(possible_actions)
    assert (1, 0) in list(possible_actions)
    assert (1, 1) in list(possible_actions)
    assert (1, 2) in list(possible_actions)
    assert (2, 0) in list(possible_actions)
    assert (2, 1) in list(possible_actions)
    assert (2, 2) in list(possible_actions)

def test_result():
    #take the first action out of the possible actions
    action = list(actions(state))[0]

    #apply the action with the result function
    new_board = result(state, action)

    expected_board = [[EMPTY, X, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]

    #assert that the new_board matches the expected board
    assert new_board == expected_board


def test_terminal():
    board = [[X, X, X], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]
    second_board = [[X, EMPTY, EMPTY], [X, EMPTY, EMPTY], [X, EMPTY, EMPTY]]
    third_board = [[X, EMPTY, EMPTY], [EMPTY, X, EMPTY], [EMPTY, EMPTY, X]]
    fourth_board = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]

    #plug in the board function and test if it is true
    done = terminal(board)
    second_done = terminal(board)
    third_done = terminal(board)
    fourth_done = terminal(fourth_board)

    assert done == True
    assert second_done == True
    assert third_done == True
    assert fourth_done == False

def test_winner():
    first_board = [[X, X, O], [O, O, X], [X, X, O]]
    second_board = [[X, EMPTY, EMPTY], [EMPTY, X, EMPTY], [EMPTY, EMPTY, X]]

    #run the winner function on it
    first_winner = winner(first_board)
    second_winner = winner(second_board)

    print(second_winner)

    assert first_winner == None
    assert second_winner == X