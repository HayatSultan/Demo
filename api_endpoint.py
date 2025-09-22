class APIV1:
    def get_data(self):
        return {"status": "success", "data": [1, 2, 3]}

try:
    api = APIV1()
    response = api.get_data()  # Changed fetch_data() to get_data()

    print("API response:", response)

except Exception as e:
    print("Details:", str(e))
