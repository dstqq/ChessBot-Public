import mysql.connector
from const import sqlpass
import time
import typing

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=sqlpass,
    database="mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE bot_info")
# mycursor.execute("CREATE TABLE board1 (id INT AUTO_INCREMENT PRIMARY KEY, field VARCHAR(255), value VARCHAR(255))")


def init_board_table(white_last_mes_id, white_id, white_name, white_username, start_time):
    sql = "DROP TABLE IF EXISTS board1"
    mycursor.execute(sql)
    mycursor.execute(
        "CREATE TABLE board1 (id INT AUTO_INCREMENT PRIMARY KEY, field VARCHAR(255), value VARCHAR(255))")
    sql = "INSERT INTO board1 (field, value) VALUES (%s, %s)"
    val = [
        # Board information
        ('a1', '04'),
        ('b1', '03'),
        ('c1', '02'),
        ('d1', '05'),
        ('e1', '06'),
        ('f1', '02'),
        ('g1', '03'),
        ('h1', '04'),
        ('a2', '01'),
        ('b2', '01'),
        ('c2', '01'),
        ('d2', '01'),
        ('e2', '01'),
        ('f2', '01'),
        ('g2', '01'),
        ('h2', '01'),
        ('a3', '00'),
        ('b3', '00'),
        ('c3', '00'),
        ('d3', '00'),
        ('e3', '00'),
        ('f3', '00'),
        ('g3', '00'),
        ('h3', '00'),
        ('a4', '00'),
        ('b4', '00'),
        ('c4', '00'),
        ('d4', '00'),
        ('e4', '00'),
        ('f4', '00'),
        ('g4', '00'),
        ('h4', '00'),
        ('a5', '00'),
        ('b5', '00'),
        ('c5', '00'),
        ('d5', '00'),
        ('e5', '00'),
        ('f5', '00'),
        ('g5', '00'),
        ('h5', '00'),
        ('a6', '00'),
        ('b6', '00'),
        ('c6', '00'),
        ('d6', '00'),
        ('e6', '00'),
        ('f6', '00'),
        ('g6', '00'),
        ('h6', '00'),
        ('a7', '11'),
        ('b7', '11'),
        ('c7', '11'),
        ('d7', '11'),
        ('e7', '11'),
        ('f7', '11'),
        ('g7', '11'),
        ('h7', '11'),
        ('a8', '14'),
        ('b8', '13'),
        ('c8', '12'),
        ('d8', '15'),
        ('e8', '16'),
        ('f8', '12'),
        ('g8', '13'),
        ('h8', '14'),
        # Game status
        ('color_turn', 'white'),  # indicates whose turn it is possible values: 'white', 'black', 'transf_white', 'transf_white'
        ('result', ' '), # possible values: 'white', 'black', 'draw'
        # Player information
        ('white_id', white_id),  # unique identifier for the white player
        ('black_id', ' '),  # unique identifier for the black player
        ('white_name', white_name),  # name of the white player
        ('black_name', ' '),  # name of the black player
        ('white_username', white_username),  # username of the white player
        ('black_username', ' '),  # username of the black player
        # Time information
        ('white_time', '600'),  # remaining time for the white player
        ('black_time', '600'),  # remaining time for the black player
        ('white_last_time_move', '0'),  # time when the white player made their last move
        ('black_last_time_move', '0'),  # time when the black player made their last move
        ('start_time', start_time),  # time when the game started
        # Message information
        ('white_last_mes_id', white_last_mes_id),  # ID of the last message sent by the white player
        ('black_last_mes_id', '0'),  # ID of the last message sent by the black player
        # Move information
        ('origin_square', ' '),  # initial field for a move (if a piece has been selected)
        ('white_left_rock_move', '0'),  # indicates whether the white left rook has moved (0 - not moved, 1 - moved)
        ('white_king_move', '0'),  # indicates whether the white king has moved (0 - not moved, 1 - moved)
        ('white_right_rock_move', '0'),  # indicates whether the white right rook has moved (0 - not moved, 1 - moved)
        ('black_left_rock_move', '0'),  # indicates whether the black left rook has moved (0 - not moved, 1 - moved) 
        ('black_king_move', '0'),  # indicates whether the black king has moved (0 - not moved, 1 - moved)
        ('black_right_rock_move', '0'),  # indicates whether the black right rook has moved (0 - not moved, 1 - moved)
    ]
    mycursor.executemany(sql, val)
    mydb.commit()


# mycursor.execute("SELECT * FROM bot_info")
# myresult = mycursor.fetchall()
# mydb.commit()
"""mycursor.execute("SHOW TABLES")"""


def create_bot_info_table():
    sql = "DROP TABLE IF EXISTS bot_info"
    mycursor.execute(sql)
    mycursor.execute(
        "CREATE TABLE bot_info (id INT AUTO_INCREMENT PRIMARY KEY, field VARCHAR(255), value VARCHAR(255))")
    sql = "INSERT INTO bot_info (field, value) VALUES (%s, %s)"
    val = ('game', '1')
    mycursor.execute(sql, val)
    mydb.commit()


def create_users_info_table():
    sql = "DROP TABLE IF EXISTS users_info"
    mycursor.execute(sql)
    mycursor.execute("CREATE TABLE users_info (id INT AUTO_INCREMENT PRIMARY KEY, tg_id BIGINT, status VARCHAR(10) DEFAULT 'chill', lang VARCHAR(10) NOT NULL DEFAULT 'ENG', last_game_id INT(10), wins INT(6), losses INT(6), draws INT(6), name VARCHAR(255) NOT NULL DEFAULT 'Chess enjoyer')")
    sql = "INSERT INTO users_info (tg_id, name) VALUES (%s, %s)"
    val = ('386760687', '⚜️Человек-удача(нет)')
    mycursor.execute(sql, val)
    mydb.commit()


def create_new_game() -> str:  # getting number of games and increase it
    mycursor.execute(f"SELECT value FROM bot_info WHERE field = 'game'")
    myresult = mycursor.fetchall()
    """sql = "UPDATE bot_info SET value = %s WHERE field = %s"
    val = (int(myresult[0][0])+1, 'game')
    mycursor.execute(sql, val)
    mydb.commit()"""
    return myresult[0][0]


def connect_to_game(user, game_num):
    sql = f"UPDATE users_info SET status = 'game', last_game_id = {int(game_num)} WHERE tg_id = {user}"
    mycursor.execute(sql)
    mydb.commit()


def disconnect_from_game(user):
    sql = f"UPDATE users_info SET status = 'chill', WHERE tg_id = {user}"
    mycursor.execute(sql)
    mydb.commit()
    

def add_tg_new_user(user):
    mycursor.execute("SELECT tg_id FROM users_info")
    myresult = mycursor.fetchall()
    myresult = tuple(myresult)
    for x in myresult:
        if x[0] == user.from_id:  
            return False
    name = " "
    if str(user.from_user.first_name) != "None":
        name = str(user.from_user.first_name)
    if str(user.from_user.last_name) != "None":
        name += str(user.from_user.last_name)
    if name == " ":
        name = "Chess enjoyer"
    sql = "INSERT INTO users_info (tg_id, name) VALUES (%s, %s)"
    val = (str(user.from_user.id), name)
    mycursor.execute(sql, val)
    mydb.commit()
    return name 


def change_user_info(user, field, value):
    sql = f"UPDATE users_info SET {field} = {value}, WHERE tg_id = {user}"
    mycursor.execute(sql)
    mydb.commit()


def update_user_wld_info(user, result):
    mycursor.execute(f"SELECT {result} FROM users_info WHERE tg_id={user}")
    myresult = mycursor.fetchall()
    new = myresult[0] + 1
    sql = f"UPDATE users_info SET {result} = {new}, WHERE tg_id = {user}"
    mycursor.execute(sql)
    mydb.commit()
    

def get_current_game_num(tg_id) -> str:
    mycursor.execute(f"SELECT last_game_id FROM users_info WHERE tg_id={tg_id}")
    myresult = mycursor.fetchone()
    return str(myresult[0])


def get_board_db(game_num: str):
    b = {}
    game_name = "board" + game_num
    mycursor.execute(f"SELECT * FROM {game_name}")
    myresult = mycursor.fetchall()
    for x in myresult[:64]:
        b[x[1]] = x[2]
    return b


def get_info_db(game_num: str):
    game_name = "board" + game_num
    mycursor.execute(f"SELECT * FROM {game_name}")
    myresult = mycursor.fetchall()
    info = {}
    for x in myresult[64:]:
        info[x[1]] = x[2]
    return info


"""sql = "UPDATE board1 SET value = %s WHERE field = %s"
sql1 = "UPDATE board1 SET value = %s WHERE field = %s"
val = ('04', 'b2')
val1 = ('00', 'a2')
mycursor.execute(sql, val)
mycursor.execute(sql1, val1)
mydb.commit()"""


def accept_game_db(game_num, black_id, black_name, black_username, white_last_time_move):
    sql = "UPDATE board"+game_num+" SET value = %s WHERE field = %s"
    val = [(black_id, 'black_id'), (black_name, 'black_name'), (black_username, 'black_username'),
           (white_last_time_move, 'white_last_time_move'), (white_last_time_move, 'start_time')]
    mycursor.executemany(sql, val)
    mydb.commit()
    connect_to_game(black_id, game_num)


def change_last_mes_id(game_num, color, mes_id):
    field = f"{color}_last_mes_id"
    sql = f"UPDATE board{game_num} SET value = {mes_id} WHERE field = '{field}'"
    mycursor.execute(sql)
    mydb.commit()
    

def get_pos_db(game_num):
    game_name = "board" + game_num
    mycursor.execute(f"SELECT * FROM {game_name}")
    myresult = mycursor.fetchall()
    start_field = myresult[79][2]  # origin_square
    return start_field


def get_all_db(game_num):
    game_name = "board" + game_num
    mycursor.execute(f"SELECT * FROM {game_name}")
    myresult = mycursor.fetchall()
    return myresult


def save_start_field_db(game_num, data):
    sql = "UPDATE board" + game_num + " SET value = %s WHERE field = %s"
    val = (data, 'origin_square')
    mycursor.execute(sql, val)
    mydb.commit()


def change_board_db(game_num, start_field, start_field_value, end_field, end_field_value):
    sql = "UPDATE board" + game_num + " SET value = %s WHERE field = %s"
    val = [(start_field_value, start_field), (end_field_value, end_field)]
    mycursor.executemany(sql, val)
    mydb.commit()


def change_turn_db(game_num):
    game_info = get_info_db(game_num)
    sql = "UPDATE board1 SET value = %s WHERE field = %s"
    if game_info["color_turn"] == "white":  # it was white turn
        color_turn = "black"  # now it's black turn
        val = [(f"{color_turn}", "color_turn"), (str(time.time()), "black_last_time_move"), ('0', "white_time")]
        # val = (str(int(game_info["white_time"]) - (time.time() - int(game_info["white_last_time_move"]))), "white_time")

    elif game_info["color_turn"] == "black":  # it was black turn
        color_turn = "white"  # now it's white turn
        val = [(f"{color_turn}", "color_turn"), (str(time.time()), "white_last_time_move"), ('0', "black_time")]
        # val = (str(int(game_info["black_time"]) - (time.time() - int(game_info["black_last_time_move"]))), "black_time")

    elif game_info["color_turn"] == "transf_white":
        color_turn = "black"  # now it's black turn
        val = [(f"{color_turn}", "color_turn"), (str(time.time()), "black_last_time_move"), ('0', "white_time")]

    elif game_info["color_turn"] == "transf_black":
        color_turn = "white"  # now it's white turn
        val = [(f"{color_turn}", "color_turn"), (str(time.time()), "white_last_time_move"), ('0', "black_time")]

    mycursor.executemany(sql, val)
    mydb.commit()
    return color_turn


def change_castling_info_db(game_num, field):
    sql = "UPDATE board" + game_num + " SET value = %s WHERE field = %s"
    # val = ("board"+game_num, "1", field)
    val = ("1", field)
    mycursor.execute(sql, val)
    mydb.commit()


def do_castling_db(game_num, castling):
    sql = "UPDATE board" + game_num + " SET value = %s WHERE field = %s"

    if castling == "white_short":
        val = [("00", "e1"), ("04", "f1"), ("06", "g1"), ("00", "h1"), ("1", "white_king_move")]  # вместо короля/новая ладья/новый король/вместо ладьи/координты короля
    elif castling == "white_long":
        val = [("00", "a1"), ("06", "c1"), ("04", "d1"), ("00", "e1"), ("1", "white_king_move")]  # вместо ладьи/новый король/новая ладья/вместо короля/координты короля
    elif castling == "black_short":
        val = [("00", "e8"), ("14", "f8"), ("16", "g8"), ("00", "h8"), ("1", "black_king_move")]  # вместо короля/новая ладья/новый король/вместо ладьи/координты короля
    else:  # "black_long"
        val = [("00", "a8"), ("16", "c8"), ("14", "d8"), ("00", "e8"), ("1", "black_king_move")]  # вместо ладьи/новый король/новая ладья/вместо короля/координты короля

    mycursor.executemany(sql, val)
    mydb.commit()
    change_turn_db(game_num)


def save_new_figure_db(game_num, value, field):
    sql = "UPDATE board" + game_num + " SET value = %s WHERE field = %s"
    val = (value, field)

    mycursor.execute(sql, val)
    mydb.commit()


def save_turn_field_db(game_num, data):
    sql = "UPDATE board" + game_num + " SET value = %s WHERE field = %s"
    val = (data, 'color_turn')
    mycursor.execute(sql, val)
    mydb.commit()


if __name__ == "__main__":
    mycursor.execute("DROP TABLE board1")
