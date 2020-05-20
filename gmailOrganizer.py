from services.EmailDeletingService import EmailDeletingService
from utils.ProgressBarUtil import ProgressBarUtil
from services.EmailSortingService import EmailSortingService
from enums.Email import Email


sorting_service = EmailSortingService()
deletion_service = EmailDeletingService()

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
    sorting_service.sort_money_transfers()
    sorting_service.sort_online_orders()
    sorting_service.sort_rentals()
    sorting_service.delete_promotions()
    sorting_service.delete_social()
    deletion_service.delete_emails()
    ProgressBarUtil.end_progress()
    # sorting_service.delete_emails_from(TO_DELETE_FROM)

if __name__ == '__main__':
    main()