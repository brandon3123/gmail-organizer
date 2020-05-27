from services.LabelService import LabelService
from services.MessageService import MessageService
from enums.Email import Email
from enums.Label import Label
from enums.Color import Color
from enums.Subject import Subject
from utils.FilterUtil import FilterUtil
from utils.ProgressBarUtil import ProgressBarUtil

message_service = MessageService()
label_service = LabelService()


class EmailSortingService:

    def sort_receipts(self):
        receipts_sorted = self.__sort_emails_with_subject_with_parent_label_to_sender(Subject.RECEIPT.value, Label.RECEIPTS.value, Color.BRIGHT_RED.value)
        ProgressBarUtil.update_progress('\r' + Label.RECEIPTS.value + ' sorted: ', receipts_sorted)

    def sort_job_postings(self):
        indeed_sorted = self.__sort_emails_from_with_parent_label(Email.INDEED.value, Label.JOB_POSTINGS.value, Label.INDEED.value, Color.BRIGHT_RED.value)
        ProgressBarUtil.update_progress(Label.INDEED.value + ' sorted: ', indeed_sorted)

        workopolis_sorted = self.__sort_emails_from_with_parent_label(Email.WORKOPOLIS.value, Label.JOB_POSTINGS.value, Label.WORKOPOLIS.value, Color.BRIGHT_RED.value)
        ProgressBarUtil.update_progress(Label.WORKOPOLIS.value + ' sorted: ', workopolis_sorted)

        neuvoo_sorted = self.__sort_emails_from_with_parent_label(Email.NEUVOO.value, Label.JOB_POSTINGS.value, Label.NEUVOO.value, Color.BRIGHT_RED.value)
        ProgressBarUtil.update_progress(Label.NEUVOO.value + ' sorted: ', neuvoo_sorted)

        glass_door_sorted = self.__sort_emails_from_with_parent_label(Email.GLASS_DOOR.value, Label.JOB_POSTINGS.value, Label.GLASS_DOOR.value, Color.BRIGHT_RED.value)
        ProgressBarUtil.update_progress(Label.GLASS_DOOR.value + ' sorted: ', glass_door_sorted)

    def sort_money_transfers(self):
        money_transfers_sorted = self.__sort_emails(Email.E_TRANSFER.value, Label.E_TRANSFERS.value)
        ProgressBarUtil.update_progress(Label.E_TRANSFERS.value + ' sorted: ', money_transfers_sorted)

    def sort_online_orders(self):
        amazon_sorted = self.__sort_emails_from_with_parent_label(Email.AMAZON_DOMAIN.value,  Label.ONLINE_ORDERS.value, Label.AMAZON.value, Color.AMAZON_ORANGE.value)
        ProgressBarUtil.update_progress(Label.AMAZON.value + ' sorted: ', amazon_sorted)

        intelcom_sorted = self.__sort_emails_from_with_parent_label(Email.INTELCOM_DOMAIN.value,  Label.ONLINE_ORDERS.value, Label.INTELCOM.value, Color.AMAZON_ORANGE.value)
        ProgressBarUtil.update_progress(Label.INTELCOM.value + ' sorted: ', intelcom_sorted)

    def sort_rentals(self):
        rent_faster_sorted = self.__sort_emails_from_with_parent_label(Email.RENT_FASTER.value, Label.RENTALS.value, Label.RENT_FASTER.value, Color.ROYAL_BLUE.value)
        ProgressBarUtil.update_progress(Label.RENT_FASTER.value + ' sorted: ', rent_faster_sorted)

    def sort_google_emails(self):
        google_account_sorted = self.__sort_emails_from_with_parent_label(Email.GOOGLE_SECURITY_ALERTS.value, Label.GOOGLE_ALERTS.value, Label.GOOGLE_ACCOUNT.value, Color.ROYAL_BLUE.value)
        ProgressBarUtil.update_progress(Label.GOOGLE_ALERTS.value + ' (' + Label.GOOGLE_ACCOUNT.value + ') sorted: ',
                                        google_account_sorted)

    def delete_emails_from(self, from_emails):
        if len(from_emails) > 0:
            for sender in from_emails:
                print(sender)
                self.__move_emails_from_sender_to_trash(sender)

    def __move_messages_to_trash(self, email_ids):
        message_service.move_to_tash(email_ids)

    def __move_emails_from_sender_to_trash(self, from_email):
        emails = message_service.messages_from_inside_inbox(from_email)

        if len(emails) > 0:
            for email in emails:
                email_id = email['id']

                # Move current email to the trash
                self.__move_messages_to_trash([email_id])

    def __sort_emails_with_subject_to_working_label(self,
                                             subject,
                                             working_label_name,
                                             label_color=None):
        filter = FilterUtil.subject(subject)
        emails_found = message_service.message_ids_with_criteria_inside_inbox(filter)
        # self.__print_email_amount(emails_found)
        if len(emails_found) > 0:
            working_label = label_service.create_label_if_not_found(working_label_name, label_color)
            if working_label is not None:
                return message_service.add_messages_to_labels_and_remove_from_inbox(emails_found, [working_label['id']])
        else:
            return []

    def __sort_emails_from_to_working_label(self,
                                             from_email,
                                             working_label_name,
                                             label_color=None):
        emails_found = self.__fetch_email_ids_matching_criteria(from_email)
        # self.__print_email_amount(emails_found)
        if len(emails_found) > 0:
            working_label = label_service.create_label_if_not_found(working_label_name, label_color)
            if working_label is not None:
                message_service.add_messages_to_labels_and_remove_from_inbox(emails_found, [working_label['id']])
        return len(emails_found)

    def __sort_emails_with_subject_with_parent_label_to_sender(self,
                                                     subject,
                                                     parent_label_name,
                                                     label_color=None):
        parent_label = label_service.create_label_if_not_found(parent_label_name, label_color)
        sorted_count = 0
        if parent_label is not None:
            filter = FilterUtil.subject(subject)
            emails_found = message_service.message_ids_with_criteria_inside_inbox(filter)
            if len(emails_found) > 0:
                email_dict = {}
                for email_id in emails_found:
                    email = message_service.get_message(email_id)
                    label_name = message_service.sender_name(email)

                    working_label = parent_label_name + '/' + label_name

                    if working_label is not None:
                        if working_label in email_dict:
                            email_dict[working_label].append(email_id)
                        else:
                            email_dict[working_label] = [email_id]

                if len(email_dict) > 0:
                    for sender in email_dict:
                        found_label = label_service.create_label_if_not_found(sender,
                                                                label_color)
                        message_service.add_messages_to_labels_and_remove_from_inbox(email_dict[sender],
                                                                                            [found_label['id']])
                sorted_count += map(lambda email_id_array: len(email_id_array), email_dict.values())
        return sorted_count

    def __sort_emails_with_subject_with_parent_label(self,
                                             subject,
                                             parent_label_name,
                                             working_label_name=None,
                                             label_color=None):
        parent_label = label_service.create_label_if_not_found(parent_label_name, label_color)
        if parent_label is not None:
            self.__sort_emails_with_subject_to_working_label(subject,
                                                     parent_label_name + '/' + working_label_name,
                                                     label_color)
    def __sort_emails_from_with_parent_label(self,
                                             from_email,
                                             parent_label_name,
                                             working_label_name=None,
                                             label_color=None):
        parent_label = label_service.create_label_if_not_found(parent_label_name, label_color)
        if parent_label is not None:
            return self.__sort_emails_from_to_working_label(from_email,
                                                     parent_label_name + '/' + working_label_name,
                                                     label_color)

    def __fetch_email_ids_matching_criteria(self,
                                       from_email):
        return message_service.fetch_email_ids_from_sender(from_email)

    def __sort_emails(self,
                      from_email,
                      parent_label_name,
                      label_color=None):
        # Fetch emails
        emails = message_service.messages_from_inside_inbox(from_email)

        if len(emails) > 0:
            # Fetch all labels

            # No parent label with provided name, need to create it.
            parent_label = label_service.create_label_if_not_found(parent_label_name, label_color, label_color)

            for email in emails:
                email_id = email['id']
                message = message_service.get_message(email_id)

                # If no label is specified, use the senders name as the label.
                label_name = message_service.sender(message)[:-(len(from_email) + 3)]

                prefix = label_service.name(parent_label) + '/'
                full_label_name = prefix + label_name

                # No label with provided name, need to create it.
                bg_color = label_service.bg_color(parent_label)
                text_color = label_service.text_color(parent_label)

                label = label_service.create_label_if_not_found(full_label_name, bg_color, text_color)

                # Move current email to the label, and remove it from the inbox.
                message_service.edit_labels(email_id, [label['id']], [Label.INBOX.value])
        return len(emails)
