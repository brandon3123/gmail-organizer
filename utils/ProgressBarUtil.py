import progressbar


class ProgressBarUtil:
    bar = None
    progress = 0

    @staticmethod
    def start_progress():
        # ProgressBarUtil.bar = progressbar.ProgressBar().start()
        ProgressBarUtil.bar = progressbar.ProgressBar(max_value=8, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        ProgressBarUtil.bar.start()

    @staticmethod
    def update_progress():
        ProgressBarUtil.bar.update(ProgressBarUtil.progress)
        ProgressBarUtil.progress += 1

    @staticmethod
    def end_progress():
        ProgressBarUtil.bar.finish()
