from services.LabelService import LabelService
from services.MessageService import MessageService
from enums.Email import Email
from enums.Label import Label

message_service = MessageService()
label_service = LabelService()


class EmailSortingService:

    def sort_job_postings(self):
        self.__sort_emails(Email.INDEED.value, Label.JOB_POSTINGS.value, Label.INDEED.value)
        self.__sort_emails(Email.WORKOPOLIS.value, Label.JOB_POSTINGS.value, Label.WORKOPOLIS.value)
        self.__sort_emails(Email.NEUVOO.value, Label.JOB_POSTINGS.value, Label.NEUVOO.value)
        self.__sort_emails(Email.GLASS_DOOR.value, Label.JOB_POSTINGS.value, Label.GLASS_DOOR.value)

    def sort_money_transfers(self):
        self.__sort_emails(Email.E_TRANSFER.value, Label.E_TRANSFERS.value)

    def __sort_emails(self, from_email, parent_label_name, label_name=None):
        emails = message_service.messages_from(from_email)
        # User the below when not testing.
        # emails = message_service.messages_from_inside_inbox(from_email)

        if len(emails) > 0:
            labels = label_service.all_labels()
            parent_label = label_service.label_with_name(labels, parent_label_name)

            emails = [emails[0]]
            for email in emails:
                email_id = email['id']
                message = message_service.get_message(email_id)

                if label_name is None:
                    label_name = message_service.sender(message)[:-(len(from_email) + 3)]

                prefix = label_service.name(parent_label) + '/'
                full_label_name = prefix + label_name

                label = label_service.label_with_name(labels, full_label_name)

                if label is None:
                    bg_color = label_service.bg_color(parent_label)
                    text_color = label_service.text_color(parent_label)

                    label = label_service.create_label_with_color(full_label_name, bg_color, text_color)

                message_service.edit_labels(email_id, [label['id']], [Label.INBOX.value])
