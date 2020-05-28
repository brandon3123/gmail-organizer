from apiRoutes.EmailApi import EmailApi
from utils.FilterUtil import FilterUtil
from enums.Label import Label
from enums.Category import Category

email_api = EmailApi()


class EmailService:

    def get_promotions(self):
        filter = FilterUtil.category(Category.PROMOTIONS.value)
        return self.fetch_email_ids_matching_criteria(filter)

    def get_socials(self):
        filter = FilterUtil.category(Category.SOCIAL.value)
        return self.fetch_email_ids_matching_criteria(filter)

    def delete_emails(self, email_ids):
        if len(email_ids) > 0:
            return email_api.delete_emails(email_ids)
        else:
            return []

    def move_unread_inbox_emails_to_trash(self):
        filter = FilterUtil.in_folder(Label.UNREAD.value)
        unread_email_ids = self.email_ids_with_criteria_inside_inbox(filter)
        if len(unread_email_ids) > 0:
            self.move_to_tash(unread_email_ids)
        return len(unread_email_ids)

    def email_ids_with_criteria_inside_inbox(self, criteria):
        filter = criteria + ' ' + FilterUtil.in_folder(Label.INBOX.value)
        emails = self.emails_matching_criteria(filter)
        return self.id_array_from_emails(emails)

    def emails_from_inside_inbox(self, from_email):
        filter = FilterUtil.from_email_with_label(from_email, Label.INBOX.value)
        return self.emails_matching_criteria(filter)

    def emails_from_with_label(self, from_email, label):
        filter = FilterUtil.from_email_with_label(from_email, label)
        return self.emails_matching_criteria(filter)

    def emails_from(self, from_email):
        filter = FilterUtil.from_email(from_email)
        return self.emails_matching_criteria(filter)

    def get_email(self, id):
        return email_api.get_email(id)

    def edit_labels(self, email_id, to_add, to_remote):
        return email_api.edit_labels(email_id, to_add, to_remote)

    def fetch_email_ids_from_sender(self,
                                    from_email):
        emails_found = self.emails_from_inside_inbox(from_email)
        return self.id_array_from_emails(emails_found)

    def fetch_email_ids_matching_criteria(self,
                                          criteria):
        emails_found = self.emails_matching_criteria(criteria)
        return self.id_array_from_emails(emails_found)

    def add_emails_to_labels_and_remove_from_inbox(self,
                                                   email_ids,
                                                   label_ids):
        return email_api.edit_labels_for_email_ids(email_ids, label_ids, [Label.INBOX.value])

    def move_to_tash(self, email_ids):
        return email_api.edit_labels_for_email_ids(email_ids, [Label.TRASH.value], [Label.INBOX.value])

    def emails_matching_criteria(self, criteria):
        return email_api.emails_matching_criteria(criteria)

    def sender(self, email):
        headers = email['payload']['headers']
        from_header = self.header_value(headers, 'From')
        return from_header

    def sender_name(self, message):
        sender_header = self.sender(message)
        return sender_header.split('<')[0][0:-1]

    def header_value(self, headers, header_name):
        for header in headers:
            if header['name'] == header_name:
                return header['value']
        return None

    def id_array_from_emails(self, emails):
        return list(map(lambda i: i['id'], emails))
