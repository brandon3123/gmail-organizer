from enums.Filter import Filter


class FilterUtil:

    @staticmethod
    def from_email_with_label(from_email, label):
        return FilterUtil.from_email(from_email) + ' ' + Filter.LABEL.value + label

    @staticmethod
    def from_email(from_email):
        return Filter.FROM.value + from_email

    @staticmethod
    def in_folder(folder_name):
        return Filter.IN.value + folder_name

    @staticmethod
    def category(category):
        return Filter.CATEGORY.value + category

    @staticmethod
    def subject(subject):
        return Filter.SUBJECT.value + subject

