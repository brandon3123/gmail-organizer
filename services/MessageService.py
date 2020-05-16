from apiRoutes.Messages import Messages
from services.FilterService import FilterService
from enums.Label import Label
from enums.Category import Category

messages_api = Messages()
filter_service = FilterService()


class MessageService:

    def get_promotions(self):
        filter = filter_service.category(Category.PROMOTIONS.value)
        return self.messages_with_criteria(filter)

    def delete_messages(self, message_ids):
        return messages_api.delete_messages(message_ids)

    def messages_from_inside_inbox(self, from_email):
        filter = filter_service.from_email_with_label(from_email, Label.INBOX.value)
        return self.messages_with_criteria(filter)

    def messages_from_with_label(self, from_email, label):
        filter = filter_service.from_email_with_label(from_email, label)
        return self.messages_with_criteria(filter)

    def messages_from(self, from_email):
        filter = filter_service.from_email(from_email)
        return self.messages_with_criteria(filter)

    def get_message(self, id):
        return messages_api.get_message(id)

    def edit_labels(self, message_id, to_add, to_remote):
        return messages_api.edit_labels(message_id, to_add, to_remote)

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
