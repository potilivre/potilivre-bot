from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from os import environ


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    """Send a message when the command /start is issued."""
    full_name = update.message.from_user.full_name
    message_start = (
        f"Olá, {full_name}, bem-vindx ao bot da PotiLivre\n\n"
        "Comandos:\n\nRegras: /regras\nDescrição: /descricao \n\n"
        "Encontrou aleatoriamente esse bot? Então, visite o nosso site"
        "(https://potilivre.org/) e conheça a comunidade PotiLivre"
        )
    update.message.reply_text(message_start)


def help(bot, update):
    """Send a message when the command /help is issued."""
    message_help = (
        "- Regras do grupo /regras\n"
        "- Está com dúvidas? Fale com nossos membros!\n"
        "- Em caso de dúvidas mais específicas procure nossos Administradores."
        )
    update.message.reply_text(message_help)


def welcome(bot, update):
    """Send a message when the command /welcome is issued."""
    full_name = update.message.new_chat_members[0].full_name
    message_welcome = (
        f"Olá {full_name}, seja bem-vindo ao PotiLivre \n\n"
        "PotiLivre é a Comunidade Potiguar de Software Livre, fundada em 2013."
        " Leia nossas /regras e visite nosso site (https://potilivre.org/)"
        )
    update.message.reply_text(message_welcome)


def rules(bot, update):
    """Send a message with the group rules."""
    message_rules = (
        "1. Respeitar os membros do grupo.\n"
        "2. Manter o tema central do grupo, Software Livre.\n"
        "3. Evitar Flood (sequência de  mensagens repetidas.\n"
        "4. Não é tolerado nenhum tipo de assédio, discriminação, falta "
        "de respeito ou humilhação entre os membros.\n"
        "5. Não compartilhar conteúdo sem autorização ou que a licença não"
        " permita.\n"
        "6. Evitar postagens de cunho comercial, venda de produtos e "
        "serviços, e outros tipos de ações correlacionadas. Não é "
        "proibido, mas peça permissão aos administradores antes.\n"
        "7. Proibido envio de vídeos ou imagens pornográficas ou de "
        "conteúdo de cunho sexual.\n"
        "8. Evitar fazer flood conversando com o potilivre_bot\n"
        "9. Proibido adicionar bots no grupo.\n\n"
        "Havendo qualquer restrição as regras, o usuário será banido."
        )
    update.message.reply_text(message_rules)


def description(bot, update):
    """Send a message with the group description."""
    message_description = (
        "PotiLivre é a Comunidade Potiguar de Software Livre, fundada em 2013."
        " Somos uma organização independente, composta por voluntários, para"
        " apoiar à filosofia e o uso do Software Livre."
        )
    update.message.reply_text(message_description)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    """Start the bot."""
    updater = Updater(environ['TOKEN'])
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("regras", rules))
    dp.add_handler(CommandHandler("descricao", description))
    dp.add_handler(CommandHandler("ajuda", help))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, welcome))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
