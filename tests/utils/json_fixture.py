class JSONFixture:


    def __init__(self):
        pass

    @staticmethod
    def for_create_issue(projectKey):
        json = {
            "fields": {
                "project":
                    {
                        "key": projectKey
                    },
                "summary": "Test Summary",
                "description": "Creating of an issue",
                "assignee": {"name": "Alex_Tropp"},
                "priority": {"name": "High"},
                "issuetype": {"name": "Test"}
            }
        }
        return json
