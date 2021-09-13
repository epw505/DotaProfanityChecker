from profanity import ProfanityChecker
from loader import Loader


MATCH_ID = 6174930894


if __name__ == "__main__":

    my_game = Loader(match_id=MATCH_ID).load_match()
    prof_checker = ProfanityChecker()

    output = {}
    for player_chat in my_game.return_player_chats():
        output[player_chat[0]] = prof_checker.analyse_text(player_chat[1])

    print(output)