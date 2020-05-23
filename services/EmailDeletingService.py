from services.MessageService import MessageService
from utils.FilterUtil import FilterUtil
from enums.Subject import Subject
from enums.Email import Email
from utils.ProgressBarUtil import ProgressBarUtil

message_service = MessageService()



class EmailDeletingService:

    def delete_emails(self):
        emails_ids_to_delete = self.__email_ids_from_senders()
        message_service.delete_messages(emails_ids_to_delete)
        ProgressBarUtil.update_progress()

    def __email_ids_from_senders(self):
        TO_DELETE_FROM = [
            Email.LINKEDIN_DOMAIN.value,
            Email.SAIT_ALUMNI.value,
            Email.COURSERA_NO_REPLY.value,
            Email.TILE_NO_REPLY.value,
            Email.TURBO_TAX.value,
            Email.GITHUB_NO_REPLY.value,
            Email.GITHUB_NOTIFICATIONS.value,
            Email.RBC_DIRECT_NO_REPLY.value,
            Email.FREELANCER_NO_REPLY.value
        ]

        email_ids_to_delete = list()

        for email in TO_DELETE_FROM:
            filter = FilterUtil.from_email(Email.FREELANCER_NO_REPLY.value)
            found_emails = message_service.message_ids_with_criteria_inside_inbox(filter)
            email_ids_to_delete += found_emails

        return email_ids_to_delete

    def __email_ids_with_subject(self):
        TO_DELETE_SUBJECTS = [
            Subject.RBC_E_STATEMENT.value
        ]

        email_ids_to_delete = list()

        for email in TO_DELETE_FROM:
            filter = FilterUtil.from_email(Email.FREELANCER_NO_REPLY.value)
            found_emails = message_service.message_ids_with_criteria_inside_inbox(filter)
            email_ids_to_delete += found_emails

        return email_ids_to_delete

