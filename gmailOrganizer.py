from utils.ProgressBarUtil import ProgressBarUtil
from services.EmailSortingService import EmailSortingService
from services.LabelService import LabelService
from enums.Email import Email
from services.MessageService import MessageService


label_service = LabelService()
sorting_service = EmailSortingService()
message_service = MessageService()

TO_DELETE_FROM = [
    Email.LINKEDIN_DOMAIN.value,
    Email.SAIT_ALUMNI.value,
    Email.COURSERA_NO_REPLY.value,
    Email.TILE_NO_REPLY.value,
    Email.TURBO_TAX.value,
    Email.GITHUB_NO_REPLY.value,
    Email.GITHUB_NOTIFICATIONS.value
]

def main():
    ProgressBarUtil.start_progress()
    sorting_service.sort_job_postings()
    sorting_service.sort_online_orders()
    sorting_service.sort_rentals()
    sorting_service.delete_promotions()
    sorting_service.delete_social()
    ProgressBarUtil.end_progress()
    # sorting_service.delete_emails_from(TO_DELETE_FROM)

if __name__ == '__main__':
    main()