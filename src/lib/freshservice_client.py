import requests

api_key = ""
base_url = ""
headers = {"Content-Type": "application/json"}

class FreshServiceClient:        

    def get_solution_articles(self, search_string, params=None, max_page=1):
        all_articles = []
        url = f"{base_url}/solutions/articles/search?search_term={search_string}"

        if params is None:
            params = {}
            params["page"] = 1
            params["per_page"] = 100

        if params["per_page"] > 100:
            params["per_page"] = 100

        page = 1
        while True:
            response = requests.get(
                url, headers=headers, auth=(api_key, "X"), params=params
            )
            if response.status_code == 200:
                articles = response.json()

                if not articles["articles"]:
                    break

                for article in articles["articles"]:
                    app = [article["title"], article["description_text"]]
                    all_articles.append(app)

                if not max_page is None and page == max_page:
                    break

                page += 1
            else:
                print("Error:", response)
                break

        return all_articles

    def get_ticket_by_id(self, id):
        url = f"{base_url}/tickets/{id}"
        response = requests.get(url=url, headers=headers, auth=(api_key, 'X'))
        if response.status_code == 200:
            return response.json()

    def get_tickets(self, params=None, max_page=None):
        url = f"{base_url}/tickets"

        all_tickets = []
        if params is None:
            params = {}
            params["page"] = 1
            params["per_page"] = 100
        if params["per_page"] > 100:
            params["per_page"] = 100

        page = 1
        while True:
            response = requests.get(
                url, headers=headers, auth=(api_key, "X"), params=params
            )
            if response.status_code == 200:
                tickets = response.json()

                if not tickets:
                    break

                for ticket in tickets["tickets"]:
                    all_tickets.append(ticket)

                if not max_page is None and page == max_page:
                    break

                page += 1
            else:
                print("Error:", response)
                break

        return all_tickets

    def get_conversations(self, ticket_id, page=1):
        conversations = []
        url = f"{base_url}/tickets"
        conv_url = url + f"/{ticket_id}/conversations"
        if page > 1:
            conv_url += f"?page={page}"

        response = requests.get(url=conv_url, headers=headers, auth=(api_key, "X"))

        if response.status_code == 200:
            conversations_data = response.json()
            conversations = conversations_data["conversations"]

            if conversations_data["meta"]["count"] > 30 and page < conversations_data["meta"]["count"] / 30:
                conversations += self.get_conversations(ticket_id, page=page + 1)

        return conversations

if __name__ == "__main__":
    pass
