from enums.Filter import Filter


class FilterService:

    def from_email_with_label(self, from_email, label):
        return self.from_email(from_email) + ' and ' + Filter.LABEL.value + label

    def from_email(self, from_email):
        return Filter.FROM.value + from_email
