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


start_game_board = {"a1": "04", "b1": "03", "c1": "02", "d1": "05", "e1": "06", "f1": "02", "g1": "03", "h1": "04",
                    "a2": "01", "b2": "01", "c2": "01", "d2": "01", "e2": "01", "f2": "01", "g2": "01", "h2": "01",
                    "a3": "00", "b3": "00", "c3": "00", "d3": "00", "e3": "00", "f3": "00", "g3": "00", "h3": "00",
                    "a4": "00", "b4": "00", "c4": "00", "d4": "00", "e4": "00", "f4": "00", "g4": "00", "h4": "00",
                    "a5": "00", "b5": "00", "c5": "00", "d5": "00", "e5": "00", "f5": "00", "g5": "00", "h5": "00",
                    "a6": "00", "b6": "00", "c6": "00", "d6": "00", "e6": "00", "f6": "00", "g6": "00", "h6": "00",
                    "a7": "11", "b7": "11", "c7": "11", "d7": "11", "e7": "11", "f7": "11", "g7": "11", "h7": "11",
                    "a8": "14", "b8": "13", "c8": "12", "d8": "15", "e8": "16", "f8": "12", "g8": "13", "h8": "14", "turn": " "}

alf = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g", 8: "h"}

figures = {"00": " ", "01": "♙", "02": "♗", "03": "♘", "04": "♖", "05": "♕", "06": "♔",
                      "11": "♟", "12": "♝", "13": "♞", "14": "♜", "15": "♛", "16": "♚"}


async def show_board(chat_id, game_num, mode, call):  # create and send game board as message+keyboard
    pos = sql.get_pos_db(game_num)
    b = sql.get_board_db(game_num)
    keyboard_white = InlineKeyboardMarkup()  # White player keyboard
    keyboard_black = InlineKeyboardMarkup()  # Black player keyboard

    # -----------------------------FIRST ROW(A-H 1)-----------------------------------
    callback_button1 = InlineKeyboardButton(text=figures[b["a1"]], callback_data="a1")
    callback_button2 = InlineKeyboardButton(text=figures[b["b1"]], callback_data="b1")
    callback_button3 = InlineKeyboardButton(text=figures[b["c1"]], callback_data="c1")
    callback_button4 = InlineKeyboardButton(text=figures[b["d1"]], callback_data="d1")
    callback_button5 = InlineKeyboardButton(text=figures[b["e1"]], callback_data="e1")
    callback_button6 = InlineKeyboardButton(text=figures[b["f1"]], callback_data="f1")
    callback_button7 = InlineKeyboardButton(text=figures[b["g1"]], callback_data="g1")
    callback_button8 = InlineKeyboardButton(text=figures[b["h1"]], callback_data="h1")

    # -----------------------------SECOND ROW(A-H 2)-----------------------------------
    callback_button9 = InlineKeyboardButton(text=figures[b["a2"]], callback_data="a2")
    callback_button10 = InlineKeyboardButton(text=figures[b["b2"]], callback_data="b2")
    callback_button11 = InlineKeyboardButton(text=figures[b["c2"]], callback_data="c2")
    callback_button12 = InlineKeyboardButton(text=figures[b["d2"]], callback_data="d2")
    callback_button13 = InlineKeyboardButton(text=figures[b["e2"]], callback_data="e2")
    callback_button14 = InlineKeyboardButton(text=figures[b["f2"]], callback_data="f2")
    callback_button15 = InlineKeyboardButton(text=figures[b["g2"]], callback_data="g2")
    callback_button16 = InlineKeyboardButton(text=figures[b["h2"]], callback_data="h2")

    # -----------------------------THIRD ROW(A-H 3)------------------------------------
    callback_button17 = InlineKeyboardButton(text=figures[b["a3"]], callback_data="a3")
    callback_button18 = InlineKeyboardButton(text=figures[b["b3"]], callback_data="b3")
    callback_button19 = InlineKeyboardButton(text=figures[b["c3"]], callback_data="c3")
    callback_button20 = InlineKeyboardButton(text=figures[b["d3"]], callback_data="d3")
    callback_button21 = InlineKeyboardButton(text=figures[b["e3"]], callback_data="e3")
    callback_button22 = InlineKeyboardButton(text=figures[b["f3"]], callback_data="f3")
    callback_button23 = InlineKeyboardButton(text=figures[b["g3"]], callback_data="g3")
    callback_button24 = InlineKeyboardButton(text=figures[b["h3"]], callback_data="h3")

    # -----------------------------FOURTH ROW(A-H 4)-----------------------------------
    callback_button25 = InlineKeyboardButton(text=figures[b["a4"]], callback_data="a4")
    callback_button26 = InlineKeyboardButton(text=figures[b["b4"]], callback_data="b4")
    callback_button27 = InlineKeyboardButton(text=figures[b["c4"]], callback_data="c4")
    callback_button28 = InlineKeyboardButton(text=figures[b["d4"]], callback_data="d4")
    callback_button29 = InlineKeyboardButton(text=figures[b["e4"]], callback_data="e4")
    callback_button30 = InlineKeyboardButton(text=figures[b["f4"]], callback_data="f4")
    callback_button31 = InlineKeyboardButton(text=figures[b["g4"]], callback_data="g4")
    callback_button32 = InlineKeyboardButton(text=figures[b["h4"]], callback_data="h4")

    # -----------------------------FIFTH ROW(A-H 5)------------------------------------
    callback_button33 = InlineKeyboardButton(text=figures[b["a5"]], callback_data="a5")
    callback_button34 = InlineKeyboardButton(text=figures[b["b5"]], callback_data="b5")
    callback_button35 = InlineKeyboardButton(text=figures[b["c5"]], callback_data="c5")
    callback_button36 = InlineKeyboardButton(text=figures[b["d5"]], callback_data="d5")
    callback_button37 = InlineKeyboardButton(text=figures[b["e5"]], callback_data="e5")
    callback_button38 = InlineKeyboardButton(text=figures[b["f5"]], callback_data="f5")
    callback_button39 = InlineKeyboardButton(text=figures[b["g5"]], callback_data="g5")
    callback_button40 = InlineKeyboardButton(text=figures[b["h5"]], callback_data="h5")

    # -----------------------------SIXTH ROW(A-H 6)------------------------------------
    callback_button41 = InlineKeyboardButton(text=figures[b["a6"]], callback_data="a6")
    callback_button42 = InlineKeyboardButton(text=figures[b["b6"]], callback_data="b6")
    callback_button43 = InlineKeyboardButton(text=figures[b["c6"]], callback_data="c6")
    callback_button44 = InlineKeyboardButton(text=figures[b["d6"]], callback_data="d6")
    callback_button45 = InlineKeyboardButton(text=figures[b["e6"]], callback_data="e6")
    callback_button46 = InlineKeyboardButton(text=figures[b["f6"]], callback_data="f6")
    callback_button47 = InlineKeyboardButton(text=figures[b["g6"]], callback_data="g6")
    callback_button48 = InlineKeyboardButton(text=figures[b["h6"]], callback_data="h6")

    # -----------------------------SEVENTH ROW(A-H 7)----------------------------------
    callback_button49 = InlineKeyboardButton(text=figures[b["a7"]], callback_data="a7")
    callback_button50 = InlineKeyboardButton(text=figures[b["b7"]], callback_data="b7")
    callback_button51 = InlineKeyboardButton(text=figures[b["c7"]], callback_data="c7")
    callback_button52 = InlineKeyboardButton(text=figures[b["d7"]], callback_data="d7")
    callback_button53 = InlineKeyboardButton(text=figures[b["e7"]], callback_data="e7")
    callback_button54 = InlineKeyboardButton(text=figures[b["f7"]], callback_data="f7")
    callback_button55 = InlineKeyboardButton(text=figures[b["g7"]], callback_data="g7")
    callback_button56 = InlineKeyboardButton(text=figures[b["h7"]], callback_data="h7")

    # -----------------------------EIGHTH ROW(A-H 8)-----------------------------------
    callback_button57 = InlineKeyboardButton(text=figures[b["a8"]], callback_data="a8")
    callback_button58 = InlineKeyboardButton(text=figures[b["b8"]], callback_data="b8")
    callback_button59 = InlineKeyboardButton(text=figures[b["c8"]], callback_data="c8")
    callback_button60 = InlineKeyboardButton(text=figures[b["d8"]], callback_data="d8")
    callback_button61 = InlineKeyboardButton(text=figures[b["e8"]], callback_data="e8")
    callback_button62 = InlineKeyboardButton(text=figures[b["f8"]], callback_data="f8")
    callback_button63 = InlineKeyboardButton(text=figures[b["g8"]], callback_data="g8")
    callback_button64 = InlineKeyboardButton(text=figures[b["h8"]], callback_data="h8")

    if pos == " ":
        callback_button65 = InlineKeyboardButton(text="ХОД", callback_data="pass")
    elif pos.find("tranformation") == -1:
        callback_button65 = InlineKeyboardButton(text="ХОД" + figures[b[pos]], callback_data="pass")
    else:
        pass

    keyboard_white.row(callback_button57, callback_button58, callback_button59, callback_button60,
                       callback_button61, callback_button62, callback_button63, callback_button64)
    keyboard_white.row(callback_button49, callback_button50, callback_button51, callback_button52,
                       callback_button53, callback_button54, callback_button55, callback_button56)
    keyboard_white.row(callback_button41, callback_button42, callback_button43, callback_button44,
                       callback_button45, callback_button46, callback_button47, callback_button48)
    keyboard_white.row(callback_button33, callback_button34, callback_button35, callback_button36,
                       callback_button37, callback_button38, callback_button39, callback_button40)
    keyboard_white.row(callback_button25, callback_button26, callback_button27, callback_button28,
                       callback_button29, callback_button30, callback_button31, callback_button32)
    keyboard_white.row(callback_button17, callback_button18, callback_button19, callback_button20,
                       callback_button21, callback_button22, callback_button23, callback_button24)
    keyboard_white.row(callback_button9, callback_button10, callback_button11, callback_button12,
                       callback_button13, callback_button14, callback_button15, callback_button16)
    keyboard_white.row(callback_button1, callback_button2, callback_button3, callback_button4,
                       callback_button5, callback_button6, callback_button7, callback_button8)
    keyboard_white.add(callback_button65)

    keyboard_black.row(callback_button1, callback_button2, callback_button3, callback_button4,
                       callback_button5, callback_button6, callback_button7, callback_button8)
    keyboard_black.row(callback_button9, callback_button10, callback_button11, callback_button12,
                       callback_button13, callback_button14, callback_button15, callback_button16)
    keyboard_black.row(callback_button17, callback_button18, callback_button19, callback_button20,
                       callback_button21, callback_button22, callback_button23, callback_button24)
    keyboard_black.row(callback_button25, callback_button26, callback_button27, callback_button28,
                       callback_button29, callback_button30, callback_button31, callback_button32)
    keyboard_black.row(callback_button33, callback_button34, callback_button35, callback_button36,
                       callback_button37, callback_button38, callback_button39, callback_button40)
    keyboard_black.row(callback_button41, callback_button42, callback_button43, callback_button44,
                       callback_button45, callback_button46, callback_button47, callback_button48)
    keyboard_black.row(callback_button49, callback_button50, callback_button51, callback_button52,
                       callback_button53, callback_button54, callback_button55, callback_button56)
    keyboard_black.row(callback_button57, callback_button58, callback_button59, callback_button60,
                       callback_button61, callback_button62, callback_button63, callback_button64)
    keyboard_black.add(callback_button65)

    myresult = sql.get_all_db(game_num)

    t = "♔ Белого короля" if myresult[64][2] == "white" or myresult[
        64][2] == "transformation_white" else "♚ Черного короля"
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
    start_field = sql.get_pos_db(game_num)
    b = sql.get_board_db(game_num)
    sql.change_board_db(game_num, start_field, "00", call.data, b[start_field])
    sql.save_start_field_db(game_num, " ")
    sql.change_turn_db(game_num)
    await show_board(chat_id, game_num, "both", call)
    game_info = sql.get_info_db(game_num)
    if check_for_check(game_num, "check", sql.get_board_db(game_num)):
        print("SHAH")
        await bot.send_message(int(game_info["white_id"]), game_info["color_turn"]+" is in check")
        await bot.send_message(int(game_info["black_id"]), game_info["color_turn"]+" is in check")
        """if check_mate(game_num):
            print("MAT")
            await bot.send_message(int(game_info["white_id"]), game_info["color_turn"]+" is in check")
            await bot.send_message(int(game_info["black_id"]), game_info["color_turn"]+" is in check")"""
    # await check_for_check(game_num, chat_id, call)



async def white_transformation(chat_id, call_data):  # sending small keyboard to white transformation 
    keyboard = InlineKeyboardMarkup()
    callback_button_q = InlineKeyboardButton(text=figures["05"], callback_data="transformation05"+call_data)  # queen
    callback_button_k = InlineKeyboardButton(text=figures["02"], callback_data="transformation05"+call_data)  # knight
    callback_button_r = InlineKeyboardButton(text=figures["04"], callback_data="transformation04"+call_data)  # rook
    callback_button_b = InlineKeyboardButton(text=figures["03"], callback_data="transformation03"+call_data)  # bishop
    keyboard.row(callback_button_q, callback_button_k,callback_button_r, callback_button_b)
    await bot.send_message(chat_id=chat_id, text="Choose transformation:", reply_markup=keyboard)
    # lib.get_text(lang, "choose_transformation"),


async def black_transformation(chat_id, call_data):  # sending small keyboard to black transformation 
    keyboard = InlineKeyboardMarkup()

    callback_button_q = InlineKeyboardButton(text=figures["15"], callback_data="transformation15"+call_data)  # queen
    callback_button_k = InlineKeyboardButton(text=figures["12"], callback_data="transformation15"+call_data)  # knight
    callback_button_r = InlineKeyboardButton(text=figures["14"], callback_data="transformation14"+call_data)  # rook
    callback_button_b = InlineKeyboardButton(text=figures["13"], callback_data="transformation13"+call_data)  # bishop

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


def check_knight(x, y):  # return all possible squares to move as a knight
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


def check_for_check(game_num, callback_query, b):  # checking for check on edited desk
    game_info = sql.get_info_db(game_num)
    first_field = sql.get_pos_db(game_num)
    white_king = game_info["white_king"]
    black_king = game_info["black_king"]
    if callback_query != "check":
        if first_field == white_king:  # king moving
            # res = check_king(game_num, callback_query, first_field[0], first_field[1], callback_query.data[0], callback_query.data[1], "go")
            white_king = callback_query.data
        if first_field == black_king:
            black_king = callback_query.data
    for i in range(1, 9):
        for j in range(1, 9):
            if game_info["color_turn"] == "white":
                if b[alf[i] + str(j)][0] == "1":
                    if b[alf[i] + str(j)] == "11":  # black pawn
                        if white_king in check_black_pawn(b, alf[i], str(j)):
                            return True

                    elif b[alf[i] + str(j)] == "12":  # black bishop
                        if white_king in check_bishop(b, alf[i], str(j)):
                            return True

                    elif b[alf[i] + str(j)] == "13":  # black knight
                        if white_king in check_knight(alf[i], str(j)):
                            return True

                    elif b[alf[i] + str(j)] == "14":  # black rook
                        if white_king in check_rook(b, alf[i], str(j)):
                            return True

                    elif b[alf[i] + str(j)] == "15":  # black queen
                        if white_king in check_queens(b, alf[i], str(j)):
                            return True

                    elif b[alf[i] + str(j)] == "16":  # black king
                        if white_king in check_kings(b, alf[i], str(j)):
                            return True

            if game_info["color_turn"] == "black":
                if b[alf[i] + str(j)][0] == "0":
                    if b[alf[i] + str(j)] == "01":  # white pawn
                        if black_king in check_white_pawn(b, alf[i], str(j)):
                            return True

                    elif b[alf[i] + str(j)] == "02":  # white bishop
                        if black_king in check_bishop(b, alf[i], str(j)):
                            return True

                    elif b[alf[i] + str(j)] == "03":  # white knight
                        if black_king in check_knight(alf[i], str(j)):
                            return True

                    elif b[alf[i] + str(j)] == "04":  # white rook
                        if black_king in check_rook(b, alf[i], str(j)):
                            return True

                    elif b[alf[i] + str(j)] == "05":  # white queen
                        if black_king in check_queens(b, alf[i], str(j)):
                            return True

                    elif b[alf[i] + str(j)] == "06":  # white king
                        if white_king in check_kings(b, alf[i], str(j)):
                            return True
    return False


def check_mate(game_num):  # checking for mate on currently desk
    res = True
    game_info = sql.get_info_db(game_num)
    for i in range(1, 9):
        for j in range(1, 9):
            if game_info["color_turn"] == "white":
                b = sql.get_board_db(game_num)
                if b[alf[i] + str(j)] == "01":  # pawn
                    possible_fields = check_white_pawn(
                        b, alf[i], str(j))
                    for field in possible_fields:
                        b1 = b
                        b1[alf[i] + str(j)] = "00"
                        b1[field] = "01"
                        if not check_for_check(game_num, "check", b1):
                            return False
                if b[alf[i] + str(j)] == "02":  # bishop
                    possible_fields = check_bishop(b, alf[i], str(j))
                    for field in possible_fields:
                        b1 = b
                        b1[alf[i] + str(j)] = "00"
                        b1[field] = "02"
                        if not check_for_check(game_num, "check", b1):
                            return False
                if b[alf[i] + str(j)] == "03":  # knight
                    possible_fields = check_knight(alf[i], str(j))
                    for field in possible_fields:
                        b1 = b
                        b1[alf[i] + str(j)] = "00"
                        b1[field] = "03"
                        if not check_for_check(game_num, "check", b1):
                            return False
                if b[alf[i] + str(j)] == "04":  # rook
                    possible_fields = check_rook(b, alf[i], str(j))
                    for field in possible_fields:
                        b1 = b
                        b1[alf[i] + str(j)] = "00"
                        b1[field] = "04"
                        if not check_for_check(game_num, "check", b1):
                            return False
                if b[alf[i] + str(j)] == "05":  # queen
                    possible_fields = check_queens(b, alf[i], str(j))
                    for field in possible_fields:
                        b1 = b
                        b1[alf[i] + str(j)] = "00"
                        b1[field] = "05"
                        if not check_for_check(game_num, "check", b1):
                            return False
                if b[alf[i] + str(j)] == "06":  # king
                    possible_fields = check_kings(b, alf[i], str(j))
                    for field in possible_fields:
                        b1 = b
                        b1[alf[i] + str(j)] = "00"
                        b1[field] = "06"
                        if not check_for_check(game_num, field, b1):
                            return False
    return res


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
        await bot.send_message(const.pufik, '/accept_game_1')


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
    """
    if transformation sector:
        bla-bla
    elif right player press button:
        bla-bla
    esle:
        Not your turn
    """
    chat_id = callback_query.message.chat.id
    game_num = "1"  # getting game number from player info
    start_field = sql.get_pos_db(game_num)
    b = sql.get_board_db(game_num)
    game_info = sql.get_info_db(game_num)
    if game_info["color_turn"].startswith("transformation"):  # if a figure transformation is taking place now
        if callback_query.data.startswith("transformation"):  
            new_figure = callback_query.data[len("transformation"):len("transformation05")]
            place = callback_query.data[len("transformation05"):]
            sql.save_new_figure_db(game_num, new_figure, place)
            sql.change_turn_db(game_num)
            await show_board(chat_id, game_num, "both", callback_query)
            if check_for_check(game_num, callback_query, sql.get_board_db(game_num)):
                color = game_info["color_turn"][len("transformation_"):]
                if color == "white":
                    msg = "Black king is in check"
                else: msg = "White king is in check"
                await bot.send_message(int(game_info["white_id"]), msg)
                await bot.send_message(int(game_info["black_id"]), msg)
        else:
            await callback_query.answer(show_alert=False, text="Now is not your turn!")
    elif game_info[game_info["color_turn"]+"_id"] == str(chat_id):  # if the player whose turn it is pressed the button
        if start_field == " ":  # if figure is NOT selected
            if callback_query.data == "pass":
                pass
            # if a non-empty field for selecting a figure is selected
            elif b[callback_query.data] != "00" and len(callback_query.data) < 4:
                # white chooses black
                if game_info["color_turn"] == "white" and b[callback_query.data][0] == "1":
                    await callback_query.answer(show_alert=False, text="Figure isn't selected")

                # black chooses white
                elif game_info["color_turn"] == "black" and b[callback_query.data][0] == "0":
                    await callback_query.answer(show_alert=False, text="Figure isn't selected")
                else:
                    await callback_query.answer(show_alert=False, text=f"You choose {figures[b[callback_query.data]]}, choose field")
                    sql.save_start_field_db(game_num, callback_query.data)
                    await show_board(chat_id, game_num, str(chat_id), callback_query)

            # empty field
            elif b[callback_query.data] == "00" and len(callback_query.data) < 4:
                await callback_query.answer(show_alert=False, text="Choose non-empty field")

        if start_field != " ":  # if figure IS selected
            # letter was/number was
            x1, y1 = start_field[0], start_field[1]
            # letter has become/number has become
            x2, y2 = callback_query.data[0], callback_query.data[1]

            if callback_query.data[0] == "transformation":  # превращение пешки
                b[callback_query.data[3:5]] = callback_query.data[1:3]
            elif callback_query.data == "pass":  # если нажата кнопка ХОД, для сброса выбранной фигуры
                sql.save_start_field_db(game_num, " ")
                await show_board(chat_id, game_num, str(chat_id), callback_query)

            elif b[callback_query.data] == "00":  # move to an empty cell
                # -----------------------WHITE PAWN----------------------------------
                if b[start_field] == "01":  # white pawn move to empty square
                    if callback_query.data in check_white_pawn(b, x1, y1):
                        b[callback_query.data] = b[start_field]
                        b[start_field] = "00"
                        if check_for_check(game_num, callback_query, b):
                            await callback_query.answer(show_alert=False, text="Будет шах даттебайо!")
                        else:
                            if y2 == "8":
                                sql.save_turn_field_db(
                                    game_num, "transformation_white")
                                sql.change_board_db(
                                    game_num, start_field, "00", callback_query.data, "01")
                                await show_board(chat_id, game_num, "both", callback_query)
                                await white_transformation(chat_id, callback_query.data)
                            else:
                                await do_turn(chat_id, callback_query, game_num)

                # -----------------------BLACK PAWN----------------------------------
                elif b[start_field] == "11":  # black pawn move to EMPTY square
                    if callback_query.data in check_black_pawn(b, x1, y1):
                        b[callback_query.data] = b[start_field]
                        b[start_field] = "00"
                        if check_for_check(game_num, callback_query, b):
                            await callback_query.answer(show_alert=False, text="Будет шах даттебайо!")
                        else:
                            if y2 == "1":
                                sql.save_turn_field_db(
                                    game_num, "transformation_black")
                                sql.change_board_db(
                                    game_num, start_field, "00", callback_query.data, "11")
                                await show_board(chat_id, game_num, "both", callback_query)
                                await black_transformation(chat_id, callback_query.data)
                            else:
                                await do_turn(chat_id, callback_query, game_num)

                # -----------------------ROOKS-------------------------------------------------
                elif b[start_field] == "04" or b[start_field] == "14":  # rooks move to EMPTY square
                    if callback_query.data in check_rook(b, x1, y1):
                        b[callback_query.data] = b[start_field]
                        b[start_field] = "00"
                        if check_for_check(game_num, callback_query, b):
                            await callback_query.answer(show_alert=False, text="Будет шах даттебайо!")
                        else:
                            await do_turn(chat_id, callback_query, game_num)

                # -----------------------KNIGHTS---------------------------------------------------
                elif b[start_field] == "03" or b[start_field] == "13":  # # knights move to EMPTY square
                    if callback_query.data in check_knight(x1, y1):
                        b[callback_query.data] = b[start_field]
                        b[start_field] = "00"
                        if check_for_check(game_num, callback_query, b):
                            await callback_query.answer(show_alert=False, text="Будет шах даттебайо!")
                        else:
                            await do_turn(chat_id, callback_query, game_num)

                # -----------------------BISHOPS-----------------------------------------
                elif b[start_field] == "02" or b[start_field] == "12":  # bishops move to EMPTY square
                    if callback_query.data in check_bishop(b, x1, y1):
                        b[callback_query.data] = b[start_field]
                        b[start_field] = "00"
                        if check_for_check(game_num, callback_query, b):
                            await callback_query.answer(show_alert=False, text="Будет шах даттебайо!")
                        else:
                            await do_turn(chat_id, callback_query, game_num)

                # -----------------------KINGS----------------------------------
                elif b[start_field] == "06" or b[start_field] == "16":  # kings move to EMPTY square
                    result = check_king(game_num, x1, y1, x2, y2)
                    # ------------------------- CASTLING ---------------------------------------
                    if result == "white_short":  # white king short castling
                        if check_for_check(game_num, "check", b):
                            await callback_query.answer(show_alert=False, text="Король под боем даттебайо!")
                        else:
                            b[callback_query.data] = b[start_field]
                            b[start_field] = "00"
                            if check_for_check(game_num, callback_query, b):
                                await callback_query.answer(show_alert=False, text="Будет шах даттебайо!")
                            else:
                                sql.do_castling_db(game_num, "white_short")
                                sql.change_turn_db(game_num)
                                await show_board(chat_id, game_num, "both", callback_query)
                                await callback_query.answer(show_alert=False, text="Короткая рокировка успешна!")
                                # text=lib.get_text(lang, "short_castling_success"))
                                change_castling(game_num)

                    elif result == "white_long":  # white king long castling
                        if check_for_check(game_num, "check", b):
                            await callback_query.answer(show_alert=False, text="Король под боем даттебайо!")
                        else:
                            b[callback_query.data] = b[start_field]
                            b[start_field] = "00"
                            if check_for_check(game_num, callback_query, b):
                                await callback_query.answer(show_alert=False, text="Будет шах даттебайо!")
                            else:
                                sql.do_castling_db(game_num, "white_long")
                                sql.change_turn_db(game_num)
                                await show_board(chat_id, game_num, "both", callback_query)
                                await callback_query.answer(show_alert=False, text="Длинная рокировка успешна!")
                                change_castling(game_num)

                    elif result == "black_short":  # black king short castling
                        if check_for_check(game_num, "check", b):
                            await callback_query.answer(show_alert=False, text="Король под боем даттебайо!")
                        else:
                            b[callback_query.data] = b[start_field]
                            b[start_field] = "00"
                            if check_for_check(game_num, callback_query, b):
                                await callback_query.answer(show_alert=False, text="Будет шах даттебайо!")
                            else:
                                sql.do_castling_db(game_num, "black_short")
                                sql.change_turn_db(game_num)
                                await show_board(chat_id, game_num, "both", callback_query)
                                await callback_query.answer(show_alert=False, text="Короткая рокировка успешна!")
                                # text=lib.get_text(lang, "short_castling_success"))
                                change_castling(game_num)

                    elif result == "black_long":  # black king long castling
                        if check_for_check(game_num, "check", b):
                            await callback_query.answer(show_alert=False, text="Король под боем даттебайо!")
                        else:
                            b[callback_query.data] = b[start_field]
                            b[start_field] = "00"
                            if check_for_check(game_num, callback_query, b):
                                await callback_query.answer(show_alert=False, text="Будет шах даттебайо!")
                            else:
                                sql.do_castling_db(game_num, "black_long")
                                sql.change_turn_db(game_num)
                                await show_board(chat_id, game_num, "both", callback_query)
                                await callback_query.answer(show_alert=False, text="Длинная рокировка успешна!")
                                # text=lib.get_text(lang, "long_castling_success"))
                                change_castling(game_num)

                    elif result == "yes":
                        b[callback_query.data] = b[start_field]
                        b[start_field] = "00"
                        if check_for_check(game_num, callback_query, b):
                            await callback_query.answer(show_alert=False, text="Будет шах даттебайо!")
                        else:
                            change_castling(game_num)
                            sql.change_king_db(game_num, callback_query.data)
                            await do_turn(chat_id, callback_query, game_num)

                    # --------------------------- ERRORS ------------------------------------
                    elif result == "castling_impossible_kk":
                        await callback_query.answer(show_alert=False, text="Castling is impossible, the place of the king is taken!")
                    elif result == "castling_impossible_f1":
                        await callback_query.answer(show_alert=False, text="Castling is impossible, obstruction on f1!")
                    elif result == "castling_impossible_f8":
                        await callback_query.answer(show_alert=False, text="Castling is impossible, obstruction on f8!")
                    elif result == "castling_impossible_k":
                        await callback_query.answer(show_alert=False,
                                                    text="Castling is not possible, the king has already left his position")
                    elif result == "castling_impossible_r":
                        await callback_query.answer(show_alert=False,
                                                    text="Castling is not possible, the rook has already left its position")
                    elif result == "castling_impossible":
                        await callback_query.answer(show_alert=False, text="Castling is impossible, an obstacle on the way!")
                    elif result == "king_wall":
                        await callback_query.answer(show_alert=False, text="The king doesn't move like that!")
                    # --------------------------- END OF KINGS ---------------------------------

                # -----------------------QUEENS----------------------------------
                elif b[start_field] == "05" or b[start_field] == "15":  # queens move to EMPTY square
                    if callback_query.data in check_queens(b, x1, y1):
                        b[callback_query.data] = b[start_field]
                        b[start_field] = "00"
                        if check_for_check(game_num, callback_query, b):
                            await callback_query.answer(show_alert=False, text="Будет шах даттебайо!")
                        else:
                            await do_turn(chat_id, callback_query, game_num)

            # if the move is to a NON_EMPTY cell
            elif b[callback_query.data] != "00" and len(callback_query.data) < 4:
                # if a figure of the same color is selected
                if b[callback_query.data][0] == b[start_field][0]:
                    await callback_query.answer(show_alert=False,
                                                text=f"You choose {figures[b[callback_query.data]]}, choose field")
                    sql.save_start_field_db(game_num, callback_query.data)
                    await show_board(chat_id, game_num, str(chat_id), callback_query)

                # if a figure of a different color is selected
                if b[callback_query.data][0] != b[start_field][0]:
                    # -----------------------KNIGHTS----------------------------------
                    if b[start_field] == "03" or b[start_field] == "13":  # knights move to NON-EMPTY square
                        if callback_query.data in check_knight(x1, y1):
                            b[callback_query.data] = b[start_field]
                            b[start_field] = "00"
                            if check_for_check(game_num, callback_query, b):
                                await callback_query.answer(show_alert=False, text="Будет шах даттебайо!")
                            else:
                                await do_turn(chat_id, callback_query, game_num)

                    # -----------------------BISHOPS----------------------------------
                    elif b[start_field] == "02" or b[start_field] == "12":  # bishops move to NON-EMPTY square
                        if callback_query.data in check_bishop(b, x1, y1):
                            b[callback_query.data] = b[start_field]
                            b[start_field] = "00"
                            if check_for_check(game_num, callback_query, b):
                                await callback_query.answer(show_alert=False, text="Будет шах даттебайо!")
                            else:
                                await do_turn(chat_id, callback_query, game_num)

                    # -----------------------ROOKS----------------------------------
                    elif b[start_field] == "04" or b[start_field] == "14":  # rooks move to NON-EMPTY square
                        if callback_query.data in check_rook(b, x1, y1):
                            b[callback_query.data] = b[start_field]
                            b[start_field] = "00"
                            if check_for_check(game_num, callback_query, b):
                                await callback_query.answer(show_alert=False, text="Будет шах даттебайо!")
                            else:
                                await do_turn(chat_id, callback_query, game_num)

                    # -----------------------QUEENS----------------------------------
                    elif b[start_field] == "05" or b[start_field] == "15":  # queens move to NON-EMPTY square
                        if callback_query.data in check_queens(b, x1, y1):
                            b[callback_query.data] = b[start_field]
                            b[start_field] = "00"
                            if check_for_check(game_num, callback_query, b):
                                await callback_query.answer(show_alert=False, text="Будет шах даттебайо!")
                            else:
                                await do_turn(chat_id, callback_query, game_num)

                    # -----------------------WHITE PAWN----------------------------------
                    elif b[start_field] == "01":  # white pawn move to NON-EMPTY square
                        if callback_query.data in check_white_pawn(b, x1, y1):
                            b[callback_query.data] = b[start_field]
                            b[start_field] = "00"
                            if check_for_check(game_num, callback_query, b):
                                await callback_query.answer(show_alert=False, text="Будет шах даттебайо!")
                            else:
                                if y2 == "8":
                                    sql.save_turn_field_db(
                                        game_num, "transformation_white")
                                    sql.change_board_db(
                                        game_num, start_field, "00", callback_query.data, "01")
                                    await show_board(chat_id, game_num, "both", callback_query)
                                    await white_transformation(chat_id, callback_query.data)
                                else:
                                    await do_turn(chat_id, callback_query, game_num)

                    # -----------------------BLACK PAWN----------------------------------
                    elif b[start_field] == "11":  # black pawn move to NON-EMPTY square
                        if callback_query.data in check_black_pawn(b, x1, y1):
                            b[callback_query.data] = b[start_field]
                            b[start_field] = "00"
                            if check_for_check(game_num, callback_query, b):
                                await callback_query.answer(show_alert=False, text="Будет шах даттебайо!")
                            else:
                                if y2 == "1":
                                    sql.save_turn_field_db(
                                        game_num, "transformation_black")
                                    sql.change_board_db(
                                        game_num, start_field, "00", callback_query.data, "01")
                                    await show_board(chat_id, game_num, "both", callback_query)
                                    await white_transformation(chat_id, callback_query.data)
                                else:
                                    await do_turn(chat_id, callback_query, game_num)

                    # -----------------------KINGS----------------------------------
                    elif b[start_field] == "06" or b[start_field] == "16":  # kings move to NON-EMPTY square
                        result = check_king(game_num, x1, y1, x2, y2,)
                        if result == "yes":
                            b[callback_query.data] = b[start_field]
                            b[start_field] = "00"
                            if check_for_check(game_num, callback_query, b):
                                await callback_query.answer(show_alert=False, text="Будет шах даттебайо!")
                            else:
                                change_castling(game_num)
                                sql.change_king_db(
                                    game_num, callback_query.data)
                                await do_turn(chat_id, callback_query, game_num)
                        elif result == "king_wall":
                            await callback_query.answer(show_alert=False, text="The king doesn't move like that!")
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
