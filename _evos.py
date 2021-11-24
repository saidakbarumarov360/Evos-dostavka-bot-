from telegram import ReplyMarkup, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, MessageHandler, CommandHandler, CallbackQueryHandler, Filters, ConversationHandler

log = {}


def keyboard_btns(type=None, resize_keyboard=None):
    if type == "main":
        btn = [
            [KeyboardButton("🛒 Buyurtma qilish")],
            [KeyboardButton("🛍 Buyurtmalarim"), KeyboardButton("👨‍👩‍👦 Evos Oilasi")],
            [KeyboardButton("✍️ Fikir Bildirish"), KeyboardButton("⚙️ Sozlamalar")],
        ]

    elif type == "location":
        btn = [
            [KeyboardButton("📍 Geo-joylashuvni yuboring", request_location=True)],
            [KeyboardButton("⬅️ Ortga", callback="ortga")]
        ]

    elif type == "contact":
        btn = [
            [KeyboardButton("📞 Contact", request_contact=True)],
            [KeyboardButton("⬅️ Ortga", callback="ortga")]
        ]


    elif type == "second_main":
        btn = [
            [KeyboardButton("📍 Geo-joylashuvni o'zgartirish"), KeyboardButton("🍴 Menyu")],
            [KeyboardButton("🛍 Buyurtmalarim"), KeyboardButton("👨‍👩‍👦 Evos Oilasi")],
            [KeyboardButton("✍️ Fikir Bildirish"), KeyboardButton("⚙️ Sozlamalar")],
        ]
    else:
        btn = []

    return ReplyKeyboardMarkup(btn, resize_keyboard=True)


def inline_btns(type=None, l_type=None, ctg=None, chat_id=None, msg_id=None):
    if type == 'main':
        btns = [
            [InlineKeyboardButton("🌯 Lavash", callback_data="lavaw"),
             InlineKeyboardButton("🍟🌯🥤 Set", callback_data="set")],
            [InlineKeyboardButton("🥙 Shaurma", callback_data="waurma"),
             InlineKeyboardButton("🍲 Donar", callback_data="donar")],
            [InlineKeyboardButton("🍔 Burger", callback_data="burger"),
             InlineKeyboardButton("🌭 Xot-dok", callback_data="xotdok")],
            [InlineKeyboardButton("🍰 Desertlar", callback_data="desert"),
             InlineKeyboardButton("☕️ Ichimliklar", callback_data="ichimliklar")],
            [InlineKeyboardButton("🍟 Gazaklar", callback_data="gazaklar")]
        ]
    elif type == "menu":
        btns = [
            [InlineKeyboardButton("Go'shtli Lavash", callback_data=f"{ctg}_goshtli"),
             InlineKeyboardButton("Go'shtli lavash pishloq bilan", callback_data=f"{ctg}_goshtlip")],
            [InlineKeyboardButton("Tovuqli Lavash", callback_data=f"{ctg}_tovuqli"),
             InlineKeyboardButton("Tovuqli Lavash pishloq bilan", callback_data=f"{ctg}_tovuqlip")],
            [InlineKeyboardButton("Qalampir Lavash", callback_data=f"{ctg}_qalampir"),
             InlineKeyboardButton("Fitter", callback_data=f"{ctg}_fitter")],
            [InlineKeyboardButton("🔝Продолжить заказ", callback_data=f"{ctg}_prodoljit")],
            [InlineKeyboardButton("⬅️ Ortga", callback_data="back")],
            [InlineKeyboardButton("Home", callback_data="home")]
        ]

    elif type == "lavaw_hajim":
        btns = [
            [InlineKeyboardButton("Klassik", callback_data=f"{ctg}_{l_type}_klassik"),
             InlineKeyboardButton("Mini", callback_data=f"{ctg}_{l_type}_mini")],
            [InlineKeyboardButton("Big", callback_data=f"{ctg}_{l_type}_big")],
            [InlineKeyboardButton("⬅️ Ortga", callback_data=f"{ctg}_{l_type}_back"),
             InlineKeyboardButton("🔝Продолжить заказ", callback_data="prodoljit")],
        ]


    elif type == "menu_s":
        btns = [
            [InlineKeyboardButton("Combo+", callback_data="combo")],
            [InlineKeyboardButton("🔝Продолжить заказ", callback_data="prodoljit")],
            [InlineKeyboardButton("⬅️ Ortga", callback_data="back")]
        ]

    elif type == "menu_d":
        btns = [
            [InlineKeyboardButton("Go'shtli Donar", callback_data=f"{ctg}_goshtli"),
             InlineKeyboardButton("Tovuqli Donar", callback_data=f"{ctg}_tovuqli")],
            [InlineKeyboardButton("🔝Продолжить заказ", callback_data="prodoljit")],
            [InlineKeyboardButton("⬅️ Ortga", callback_data="back")]
        ]

    elif type == "donar_hajim":
        btns = [
            [InlineKeyboardButton("Klassik", callback_data=f"{ctg}_{l_type}_klassik"),
             InlineKeyboardButton("Katta", callback_data=f"{ctg}_{l_type}_katta")],
            [InlineKeyboardButton("⬅️ Ortga", callback_data="back")]
        ]

    elif type == "menu_w":
        btns = [
            [InlineKeyboardButton("Go'shtli Shaurma", callback_data=f"{ctg}_goshtli"),
             InlineKeyboardButton("Go'shtli Shaurma achchiq", callback_data=f"{ctg}_goshtli")],
            [InlineKeyboardButton("Tovuqli Shaurma", callback_data=f"{ctg}_tovuqli"),
             InlineKeyboardButton("Tovuqli Shaurma achchiq", callback_data=f"{ctg}_tovuqli")],
            [InlineKeyboardButton("🔝Продолжить заказ", callback_data="prodoljit")],
            [InlineKeyboardButton("⬅️ Ortga", callback_data="back")]
        ]

    elif type == "waurma_hajim":
        btns = [
            [InlineKeyboardButton("Klassik", callback_data=f"{ctg}_{l_type}_klassik"),
             InlineKeyboardButton("Katta", callback_data=f"{ctg}_{l_type}_katta")],
            [InlineKeyboardButton("🔝Продолжить заказ", callback_data="prodoljit")],
            [InlineKeyboardButton("⬅️ Ortga", callback_data="back")]
        ]

    elif type == "menu_b":
        btns = [
            [InlineKeyboardButton("Gamburger", callback_data=f"{ctg}_gamburger"),
             InlineKeyboardButton("Chizburger", callback_data=f"{ctg}_chizburger")],
            [InlineKeyboardButton("🔝Продолжить заказ", callback_data="prodoljit")],
            [InlineKeyboardButton("⬅️ Ortga", callback_data="back")]
        ]

    elif type == "burger_hajim":
        btns = [
            [InlineKeyboardButton("Gamburger", callback_data=f"{ctg}_{l_type}_klassik"),
             InlineKeyboardButton("Даблбургерб", callback_data=f"{ctg}_{l_type}_dablburger")],
            [InlineKeyboardButton("🔝Продолжить заказ", callback_data="prodoljit")],
            [InlineKeyboardButton("⬅️ Ortga", callback_data="back")]
        ]

    elif type == "chizburger_hajim":
        btns = [
            [InlineKeyboardButton("Gamburger", callback_data=f"{ctg}_{l_type}_klassik"),
             InlineKeyboardButton("Даблчиз", callback_data=f"{ctg}_{l_type}_dablchiz")],
            [InlineKeyboardButton("🔝Продолжить заказ", callback_data="prodoljit")],
            [InlineKeyboardButton("⬅️ Ortga", callback_data="back")]
        ]


    elif type == "menu_x":
        btns = [
            [InlineKeyboardButton("Klassik Xot-dog", callback_data=f"{ctg}klassik"),
             InlineKeyboardButton("Oddiy", callback_data=f"{ctg}_oddiy")],
            [InlineKeyboardButton("Shpohona", callback_data=f"{ctg}_shohona_x")],
            [InlineKeyboardButton("🔝Продолжить заказ", callback_data="prodoljit")],
            [InlineKeyboardButton("⬅️ Ortga", callback_data="back")]
        ]

    elif type == "nomer":
        btns = [
            [InlineKeyboardButton("1", callback_data=f"{ctg}_{l_type}_bir"),
             InlineKeyboardButton("2", callback_data=f"{ctg}_{l_type}_ikki"),
             InlineKeyboardButton("3", callback_data=f"{ctg}_{l_type}_uch")],
            [InlineKeyboardButton("4", callback_data=f"{ctg}_{l_type}_tort"),
             InlineKeyboardButton("5", callback_data=f"{ctg}_{l_type}_besh"),
             InlineKeyboardButton("2", callback_data=f"{ctg}_{l_type}_olti")],
            [InlineKeyboardButton("7", callback_data=f"{ctg}_{l_type}_yetti"),
             InlineKeyboardButton("8", callback_data=f"{ctg}_{l_type}_sakkiz"),
             InlineKeyboardButton("2", callback_data=f"{ctg}_{l_type}_toqqiz")],
            [InlineKeyboardButton("⬅️ Ortga", callback_data=f"{ctg}_{l_type}_back"),
             InlineKeyboardButton("🔝Продолжить заказ", callback_data="prodoljit")],
        ]

    elif type == "menu_d":
        btns = [
            [InlineKeyboardButton("Asalim", callback_data=f"{ctg}_asalim"),
             InlineKeyboardButton("Чизкейк", callback_data=f"{ctg}_chizkeyk")],
            [InlineKeyboardButton("Choco", callback_data=f"{ctg}_choco")],
            [InlineKeyboardButton("🔝Продолжить заказ", callback_data=f"prodoljit")],
            [InlineKeyboardButton("⬅️ Ortga", callback_data="back")]
        ]

    elif type == "menu_ichimliklar":
        btns = [
            [InlineKeyboardButton("Suv", callback_data=f"{ctg}_suv"),
             InlineKeyboardButton("CcaCola", callback_data=f"{ctg}_cola")],
            [InlineKeyboardButton("Issiq ichimliklar", callback_data=f"{ctg}_issiq_ichimliklar1")]
        ]


    elif type == "cola":
        btns = [
            [InlineKeyboardButton("0.5 L", callback_data=f"{ctg}_{l_type}_cola"),
             InlineKeyboardButton("Разлив", callback_data=f"{ctg}_{l_type}_razliv")],
            [InlineKeyboardButton("1.5 L", callback_data=f"{ctg}_{l_type}_katta")],
            [InlineKeyboardButton("🔝Продолжить заказ", callback_data=f"prodoljit")],
            [InlineKeyboardButton("⬅️ Ortga", callback_data="back")]
        ]

    elif type == "issiq_ichimliklar":
        btns = [
            [InlineKeyboardButton("Limonli choy", callback_data=f"{ctg}_{l_type}_choy"),
             InlineKeyboardButton("Coffee 3/1", callback_data=f"{ctg}_{l_type}_cofe")],
            [InlineKeyboardButton("Qora coffee", callback_data=f"{ctg}_{l_type}_qora")],
            [InlineKeyboardButton("🔝Продолжить заказ", callback_data="prodoljit")],
            [InlineKeyboardButton("⬅️ Ortga", callback_data="back")]
        ]


    elif type == "menu_s":
        btns = [
            [InlineKeyboardButton("Combo+", callback_data=f"{ctg}_{l_type}_combo")],
            [InlineKeyboardButton("🔝Продолжить заказ", callback_data="prodoljit")],
            [InlineKeyboardButton("⬅️ Ortga", callback_data="back")]
        ]

    else:
        btns = []

    return InlineKeyboardMarkup(btns)


def start(update, cnext):
    log["qadam"] = 1
    user = update.message.from_user
    update.message.reply_text(f"Assalomu aleykum\n {user.first_name}\nTanlovingiz uchun rahmat")
    update.message.reply_text("Quyidailardan birirni tanlang ⬇", reply_markup=keyboard_btns(type="main"))


def recived_msg(update, context):
    msg = update.message.text
    if msg == "🛒 Buyurtma qilish":
        log["qadam"] = 2
        update.message.reply_text(f"Eltib berish uchun geo-joylashuvni jo'nating yoki manzilni tanlang",
                                  reply_markup=keyboard_btns("location"))
    elif log.get("qadam") == 2:
        resived_location(update, context)


def resived_location(update, context):
    loc = update.message.location
    if loc:
        log["qadam"] = 3
        update.message.reply_text(f"Quyidagilardan birini tanlang", reply_markup=keyboard_btns("second_main"))
        update.message.reply_html(f"kategorylardan birini tanlang<a href='https://telegra.ph/EVOS-MENU-04-05-2'>.</a>",
                                  reply_markup=inline_btns("main"))
    else:
        update.message.reply_text(f"Eltib berish uchun geo-joylashuvni jo'nating yoki manzilni tanlang",
                                  reply_markup=keyboard_btns("location"))


def received_inline(update, context):
    query = update.callback_query

    data_sp = query.data.split("_")
    print(data_sp)
    if data_sp[0] == "lavaw":
        if len(data_sp) > 1 and (data_sp[1] == "goshtli" or data_sp[1] == "goshtlip"):
            if len(data_sp) > 2 and data_sp[2] == "klassik":
                print("klassicka keldi")

            elif len(data_sp) > 2 and data_sp[2] == "big":
                print("bigga keldi")

            elif len(data_sp) > 2 and data_sp[2] == "mini":
                print("mini keldi")

            elif len(data_sp) > 2 and data_sp[2] == "back":
                query.message.edit_text("Lavash Hajmini tanlang",
                                        reply_markup=inline_btns("menu", ctg=data_sp[0]))
            else:
                query.message.edit_text("Lavash turini tanlang",
                                        reply_markup=inline_btns("lavaw_hajim", l_type=data_sp[1], ctg=data_sp[0]))


        elif len(data_sp) > 1 and (data_sp[1] == "tovuqli" or data_sp[1] == "tovuqlip"):
            if len(data_sp) > 2 and data_sp[2] == "klassik":
                print("klassicka keldi")

            elif len(data_sp) > 2 and data_sp[2] == "big":
                print("bigga keldi")

            elif len(data_sp) > 2 and data_sp[2] == "mini":
                print("mini keldi")

            elif len(data_sp) > 2 and data_sp[2] == "back":
                query.message.edit_text("Lavash Hajmini tanlang",
                                        reply_markup=inline_btns("menu", ctg=data_sp[0]))
            else:
                query.message.edit_text("Lavash Hajmini tanlang",
                                        reply_markup=inline_btns("lavaw_hajim", l_type=data_sp[1], ctg=data_sp[0]))


        elif len(data_sp) > 1 and data_sp[1] == "qalampir":
            if len(data_sp) > 2 and data_sp[2] == "klassik":
                print("klassicka keldi")

            elif len(data_sp) > 2 and data_sp[2] == "big":
                print("bigga keldi")

            elif len(data_sp) > 2 and data_sp[2] == "mini":
                print("mini keldi")

            elif len(data_sp) > 2 and data_sp[2] == "back":
                query.message.edit_text("Lavash Hajmini tanlang",
                                        reply_markup=inline_btns("menu", ctg=data_sp[0]))
            else:
                query.message.edit_text("Lavash Hajmini tanlang",
                                        reply_markup=inline_btns("lavaw_hajim", l_type=data_sp[1], ctg=data_sp[0]))


        elif len(data_sp) > 1 and data_sp[1] == "fitter":
            if len(data_sp) > 2 and data_sp[2] == "nomer":
                print("fitterga keldi")

            elif len(data_sp) > 2 and data_sp[2] == "back":
                query.message.edit_text("Lavash Hajmini tanlang",
                                        reply_markup=inline_btns("menu", ctg=data_sp[0]))
            else:
                query.message.edit_text("Miqdorini tanlang yoki kiriting",
                                        reply_markup=inline_btns("nomer", l_type=data_sp[1], ctg=data_sp[0]))
        else:
            query.message.edit_text("Lavash Hajmini tanlang",
                                        reply_markup=inline_btns("menu", ctg=data_sp[0]))
    elif data_sp[0] == "set":
        if len(data_sp) > 1 and data_sp[1] == "combo":
            if len(data_sp) > 2 and data_sp[2] == "nomer":
                print("combo+ ga keldi")

            elif len(data_sp) > 2 and data_sp[2] == "back":
                query.message.edit_text("Lavash Hajmini tanlang",
                                        reply_markup=inline_btns(type="menu", ctg=data_sp[0]))
            else:
                query.message.edit_text("Miqdorini tanlang yoki kiriting",
                                        reply_markup=inline_btns("nomer",l_type=data_sp[1], ctg=data_sp[0]))
        else:
            query.message.edit_text("Miqdorini tanlang yoki kiriting",
                                        reply_markup=inline_btns("menu_s", ctg=data_sp[0]))


    elif data_sp[0] == "back":
        query.message.edit_text(f"kategorylardan birini tanlang<a href='https://telegra.ph/EVOS-MENU-04-05-2'>.</a>",
                                reply_markup=inline_btns("main"))

    elif data_sp[0] == "home":
        context.bot.delete_message(message_id=query.message.message_id, chat_id=query.message.chat_id)
        context.bot.send_message(text=f"Quyidagilardan birini tanlang", reply_markup=keyboard_btns("main"),
                                 chat_id=query.message.chat_id)

def main():
    Token = "1966839803:AAGtZSUQgq46ck6ya7OeyssXMZa991U22NU"
    updater = Updater(Token)

    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, recived_msg))
    updater.dispatcher.add_handler(MessageHandler(Filters.location, resived_location))
    updater.dispatcher.add_handler(CallbackQueryHandler(received_inline))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()

