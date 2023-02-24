from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from decimal import Decimal, localcontext
import typing
import time
import const
import sql
# import logging
# logging.basicConfig(format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
#                    level=logging.ERROR)

bot = Bot(token=const.tocken, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

alf = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h"}

figures = {"00": " ", "01": "♙", "02": "♗", "03": "♘", "04": "♖", "05": "♕", "06": "♔",
                      "11": "♟", "12": "♝", "13": "♞", "14": "♜", "15": "♛", "16": "♚"}


async def show_board(chat_id, game_num, mode, call):  # create and send game board as message+keyboard
    pos = sql.get_pos_db(game_num)
    b = sql.get_board_db(game_num)
    keyboard_white = InlineKeyboardMarkup()  # White player keyboard
    keyboard_black = InlineKeyboardMarkup()  # Black player keyboard

    # -----------------------------FIRST ROW(A-H 1)-----------------------------------
    button_a1 = InlineKeyboardButton(text=figures[b["a1"]], callback_data="a1")
    button_b1 = InlineKeyboardButton(text=figures[b["b1"]], callback_data="b1")
    button_c1 = InlineKeyboardButton(text=figures[b["c1"]], callback_data="c1")
    button_d1 = InlineKeyboardButton(text=figures[b["d1"]], callback_data="d1")
    button_e1 = InlineKeyboardButton(text=figures[b["e1"]], callback_data="e1")
    button_f1 = InlineKeyboardButton(text=figures[b["f1"]], callback_data="f1")
    button_g1 = InlineKeyboardButton(text=figures[b["g1"]], callback_data="g1")
    button_h1 = InlineKeyboardButton(text=figures[b["h1"]], callback_data="h1")

    # -----------------------------SECOND ROW(A-H 2)-----------------------------------
    button_a2 = InlineKeyboardButton(text=figures[b["a2"]], callback_data="a2")
    button_b2 = InlineKeyboardButton(text=figures[b["b2"]], callback_data="b2")
    button_c2 = InlineKeyboardButton(text=figures[b["c2"]], callback_data="c2")
    button_d2 = InlineKeyboardButton(text=figures[b["d2"]], callback_data="d2")
    button_e2 = InlineKeyboardButton(text=figures[b["e2"]], callback_data="e2")
    button_f2 = InlineKeyboardButton(text=figures[b["f2"]], callback_data="f2")
    button_g2 = InlineKeyboardButton(text=figures[b["g2"]], callback_data="g2")
    button_h2 = InlineKeyboardButton(text=figures[b["h2"]], callback_data="h2")

    # -----------------------------THIRD ROW(A-H 3)------------------------------------
    button_a3 = InlineKeyboardButton(text=figures[b["a3"]], callback_data="a3")
    button_b3 = InlineKeyboardButton(text=figures[b["b3"]], callback_data="b3")
    button_c3 = InlineKeyboardButton(text=figures[b["c3"]], callback_data="c3")
    button_d3 = InlineKeyboardButton(text=figures[b["d3"]], callback_data="d3")
    button_e3 = InlineKeyboardButton(text=figures[b["e3"]], callback_data="e3")
    button_f3 = InlineKeyboardButton(text=figures[b["f3"]], callback_data="f3")
    button_g3 = InlineKeyboardButton(text=figures[b["g3"]], callback_data="g3")
    button_h3 = InlineKeyboardButton(text=figures[b["h3"]], callback_data="h3")

    # -----------------------------FOURTH ROW(A-H 4)-----------------------------------
    button_a4 = InlineKeyboardButton(text=figures[b["a4"]], callback_data="a4")
    button_b4 = InlineKeyboardButton(text=figures[b["b4"]], callback_data="b4")
    button_c4 = InlineKeyboardButton(text=figures[b["c4"]], callback_data="c4")
    button_d4 = InlineKeyboardButton(text=figures[b["d4"]], callback_data="d4")
    button_e4 = InlineKeyboardButton(text=figures[b["e4"]], callback_data="e4")
    button_f4 = InlineKeyboardButton(text=figures[b["f4"]], callback_data="f4")
    button_g4 = InlineKeyboardButton(text=figures[b["g4"]], callback_data="g4")
    button_h4 = InlineKeyboardButton(text=figures[b["h4"]], callback_data="h4")

    # -----------------------------FIFTH ROW(A-H 5)------------------------------------
    button_a5 = InlineKeyboardButton(text=figures[b["a5"]], callback_data="a5")
    button_b5 = InlineKeyboardButton(text=figures[b["b5"]], callback_data="b5")
    button_c5 = InlineKeyboardButton(text=figures[b["c5"]], callback_data="c5")
    button_d5 = InlineKeyboardButton(text=figures[b["d5"]], callback_data="d5")
    button_e5 = InlineKeyboardButton(text=figures[b["e5"]], callback_data="e5")
    button_f5 = InlineKeyboardButton(text=figures[b["f5"]], callback_data="f5")
    button_g5 = InlineKeyboardButton(text=figures[b["g5"]], callback_data="g5")
    button_h5 = InlineKeyboardButton(text=figures[b["h5"]], callback_data="h5")

    # -----------------------------SIXTH ROW(A-H 6)------------------------------------
    button_a6 = InlineKeyboardButton(text=figures[b["a6"]], callback_data="a6")
    button_b6 = InlineKeyboardButton(text=figures[b["b6"]], callback_data="b6")
    button_c6 = InlineKeyboardButton(text=figures[b["c6"]], callback_data="c6")
    button_d6 = InlineKeyboardButton(text=figures[b["d6"]], callback_data="d6")
    button_e6 = InlineKeyboardButton(text=figures[b["e6"]], callback_data="e6")
    button_f6 = InlineKeyboardButton(text=figures[b["f6"]], callback_data="f6")
    button_g6 = InlineKeyboardButton(text=figures[b["g6"]], callback_data="g6")
    button_h6 = InlineKeyboardButton(text=figures[b["h6"]], callback_data="h6")

    # -----------------------------SEVENTH ROW(A-H 7)----------------------------------
    button_a7 = InlineKeyboardButton(text=figures[b["a7"]], callback_data="a7")
    button_b7 = InlineKeyboardButton(text=figures[b["b7"]], callback_data="b7")
    button_c7 = InlineKeyboardButton(text=figures[b["c7"]], callback_data="c7")
    button_d7 = InlineKeyboardButton(text=figures[b["d7"]], callback_data="d7")
    button_e7 = InlineKeyboardButton(text=figures[b["e7"]], callback_data="e7")
    button_f7 = InlineKeyboardButton(text=figures[b["f7"]], callback_data="f7")
    button_g7 = InlineKeyboardButton(text=figures[b["g7"]], callback_data="g7")
    button_h7 = InlineKeyboardButton(text=figures[b["h7"]], callback_data="h7")

    # -----------------------------EIGHTH ROW(A-H 8)-----------------------------------
    button_a8 = InlineKeyboardButton(text=figures[b["a8"]], callback_data="a8")
    button_b8 = InlineKeyboardButton(text=figures[b["b8"]], callback_data="b8")
    button_c8 = InlineKeyboardButton(text=figures[b["c8"]], callback_data="c8")
    button_d8 = InlineKeyboardButton(text=figures[b["d8"]], callback_data="d8")
    button_e8 = InlineKeyboardButton(text=figures[b["e8"]], callback_data="e8")
    button_f8 = InlineKeyboardButton(text=figures[b["f8"]], callback_data="f8")
    button_g8 = InlineKeyboardButton(text=figures[b["g8"]], callback_data="g8")
    button_h8 = InlineKeyboardButton(text=figures[b["h8"]], callback_data="h8")

    if pos == " ":
        button_turn = InlineKeyboardButton(text="ХОД", callback_data="pass")
    elif pos.find("tranformation") == -1:
        button_turn = InlineKeyboardButton(text="ХОД" + figures[b[pos]], callback_data="pass")
    else:
        pass

    keyboard_white.row(button_a8, button_b8, button_c8, button_d8,
                       button_e8, button_f8, button_h8, button_g8)
    keyboard_white.row(button_a7, button_b7, button_c7, button_d7,
                       button_e7, button_f7, button_h7, button_g7)
    keyboard_white.row(button_a6, button_b6, button_c6, button_d6,
                       button_e6, button_f6, button_h6, button_g6)
    keyboard_white.row(button_a5, button_b5, button_c5, button_d5,
                       button_e5, button_f5, button_h5, button_g5)
    keyboard_white.row(button_a4, button_b4, button_c4, button_d4,
                       button_e4, button_f4, button_h4, button_g4)
    keyboard_white.row(button_a3, button_b3, button_c3, button_d3,
                       button_e3, button_f3, button_h3, button_g3)
    keyboard_white.row(button_a2, button_b2, button_c2, button_d2,
                       button_e2, button_f2, button_h2, button_g2)
    keyboard_white.row(button_a1, button_b1, button_c1, button_d1,
                       button_e1, button_f1, button_h1, button_g1)
    keyboard_white.add(button_turn)

    keyboard_black.row(button_a1, button_b1, button_c1, button_d1,
                       button_e1, button_f1, button_h1, button_g1)
    keyboard_black.row(button_a2, button_b2, button_c2, button_d2,
                       button_e2, button_f2, button_h2, button_g2)
    keyboard_black.row(button_a3, button_b3, button_c3, button_d3,
                       button_e3, button_f3, button_h3, button_g3)
    keyboard_black.row(button_a4, button_b4, button_c4, button_d4,
                       button_e4, button_f4, button_h4, button_g4)
    keyboard_black.row(button_a5, button_b5, button_c5, button_d5,
                       button_e5, button_f5, button_h5, button_g5)
    keyboard_black.row(button_a6, button_b6, button_c6, button_d6,
                       button_e6, button_f6, button_h6, button_g6)
    keyboard_black.row(button_a7, button_b7, button_c7, button_d7,
                       button_e7, button_f7, button_h7, button_g7)
    keyboard_black.row(button_a8, button_b8, button_c8, button_d8,
                       button_e8, button_f8, button_h8, button_g8)
    keyboard_black.add(button_turn)

    myresult = sql.get_all_db(game_num)

    t = "♔ Белого короля" if myresult[64][2] == "0" or myresult[
        64][2] == "transformation_white" else "♚ Черного короля"  # myresult[64][2] == game_info['color_turn']
    """timer = str(players["timew"]) if players["turn"] == "white" else str(players["timeb"])
    timew, timeb = Decimal(str(players["timew"])), Decimal(
        str(players["timeb"]))
    with localcontext as ctx:
            ctx.prec = 1
            timer = f"{str(timew / 60)} m {str(timew / 60)} s" if players[
                           "turn"] == "white" else f"{timeb / 60} m {timeb / 60} s"
    print(timer)"""
    msg = (
        "Шахматная дуэль между:\n"
        "Белый король: " +
        f'<a href=\'https://t.me/{myresult[75][2]}\'>{myresult[73][2]}</a>\n'
        "<b>VS</b>\n"
        "Черный король: " +
        f'<a href=\'https://t.me/{myresult[76][2]}\'>{myresult[74][2]}</a>\n'
        "Сейчас ход " + f"<b>{t}</b> ⏳"  # + timer
    )
    if mode == "both":
        message_objw = await bot.send_message(int(myresult[71][2]), parse_mode="HTML", disable_web_page_preview=True, text=msg, reply_markup=keyboard_white)
        message_objb = await bot.send_message(int(myresult[72][2]), parse_mode="HTML", disable_web_page_preview=True, text=msg, reply_markup=keyboard_black)
        # players['mes_idw'], players['mes_idb'] = message_objw.message_id, message_objb.message_id  заменить
    else:
        if chat_id == int(myresult[71][2]):
            await bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, disable_web_page_preview=True, reply_markup=keyboard_white)
        elif chat_id == int(myresult[72][2]):
            await bot.edit_message_text(msg, call.message.chat.id, call.message.message_id, disable_web_page_preview=True, reply_markup=keyboard_black)


def change_castling(game_num):  # func to change player castling status
    last_field = sql.get_pos_db(game_num)
    if last_field == "a1":
        sql.change_castling_info_db(game_num, "white_left_rock_move")
    elif last_field == "e1":
        sql.change_castling_info_db(game_num, "white_king_move")
    elif last_field == "h1":
        sql.change_castling_info_db(game_num, "white_right_rock_move")
    elif last_field == "a8":
        sql.change_castling_info_db(game_num, "black_left_rock_move")
    elif last_field == "e8":
        sql.change_castling_info_db(game_num, "black_king_move")
    elif last_field == "h8":
        sql.change_castling_info_db(game_num, "black_right_rock_move")


async def do_turn(chat_id, call, game_num):  # movement mechanism
    origin_square = sql.get_pos_db(game_num)
    b = sql.get_board_db(game_num)
    sql.change_board_db(game_num, origin_square, "00", call.data, b[origin_square])
    sql.save_start_field_db(game_num, " ")
    color_turn = sql.change_turn_db(game_num)
    await show_board(chat_id, game_num, "both", call)
    game_info = sql.get_info_db(game_num)
    if check_for_check(color_turn, sql.get_board_db(game_num)):
        print("SHAH")
        await bot.send_message(int(game_info["white_id"]), game_info["color_turn"]+" is in check")
        await bot.send_message(int(game_info["black_id"]), game_info["color_turn"]+" is in check")
        if check_mate(game_num):
            print("MAT")
            await bot.send_message(int(game_info["white_id"]), game_info["color_turn"]+" is mated")
            await bot.send_message(int(game_info["black_id"]), game_info["color_turn"]+" is mated")



async def white_transformation(chat_id, square):  # sending small keyboard to white transformation 
    keyboard = InlineKeyboardMarkup()
    # callback_data = "transf|figure|squere" Example:"transf|05|d8" -> button to create a white queen on d8 square
    callback_button_q = InlineKeyboardButton(text=figures["05"], callback_data=f"transf|05|{square}")  # queen
    callback_button_k = InlineKeyboardButton(text=figures["02"], callback_data=f"transf|02|{square}")  # knight
    callback_button_r = InlineKeyboardButton(text=figures["04"], callback_data=f"transf|04|{square}")  # rook
    callback_button_b = InlineKeyboardButton(text=figures["03"], callback_data=f"transf|03|{square}")  # bishop
    keyboard.row(callback_button_q, callback_button_k,callback_button_r, callback_button_b)
    await bot.send_message(chat_id=chat_id, text="Choose transformation:", reply_markup=keyboard)
    # lib.get_text(lang, "choose_transformation"),


async def black_transformation(chat_id, square):  # sending small keyboard to black transformation 
    keyboard = InlineKeyboardMarkup()
    # callback_data = "transf|figure|squere" Example:"transf|15|d1" -> button to create a black queen on d1 square
    callback_button_q = InlineKeyboardButton(text=figures["15"], callback_data=f"transf|15|{square}")  # queen
    callback_button_k = InlineKeyboardButton(text=figures["12"], callback_data=f"transf|12|{square}")  # knight
    callback_button_r = InlineKeyboardButton(text=figures["14"], callback_data=f"transf|14|{square}")  # rook
    callback_button_b = InlineKeyboardButton(text=figures["13"], callback_data=f"transf|13|{square}")  # bishop

    keyboard.row(callback_button_q, callback_button_k, callback_button_r, callback_button_b)
    await bot.send_message(chat_id=chat_id, text="Choose transformation", reply_markup=keyboard)
    # lib.get_text(lang, "choose_transformation"),


def check_white_pawn(b, x, y):  # return all possible cells to move as a white pawn
    res, i = [],  1
    while alf[i] != x:
        i += 1
    if y == "2" and b[x+"4"] == "00":  # two squares on its first move
        if b[x+"3"] == "00":
            res = [x+"3", x+"4"]
    if b[x+str(int(y)+1)] == "00":  # move one cell forward
        if x+str(int(y)+1) not in res:
            res.append(x+str(int(y)+1))
    if x == "a":  # pawn captures and stands on a line
        if b["b"+str(int(y)+1)][0] == "1":
            res.append("b"+str(int(y)+1))
    elif x == "h":  # pawn captures and stands on h line
        if b["g"+str(int(y)+1)][0] == "1":
            res.append("g"+str(int(y)+1))
    else:  # pawn captures in both ways
        if b[alf[i+1]+str(int(y)+1)][0] == "1":
            res.append(alf[i+1]+str(int(y)+1))
        if b[alf[i-1]+str(int(y)+1)][0] == "1":
            res.append(alf[i-1]+str(int(y)+1))
    return res


# return True if 2 different squares are occupied by different colors figures
def different_color_figure(b, x1, y1, x2, y2):
    if (b[x1+y1][0] == "0" and b[x1+y1][1] != "0") or (b[x2+y2][0] == "0" and b[x2+y2][1] != "0"):
        if b[x1+y1][0] != b[x2+y2][0]:
            return True
        else:
            return False


def check_black_pawn(b, x, y):  # return all possible cells to move as a black pawn
    res, i = [],  1
    while alf[i] != x:
        i += 1
    if y == "7" and b[x+"5"] == "00":  # two squares on its first move
        if b[x+"6"] == "00":
            res = [x+"6", x+"5"]
    if b[x+str(int(y)-1)] == "00":  # move one cell forward
        if x+str(int(y)-1) not in res:
            res.append(x+str(int(y)-1))
    if x == "a":  # pawn captures and stands on a line
        if b["b"+str(int(y)-1)][0] == "0" and b["b"+str(int(y)-1)][1] != "0":
            res.append("b"+str(int(y)-1))
    elif x == "h":  # pawn captures and stands on h line
        if b["g"+str(int(y)-1)][0] == "0" and b["g"+str(int(y)-1)][1] != "0":
            res.append("g"+str(int(y)-1))
    else:  # pawn captures in both ways
        if b[alf[i+1]+str(int(y)-1)][0] == "0" and b[alf[i+1]+str(int(y)-1)][1] != "0":
            res.append(alf[i+1]+str(int(y)-1))
        if b[alf[i-1]+str(int(y)-1)][0] == "0" and b[alf[i-1]+str(int(y)-1)][1] != "0":
            res.append(alf[i-1]+str(int(y)-1))
    return res


def check_rook(b, x, y):  # return all possible squares to move as a rook
    # x - letter y - number
    res, i = [], 1
    while alf[i] != x:
        i += 1
    for j in range(int(y)+1, 9):  # horizontal right
        if b[x+str(j)] == "00":
            res.append(x+str(j))
        elif different_color_figure(b, x, y, x, str(j)):
            res.append(x+str(j))
            break
        else:
            break
    for j in reversed(range(1, int(y))):  # horizontally left
        if b[x+str(j)] == "00":
            res.append(x+str(j))
        elif different_color_figure(b, x, y, x, str(j)):
            res.append(x+str(j))
            break
        else:
            break
    for j in range(i+1, 9):  # vertically up
        if b[alf[j]+y] == "00":
            res.append(alf[j]+y)
        elif different_color_figure(b, x, y, alf[j], y):
            res.append(alf[j]+y)
            break
        else:
            break
    for j in reversed(range(1, i)):  # vertically down
        if b[alf[j]+y] == "00":
            res.append(alf[j]+y)
        elif different_color_figure(b, x, y, alf[j], y):
            res.append(alf[j]+y)
            break
        else:
            break
    return res


def check_knight(b, x, y):  # return all possible squares to move as a knight
    res, k = [], 1
    while alf[k] != x:
        k += 1
    for i in range(-2, 3):
        for j in range(-2, 3):
            if abs(i) + abs(j) == 3:
                # if the field is inside the board
                if k+i in range(1, 9) and int(y)+j in range(1, 9):
                    res.append(alf[k+i]+str(int(y)+j))
    return res


def check_bishop(b, x, y):  # return all possible squares to move as a bishop
    res, k = [], 1
    while alf[k] != x:
        k += 1
    j = 1
    for i in range(k+1, 9):  # first quadrant
        if i in range(1, 9) and (int(y)+j) in range(1, 9):
            if b[alf[i]+str(int(y)+j)] == "00":
                res.append(alf[i]+str(int(y)+j))
                j += 1
            elif different_color_figure(b, x, y, alf[i], str(int(y)+j)):
                res.append(alf[i]+str(int(y)+j))
                break
            else:
                break
    j = 1
    for i in range(k+1, 9):  # second quadrant
        if i in range(1, 9) and (int(y)-j) in range(1, 9):
            if b[alf[i]+str(int(y)-j)] == "00":
                res.append(alf[i]+str(int(y)-j))
                j += 1
            elif different_color_figure(b, x, y, alf[i], str(int(y)-j)):
                res.append(alf[i]+str(int(y)-j))
                break
            else:
                break
    j = 1
    for i in reversed(range(1, k)):  # forth quadrant
        if i in range(1, 9) and (int(y)+j) in range(1, 9):
            if b[alf[i]+str(int(y)+j)] == "00":
                res.append(alf[i]+str(int(y)+j))
                j += 1
            elif different_color_figure(b, x, y, alf[i], str(int(y)+j)):
                res.append(alf[i]+str(int(y)+j))
                break
            else:
                break
    j = 1
    for i in reversed(range(1, k)):  # third quadrant
        if i in range(1, 9) and (int(y)-j) in range(1, 9):
            if b[alf[i]+str(int(y)-j)] == "00":
                res.append(alf[i]+str(int(y)-j))
                j += 1
            elif different_color_figure(b, x, y, alf[i], str(int(y)-j)):
                res.append(alf[i]+str(int(y)-j))
                break
            else:
                break
    return res


def check_queens(b, x, y):  # return all possible squares to move as a queen
    return check_bishop(b, x, y) + check_rook(b, x, y)


def check_kings(b, x, y):  # return all possible squares to move as a king
    res, k = [], 1
    while alf[k] != x:
        k += 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            if k+i in range(1, 9) and int(y)+j in range(1, 9):
                if b[alf[k+i]+str(int(y)+j)] == "00" or different_color_figure(b, x, y, alf[k+i], str(int(y)+j)):
                    if alf[k+i]+str(int(y)+j) != x+y:
                        res.append(alf[k+i]+str(int(y)+j))
    return res


figures_move_options = {
    "01": check_white_pawn,
    "02": check_bishop,
    "03": check_knight,
    "04": check_rook,
    "05": check_queens,
    "06": check_kings,
    "11": check_black_pawn,
    "12": check_bishop,
    "13": check_knight,
    "14": check_rook,
    "15": check_queens,
    "16": check_kings
}


# return all possible squares to move as a king
def check_king(game_num, x1, y1, x2, y2):
    call = x2+y2  # new position
    i, j = 1, 1
    while alf[i] != x1:
        i += 1
    while alf[j] != x2:
        j += 1
    start_field = sql.get_pos_db(game_num)
    b = sql.get_board_db(game_num)
    game_info = sql.get_info_db(game_num)

    if b[start_field] == "06" and call == "g1" and game_info["white_king_move"] == "0":
        # white king kingside castling
        if b[call] != "00":  # if the new king field isn't empty
            return "castling_impossible_kk"
        # if the king and king's rook didn't move for the game
        elif game_info["white_king_move"] == "0" and game_info["white_right_rock_move"] == "0":
            if b["f1"] == "00":  # if the field f1 is empty, then castling is possible
                return "white_short"
            else:
                return "castling_impossible_f1"
        else:
            if game_info["white_king_move"] == "1":
                return "castling_impossible_k"
            else:
                return "castling_impossible_r"

    elif b[start_field] == "06" and call == "c1" and game_info["white_king_move"] == "0":
        # white king queenside castling
        if b[call] != "00":
            return "castling_impossible_kk"
        # if the king and queen's rook didn't move for the game
        elif game_info["white_left_rock_move"] == "0" and game_info["white_king_move"] == "0":
            # if the fields b1 and d1 are empty, then castling is possible
            if b["b1"] == "00" and b["d1"] == "00":
                return "white_long"
            else:
                return "castling_impossible"
        else:
            if game_info["white_king_move"] == "1":
                return "castling_impossible_k"
            else:
                return "castling_impossible_r"

    if b[start_field] == "16" and call == "g8" and game_info["black_king_move"] == "0":
        # black king kingside castling
        if b[call] != "00":
            return "castling_impossible_kk"

        # if the king and king's rook didn't move for the game
        elif game_info["black_king_move"] == "0" and game_info["black_right_rock_move"] == "0":
            if b["f8"] == "00":  # if the field f8 is empty, then castling is possible
                return "black_short"
            else:
                return "castling_impossible_f8"

        else:
            if game_info["black_king_move"] == "1":
                return "castling_impossible_k"
            else:
                return "castling_impossible_r"

    elif b[start_field] == "16" and call == "c8" and game_info["black_king_move"] == "0":
        # black king queenside castling
        if b[call] != "00":
            return "castling_impossible_kk"
        # if the king and queen's rook didn't move for the game
        elif game_info["black_left_rock_move"] == "0" and game_info["black_king_move"] == "0":
            # if the fields b8 and d8 are empty, then castling is possible
            if b["b8"] == "00" and b["d8"] == "00":
                return "black_long"
            else:
                return "castling_impossible"
        else:
            if game_info["black_king_move"] == "1":
                return "castling_impossible_k"
            else:
                return "castling_impossible_r"
    else:
        if abs(i-j)+abs(int(y1)-int(y2)) < 3 and (abs(i-j) == 0 and abs(int(y1)-int(y2)) == 1) or (abs(i-j) == 1 and abs(int(y1)-int(y2) == 0)) or (abs(i-j) == 1 and abs(int(y1)-int(y2)) == 1):
            return "yes"
        else:
            return "king_wall"


def get_values(d, keys, default=None):
    reverse = dict(zip(d.values(), d.keys()))
    return (reverse.get(keys))


def check_for_check(color_turn, b) -> bool:  # checking for check on edited desk
    white_king_pos = get_values(b, '06')
    black_king_pos = get_values(b, '16')

    for pos, figure in b.items():
        if color_turn == "0" and figure[0] == "1":
            if white_king_pos in figures_move_options[figure](b, pos[0], pos[1]):
                return True
        elif color_turn == "1" and figure[0] == "0" and figure[1] != "0":
            if black_king_pos in figures_move_options[figure](b, pos[0], pos[1]):
                return True

    return False


def check_mate(game_num):
    game_info = sql.get_info_db(game_num)
    b = sql.get_board_db(game_num)
    color_turn = game_info["color_turn"]
        
    for pos, figure in b.items():
        if figure.startswith(color_turn):
            moves = figures_move_options.get(figure, lambda b, x, y: [])
            possible_fields = moves(b, pos[0], pos[1])
            for field in possible_fields:
                b1 = b.copy()
                b1[pos] = "00"
                b1[field] = figure
                if not check_for_check(color_turn, b1):
                    print(f'{figure} from {pos} to {field}')
                    return False
    return True


@dp.message_handler(commands=['start_game'])  # creating new game function
async def start_game(message: types.Message):
    if message.chat.id < 0:  # check for game creation chat, if it is the group then sends away
        await bot.send_message(message.chat.id, "Use privat chat to create game PLEASE!!!")
    else:
        game: str = sql.create_new_game()
        msg = (
            f"You created game <b>№{game}</b>\n"
            "To invite a player, he must send this message to the game bot."
        )
        message_obj = await bot.send_message(message.chat.id, text=msg)
        name = " "
        if str(message.from_user.first_name) != "None":
            name = str(message.from_user.first_name)
        if str(message.from_user.last_name) != "None":
            name += str(message.from_user.last_name)
        sql.init_board_table(str(message_obj.message_id), str(message.chat.id), str(
            name), message.from_user.username, str(time.time()))
        await bot.send_message(const.diema, '/accept_game_1')


@dp.message_handler(commands=['accept_game_1'])
async def accept_game_1(message: types.Message):
    name = " "
    if str(message.from_user.first_name) != "None":
        name = str(message.from_user.first_name)
    if str(message.from_user.last_name) != "None":
        name += str(message.from_user.last_name)
    sql.accept_game_db("1", str(message.from_user.id), str(
        name), message.from_user.username, str(time.time()))
    await show_board(message.chat.id, "1", "both", 1)


@dp.message_handler(commands=['get_board'])
async def accept_game_1(message: types.Message):
    b = sql.get_board_db('1')
    print(b)


# mydatabase.bot_info creating function
@dp.message_handler(commands=['start_db'])
async def create_bot_info_table(message: types.Message):
    """
    !!!mydatabase MUST BE CREATED!!!
    """
    if message.from_user.id == const.admin:
        sql.create_bot_info_table()
        await bot.send_message(const.admin, 'TABLE bot_info created seccessfully.')


@dp.callback_query_handler()  # lambda c: c.data == 'a1' all callback_query handle
async def on_first_button_first_answer(callback_query: types.CallbackQuery):
    chat_id = callback_query.message.chat.id
    game_num = "1"  # getting game number from player info
    origin_square = sql.get_pos_db(game_num)
    b = sql.get_board_db(game_num)
    game_info = sql.get_info_db(game_num)
    # game_info["color_turn"] possible values: "0", "1", "transf_0", "transf_1"
    player_id:str = "white_id" if game_info["color_turn"] == "0" else "black_id"
    print(f"callback_query.data = {callback_query.data}")
    if game_info["color_turn"].startswith("transf"):  # if a figure transformation is taking place now
        if callback_query.data.startswith("transf"):  # transf|15|d1
            callback_query_info = callback_query.data.split("|")  # ['transf', '15', 'd1']
            new_figure = callback_query_info[1]
            place = callback_query_info[2]
            sql.save_new_figure_db(game_num, new_figure, place)
            color_turn = sql.change_turn_db(game_num)  # color_turn "transt_0|1" -> "1"|"0"
            await show_board(chat_id, game_num, "both", callback_query)
            if check_for_check(color_turn, sql.get_board_db(game_num)):
                msg = "Black king is in check" if game_info["color_turn"][-1] == "0" else "White king is in check"
                await bot.send_message(int(game_info["white_id"]), msg)
                await bot.send_message(int(game_info["black_id"]), msg)
        else:
            await callback_query.answer(show_alert=False, text="Now is not your turn!")
    elif game_info[player_id] == str(chat_id):  # if the player whose turn it is pressed the button
        target_square = callback_query.data
        if origin_square == " ":  # if figure is NOT selected
            if target_square == "pass":
                pass
            # if a non-empty field for selecting a figure is selected
            elif b[target_square] != "00" and len(target_square) < 4:
                # white chooses black
                if game_info["color_turn"] != b[target_square][0]:
                    await callback_query.answer(show_alert=False, text="Figure isn't selected")
                else:
                    await callback_query.answer(show_alert=False, text=f"You choose {figures[b[target_square]]}, choose field")
                    sql.save_start_field_db(game_num, target_square)
                    await show_board(chat_id, game_num, "update", callback_query)
            # empty field
            else:
                await callback_query.answer(show_alert=False, text="Choose non-empty field")

        if origin_square != " ":  # if figure IS selected
            # letter was/number was
            x1, y1 = origin_square[0], origin_square[1]
            # letter has become/number has become
            x2, y2 = target_square[0], target_square[1]
            if target_square == "pass":  # если нажата кнопка ХОД, для сброса выбранной фигуры
                sql.save_start_field_db(game_num, " ")
                await show_board(chat_id, game_num, "update", callback_query)
            else:
                if not different_color_figure(b, x1, y1, x2, y2) and b[target_square] != "00":  # if a figure of the same color is selected
                    await callback_query.answer(show_alert=False,
                                                text=f"You choose {figures[b[target_square]]}, choose field")
                    sql.save_start_field_db(game_num, callback_query.data)
                    await show_board(chat_id, game_num, "update", callback_query)
                else:
                    figure = b[origin_square]
                    if target_square in figures_move_options[figure](b, x1, y1):
                        b[target_square] = figure
                        b[origin_square] = "00"
                        if check_for_check(game_info["color_turn"], b):
                            await callback_query.answer(show_alert=False, text="Будет шах даттебайо!")
                        else:
                            if figure == "01" and y2 == "8":
                                sql.save_turn_field_db(game_num, "transf_0")
                                sql.change_board_db(game_num, origin_square, "00", target_square, "01")
                                await show_board(chat_id, game_num, "both", callback_query)
                                await white_transformation(chat_id, target_square)
                            elif figure == "11" and y2 == "1":
                                sql.save_turn_field_db(game_num, "transf_1")
                                sql.change_board_db(game_num, origin_square, "00", target_square, "11")
                                await show_board(chat_id, game_num, "both", callback_query)
                                await black_transformation(chat_id, target_square)
                            else:
                                await do_turn(chat_id, callback_query, game_num)
    else:
        await callback_query.answer(text="Now is not your turn!")


@dp.message_handler(types.Message)  # text messages handler
async def accept_game(message: types.Message):
    s = message.text
    try:
        if message.forward_from.id == const.bot and "To invite a player" in s:
            name = " "
            if str(message.from_user.first_name) != "None":
                name = str(message.from_user.first_name)
            if str(message.from_user.last_name) != "None":
                name += str(message.from_user.last_name)
            sql.accept_game_db(s[s.find("№") + 1:s.find("To invite a player") - 1], str(
                message.from_user.id), str(name), str(message.from_user.username), str(time.time()))
            await show_board(message.chat.id, s[s.find("№") + 1:s.find("To invite a player") - 1], "both", 1)
    except AttributeError:
        pass


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
