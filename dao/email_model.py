from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError


from db.db import *# Ensure Base and Emails are imported from your db module
from models.models import Emails


class Email:
    __session = None
    __conn = None
    def __init__(self):
        self.__conn = Db().make_connection()
        self.__engine = create_engine(self.__conn, echo=False)
        Base.metadata.create_all(self.__engine)  # Ensure tables are created
        Session = sessionmaker(bind=self.__engine)

        self.__session = Session()

    def save_data(self, from_email, to_email, mail_text,sent_date,subject):
        """
        Saves an email record to the emails table.

        :param mail_id: Unique identifier for the email
        :param from_email: Sender's
        ession = sessionmaker(bind=self.__email address
        :param to_email: Recipient's email address
        :param mail_text: Content of the email
        :return: The saved Emails object or None if failed
        """
        try:
            # Create an instance of Emails with the provided data
            new_email = Emails(
                from_email=from_email,
                to_email=to_email,
                mail_text=mail_text,
                sent_date = sent_date,
                subject = subject
            )

            # Add the new email to the session
            self.__session.add(new_email)

            # Commit the transaction
            self.__session.commit()

            print(f"Email with mail_id saved successfully.")
            return new_email
        except SQLAlchemyError as e:
            # Rollback the session in case of error
            self.__session.rollback()
            print(f"Error saving email: {e}")
            return None
        finally:
            # Optionally, close the session if you don't need it anymore
            self.__session.close()

    def __del__(self):
        pass
