import mysql.connector
from const import sqlpass
import time

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
    mycursor.execute("CREATE TABLE board1 (id INT AUTO_INCREMENT PRIMARY KEY, field VARCHAR(255), value VARCHAR(255))")
    sql = "INSERT INTO board1 (field, value) VALUES (%s, %s)"    
    val = [
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
        ('color_turn', '0'),  #  ('color_turn', 'white') ->  ('color_turn', '0')
        ('white_last_mes_id', white_last_mes_id),
        ('black_last_mes_id', '0'),
        ('white_time', '600'),
        ('black_time', '600'),
        ('white_last_time_move', '0'),
        ('black_last_time_move', '0'),
        ('white_id', white_id),
        ('black_id', ' '),
        ('white_name', white_name),
        ('black_name', ' '),
        ('white_username', white_username),
        ('black_username', ' '),
        ('start_field', ' '),
        ('white_left_rock_move', '0'),
        ('white_king_move', '0'),
        ('white_right_rock_move', '0'),
        ('black_left_rock_move', '0'),
        ('black_king_move', '0'),
        ('black_right_rock_move', '0'),
        ('start_time', start_time),
        ('white_king', 'e1'),
        ('black_king', 'e8')
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
    mycursor.execute("CREATE TABLE bot_info (id INT AUTO_INCREMENT PRIMARY KEY, field VARCHAR(255), value VARCHAR(255))")
    sql = "INSERT INTO bot_info (field, value) VALUES (%s, %s)"
    val = ('game', '1')
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


def get_board_db(game_num:str):
    b = {}
    game_name = "board" + game_num
    mycursor.execute(f"SELECT * FROM {game_name}")
    myresult = mycursor.fetchall()
    for x in myresult[:64]:
        b[x[1]] = x[2]
    return b

def get_info_db(game_num:str):
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
    val = [(black_id, 'black_id'), (black_name, 'black_name'), (black_username, 'black_username'), (white_last_time_move, 'white_last_time_move'), (white_last_time_move, 'start_time')]
    mycursor.executemany(sql, val)
    mydb.commit()


def get_pos_db(game_num):
    game_name = "board" + game_num
    mycursor.execute(f"SELECT * FROM {game_name}")
    myresult = mycursor.fetchall()
    start_field = myresult[77][2]
    return start_field


def get_all_db(game_num):
    game_name = "board" + game_num
    mycursor.execute(f"SELECT * FROM {game_name}")
    myresult = mycursor.fetchall()
    return myresult


def save_start_field_db(game_num, data):
    sql = "UPDATE board" + game_num +" SET value = %s WHERE field = %s"
    val = (data, 'start_field')
    mycursor.execute(sql, val)
    mydb.commit()


def change_board_db(game_num, start_field, start_field_value, end_field, end_field_value):
    sql = "UPDATE board" + game_num +" SET value = %s WHERE field = %s"
    val = [(start_field_value, start_field), (end_field_value, end_field)]
    mycursor.executemany(sql, val)
    mydb.commit()
    

def change_turn_db(game_num):
    game_info = get_info_db(game_num)
    sql = "UPDATE board1 SET value = %s WHERE field = %s"
    if game_info["color_turn"] == "0":  # it was white turn
        color_turn = "1"  # now it's black turn
        val = [(f"{color_turn}", "color_turn"), (str(time.time()), "black_last_time_move"), ('0', "white_time")]
        # val = (str(int(game_info["white_time"]) - (time.time() - int(game_info["white_last_time_move"]))), "white_time")

    elif game_info["color_turn"] == "1":  # it was black turn
        color_turn = "0"  # now it's white turn
        val = [(f"{color_turn}", "color_turn"), (str(time.time()), "white_last_time_move"),('0', "black_time")]
        # val = (str(int(game_info["black_time"]) - (time.time() - int(game_info["black_last_time_move"]))), "black_time")

    elif game_info["color_turn"] == "transf_0":
        color_turn = "1"  # now it's black turn
        val = [("1", "color_turn"), (str(time.time()), "black_last_time_move"),('0', "white_time")]
    
    elif game_info["color_turn"] == "transf_1":
        color_turn = "0"  # now it's white turn
        val = [("0", "color_turn"), (str(time.time()), "white_last_time_move"),('0', "black_time")]

    mycursor.executemany(sql, val)
    mydb.commit()
    return color_turn


def change_castling_info_db(game_num, field):
    sql = "UPDATE board" + game_num +" SET value = %s WHERE field = %s"
    # val = ("board"+game_num, "1", field)
    val = ("1", field)
    mycursor.execute(sql, val)
    mydb.commit()


def do_castling_db(game_num, castling):
    sql = "UPDATE board" + game_num +" SET value = %s WHERE field = %s"

    if castling == "white_short":
        val = [("00", "e1"), ("04", "f1"), ("06", "g1"), ("00", "h1"), ("g1", "white_king"), ("1", "white_king_move")]  # вместо короля/новая ладья/новый король/вместо ладьи/координты короля
    elif castling == "white_long":
        val = [("00", "a1"), ("06", "c1"), ("04", "d1"), ("00", "e1"), ("c1", "white_king"), ("1", "white_king_move")]  # вместо ладьи/новый король/новая ладья/вместо короля/координты короля
    elif castling == "black_short":
        val = [("00", "e8"), ("14", "f8"), ("16", "g8"), ("00", "h8"), ("g8", "black_king"), ("1", "black_king_move")]  # вместо короля/новая ладья/новый король/вместо ладьи/координты короля
    else:  # "black_long"
        val = [("00", "a8"), ("16", "c8"), ("14", "d8"), ("00", "e8"), ("c8", "black_king",), ("1", "black_king_move")]  # вместо ладьи/новый король/новая ладья/вместо короля/координты короля

    mycursor.executemany(sql, val)
    mydb.commit()
    change_turn_db(game_num)


def save_new_figure_db(game_num, value, field):
    sql = "UPDATE board" + game_num +" SET value = %s WHERE field = %s"
    val = (value, field)

    mycursor.execute(sql, val)
    mydb.commit()


def save_turn_field_db(game_num, data):
    sql = "UPDATE board" + game_num +" SET value = %s WHERE field = %s"
    val = (data, 'color_turn')
    mycursor.execute(sql, val)
    mydb.commit()


def change_king_db(game_num, data):
    sql = "UPDATE board" + game_num +" SET value = %s WHERE field = %s"
    start_field = get_pos_db(game_num)
    b = get_board_db(game_num)
    if b[start_field] == "06":
        val = (data, "white_king")
    elif b[start_field] == "16":
        val = (data, "black_king")
    mycursor.execute(sql, val)
    mydb.commit()



if __name__ == "__main__":
    mycursor.execute("DROP TABLE board1")