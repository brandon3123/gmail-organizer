from __future__ import print_function
from apiRoutes.ApiRoute import ApiRoute
from email.mime.text import MIMEText
import base64


class Messages(ApiRoute):

    def edit_labels_for_message_ids(self,
                                    message_ids,
                                    to_add,
                                    to_remove):
        if len(message_ids) > 1000:
            message_chunks = [message_ids[x:x + 1000] for x in range(0, len(message_ids), 1000)]
            response = ''
            for chunk in message_chunks:
                payload = self.__batch_message_labels_json(chunk, to_add, to_remove)
                response += self.api().batchModify(userId='me', body=payload).execute()
            return response
        else:
            payload = self.__batch_message_labels_json(message_ids, to_add, to_remove)
            return self.api().batchModify(userId='me', body=payload).execute()


    def delete_messages(self, message_ids):
        return self.api().batchDelete(userId='me', body={'ids': message_ids}).execute()

    def edit_labels(self, id, to_add, to_remove):
        payload = self.__labels_json(to_add, to_remove)
        return self.api().modify(userId='me', id=id, body=payload).execute()

    def messages_with_criteria(self, criteria):
        results = self.api().list(userId='me', q=criteria).execute()
        messages = list()
        if self.__is_not_empty(results):
            messages += results['messages']
            while self.__has_next_page(results):
                results = self.api().list(userId='me', q=criteria, pageToken=results['nextPageToken']).execute()
                messages += results['messages']
            return messages
        else:
            return []

    def get_all_messages(self):
        return self.api().list(userId='me').execute()

    def get_message(self, id):
        return self.api().get(userId='me', id=id).execute()

    def send_message(self, to, subject, body):
        message = self.__message_json(to, subject, body)

        message = self.api().send(userId='jodieemaee@gmail.com', body=message).execute()
        return message

    def api(self):
        return super().gmail_api().users().messages()

    def __message_json(self, sender, to, subject, message_text):
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

    def __batch_message_labels_json(self, message_ids, add=[], remove=[]):
        """Create object to update labels.

        Returns:
          A label update object.
        """
        return {'ids': message_ids, 'removeLabelIds': remove, 'addLabelIds': add}

    def __labels_json(self, add=[], remove=[]):
        """Create object to update labels.

        Returns:
          A label update object.
        """
        return {'removeLabelIds': remove, 'addLabelIds': add}

    def __is_not_empty(self, results):
        return results['resultSizeEstimate'] > 0

    def __has_next_page(self, results):
        has_next_page = 'nextPageToken' in results
        return has_next_page
