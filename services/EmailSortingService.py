from services.LabelService import LabelService
from services.MessageService import MessageService
from enums.Email import Email
from enums.Label import Label
from enums.Color import Color

message_service = MessageService()
label_service = LabelService()


class EmailSortingService:

    def sort_job_postings(self):
        self.__sort_emails(Email.INDEED.value, Label.JOB_POSTINGS.value, Label.INDEED.value, Color.BRIGHT_RED.value)
        # self.__sort_emails(Email.WORKOPOLIS.value, Label.JOB_POSTINGS.value, Label.WORKOPOLIS.value)
        # self.__sort_emails(Email.NEUVOO.value, Label.JOB_POSTINGS.value, Label.NEUVOO.value)
        # self.__sort_emails(Email.GLASS_DOOR.value, Label.JOB_POSTINGS.value, Label.GLASS_DOOR.value)

    def sort_money_transfers(self):
        self.__sort_emails(Email.E_TRANSFER.value, Label.E_TRANSFERS.value)

    def sort_amazon_orders(self):
        self.__sort_emails_one_label(Email.AMAZON_DOMAIN.value, Label.AMAZON.value, Color.AMAZON_ORANGE.value)

    def sort_rentals(self):
        self.__sort_emails(Email.RENT_FASTER.value, Label.RENTALS.value, Label.RENT_FASTER.value, Color.ROYAL_BLUE.value)

    def delete_emails_from(self, from_emails):
        if len(from_emails) > 0:
            for sender in from_emails:
                print(sender)
                self.__move_emails_from_sender_to_trash(sender)

    def delete_promotions(self):
        promotion_emails = message_service.get_promotions()
        while len(promotion_emails) > 0:
            message_ids = message_service.id_array_from_messages(promotion_emails)
            message_service.delete_messages(message_ids)
            promotion_emails = message_service.get_promotions()

    def __move_messages_to_trash(self, email_ids):
        message_service.move_to_tash(email_ids)

    def __move_emails_from_sender_to_trash(self, from_email):
        emails = message_service.messages_from(from_email)
        # User the below when not testing.
        # emails = message_service.messages_from_inside_inbox(from_email)

        if len(emails) > 0:
            emails = [emails[0]]
            for email in emails:
                email_id = email['id']

                # Move current email to the trash
                self.__move_messages_to_trash([email_id])


    def __sort_emails_one_label(self,
                                from_email,
                                parent_label_name,
                                label_color=None):
        # Fetch emails
        emails = message_service.messages_from(from_email)
        # User the below when not testing.
        # emails = message_service.messages_from_inside_inbox(from_email)

        emails = [emails[0]]
        if len(emails) > 0:
            # Fetch all labels
            labels = label_service.all_labels()
            parent_label = label_service.label_with_name(labels, parent_label_name)

            # No parent label with provided name, need to create it.
            if parent_label is None:
                parent_label = label_service.create_label_with_color(parent_label_name, label_color, label_color)

            emails = [emails[0]]
            for email in emails:
                email_id = email['id']

                # Move current email to the label, and remove it from the inbox.
                message_service.edit_labels(email_id, [parent_label['id']], [Label.INBOX.value])

    def __sort_emails(self,
                      from_email,
                      parent_label_name,
                      label_name=None,
                      label_color=None):
        # Fetch emails
        emails = message_service.messages_from(from_email)
        # User the below when not testing.
        # emails = message_service.messages_from_inside_inbox(from_email)

        emails = [emails[0]]
        if len(emails) > 0:
            # Fetch all labels
            labels = label_service.all_labels()
            parent_label = label_service.label_with_name(labels, parent_label_name)

            # No parent label with provided name, need to create it.
            if parent_label is None:
                parent_label = label_service.create_label_with_color(parent_label_name, label_color, label_color)

            emails = [emails[0]]
            for email in emails:
                email_id = email['id']
                message = message_service.get_message(email_id)

                # If no label is specified, use the senders name as the label.
                if label_name is None:
                    label_name = message_service.sender(message)[:-(len(from_email) + 3)]

                prefix = label_service.name(parent_label) + '/'
                full_label_name = prefix + label_name

                label = label_service.label_with_name(labels, full_label_name)

                # No label with provided name, need to create it.
                if label is None:
                    bg_color = label_service.bg_color(parent_label)
                    text_color = label_service.text_color(parent_label)

                    label = label_service.create_label_with_color(full_label_name, bg_color, text_color)

                # Move current email to the label, and remove it from the inbox.
                message_service.edit_labels(email_id, [label['id']], [Label.INBOX.value])
