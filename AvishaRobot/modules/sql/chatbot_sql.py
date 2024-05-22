import threading

from sqlalchemy import Column, String

from AvishaRobot.modules.sql import BASE, SESSION


class AvishaChats(BASE):
    __tablename__ = "avisha_chats"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


AvishaChats.__table__.create(checkfirst=True)
INSERTION_LOCK = threading.RLock()


def is_avisha(chat_id):
    try:
        chat = SESSION.query(AvishaChats).get(str(chat_id))
        return bool(chat)
    finally:
        SESSION.close()


def set_avisha(chat_id):
    with INSERTION_LOCK:
        avishachat = SESSION.query(AvishaChats).get(str(chat_id))
        if not avishachat:
            avishachat = AvishaChats(str(chat_id))
        SESSION.add(avishachat)
        SESSION.commit()


def rem_avisha(chat_id):
    with INSERTION_LOCK:
        avishachat = SESSION.query(avishaChats).get(str(chat_id))
        if avishachat:
            SESSION.delete(avishachat)
        SESSION.commit()
      
