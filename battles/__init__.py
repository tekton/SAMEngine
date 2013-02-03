"""
    All of the battles backend and UI should be in here
"""

"""
    redis scratch ::

    key: next.battle.id

    battles.<id> ??
        key: current_player
        key: current_turn

    battles_combat_log_<id> (list)
        doign it as a list allows for rpush-ing and then lpop-ing later for persistance in db!

    battles_move_list_<id>
        possibly not an actual list as turns can be variable in length...
        ...just needs to be a flexiable queuing system!

    battle_character_store_hash_<id> (hash)
        character.<id>.<base_character_id>
            owner :: the player who can edit this thing
            inventory :: json of inventory
            abilities :: json of abilities
            skills :: json of skills
            name
            slot :: visual location of the character on the board: 0,1,2
        hgetall returns a dictionary of thigns to make it easier...
        hmget returns a 0 based array in the same ordered asked for
        IDEA: hash for inventory, and the inventory var just points to it?


    ON ABILITY SUBMISSION --
        insert next time person goes
        LPOP and process that person going next

    CLEAN UP
        Go through the battle hashes, get other hashes/lists and POP those that go in the DB and erase the rest...
"""
