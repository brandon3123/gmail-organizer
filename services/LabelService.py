from apiRoutes.Labels import Labels

label_api = Labels()


class LabelService:

    def all_labels(self):
        return label_api.get_all_labels()

    def create_label(self, name):
        return label_api.create_label(name)

    def create_label_with_color(self, name, bg_color, text_color):
        return label_api.create_label_with_color(name, bg_color, text_color)

    def label_with_name(self, labels, name):
        for label in labels:
            if label['name'] == name:
                return label
        return None

    def name(self, label):
        return label['name']

    def bg_color(self, label):
        return str(self.color(label)['backgroundColor'])

    def color(self, label):
        return label['color']

    def text_color(self, label):
        return str(self.color(label)['textColor'])
