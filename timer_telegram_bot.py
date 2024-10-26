import ptbot
import os
from dotenv import load
from pytimeparse import parse


load()


def choose(author_id):
    answer = "Время вышло!"
    bot.send_message(author_id, answer)


def notify_progress(secs_left, author_id, bot_answer_id, message):
    bot.update_message(author_id, bot_answer_id, """Осталось {secs_left} секунд\n{render}""".format(secs_left=secs_left, render = render_progressbar(parse(message), parse(message) - secs_left)))


def render_progressbar(total, iteration, prefix='', suffix='', length=30, fill='█', zfill='░'):
    iteration = min(total, iteration)
    percent = "{0:.1f}"
    percent = percent.format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    pbar = fill * filled_length + zfill * (length - filled_length)
    return '{0} |{1}| {2}% {3}'.format(prefix, pbar, percent, suffix)
    
    
def reply(chat_id, message):
    answer_id = bot.send_message(chat_id, "Запускаю таймер")
    bot.create_countdown(parse(message), notify_progress, author_id=chat_id, bot_answer_id=answer_id, message=message)
    bot.create_timer(parse(message), choose, author_id=chat_id)


if __name__ == '__main__':
    bot = ptbot.Bot(os.getenv("TELEGRAM_TOKEN"))
    bot.reply_on_message(reply)
    bot.run_bot()