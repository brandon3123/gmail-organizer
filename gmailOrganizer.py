from services.EmailDeletingService import EmailDeletingService
from utils.ProgressBarUtil import ProgressBarUtil
from services.EmailSortingService import EmailSortingService

sorting_service = EmailSortingService()
deletion_service = EmailDeletingService()

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