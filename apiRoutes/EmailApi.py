from __future__ import print_function
from apiRoutes.ApiRoute import ApiRoute
from email.mime.text import MIMEText
import base64


class EmailApi(ApiRoute):

    def edit_labels_for_email_ids(self,
                                  email_ids,
                                  to_add,
                                  to_remove):
        if len(email_ids) > 1000:
            email_batch = [email_ids[x:x + 1000] for x in range(0, len(email_ids), 1000)]
            response = ''
            for chunk in email_batch:
                payload = self.__batch_email_labels_json(chunk, to_add, to_remove)
                response += self.api().batchModify(userId='me', body=payload).execute()
            return response
        else:
            payload = self.__batch_email_labels_json(email_ids, to_add, to_remove)
            return self.api().batchModify(userId='me', body=payload).execute()

    def delete_emails(self, email_ids):
        return self.api().batchDelete(userId='me', body={'ids': email_ids}).execute()

    def edit_labels(self, id, to_add, to_remove):
        payload = self.__labels_json(to_add, to_remove)
        return self.api().modify(userId='me', id=id, body=payload).execute()

    def emails_matching_criteria(self, criteria):
        results = self.api().list(userId='me', q=criteria).execute()
        emails = list()
        if self.__is_not_empty(results):
            emails += results['messages']
            while self.__has_next_page(results):
                results = self.api().list(userId='me', q=criteria, pageToken=results['nextPageToken']).execute()
                emails += results['messages']
            return emails
        else:
            return []

    def get_all_emails(self):
        return self.api().list(userId='me').execute()

    def get_email(self, id):
        return self.api().get(userId='me', id=id).execute()

    def api(self):
        return super().gmail_api().users().messages()

    def __email_json(self, sender, to, subject, text):
        """Create a message for an email.

        Args:
          sender: Email address of the sender.
          to: Email address of the receiver.
          subject: The subject of the email message.
          text: The text of the email message.

        Returns:
          An object containing a base64url encoded email object.
        """
        email = MIMEText(text)
        email['To'] = to
        email['From'] = sender
        email['Subject'] = subject
        return {'raw': base64.urlsafe_b64encode(email.as_string())}

    def __batch_email_labels_json(self, message_ids, add=[], remove=[]):
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
