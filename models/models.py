# coding: utf-8
from sqlalchemy import BigInteger, CHAR, Column, Date, Enum, ForeignKey, Index, Integer, String, TIMESTAMP, Text, Time, text,VARCHAR
from sqlalchemy.dialects.mysql import INTEGER, TINYINT,BIGINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import LONGTEXT

Base = declarative_base()
metadata = Base.metadata


class Emails(Base):
    __tablename__ = 'emails'

    id = Column(INTEGER, primary_key=True)
    mail_id = Column(VARCHAR(40), nullable=False, server_default=text("''"))
    from_email = Column(VARCHAR(40), nullable=False, server_default=text("''"))
    to_email = Column(VARCHAR(40), nullable=False, server_default=text("''"))
    mail_text = Column(VARCHAR(500), nullable=False, server_default=text("''"))
    subject = Column(VARCHAR(500), nullable=False, server_default=text("''"))
    sent_date = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

