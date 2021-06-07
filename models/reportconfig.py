
class ReportConfig:

    reportId = None
    reportName = None
    embedUrl = None
    datasetId = None
    pageName = None

    def __init__(self, report_id, report_name, embed_url, dataset_id = None, page_name = None):
        self.reportId = report_id
        self.reportName = report_name
        self.embedUrl = embed_url
        self.datasetId = dataset_id
        self.pageName = page_name
