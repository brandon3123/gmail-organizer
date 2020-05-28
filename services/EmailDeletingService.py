from services.EmailService import EmailService
from utils.FilterUtil import FilterUtil
from enums.Subject import Subject
from enums.Email import Email
from utils.ProgressBarUtil import ProgressBarUtil

message_service = EmailService()


class EmailDeletingService:

    def delete_emails(self):
        unread_emails_trashed_amount = message_service.move_unread_inbox_emails_to_trash()
        ProgressBarUtil.update_progress('Unread emails moved to trash: ', unread_emails_trashed_amount)
        promotion_emails_amount = self.__delete_promotions()
        ProgressBarUtil.update_progress('Promotions delete: ', promotion_emails_amount)
        social_emails_amount = self.__delete_social()
        ProgressBarUtil.update_progress('Social delete: ', social_emails_amount)

    def __delete_promotions(self):
        promotion_emails = message_service.get_promotions()
        if len(promotion_emails) > 0:
            message_service.delete_emails(promotion_emails)
        return len(promotion_emails)

    def __delete_social(self):
        social_emails = message_service.get_socials()
        if len(social_emails) > 0:
            message_service.delete_emails(social_emails)
        return len(social_emails)

    def __email_ids_from_senders(self):
        to_delete_from = [
            Email.LINKEDIN_DOMAIN.value,
            Email.SAIT_ALUMNI.value,
            Email.COURSERA_NO_REPLY.value,
            Email.TILE_NO_REPLY.value,
            Email.TURBO_TAX.value,
            Email.GITHUB_NO_REPLY.value,
            Email.GITHUB_NOTIFICATIONS.value,
            Email.RBC_DIRECT_NO_REPLY.value,
            Email.FREELANCER_NO_REPLY.value,
            Email.STACK_OVERFLOW_NO_REPLY.value,
            Email.CLOUD_GURUR_DOMAIN.value,
            Email.PRIME_NO_REPLY.value,
            Email.GOOGLE_CALENDAR.value,
            Email.DIGITAL_OCEAN.value
        ]

        email_ids_to_delete = list()

        for email in to_delete_from:
            filter = FilterUtil.from_email(email)
            found_emails = message_service.email_ids_with_criteria_inside_inbox(filter)
            email_ids_to_delete += found_emails

        return email_ids_to_delete

    def __email_ids_with_subject(self):
        to_delete_subjects = [
            Subject.RBC_E_STATEMENT.value
        ]

        email_ids_to_delete = list()

        for email in to_delete_subjects:
            filter = FilterUtil.subject(email)
            found_emails = message_service.email_ids_with_criteria_inside_inbox(filter)
            email_ids_to_delete += found_emails

        return email_ids_to_delete
