from __future__ import print_function
from apiRoutes.ApiRoute import ApiRoute
import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import os

from apiclient import errors


class Messages(ApiRoute):

    def edit_labels(self, id, to_add, to_remove):
        payload = self.labels_json(to_add, to_remove)
        return self.api().modify(userId='me', id=id, body=payload).execute()

    def messages_with_criteria(self, criteria):
        return self.api().list(userId='me', q=criteria).execute()['messages']

    def get_all_messages(self):
        return self.api().list(userId='me').execute()

    def get_message(self, id):
        return self.api().get(userId='me', id=id).execute()

    def send_message(self, to, subject, body):
        message = self.message_json(to, subject, body)

        message = self.api().send(userId='jodieemaee@gmail.com', body=message).execute()
        return message

    def api(self):
        return super().gmail_api().users().messages()

    def message_json(self, sender, to, subject, message_text):
        """Create a message for an email.

        Args:
          sender: Email address of the sender.
          to: Email address of the receiver.
          subject: The subject of the email message.
          message_text: The text of the email message.

        Returns:
          An object containing a base64url encoded email object.
        """
        message = MIMEText(message_text)
        message['To'] = to
        message['From'] = sender
        message['Subject'] = subject
        return {'raw': base64.urlsafe_b64encode(message.as_string())}

    def labels_json(self, add=[], remove=[]):
        """Create object to update labels.

        Returns:
          A label update object.
        """
        return {'removeLabelIds': remove, 'addLabelIds': add}
