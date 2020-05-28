import progressbar


class ProgressBarUtil:
    bar = None
    progress = 1

    @staticmethod
    def start_progress():
        ProgressBarUtil.bar = progressbar.ProgressBar(max_value=15, redirect_stdout=True,
                                                      widgets=[progressbar.Bar('=', '[', ']'), ' ',
                                                               progressbar.Percentage()])
        ProgressBarUtil.bar.start()

    @staticmethod
    def update_progress(message, amount_sorted):
        print(message, amount_sorted)
        ProgressBarUtil.bar.update(ProgressBarUtil.progress)
        ProgressBarUtil.progress += 1

    @staticmethod
    def end_progress():
        ProgressBarUtil.bar.finish()
