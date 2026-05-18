class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content


class PdfReportGenerator:
    def generate(self, report):
        print(f"PDF generated for {report.title}")


class ReportSaver:
    def save(self, filename):
        print(f"Saved {filename}")