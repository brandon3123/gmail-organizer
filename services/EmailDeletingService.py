from services.MessageService import MessageService
from utils.FilterUtil import FilterUtil
from enums.Subject import Subject
from utils.ProgressBarUtil import ProgressBarUtil

message_service = MessageService()


class EmailDeletingService:

    def delete_emails(self):
        # Delete e-statement notifications from RBC
        rbc_e_statement_alerts = message_service.message_ids_with_criteria_inside_inbox(
            FilterUtil.subject(Subject.RBC_E_STATEMENT.value)
        )
        self.__delete_emails(rbc_e_statement_alerts)

    def __delete_emails(self, email_ids):
        if len(email_ids) > 0:
            message_service.delete_messages(email_ids)
        ProgressBarUtil.update_progress()
