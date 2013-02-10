import random
from SAMEngine.redis_cli import R
from django.shortcuts import login_required

# Create your views here.


@login_required
def NewBattleView(request):
    pass


def BasicTable(request):
    """
        test function to get the feel of the table right
    """
    return "some basic template file that's blank"


def GetCurrentTurn(request, battle_id):
    # since most battles should/will take place in redis, lets check!
    r = R.r
    turn = r.hget("battle_" + battle_id, "current_turn")
    current_player = r.hget("battle_" + battle_id, "current_player")
    rtn_dict = {"turn": turn, "current_player": current_player}
    return "json object of whose turn it is...and whose line it is", rtn_dict


def StartNewBattle():
    r = R.r
    battle_id = r.incr("next.battle.id")
    battle_hash = "battle.{0}".fortmat([battle_id])
    player = random.randint(1, 2)
    # instead of making multiple calls, just set multiples all at once!
    r.hset(battle_hash, "turn", 0,
            "player", player
    )
    # set the current turn to 0; the start of the game; and randomly decides who goes first
    # who is player 1 and who is player 2 will be set elsewhere...
    return battle_id
