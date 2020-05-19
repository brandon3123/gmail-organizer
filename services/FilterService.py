from enums.Filter import Filter


class FilterService:

    def from_email_with_label(self, from_email, label):
        return self.from_email(from_email) + ' ' + Filter.LABEL.value + label

    def from_email(self, from_email):
        return Filter.FROM.value + from_email

    def in_folder(self, folder_name):
        return Filter.IN.value + folder_name

    def category(self, category):
        return Filter.CATEGORY.value + category
