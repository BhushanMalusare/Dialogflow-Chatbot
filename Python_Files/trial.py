a = {
  "responseId": "0f174f7b-e5d5-45d1-a439-b635807ca53c-cc68fdcf",
  "queryResult": {
    "queryText": "new order",
    "parameters": {},
    "allRequiredParamsPresent": "true",
    "fulfillmentText": "Ok, starting a new order. You can say things like \"I want two pizzas and one mango lassi\". Make sure to specify a quantity for every food item! Also, we have only the following items on our menu: Pav Bhaji, Chole Bhature, Pizza, Mango Lassi, Masala Dosa, Biryani, Vada Pav, Rava Dosa, and Samosa.",
    "fulfillmentMessages": [
      {
        "text": {
          "text": [
            "Ok, starting a new order. You can say things like \"I want two pizzas and one mango lassi\". Make sure to specify a quantity for every food item! Also, we have only the following items on our menu: Pav Bhaji, Chole Bhature, Pizza, Mango Lassi, Masala Dosa, Biryani, Vada Pav, Rava Dosa, and Samosa."
          ]
        }
      }
    ],
    "outputContexts": [
      {
        "name": "projects/eatery-chatbot-xkru/agent/sessions/005b1366-2fb5-5d62-7f3c-f15a14ecbd3d/contexts/ongoing-order",
        "lifespanCount": 5,
        "parameters": {
          "number": [
            2
          ],
          "food-item.original": [
            "pizza"
          ],
          "number.original": [
            "2"
          ],
          "food-item": [
            "Pizza"
          ]
        }
      }
    ],
    "intent": {
      "name": "projects/eatery-chatbot-xkru/agent/intents/5be6248d-f771-457b-9f41-6ad0ca4141dc",
      "displayName": "new.order"
    },
    "intentDetectionConfidence": 1,
    "languageCode": "en",
    "sentimentAnalysisResult": {
      "queryTextSentiment": {
        "score": -0.2,
        "magnitude": 0.2
      }
    }
  }
}

new_order_forgetting_quantity = a["queryResult"]["outputContexts"][0]["parameters"]["number"]
print(new_order_forgetting_quantity)