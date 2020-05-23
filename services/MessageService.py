from apiRoutes.Messages import Messages
from utils.FilterUtil import FilterUtil
from enums.Label import Label
from enums.Category import Category

messages_api = Messages()


class MessageService:

    def get_promotions(self):
        filter = FilterUtil.category(Category.PROMOTIONS.value)
        return self.fetch_email_ids_matching_criteria(filter)

    def get_socials(self):
        filter = FilterUtil.category(Category.SOCIAL.value)
        return self.fetch_email_ids_matching_criteria(filter)

    def delete_messages(self, message_ids):
        if len(message_ids > 0):
            return messages_api.delete_messages(message_ids)
        else:
            return None

    def message_ids_with_criteria_inside_inbox(self, criteria):
        filter = criteria + FilterUtil.in_folder(Label.INBOX.value)
        messages = self.messages_with_criteria(filter)
        return self.id_array_from_messages(messages)

    def messages_from_inside_inbox(self, from_email):
        filter = FilterUtil.from_email_with_label(from_email, Label.INBOX.value)
        return self.messages_with_criteria(filter)

    def messages_from_with_label(self, from_email, label):
        filter = FilterUtil.from_email_with_label(from_email, label)
        return self.messages_with_criteria(filter)

    def messages_from(self, from_email):
        filter = FilterUtil.from_email(from_email)
        return self.messages_with_criteria(filter)

    def get_message(self, id):
        return messages_api.get_message(id)

    def edit_labels(self, message_id, to_add, to_remote):
        return messages_api.edit_labels(message_id, to_add, to_remote)

    def fetch_email_ids_from_sender(self,
                                    from_email):
        emails_found = self.messages_from_inside_inbox(from_email)
        return self.id_array_from_messages(emails_found)

    def fetch_email_ids_matching_criteria(self,
                                    criteria):
        emails_found = self.messages_with_criteria(criteria)
        return self.id_array_from_messages(emails_found)

    def add_messages_to_labels_and_remove_from_inbox(self,
                                    message_ids,
                                    label_ids):
        return messages_api.edit_labels_for_message_ids(message_ids, label_ids, [Label.INBOX.value])

    def move_to_tash(self, message_ids):
        return messages_api.edit_labels_for_message_ids(message_ids, [Label.TRASH.value], [Label.INBOX.value])

    def messages_with_criteria(self, criteria):
        return messages_api.messages_with_criteria(criteria)

    def sender(self, message):
        headers = message['payload']['headers']
        from_header = self.header_value(headers, 'From')
        return from_header

    def header_value(self, headers, header_name):
        for header in headers:
            if header['name'] == header_name:
                return header['value']
        return None

    def id_array_from_messages(self, messages):
        return list(map(lambda i: i['id'], messages))
