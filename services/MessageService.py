from apiRoutes.Messages import Messages
from services.LabelService import LabelService

messages_api = Messages()
label_service = LabelService()


class MessageService:

    def sort_transfers(self):
        e_transfer_email = 'catch@payments.interac.ca'
        e_transfers = messages_api.messages_with_criteria('from:' + e_transfer_email)

        e_transfers = [e_transfers[0]]
        if len(e_transfers) > 0:
            labels = label_service.all_labels()
            e_transfer_parent_label = label_service.label_with_name(labels, 'E- Transfers')

            for transfer_data in e_transfers:
                message = messages_api.get_message(transfer_data['id'])

                from_header = self.sender(message)[:-(len(e_transfer_email) + 3)]

                prefix = label_service.name(e_transfer_parent_label) + '/'
                transfer_label_name = prefix + from_header + ' e-transfers'

                label = label_service.label_with_name(labels, transfer_label_name)

                if label is None:
                    bg_color = label_service.bg_color(e_transfer_parent_label)
                    text_color = label_service.text_color(e_transfer_parent_label)

                    label = label_service.create_label_with_color(transfer_label_name, bg_color, text_color)
                    # label = label_service.update_label(label['id'], bg_color, text_color)

                print(label)



    def sender(self, message):
        headers = message['payload']['headers']
        from_header = self.header_value(headers, 'From')
        return from_header

    def header_value(self, headers, header_name):
        for header in headers:
            if header['name'] == header_name:
                return header['value']
        return None
