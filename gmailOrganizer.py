from services.EmailDeletingService import EmailDeletingService
from utils.ProgressBarUtil import ProgressBarUtil
from services.EmailSortingService import EmailSortingService

sorting_service = EmailSortingService()
deletion_service = EmailDeletingService()

def main():
    ProgressBarUtil.start_progress()
    sorting_service.sort_receipts()
    sorting_service.sort_job_postings()
    sorting_service.sort_money_transfers()
    sorting_service.sort_online_orders()
    sorting_service.sort_rentals()
    sorting_service.sort_google_emails()
    deletion_service.delete_emails()
    ProgressBarUtil.end_progress()

if __name__ == '__main__':
    main()