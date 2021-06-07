
class EmbedTokenRequestBody:

    datasets = None
    reports = None
    targetWorkspaces = None
    identities = None

    def __init__(self):
        self.datasets = []
        self.reports = []
        self.targetWorkspaces = []
        self.identities = []
